# -*- coding: utf-8 -*-
"""Audit d'intégrité et de couverture des données du catalogue.

Usage :
    python database/check_data.py [--strict] [--json] [--module MODULE_ID]

- ``--strict`` : les avertissements deviennent des erreurs (à utiliser en CI) ;
- ``--json``   : sortie machine (dict JSON) au lieu du rapport lisible ;
- ``--module`` : détail limité à un module (module_id de ``catalog.MODULES``).

Le script vérifie :
  1. la cohérence du manifeste du catalogue (modules, statuts, unicité) ;
  2. l'unicité des identifiants de hadiths (inter-modules) et des rangs ;
  3. l'intégrité référentielle complète via l'assembleur
     (``create_seed_data()`` : chaque voie → chaîne existante, chaque nœud →
     narrateur existant, aucun turuq vide) ;
  4. la couverture vers l'objectif (~300 hadiths mutawatir validés).

Code de sortie : 0 = intégrité intacte, 1 = au moins une erreur,
2 = erreurs + avertissements en mode ``--strict``.
"""

import argparse
import json
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from .data.catalog import (
    ALL_HADITHS,
    MODULES,
    _status_ok,
    coverage_status,
    module_status,
)
from .data.hadiths_data import HADITHS
from .data.hadiths_data_mw1 import HADITHS_MW1
from .data.hadiths_data_mw2 import HADITHS_MW2
from .data.hadiths_data_mw3 import HADITHS_MW3
from .data.hadiths_data_mw4 import HADITHS_MW4
from .data.rawis_data import RAWIS
from .data.rawis_data_extra import RAWIS_EXTRA
from .data.rawis_rijal import RAWIS_RIJAL
from .data.sources_data import SOURCES, SOURCE_IDS
from .seed_data import SeedDataError, create_seed_data

_HADITH_REGISTRIES = {
    "hadiths_data": HADITHS,
    "hadiths_data_mw1": HADITHS_MW1,
    "hadiths_data_mw2": HADITHS_MW2,
    "hadiths_data_mw3": HADITHS_MW3,
    "hadiths_data_mw4": HADITHS_MW4,
}


def _audit() -> dict:
    errors, warnings = [], []

    # --- 1. Cohérence du manifeste ----------------------------------------
    module_ids = [m["module_id"] for m in MODULES]
    if len(module_ids) != len(set(module_ids)):
        errors.append("Identifiants de modules dupliqués dans le manifeste.")
    known_ids = set(_HADITH_REGISTRIES)
    for module in MODULES:
        mid = module["module_id"]
        if mid not in known_ids:
            errors.append(f"Module '{mid}' déclaré sans registre de hadiths.")
        if not _status_ok(module["status"]):
            errors.append(f"Module '{mid}' : statut invalide '{module['status']}'.")
    for mid in known_ids:
        if mid not in module_ids:
            errors.append(f"Registre '{mid}' non déclaré dans le manifeste.")

    # --- 2. Unicité des hadiths et des rangs ------------------------------
    seen_ids, seen_ranks = {}, {}
    for module in MODULES:
        mid = module["module_id"]
        for spec in _HADITH_REGISTRIES.get(mid, []):
            hid = spec.get("id")
            if hid in seen_ids:
                errors.append(
                    f"Hadith dupliqué '{hid}' : modules '{seen_ids[hid]}' et '{mid}'."
                )
            else:
                seen_ids[hid] = mid
            rank = spec.get("rank")
            if rank is None:
                warnings.append(f"Hadith '{hid}' : aucun rang (sera trié en fin).")
            elif rank in seen_ranks:
                errors.append(
                    f"Rang {rank} dupliqué : '{seen_ranks[rank]}' et '{hid}'."
                )
            else:
                seen_ranks[rank] = hid

    # --- 3. Intégrité référentielle (repose sur l'assembleur) -------------
    try:
        data = create_seed_data()
    except SeedDataError as exc:
        errors.append(f"Assemblage impossible : {exc}")
        data = None

    # --- 3bis. Répertoire « Sources & Savants » ----------------------------
    _REQUIRED_SOURCE_FIELDS = (
        "id", "collection_fr", "collection_ar", "scholar_fr", "scholar_ar",
        "obedience", "dates_fr", "century_hijri", "tokens", "contribution",
    )
    if len(SOURCE_IDS) != len(set(SOURCE_IDS)):
        errors.append("Identifiants de sources dupliqués dans sources_data.py.")
    for src in SOURCES:
        for field in _REQUIRED_SOURCE_FIELDS:
            if not src.get(field):
                errors.append(
                    f"Source '{src.get('id', '?')}' : champ manquant '{field}'."
                )
        if src.get("obedience") not in ("sunnite", "chiite", "commun"):
            errors.append(
                f"Source '{src.get('id', '?')}' : obédience invalide "
                f"'{src.get('obedience')}'."
            )
        if not src.get("tokens"):
            errors.append(f"Source '{src.get('id', '?')}' : aucun token de repérage.")

    if data is not None:
        for hid, hadith in data["hadiths"].items():
            if not hadith["matn_translation_fr"]:
                warnings.append(f"Hadith '{hid}' : traduction française absente.")
            if not hadith["thematic_category"]:
                warnings.append(f"Hadith '{hid}' : catégorie thématique absente.")
            if not hadith["keywords"]:
                warnings.append(f"Hadith '{hid}' : aucun mot-clé.")

    # --- 4. Couverture -----------------------------------------------------
    coverage = coverage_status()

    return {
        "ok": not errors,
        "strict_mode": False,
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "coverage": coverage,
    }


