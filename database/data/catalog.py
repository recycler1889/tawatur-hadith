# -*- coding: utf-8 -*-
"""Catalogue central des données du projet Tawatur Hadith.

Ce module est l'UNIQUE point d'entrée pour la construction des données : il
agrège tous les registres du package ``database.data`` et porte le manifeste
des modules. Objectif : accueillir de manière modulaire, propre et complète
l'ensemble des hadiths mutawatir validés par les savants (~300 au total), avec
toutes leurs voies (Turuq) et chaînes (Isnad).

Architecture :
--------------

    database/data/
      hadiths_data.py        Catalogue fondateur (50 hadiths, classés par rang)
      hadiths_data_mw1.py    1re vague d'extension (20)
      hadiths_data_mw2.py    2e vague d'extension (28)
      hadiths_data_mw3.py    Mutawatir supplémentaires sourcés (2)
      hadiths_data_mw4.py    3e vague — intégration en cours (modèle DRAFT)
      isnad_expansions.py    Chaînes détaillées ajoutées à des hadiths existants
      rawis_data.py          Registre des narrateurs (Rijal) — base
      rawis_data_extra.py    Narrateurs additionnels (fusionnés)
      rawis_rijal.py         Narrateurs intermédiaires issus des asanid
      catalog.py             ← CE FICHIER (manifeste + agrégation + suivi)

Intégration d'une nouvelle vague :
   1. Créer ``hadiths_data_mw<N>.py`` exportant ``HADITHS_MW<N>`` ;
   2. Y déclarer les entrées (schéma : ``database/data/hadiths_data.py``) ;
   3. Ajouter un bloc dans ``MODULES`` ci-dessous (avec son statut) ;
   4. Étendre ``_HADITH_MODULES`` avec ``(registry, module_id, label)`` ;
   5. Vérifier : ``python database/check_data.py``.
Rien d'autre n'est à toucher : l'assembleur (``database/seed_data.py``) et
l'application consomment déjà ce catalogue.
"""

from typing import Dict, List

from database.data.hadiths_data import HADITHS
from database.data.hadiths_data_mw1 import HADITHS_MW1
from database.data.hadiths_data_mw2 import HADITHS_MW2
from database.data.hadiths_data_mw3 import HADITHS_MW3
from database.data.hadiths_data_mw4 import HADITHS_MW4
from database.data.isnad_expansions import ISNAD_EXPANSIONS
from database.data.rawis_data import RAWIS
from database.data.rawis_data_extra import RAWIS_EXTRA
from database.data.rawis_rijal import RAWIS_RIJAL
from database.data.sources_data import SOURCES

# Objectif global validé par les savants (catalogue exhaustif des mutawatir).
TARGET_COUNT = 300

# Statuts de fiabilité d'un module.
VALIDATED = "VALIDATED"  # entrées validées par les savants
BETA = "BETA"            # entrées vérifiées mais en cours d'arbitrage final
DRAFT = "DRAFT"          # entrées en préparation (intégration progressive)


def _status_ok(status: str) -> bool:
    return status in {VALIDATED, BETA, DRAFT}


# ---------------------------------------------------------------------------
# Manifeste des modules de hadiths.
#   - ``registry`` : liste des entrées exportée par le module.
#   - ``module_id``: identifiant stable (slug).
#   - ``label``    : libellé humain pour les rapports d'audit.
# ---------------------------------------------------------------------------
_HADITH_MODULES = [
    (HADITHS, "hadiths_data", "Catalogue fondateur (classé par rang)"),
    (HADITHS_MW1, "hadiths_data_mw1", "1re vague d'extension"),
    (HADITHS_MW2, "hadiths_data_mw2", "2e vague d'extension"),
    (HADITHS_MW3, "hadiths_data_mw3", "Mutawatir supplémentaires sourcés"),
    (HADITHS_MW4, "hadiths_data_mw4", "3e vague — intégration en cours"),
]

