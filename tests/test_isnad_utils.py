# -*- coding: utf-8 -*-
"""Tests des utilitaires d'Isnad (backend.graph.isnad_utils)."""
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest

from backend.graph.isnad_utils import (
    build_turuq_network,
    format_isnad_text,
    obedience_fr,
    reliability_fr,
    tawatur_fr,
)
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data


@pytest.fixture(scope="module")
def models():
    d = create_seed_data()
    hadiths = [Hadith(**h) for h in d["hadiths"].values()]
    rawis = {k: Rawiy(**v) for k, v in d["rawis"].items()}
    chains = {k: IsnadChain(**v) for k, v in d["isnad_chains"].items()}
    return hadiths, rawis, chains


def test_traductions_fr():
    assert reliability_fr("thiqa").startswith("Fiable")
    assert "Lafzi" in tawatur_fr("lafzi")
    assert obedience_fr("commun").startswith("Commun")


def test_format_isnad_text(models):
    hadiths, rawis, chains = models
    hadith = hadiths[0]
    chain = chains[hadith.turuq[0].isnad_chain_id]
    texte = format_isnad_text(chain)
    assert chain.nodes[0].rawi_name in texte
    assert " → " in texte or len(chain.nodes) == 1


def test_build_turuq_network(models):
    hadiths, rawis, chains = models
    hadith = hadiths[0]
    net = build_turuq_network(hadith, chains, rawis)

    assert net["stats"]["n_chains"] >= 1
    assert net["nodes"], "le réseau doit contenir au moins un nœud"
    assert net["edges"], "le réseau doit contenir au moins un lien"

    ids = [n["id"] for n in net["nodes"]]
    assert len(ids) == len(set(ids)), "les nœuds doivent être dédupliqués"

    for node in net["nodes"]:
        assert node["reliability_fr"], f"{node['id']} : fiabilité non traduite"
        assert node["frequency"] >= 1


def test_build_turuq_network_seuil(models):
    """Un seuil de chemins très élevé doit pouvoir vider le réseau."""
    hadiths, rawis, chains = models
    hadith = hadiths[0]
    net = build_turuq_network(hadith, chains, rawis, min_paths=10**9)
    assert net["stats"]["n_chains"] == 0
    assert net["nodes"] == []