def _render_human(report: dict) -> str:
    lines = ["=== Audit des données — Tawatur Hadith ==="]
    if report["errors"]:
        lines.append(f"\nERREURS ({len(report['errors'])}) :")
        lines += [f"  ✗ {e}" for e in report["errors"]]
    else:
        lines.append("\nIntégrité : OK (aucune erreur).")
    if report["warnings"]:
        lines.append(f"\nAvertissements ({len(report['warnings'])}) :")
        lines += [f"  ⚠ {w}" for w in report["warnings"]]
    c = report["coverage"]
    lines.append(f"\nCouverture : {c['current']}/{c['target']} hadiths "
                 f"catalogués ({c['validated']} validés), {c['remaining']} restants.")
    lines.append(f"  voies (Turuq) : {c['turuq_inline']} inline "
                 f"+ {c['isnad_expansions']} hadiths enrichis de chaînes détaillées.")
    lines.append(f"  chaînes estimées : {c['chains_estimees']} — narrateurs : {c['rawis']}.")
    lines.append(f"  modules : {c['modules_validated']}/{c['modules']} VALIDATED"
                 f", {c['modules_draft']} en cours (DRAFT/BETA).")
    return "\n".join(lines)


def _render_module(module_id: str) -> str:
    module = next((m for m in MODULES if m["module_id"] == module_id), None)
    if module is None:
        raise SystemExit(f"Module inconnu : '{module_id}' (voir catalog.MODULES).")
    specs = _HADITH_REGISTRIES.get(module_id, [])
    lines = [f"=== Module '{module_id}' — {module['label_fr']} ===",
             f"Statut : {module['status']} — {len(specs)} hadiths"]
    for spec in specs:
        hid = spec.get("id")
        turuq = len(spec.get("turuq", []))
        lines.append(f"  - {hid} (rang {spec.get('rank')}) : {turuq} voie(s) — "
                     f"{spec.get('title_fr', 'sans titre')}")
    if not specs:
        lines.append("  (aucune entrée pour l'instant — template d'intégration)")
    return "\n".join(lines)


def main(argv) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--module", default=None)
    args = parser.parse_args(argv)

    if args.module:
        if args.as_json:
            module = next((m for m in MODULES if m["module_id"] == args.module), None)
            specs = _HADITH_REGISTRIES.get(args.module, []) if module else []
            print(json.dumps({
                "module": args.module,
                "found": module is not None,
                "status": module["status"] if module else None,
                "count": len(specs),
            }, ensure_ascii=False, indent=2))
        else:
            print(_render_module(args.module))
        return 0

    report = _audit()
    report["strict_mode"] = args.strict

    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(_render_human(report))

    if report["errors"]:
        return 1
    if args.strict and report["warnings"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))