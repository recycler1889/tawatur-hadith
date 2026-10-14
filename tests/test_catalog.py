# -*- coding: utf-8 -*-
"""Tests du catalogue central (``database.data.catalog``) et de l'audit."""
import sys
import os

# Ajout de la racine du projet au path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from database.data.catalog import (
    ALL_HADITHS,
    ALL_RAWIS,
    MODULES,
    TARGET_COUNT,
    VALIDATED,
    coverage_status,
    module_status,
)
from database.data.hadiths_data import HADITHS
from database.data.hadiths_data_mw1 import HADITHS_MW1
from database.data.hadiths_data_mw2 import HADITHS_MW2
from database.data.hadiths_data_mw3 import HADITHS_MW3
from database.data.hadiths_data_mw4 import HADITHS_MW4
from database.data.isnad_expansions import ISNAD_EXPANSIONS
from database.data.rawis_data import RAWIS
from database.data.rawis_data_extra import RAWIS_EXTRA
from database.data.rawis_rijal import RAWIS_RIJAL

_REGISTRIES = {
    "hadiths_data": HADITHS,
    "hadiths_data_mw1": HADITHS_MW1,
    "hadiths_data_mw2": HADITHS_MW2,
    "hadiths_data_mw3": HADITHS_MW3,
    "hadiths_data_mw4": HADITHS_MW4,
}


def test_objectif_catalogue():
    assert TARGET_COUNT == 300


def test_manifeste_coherent():
    ids = [m["module_id"] for m in MODULES]
    assert len(ids) == len(set(ids)), "module_id non uniques"
    for module in MODULES:
        assert module["status"] in {"VALIDATED", "BETA", "DRAFT"}
        assert module["module_id"] in _REGISTRIES, (
            f"module '{module['module_id']}' sans registre"
        )
    assert set(_REGISTRIES) == set(ids), "des registres ne sont pas déclarés"


def test_aggregation_hadiths_exhaustive():
    attendu = sum(len(r) for r in _REGISTRIES.values())
    assert len(ALL_HADITHS) == attendu
    ids = [h["id"] for h in ALL_HADITHS]
    assert len(ids) == len(set(ids)), "identifiants de hadiths dupliqués inter-modules"


def test_aggregation_rawis_fusionnee():
    attendu = {**RAWIS, **RAWIS_EXTRA, **RAWIS_RIJAL}
    assert set(ALL_RAWIS) == set(attendu)
    assert ALL_RAWIS["ali"]["id"] == "ali"


def test_couverture_vers_objectif():
    cov = coverage_status()
    assert cov["current"] == len(ALL_HADITHS) == 100
    assert cov["validated"] == 100
    assert cov["remaining"] == 200
    assert cov["turuq_inline"] == 346
    assert cov["isnad_expansions"] == len(ISNAD_EXPANSIONS)


def test_chaines_estimees():
    cov = coverage_status()
    inline = sum(len(h.get("turuq", [])) for h in ALL_HADITHS)
    expansions = sum(len(v) for v in ISNAD_EXPANSIONS.values())
    assert cov["chains_estimees"] == inline + expansions == 370


def test_modules_et_statuts():
    cov = coverage_status()
    assert cov["modules"] == len(MODULES) == 5
    assert cov["modules_validated"] == 4
    assert cov["modules_draft"] == 1
    assert module_status("hadiths_data") == VALIDATED
    assert module_status("hadiths_data_mw4") == "DRAFT"


def test_module_mw4_template_vide():
    """Le module d'intégration est déclaré (DRAFT) et encore sans entrée."""
    assert MODULES[-1]["module_id"] == "hadiths_data_mw4"
    assert MODULES[-1]["status"] == "DRAFT"
    assert HADITHS_MW4 == []


def test_audit_integre():
    from database.check_data import _audit

    report = _audit()
    assert report["ok"] is True
    assert report["errors"] == []