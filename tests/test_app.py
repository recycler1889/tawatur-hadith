# -*- coding: utf-8 -*-
"""Tests de non-régression de l'interface Streamlit (AppTest)."""
import os

from streamlit.testing.v1 import AppTest

APP = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "frontend",
    "app.py",
)


def _run():
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    return at


def _cards(at):
    return [b.key for b in at.button if b.key and b.key.startswith("sel_")]


def test_app_sans_exception():
    at = _run()
    assert not at.exception, [e.message for e in at.exception]
    assert len(_cards(at)) > 0


def test_filtres_disponibles():
    at = _run()
    labels = {m.label for m in at.multiselect}
    assert {"Obédience", "Type de Tawatur", "Catégorie thématique"} <= labels


def test_filtre_categorie():
    at = _run()
    total = len(_cards(at))
    cat = next(m for m in at.multiselect if m.label == "Catégorie thématique")
    cat.set_value(["Eschatologie"]).run()
    assert not at.exception, [e.message for e in at.exception]
    assert 0 < len(_cards(at)) < total


def test_filtre_tawatur():
    at = _run()
    total = len(_cards(at))
    tw = next(m for m in at.multiselect if m.label == "Type de Tawatur")
    tw.set_value(["Mutawatir Lafzi (mot à mot)"]).run()
    assert not at.exception
    assert 0 < len(_cards(at)) < total


def test_changement_theme_par_bouton():
    at = _run()
    at.button(key="theme_Clair").click().run()
    assert not at.exception, [e.message for e in at.exception]
    assert at.session_state["theme"] == "Clair"


def test_ouverture_detail():
    at = _run()
    at.button(key=_cards(at)[0]).click().run()
    assert not at.exception, [e.message for e in at.exception]
    assert at.session_state["selected_hadith_id"]