MODULES: List[Dict] = [
    {
        "module_id": "hadiths_data",
        "label_fr": "Catalogue fondateur (classé par rang)",
        "source_base": (
            "al-Suyuti (al-Azhar al-Mutanathira), al-Kattani "
            "(Nazm al-Mutanathir), ainsi que recueils chiites "
            "(al-Kafi, Man la yahduruhu al-Faqih)"
        ),
        "status": VALIDATED,
    },
    {
        "module_id": "hadiths_data_mw1",
        "label_fr": "1re vague d'extension",
        "source_base": (
            "al-Suyuti (al-Azhar al-Mutanathira), Tuhfat al-Ashraf, "
            "al-Muttaqi al-Hindi (Kanz al-Ummal)"
        ),
        "status": VALIDATED,
    },
    {
        "module_id": "hadiths_data_mw2",
        "label_fr": "2e vague d'extension",
        "source_base": (
            "al-Kattani (Nazm al-Mutanathir), Ibn al-Jawzi, "
            "al-Tabarani (al-Kabir)"
        ),
        "status": VALIDATED,
    },
    {
        "module_id": "hadiths_data_mw3",
        "label_fr": "Mutawatir supplémentaires sourcés",
        "source_base": (
            "Complément scientifique — chaînes vérifiées dans "
            "les Musnad/Sunan/Al-Kutub al-Sittah"
        ),
        "status": VALIDATED,
    },
    {
        "module_id": "hadiths_data_mw4",
        "label_fr": "3e vague — intégration en cours",
        "source_base": "À confirmer par les savants (voir module)",
        "status": DRAFT,
    },
]


def _collect_hadiths() -> List[Dict]:
    """Concatène les registres de hadiths dans l'ordre du manifeste."""
    return [h for registry, _mid, _label in _HADITH_MODULES for h in registry]


def _collect_rawis() -> Dict[str, Dict]:
    """Fusionne tous les registres de narrateurs (les plus récents gagnent)."""
    return {**RAWIS, **RAWIS_EXTRA, **RAWIS_RIJAL}


ALL_HADITHS: List[Dict] = _collect_hadiths()
ALL_RAWIS: Dict[str, Dict] = _collect_rawis()

# Répertoire des sources/savants mobilisés par l'outil (cf. sources_data.py).
ALL_SOURCES: List[Dict] = list(SOURCES)


def module_status(module_id: str) -> str:
    """Statut de fiabilité d'un module (DRAFT/BETA/VALIDATED)."""
    for module in MODULES:
        if module["module_id"] == module_id:
            return module["status"]
    raise KeyError(f"module inconnu : '{module_id}'")


def validated_count() -> int:
    """Nombre de hadiths issus des modules VALIDATED (les autres sont exclus)."""
    return sum(
        len(registry)
        for registry, module_id, _label in _HADITH_MODULES
        if module_status(module_id) == VALIDATED
    )


def coverage_status() -> Dict:
    """Indicateurs de suivi de l'intégration progressive vers l'objectif."""
    inline_turuq = sum(len(h.get("turuq", [])) for h in ALL_HADITHS)
    expansions = sum(len(voies) for voies in ISNAD_EXPANSIONS.values())
    validated = validated_count()
    return {
        "target": TARGET_COUNT,
        "current": len(ALL_HADITHS),
        "validated": validated,
        "remaining": TARGET_COUNT - len(ALL_HADITHS),
        "turuq_inline": inline_turuq,
        "isnad_expansions": len(ISNAD_EXPANSIONS),
        "chains_estimees": inline_turuq + expansions,
        "rawis": len(ALL_RAWIS),
        "sources": len(ALL_SOURCES),
        "modules": len(MODULES),
        "modules_validated": sum(1 for m in MODULES if m["status"] == VALIDATED),
        "modules_draft": sum(1 for m in MODULES if m["status"] != VALIDATED),
    }