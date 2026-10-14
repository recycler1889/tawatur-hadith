# -*- coding: utf-8 -*-
"""Tests d'intégrité du catalogue de données (``database.seed_data`)."""
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest

from database.seed_data import create_seed_data


@pytest.fixture(scope="module")
def data():
    return create_seed_data()


def test_catalogue_non_vide(data):
    assert len(data["hadiths"]) >= 1
    assert len(data["isnad_chains"]) >= 1
    assert len(data["rawis"]) >= 1


def test_identifiants_hadith_uniques(data):
    ids = list(data["hadiths"].keys())
    assert len(ids) == len(set(ids))


def test_rangs_presents_et_uniques(data):
    ranks = [h["rank"] for h in data["hadiths"].values()]
    assert None not in ranks, "chaque hadith doit porter un rang"
    assert len(ranks) == len(set(ranks)), "les rangs doivent être uniques"


def test_chaque_hadith_a_des_voies(data):
    for h in data["hadiths"].values():
        assert h["turuq"], f"le hadith {h['id']} n'a aucune voie (turuq)"


def test_champs_obligatoires_renseignes(data):
    for h in data["hadiths"].values():
        assert h["matn"].strip(), f"{h['id']} : matn vide"
        assert h["title_fr"].strip(), f"{h['id']} : titre vide"
        assert h["obedience"] in {"sunnite", "chiite", "commun"}
        assert h["tawatur_type"] in {"lafzi", "ma'nawi"}


def test_sources_de_validation_presentes(data):
    for h in data["hadiths"].values():
        assert h["validation_sources"], f"{h['id']} : aucune source de validation"


def test_integrite_referentielle(data):
    """Toute voie pointe vers une chaîne connue ; tout nœud vers un rawi connu."""
    rawis = data["rawis"]
    chains = data["isnad_chains"]

    for h in data["hadiths"].values():
        for voie in h["turuq"]:
            assert voie["isnad_chain_id"] in chains, (
                f"{h['id']} : chaîne inconnue '{voie['isnad_chain_id']}'"
            )

    for cid, chain in chains.items():
        assert chain["nodes"], f"chaîne '{cid}' vide"
        for node in chain["nodes"]:
            assert node["rawi_id"] in rawis, (
                f"chaîne '{cid}' : narrateur inconnu '{node['rawi_id']}'"
            )
