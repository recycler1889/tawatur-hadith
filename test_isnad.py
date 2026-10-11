# -*- coding: utf-8 -*-
"""Vérification rapide des données et de l'affichage des chaînes d'Isnad.

Exécution :
    python test_isnad.py

Affiche un résumé du catalogue, quelques chaînes de transmission sous forme
textuelle, puis écrit un exemple d'arbre d'Isnad dans
``data/example_isnad_tree.json``.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
sys.stdout.reconfigure(encoding="utf-8")

from backend.graph.isnad_utils import build_isnad_tree, build_turuq_network, format_isnad_text
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data


def display_isnad_example():
    data = create_seed_data()
    hadiths = [Hadith(**h) for h in data["hadiths"].values()]
    rawis = {k: Rawiy(**v) for k, v in data["rawis"].items()}
    chains = {k: IsnadChain(**v) for k, v in data["isnad_chains"].items()}
    hadiths.sort(key=lambda h: (h.rank if h.rank is not None else 10**9))

    print("=" * 60)
    print("TAWATUR HADITH - CHAÎNES D'ISNAD")
    print("=" * 60)
    print(f"{len(hadiths)} hadiths, {len(chains)} chaînes, {len(rawis)} narrateurs.\n")

    for hadith in hadiths[:5]:
        print(f"[{hadith.rank}] {hadith.title_fr}")
        for turuq in hadith.turuq:
            chain = chains.get(turuq.isnad_chain_id)
            if chain:
                print(f"  - {turuq.label} : {format_isnad_text(chain)}")
        print()

    # Exemple : réseau fusionné + arbre d'une chaîne du hadith le mieux classé.
    top = hadiths[0]
    network = build_turuq_network(top, chains, rawis)
    first_chain = chains.get(top.turuq[0].isnad_chain_id)
    example_tree = build_isnad_tree(first_chain, rawis)

    out = os.path.join(ROOT, "data", "example_isnad_tree.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(
            {
                "hadith": top.title_fr,
                "network_stats": network["stats"],
                "example_chain": example_tree,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    print(f"Exemple écrit dans {out}")


if __name__ == "__main__":
    display_isnad_example()
