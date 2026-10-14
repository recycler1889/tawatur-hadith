# -*- coding: utf-8 -*-
"""
Tawatur Hadith — Visualiseur d'Isnad (Streamlit)
================================================
- Thèmes : Clair, Sépia, Sombre (motifs géométriques islamiques).
- Sélection des hadiths par cartes, filtres (recherche / obédience / tawatur).
- Support multi-voies (Turuq) → chaîne d'Isnad → arbre interactif + narrateurs.
- Chargement des données durci (try/except + st.error) : jamais d'écran blanc.
"""

import os
import sys
from pathlib import Path

# Racine du projet = dossier courant (app.py à la racine)
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from backend.graph.isnad_utils import (
    build_turuq_network,
    format_isnad_text,
    layout_network,
    obedience_fr,
    reliability_fr,
    tawatur_fr,
)
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data
from database.data.sources_data import SOURCES

_FAVICON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "frontend", "assets", "favicon.png"
)

st.set_page_config(
    page_title="Tawatur Hadith | Visualisation des Hadiths Mutawatir",
    page_icon=_FAVICON if os.path.exists(_FAVICON) else "۞",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------------------------
# 1. Chargement des données (durci — jamais d'écran blanc)
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    data = create_seed_data()
    hadiths = [Hadith(**h) for h in data["hadiths"].values()]
    hadiths.sort(key=lambda x: x.id)
    rawis = {k: Rawiy(**v) for k, v in data["rawis"].items()}
    chains = {k: IsnadChain(**v) for k, v in data["isnad_chains"].items()}
    return hadiths, rawis, chains


def safe_load_data():
    """Charge les données et affiche toute erreur DANS l'interface."""
    try:
        hadiths, rawis, chains = load_data()
    except Exception as exc:
        st.error("⚠️ **Impossible de charger les données initiales.**")
        st.caption(
            f"**Détail de l'erreur :** `{exc}`\n\n"
            "Vérifiez `database/seed_data.py` et `backend/models/hadith_models.py`."
        )
        st.stop()
    if not hadiths:
        st.error("⚠️ **Le jeu de données est vide.**")
        st.stop()
    if not chains:
        st.error("⚠️ **Aucune chaîne d'isnad n'est définie.**")
        st.stop()
    return hadiths, rawis, chains


hadiths, rawis, chains = safe_load_data()


def authenticity_key(h):
    """Clé de classement par authenticité (du plus fort au plus faible) :
    1) le rang éditorial explicite (``rank``, 1 = plus haut degré d'unanimité) ;
    2) le type Mutawatir Lafzi (mot à mot) avant Ma'nawi (par le sens) ;
    3) le nombre de voies (Turuq) concordantes ;
    4) le total des chemins transmis (path_count) déclarés."""
    rank = getattr(h, "rank", None)
    lafzi = 1 if h.tawatur_type.value == "lafzi" else 0
    turuq = h.turuq or []
    total_paths = 0
    for voie in turuq:
        c = chains.get(voie.isnad_chain_id)
        if c and c.path_count:
            total_paths += c.path_count
    return (-(rank if rank is not None else 9999), lafzi, len(turuq), total_paths)


# Classement global : hadiths mutawatir les plus authentiques en tête.
hadiths = sorted(hadiths, key=authenticity_key, reverse=True)


def primary_chain(hadith):
    """Chaîne principale d'un hadith, via sa première voie (Turuq)."""
    turuq = getattr(hadith, "turuq", None) or []
    for voie in turuq:
        if voie.isnad_chain_id in chains:
            return chains[voie.isnad_chain_id]
    return None


# Seuil (chemins cumulés) au-delà duquel un hadith est « au sommet du Tawatur ».
SUMMIT_MIN_PATHS = 150


def total_paths(hadith):
    """Somme des chemins (path_count) déclarés sur toutes les voies d'un hadith."""
    total = 0
    for voie in (hadith.turuq or []):
        c = chains.get(voie.isnad_chain_id)
        if c and c.path_count:
            total += c.path_count
    return total


def is_summit(hadith):
    """Hadith au plus haut degré d'unanimité : au moins SUMMIT_MIN_PATHS chemins cumulés."""
    return total_paths(hadith) >= SUMMIT_MIN_PATHS


def year_fr(value):
    if value is None or value == "":
        return "—"
    return f"{value} (env.)"


# ---------------------------------------------------------------------------
# Classification des rapporteurs et de la chaîne de transmission
# ---------------------------------------------------------------------------
def chain_stats(hadith):
    """Agrège les métriques de qualité des rapporteurs et de la chaîne (Turuq).

    - ``turuq``      : nombre de voies de transmission ;
    - ``rawis``      : nombre de narrateurs distincts (qualité/richesse du réseau) ;
    - ``companions`` : nombre de Compagnons distincts (grandeur de la transmission) ;
    - ``max_len``    : longueur de la chaîne la plus détaillée (maillons) ;
    - ``paths``      : total des chemins cumulés déclarés.
    """
    turuq = hadith.turuq or []
    node_ids, companions = set(), set()
    max_len, total = 0, 0
    for voie in turuq:
        c = chains.get(voie.isnad_chain_id)
        if not c or not c.nodes:
            continue
        max_len = max(max_len, len(c.nodes))
        total += c.path_count or 0
        for n in c.nodes:
            node_ids.add(n.rawi_id)
            if n.level >= 4:
                companions.add(n.rawi_id)
    return {
        "turuq": len(turuq),
        "rawis": len(node_ids),
        "companions": len(companions),
        "max_len": max_len,
        "paths": total,
    }


CHAIN_QUALITY_OPTIONS = [
    "Chaîne détaillée (≥5 maillons)",
    "Chaîne établie (3–4 maillons)",
    "Chaîne concise (≤2 maillons)",
]
CHAIN_GRANDEUR_OPTIONS = [
    "Grandeur élevée (3+ Compagnons)",
    "Grandeur moyenne (2 Compagnons)",
    "Transmission simple (1 Compagnon)",
]
RELEVANCE_SORT_OPTIONS = [
    "Rang d'authenticité (recommandé)",
    "Nombre de voies (décroissant)",
    "Narrateurs distincts (décroissant)",
    "Compagnons distincts (décroissant)",
    "Longueur de chaîne (décroissant)",
    "Chemins cumulés (décroissant)",
]


def chain_quality_tier(hadith):
    """Palier de qualité de la chaîne, selon la profondeur (nombre de maillons)."""
    ml = chain_stats(hadith)["max_len"]
    if ml >= 5:
        return CHAIN_QUALITY_OPTIONS[0]
    if ml >= 3:
        return CHAIN_QUALITY_OPTIONS[1]
    return CHAIN_QUALITY_OPTIONS[2]


def chain_grandeur_tier(hadith):
    """Grandeur de la transmission selon le nombre de Compagnons distincts."""
    n = chain_stats(hadith)["companions"]
    if n >= 3:
        return CHAIN_GRANDEUR_OPTIONS[0]
    if n == 2:
        return CHAIN_GRANDEUR_OPTIONS[1]
    return CHAIN_GRANDEUR_OPTIONS[2]


def chain_generations(hadith):
    """Ensemble des générations (Tabaqa) de rapporteurs présentes dans les voies."""
    gens = set()
    for voie in (hadith.turuq or []):
        c = chains.get(voie.isnad_chain_id)
        if not c:
            continue
        for n in c.nodes:
            r = rawis.get(n.rawi_id)
            if r and r.tabaqa:
                gens.add(r.tabaqa)
    return gens


def relevance_sort_key(criterion):
    """Renvoie la clé de tri (décroissante) correspondant au critère choisi."""
    if criterion == "Nombre de voies (décroissant)":
        return lambda h: len(h.turuq or [])
    if criterion == "Narrateurs distincts (décroissant)":
        return lambda h: chain_stats(h)["rawis"]
    if criterion == "Compagnons distincts (décroissant)":
        return lambda h: chain_stats(h)["companions"]
    if criterion == "Longueur de chaîne (décroissant)":
        return lambda h: chain_stats(h)["max_len"]
    if criterion == "Chemins cumulés (décroissant)":
        return lambda h: chain_stats(h)["paths"]
    return None


# ---------------------------------------------------------------------------
# 2. Thèmes CSS (+ garde-fou anti écran blanc)
# ---------------------------------------------------------------------------
FONTS = (
    "@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700"
    "&family=Noto+Sans+Arabic:wght@400;700&family=Inter:wght@400;600"
    "&family=Lora:wght@400;600&display=swap');"
)

SAFETY = """
/* Garde-fou : le conteneur principal et le markdown ne doivent jamais
   hériter d'une couleur transparente (cause classique d'écran blanc). */
[data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"],
[data-testid="stHeader"] { color: inherit; }
"""

# Champs de formulaire & composants Streamlit : colorsés via variables posées
# par chaque thème (--ui-*). Élimine définitivement les fonds noirs en Clair/Sépia.
WIDGET_CSS = """
/* ===== Champs de formulaire & composants (cohérence multi-thèmes) ===== */
[data-testid="stAppViewContainer"] { background: var(--ui-bg); color: var(--ui-text); }
div[data-baseweb="input"], div[data-baseweb="base-input"],
[data-baseweb="select"] > div, div[data-baseweb="textarea"] {
  background-color: var(--ui-field-bg, var(--ui-surface)) !important;
  border-color: var(--ui-field-border, var(--ui-border)) !important;
}
.stApp input, .stApp textarea, .stApp select {
  background-color: var(--ui-field-bg, var(--ui-surface)) !important;
  color: var(--ui-text) !important;
  caret-color: var(--ui-accent) !important;
}
.stApp input::placeholder, .stApp textarea::placeholder {
  color: var(--ui-muted) !important; opacity: 1 !important;
}
[data-baseweb="select"] { color: var(--ui-text) !important; }
/* PUCS 'tag' (Plan A) : fond transparent, aucune bordure, texte bien lisible.
   Seule la couleur du texte (--ui-tag-text) subsiste pour repérer les
   valeurs sélectionnées — aucun bloc blanc/clair n'est possible. */
[data-baseweb="select"] [data-baseweb="tag"],
div[data-baseweb="tag"],
[data-baseweb="select"] [data-baseweb="tag"] *,
div[data-baseweb="tag"] * {
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
}
[data-baseweb="select"] [data-baseweb="tag"],
div[data-baseweb="tag"] {
  color: var(--ui-tag-text) !important;
  border-radius: 4px !important;
}
[data-baseweb="select"] [data-baseweb="tag"] span,
div[data-baseweb="tag"] span { color: var(--ui-tag-text) !important; }
[data-baseweb="select"] svg { fill: var(--ui-text) !important; }
/* ===== Menus déroulants (selectbox / multiselect) : fond feutré, texte lisible ===== */
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="popover"] div[role="listbox"],
ul[data-baseweb="menu"] {
  background-color: var(--ui-menu-bg) !important;
  border: 1px solid var(--ui-menu-border) !important;
  border-radius: 10px !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.30) !important;
  color: var(--ui-menu-text) !important;
}
div[data-baseweb="popover"] svg { fill: var(--ui-menu-text) !important; }
ul[data-baseweb="menu"] li,
li[role="option"],
div[role="option"] {
  background-color: var(--ui-menu-bg) !important;
  color: var(--ui-menu-text) !important;
}
ul[data-baseweb="menu"] li:hover,
li[role="option"]:hover,
li[role="option"][aria-selected="true"],
div[role="option"]:hover,
div[role="option"][aria-selected="true"] {
  background-color: var(--ui-menu-hover) !important;
  color: var(--ui-menu-text) !important;
}
li[role="option"][data-highlighted="true"] { background-color: var(--ui-menu-hover) !important; }
/* ===== Fond blanc des menus OUVERTS (panneau BaseWeb Dropdown/Listbox) =====
   Streamlit injecte via son thème (menuFill) un fond clair/blanc (#f6fbf8) et
   une bordure claire sur les couches internes du menu déroulant, même en thème
   Sombre. On les éradique définitivement : le panneau interne est fondu dans
   --ui-menu-bg, et seules les occurrences (li[role=option]) gardent leur
   état survol/sélection via --ui-menu-hover. Aucun contour blanc ne subsiste. */
div[data-baseweb="popover"] > div > div,
div[data-baseweb="popover"] > div > div div,
div[data-baseweb="popover"] > div > div ul,
div[data-baseweb="popover"] > div > div input {
  background-color: var(--ui-menu-bg) !important;
  color: var(--ui-menu-text) !important;
  border: none !important;
  box-shadow: none !important;
}
div[data-baseweb="popover"] > div > div > div,
div[data-baseweb="popover"] > div > div > ul {
  border: none !important;
}
div[data-baseweb="popover"] > div > div ul li,
div[data-baseweb="popover"] > div > div ul [role="option"],
div[data-baseweb="popover"] > div > div ul div[role="option"] {
  background-color: transparent !important;
  color: var(--ui-menu-text) !important;
  border: none !important;
}
div[data-baseweb="popover"] > div > div ul li:hover,
div[data-baseweb="popover"] > div > div ul [role="option"]:hover,
div[data-baseweb="popover"] > div > div ul [role="option"][aria-selected="true"],
div[data-baseweb="popover"] > div > div ul [role="option"][data-highlighted="true"],
div[data-baseweb="popover"] > div > div ul div[role="option"]:hover {
  background-color: var(--ui-menu-hover) !important;
  color: var(--ui-menu-text) !important;
}
div[data-baseweb="popover"] > div > div svg { fill: var(--ui-menu-text) !important; }

/* Labels & textes */
[data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] label { color: var(--ui-text) !important; }
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p { color: var(--ui-muted) !important; }
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li,
.stApp p, .stApp li { color: var(--ui-text); }

/* Expanders */
[data-testid="stExpander"] details, [data-testid="stExpander"] summary {
  background-color: var(--ui-surface) !important; color: var(--ui-text) !important;
  border: 1px solid var(--ui-border) !important; border-radius: 10px !important;
}
[data-testid="stExpander"] summary:hover { background-color: var(--ui-surface-2) !important; }
[data-testid="stExpander"] svg { fill: var(--ui-text) !important; }

/* Métriques */
[data-testid="stMetric"] {
  background-color: var(--ui-surface) !important; border: 1px solid var(--ui-border) !important;
  border-radius: 12px !important; padding: 0.7rem 0.85rem !important;
}
[data-testid="stMetricLabel"], [data-testid="stMetricLabel"] p {
  color: var(--ui-text) !important; font-size: 0.8rem !important; line-height: 1.25 !important;
  white-space: normal !important; overflow: visible !important; text-overflow: clip !important;
}
[data-testid="stMetricValue"], [data-testid="stMetricValue"] > div {
  color: var(--ui-text) !important; font-size: 1.08rem !important; line-height: 1.3 !important;
  font-weight: 600 !important;
  white-space: normal !important; overflow: visible !important; text-overflow: clip !important;
  overflow-wrap: anywhere; word-break: break-word;
}

/* Sliders */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] { background-color: var(--ui-accent) !important; }
[data-testid="stSlider"] [data-baseweb="slider"] div { color: var(--ui-text) !important; }

/* Cases à cocher & boutons radio */
[data-testid="stCheckbox"] label, [data-testid="stCheckbox"] label span,
[data-testid="stRadio"] label, [data-testid="stRadio"] label span { color: var(--ui-text) !important; }

/* Alertes */
[data-testid="stAlert"] { background-color: var(--ui-surface-2) !important; color: var(--ui-text) !important; }
[data-testid="stAlert"] p, [data-testid="stAlert"] span { color: var(--ui-text) !important; }

/* Séparateurs */
hr { border-color: var(--ui-border) !important; }

/* Boutons : lisibilité garantie, jamais de bloc noir massif */
.stButton > button, [data-testid="stButton"] button {
  background: var(--ui-btn-bg) !important;
  color: var(--ui-btn-text) !important;
  border: 1px solid var(--ui-border) !important;
}
.stButton > button[kind="primary"], [data-testid="stButton"] button[kind="primary"] {
  background: var(--ui-btn-bg-strong) !important;
}

/* ===== Défilement fluide + bouton « Retour en haut » flottant ===== */
/* Bouton ancré à mi-hauteur, contre le bord droit (1.5rem = moitié de sa
   taille 3rem : le centre du cercle est exactement à 50 % du viewport). */
html, body, section.main, [data-testid="stAppViewContainer"],
[data-testid="stMain"] { scroll-behavior: smooth; }
.back-to-top {
  position: fixed; right: 22px; bottom: calc(50% - 1.5rem); z-index: 99999;
  display: inline-flex; align-items: center; justify-content: center;
  width: 3rem; height: 3rem; border-radius: 50%;
  background: var(--ui-btn-bg-strong); color: var(--ui-btn-text) !important;
  border: 1px solid var(--ui-border); text-decoration: none !important;
  font-weight: 700; font-size: 1.25rem; line-height: 1;
  box-shadow: 0 10px 26px rgba(0,0,0,0.38);
  opacity: 0; visibility: hidden; transform: translateY(10px) scale(0.92);
  transition: opacity .25s ease, transform .25s ease, visibility .25s ease,
              filter .15s ease;
}
.back-to-top.visible { opacity: 1; visibility: visible; transform: translateY(0) scale(1); }
.back-to-top:hover { filter: brightness(1.08); transform: translateY(-2px); }

/* ===== Sommet du Tawatur : lueur dorée (Golden Glow) ===== */
.theme-card.golden {
  border: 1.5px solid #d9b24c !important;
  box-shadow: 0 0 0 1px rgba(233,196,106,0.45),
              0 0 22px rgba(214,171,66,0.42),
              0 10px 30px rgba(150,110,20,0.28) !important;
}
.theme-card.golden:hover {
  box-shadow: 0 0 0 1px rgba(240,205,110,0.65),
              0 0 30px rgba(224,182,70,0.55),
              0 14px 34px rgba(150,110,20,0.32) !important;
}
.theme-card.golden::before {
  height: 5px; opacity: 1;
  background: linear-gradient(90deg, transparent, #f7dd93 20%, #d4af37 50%, #f7dd93 80%, transparent) !important;
}
.golden-flag {
  display:inline-block; margin-top:0.6rem; padding:0.18rem 0.65rem; border-radius:999px;
  font-family:'Lora',serif; font-size:0.72rem; font-weight:600; letter-spacing:0.06em;
  color:#3a2c08; background:linear-gradient(180deg,#f7dd93,#dcb64e);
  border:1px solid rgba(160,120,20,0.5); box-shadow:0 1px 6px rgba(200,160,40,0.45);
}

/* ===== Cartes entièrement cliquables — overlay natif 100% invisible =====
   Robustesse maximale : l'overlay est ciblé par clé de composant
   (st-key-card_ / st-key-sel_) ET par structure DOM (:has), sans dépendre
   d'une version précise de Streamlit. Tout le conteneur du bouton est rendu
   totalement transparent (opacité 0) : aucun pavé blanc parasite, quelle que
   soit la structure interne. L'opacité n'affecte pas le hit-testing : la
   surface de la carte reste entièrement cliquable. */
[class*="st-key-card_"],
[data-testid="stVerticalBlock"]:has(> [data-testid="stElementContainer"] .theme-card) {
  position: relative;
  cursor: pointer;
}
[class*="st-key-card_"] [class*="st-key-sel_"],
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] {
  position: absolute !important;
  top: 0 !important; right: 0 !important; bottom: 0 !important; left: 0 !important;
  z-index: 5 !important; margin: 0 !important; padding: 0 !important;
  width: auto !important; height: auto !important;
  opacity: 0 !important;
  pointer-events: auto !important;
}
[class*="st-key-card_"] [class*="st-key-sel_"] [data-testid="stButton"],
[class*="st-key-card_"] [class*="st-key-sel_"] [data-testid="stButton"] > div,
[class*="st-key-card_"] [class*="st-key-sel_"] .stButton,
[class*="st-key-card_"] [class*="st-key-sel_"] .stButton > div,
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] [data-testid="stButton"],
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] [data-testid="stButton"] > div,
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] .stButton,
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] .stButton > div {
  width: 100% !important; height: 100% !important; margin: 0 !important;
  background: transparent !important; border: none !important;
  box-shadow: none !important;
}
[class*="st-key-card_"] [class*="st-key-sel_"] button,
[data-testid="stElementContainer"]:has(.theme-card) ~ [data-testid="stElementContainer"] button {
  position: absolute !important;
  top: 0 !important; right: 0 !important; bottom: 0 !important; left: 0 !important;
  width: 100% !important; height: 100% !important;
  min-height: 0 !important; margin: 0 !important; padding: 0 !important;
  background: transparent !important; color: transparent !important;
  border: none !important; box-shadow: none !important; cursor: pointer !important;
}
/* Focus clavier : met la carte en évidence malgré l'opacité de l'overlay. */
[class*="st-key-card_"]:focus-within .theme-card,
[data-testid="stVerticalBlock"]:has(> [data-testid="stElementContainer"] .theme-card):focus-within .theme-card {
  outline: 3px solid var(--ui-accent); outline-offset: 2px;
}
/* Animation de lévitation : l'overlay cliquable étant posé par-dessus la carte,
   le survol de la carte déclenche le :hover du conteneur, qui anime .theme-card. */
[class*="st-key-card_"] .theme-card,
[data-testid="stVerticalBlock"]:has(> [data-testid="stElementContainer"] .theme-card) .theme-card {
  transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
  will-change: transform;
}
[class*="st-key-card_"]:hover .theme-card:not(.golden),
[data-testid="stVerticalBlock"]:has(> [data-testid="stElementContainer"] .theme-card):hover .theme-card:not(.golden) {
  transform: translateY(-5px);
  box-shadow: 0 14px 30px rgba(16,185,129,0.30);
  filter: brightness(1.03);
}
[class*="st-key-card_"]:hover .theme-card.golden,
[data-testid="stVerticalBlock"]:has(> [data-testid="stElementContainer"] .theme-card):hover .theme-card.golden {
  transform: translateY(-5px);
  box-shadow: 0 0 0 1px rgba(240,205,110,0.65),
              0 0 30px rgba(224,182,70,0.55),
              0 14px 34px rgba(150,110,20,0.32) !important;
}

/* ===== Sélecteur d'ambiance : boutons-icônes compacts =====
   Rendu avec st.button (aucun rechargement de page → sélection et défilement
   préservés). Icônes sans cadre au repos ; l'icône active (type=primary) est
   mise en valeur par un cercle fin + léger halo. */
.st-key-theme_switch {
  flex-direction: row !important; justify-content: flex-end; align-items: center;
  gap: 0.35rem; padding: 0.05rem 0;
}
.st-key-theme_switch [data-testid="stElementContainer"] {
  width: auto !important; flex: 0 0 auto !important;
}
.st-key-theme_switch .stButton,
.st-key-theme_switch [data-testid="stButton"] { width: auto !important; }
.st-key-theme_switch [data-testid="stButton"] button {
  width: 1.9rem !important; height: 1.9rem !important;
  min-height: 1.9rem !important; max-width: 1.9rem !important;
  padding: 0 !important; border-radius: 50% !important;
  font-size: 0.95rem !important; line-height: 1 !important;
  color: var(--ui-muted, #9aada4) !important;
  background: transparent !important; border: 1px solid transparent !important;
  box-shadow: none !important; opacity: 0.72;
  transition: transform .15s ease, background .15s ease,
              border-color .15s ease, box-shadow .15s ease, opacity .15s ease;
}
.st-key-theme_switch [data-testid="stButton"] button:hover {
  transform: translateY(-1px); opacity: 1;
  background: var(--ui-tag-bg, rgba(120,120,120,0.14)) !important;
}
.st-key-theme_switch [data-testid="stButton"] button[kind="primary"] {
  opacity: 1; color: var(--ui-accent) !important;
  background: var(--ui-tag-bg, rgba(120,120,120,0.14)) !important;
  border-color: var(--ui-accent) !important;
  box-shadow: 0 0 0 3px var(--ui-tag-bg, rgba(120,120,120,0.10)) !important;
}

/* ===== Champs de saisie & filtres : SOLUTION DÉFINITIVE (caduques blancs) ====
   MÊME BLOC CSS EXACT pour la barre de recherche ET tous les sélecteurs
   (Obédience, Type de Tawatur, Catégorie thématique, Classification des
   rapporteurs…). Deux plans combinés :
   - PLAN B (camouflage parfait) : le fond ET la bordure du widget portent
     EXACTEMENT la couleur de l'arrière-plan du thème (--ui-bg, vert sombre
     #0b1a17 en Sombre). Tout cadre résiduel hérite donc de la même teinte que
     le décor et devient invisible. Texte et flèche restent clairs (--ui-text).
   - PLAN A (transparence) : toutes les couches internes (div imbriqués,
     base-input, inputs, puces 'tag', conteneurs de listes) sont forcées en
     transparent et sans bordure ni ombre ; les styles par défaut blancs de
     Streamlit/BaseWeb sont neutralisés à tous les niveaux. */
div[data-baseweb="input"],
div[data-baseweb="select"],
[data-testid="stMultiSelect"] [data-baseweb="select"],
[data-testid="stSelectbox"] [data-baseweb="select"] {
  background-color: var(--ui-field-bg, #0b1f1a) !important;
  border: 1px solid var(--ui-field-border, #0b1f1a) !important;
  border-radius: 4px !important;
  box-shadow: none !important;
  outline: none !important;
  color: var(--ui-text) !important;
  transition: border-color .15s ease;
}
/* Survol / focus : léger fil d'accent, jamais de blanc, aucun anneau. */
div[data-baseweb="input"]:hover,
div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:hover,
div[data-baseweb="select"]:focus-within {
  border-color: color-mix(in srgb, var(--ui-accent) 45%, var(--ui-field-border, #0b1f1a)) !important;
  box-shadow: none !important;
  outline: none !important;
}
/* PLAN A — Éradication FORCÉE des fonds/bordures sur TOUTES les couches
   internes des sélecteurs, des puces et du champ texte. */
div[data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-baseweb="base-input"],
div[data-baseweb="listbox"],
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div > div:not([data-baseweb="tag"]),
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div:not([data-baseweb="tag"]),
div[data-testid="stMultiSelect"] div[data-baseweb="select"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] input {
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
}
/* PLAN A/B — Conteneurs de widgets : fond et bordure fusionnés dans le thème. */
[data-testid="stMultiSelect"],
[data-testid="stSelectbox"],
[data-testid="stMultiSelect"] > div,
[data-testid="stSelectbox"] > div {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
}
/* Étiquette de section (Classification des rapporteurs & de la chaîne). */
.filter-section-label {
  font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ui-muted) !important; font-weight: 600;
  margin: 0.55rem 0 0.15rem;
}
/* Métadonnées (Détails du Hadith) : aucune troncature, retour à la ligne garanti. */
[data-testid="stMetric"] { min-width: 0 !important; }
[data-testid="stMetricLabel"], [data-testid="stMetricValue"],
[data-testid="stMetricValue"] > div {
  white-space: normal !important; overflow: visible !important;
  text-overflow: clip !important; overflow-wrap: anywhere; word-break: break-word;
}
/* ===== Onglets de vue (Bibliothèque / Sources & Savants) ===== */
.st-key-view_switch { margin: 0.15rem 0 0.1rem; gap: 0.5rem; }
.st-key-view_switch [data-testid="stButton"] { width: 100% !important; }
.st-key-view_switch [data-testid="stButton"] button {
  white-space: nowrap;
  background: linear-gradient(135deg, rgba(16,185,129,0.14) 0%, rgba(16,185,129,0.05) 100%) !important;
  border: 1px solid var(--ui-accent, #10b981) !important;
  border-radius: 12px !important;
  color: var(--ui-text, #e2e8f0) !important;
  font-weight: 600 !important;
  letter-spacing: 0.01em !important;
  padding: 0.55rem 1.05rem !important;
  box-shadow: 0 4px 10px -2px rgba(0,0,0,0.28), inset 0 1px 0 rgba(255,255,255,0.06) !important;
  transition: background .3s ease, border-color .3s ease, box-shadow .3s ease, transform .18s ease !important;
}
.st-key-view_switch [data-testid="stButton"] button:hover {
  background: linear-gradient(135deg, rgba(16,185,129,0.28) 0%, rgba(16,185,129,0.12) 100%) !important;
  border-color: var(--ui-accent, #10b981) !important;
  box-shadow: 0 0 16px rgba(16,185,129,0.35), 0 4px 12px -2px rgba(0,0,0,0.3) !important;
  transform: translateY(-1px) !important;
}
.st-key-view_switch [data-testid="stButton"] button[kind="primary"] {
  background: linear-gradient(135deg, rgba(16,185,129,0.30) 0%, rgba(16,185,129,0.12) 100%) !important;
  border-color: #f59e0b !important;
  box-shadow: 0 0 0 1px rgba(245,158,11,0.35), 0 0 18px rgba(245,158,11,0.25) !important;
}
/* ===== Répertoire « Sources & Savants » (cartes adaptatives via var(--ui-*)) ===== */
.source-card {
  background: var(--ui-surface, #0f251e);
  border: 1px solid var(--ui-border, rgba(52,211,153,0.25));
  border-radius: 14px; padding: 1.05rem 1.15rem 1.15rem;
  box-shadow: 0 4px 14px rgba(0,0,0,0.22);
  color: var(--ui-text); display: flex; flex-direction: column;
  gap: 0.32rem; height: 100%;
}
.source-card .sc-title { font-family:'Lora',serif; font-size:1.02rem; font-weight:700;
  color: var(--ui-text); line-height:1.35; }
.source-card .sc-ar { font-family:'Amiri','Lora',serif; direction:rtl;
  font-size:1.08rem; color: var(--ui-accent); unicode-bidi:isolate; }
.source-card .sc-scholar { font-size:0.92rem; color: var(--ui-text); }
.source-card .sc-scholar b { font-weight:700; }
.source-card .sc-dates { font-size:0.82rem; color: var(--ui-accent); font-weight:600; }
.source-card .sc-contribution { font-size:0.86rem; line-height:1.55;
  color: var(--ui-text); opacity:0.95; }
.source-card .sc-links { font-size:0.8rem; color: var(--ui-muted); line-height:1.6;
  padding-top:0.1rem; border-top:1px dashed var(--ui-border); }
"""


def _ornament(hexcolor, opacity=0.10):
    """Motif géométrique islamique (étoile à 8 branches) en filigrane SVG."""
    hex_s = hexcolor.strip("#").upper()
    return (
        "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
        "width='72' height='72' viewBox='0 0 72 72'%3E"
        "%3Cg fill='none' stroke='%23" + hex_s + "' stroke-opacity='" + str(opacity) + "'%3E"
        "%3Crect x='18' y='18' width='36' height='36'/%3E"
        "%3Crect x='18' y='18' width='36' height='36' transform='rotate(45 36 36)'/%3E"
        "%3Ccircle cx='36' cy='36' r='5'/%3E%3C/g%3E%3C/svg%3E\")"
    )


def _accent(theme):
    return {"Sombre": "#34d399", "Clair": "#0f7a4d", "Sépia": "#b98a44"}[theme]


DARK_CSS = """
<style>
__FONTS__
* { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
body, .stApp { background: radial-gradient(ellipse at top, #0b1f1a 0%, #050d0b 100%); color: #dcefe6; }
:root, .stApp {
  --ui-bg:#0b1f1a; --ui-surface:#0f251e; --ui-surface-2:#123027; --ui-border:rgba(52,211,153,0.25);
  --ui-text:#dcefe6; --ui-muted:#93b7a8; --ui-accent:#34d399;
  --ui-tag-bg:rgba(16,185,129,0.16); --ui-tag-text:#a7f3d0;
  --ui-btn-bg:linear-gradient(180deg,#1f9d63,#0f7a4d); --ui-btn-bg-strong:linear-gradient(180deg,#18a06b,#0f7d54);
  --ui-btn-text:#ffffff;
  --ui-menu-bg:#061310; --ui-menu-text:#e6f4ec; --ui-menu-hover:#143a2c; --ui-menu-border:rgba(52,211,153,0.30);
  --ui-field-bg:var(--ui-bg); --ui-field-border:var(--ui-bg);
}
h1, h2, h3, h4 { color: #eafaf1; letter-spacing: -0.02em; }

/* ---- En-tête ornemental (art islamique) ---- */
.app-header { text-align:center; padding:1.1rem 0 0.7rem; position:relative; }
.app-header::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 84px auto; background-position: top center; background-repeat: repeat;
  opacity:0.55; pointer-events:none; }
.app-header > * { position:relative; z-index:1; }
.app-title { font-family:'Amiri','Lora',serif; font-weight:700; font-size:3.05rem; line-height:1.15;
  margin:0.2rem 0 0; color:#f2fbf6; letter-spacing:0.01em; text-shadow:0 2px 20px rgba(16,185,129,0.28); }
.app-subtitle { font-size:0.92rem; letter-spacing:0.16em; text-transform:uppercase;
  color:#8fd9b6; margin-top:0.4rem; font-weight:600; }
.orn-row { display:flex; align-items:center; justify-content:center; gap:0.9rem; max-width:660px; margin:0.5rem auto; }
.orn-line { height:1px; flex:1; background: linear-gradient(90deg, transparent, __ACCENT__, transparent); }
.orn-star { color: __ACCENT__; font-size:1.35rem; line-height:1; }
.theme-switch-label { text-align:right; font-size:0.74rem; letter-spacing:0.14em; text-transform:uppercase;
  color:#7fcba8; margin-bottom:0.3rem; font-weight:600; }

/* ---- Cartes de sélection ---- */
.theme-card { position: relative; overflow: hidden; border-radius: 16px; padding: 1.15rem 1.25rem 1.3rem;
  background: linear-gradient(180deg, #0c1f1a 0%, #0a1713 100%); border: 1px solid rgba(52,211,153,0.18);
  color: #dcefe6; box-shadow: 0 4px 18px rgba(2,6,23,0.55); transition: transform .18s ease, box-shadow .18s ease; }
.theme-card:hover { transform: translateY(-3px); box-shadow: 0 10px 26px rgba(16,185,129,0.28); }
.theme-card::before { content:""; position:absolute; top:0; left:0; right:0; height:4px;
  background: linear-gradient(90deg, transparent, __ACCENT__, transparent); opacity:.9; }
.theme-card::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 96px auto; background-position: top right; background-repeat: repeat; }
.theme-card > * { position: relative; z-index: 1; }
.theme-card strong { display:block; font-family:'Lora', serif; font-size:1.06rem; line-height:1.5;
  margin-top:0.5rem; color:#eafaf1; }
.theme-card div { position: relative; z-index: 1; }

/* ---- Badges ---- */
.badge { display:inline-block; padding:0.22rem 0.62rem; border-radius:8px; font-size:0.8rem; font-weight:500;
  border:1px solid rgba(52,211,153,0.3); background:rgba(16,185,129,0.12); color:#a7f3d0; margin:0 0.35rem 0.35rem 0; }

/* ---- Textes du hadith : traduction française en vedette ---- */
.matn-label { font-family:'Lora',serif; font-size:0.78rem; font-weight:600; letter-spacing:0.16em;
  text-transform:uppercase; color:__ACCENT__; margin:0 0 0.4rem 0.15rem; opacity:0.95; }
.translation-fr { font-family:'Lora',serif; font-size:1.22rem; line-height:2.1; color:#eefaf3;
  background:linear-gradient(180deg, #0c231c 0%, #081913 100%);
  border:1px solid rgba(52,211,153,0.30); border-left:4px solid __ACCENT__;
  border-radius:14px; padding:1.35rem 1.6rem; margin:0 0 1.1rem 0;
  box-shadow:0 8px 24px rgba(0,0,0,0.28); }
.arabic-matn { font-family:'Amiri','Noto Sans Arabic',serif; font-size:1.7rem; line-height:2.6rem;
  text-align:right; direction:rtl; unicode-bidi:isolate; padding:1.35rem 1.7rem;
  background:rgba(6,30,24,0.5); border:1px solid rgba(52,211,153,0.18); border-left:4px solid __ACCENT__;
  border-radius:14px; color:#eaf3ec; }

/* ---- Boutons (verts profonds, jamais noirs) ---- */
.stButton, [data-testid="stButton"] { width: 100%; }
.stButton > button { width:100%; border-radius:10px; padding:0.56rem 0.9rem; font-weight:600;
  background: linear-gradient(180deg, #1f9d63, #0f7a4d); color:#ffffff; border: 1px solid rgba(52,211,153,0.28);
  cursor:pointer; transition: box-shadow .18s ease, filter .18s ease, background .18s ease; }
.stButton > button:hover { box-shadow: 0 6px 18px rgba(16,185,129,0.38); filter: brightness(1.08); }
.stButton > button:active { filter: brightness(0.95); }
.stButton > button[kind="primary"] { background: linear-gradient(180deg, #18a06b, #0f7d54);
  border-color: rgba(52,211,153,0.7);
  box-shadow: 0 0 0 1px rgba(52,211,153,0.4), 0 6px 16px rgba(16,185,129,0.3); }

/* ---- Légende dédiée du réseau ---- */
.chart-legend { display:flex; flex-wrap:wrap; align-items:center; gap:0.35rem 1.15rem;
  margin:0.2rem 0 0.9rem 0; padding:0.55rem 0.9rem; border-radius:10px; font-size:0.86rem;
  border:1px dashed rgba(52,211,153,0.34); background: rgba(6,30,24,0.5); color:#b7d9ca; line-height:1.6; }
.chart-legend .dot { display:inline-block; width:13px; height:13px; border-radius:50%;
  margin-right:0.35rem; vertical-align:-2px; }
.chart-legend .legend-item { display:inline-flex; align-items:center; }
__SAFETY__
/* CORRECTION CRITIQUE — Suppression totale des bordures et fonds blancs en
   mode sombre. Ce bloc n'est injecté QUE par DARK_CSS (thème Sombre) : les
   thèmes Clair/Sépia ne sont jamais touchés. La boîte visible reçoit un fond
   légèrement surélevé par rapport à la page (blanc translucide → gris-vert
   très sombre) et un liseré vert 1px de la charte (#10b981). Placé après
   __SAFETY__ (le Plan A), il gagne la cascade aux égalités de spécificité. */
div[data-baseweb="select"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
div[data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] [data-baseweb="select"] > div,
div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid #10b981 !important;
    border-radius: 6px !important;
    box-shadow: none !important;
}

/* Texte interne du sélecteur (« Choose options », valeur, saisie, placeholder) :
   clair et parfaitement lisible sur le fond surélevé. */
div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
div[data-baseweb="select"] div[class*="value"],
div[data-baseweb="select"] div[class*="placeholder"],
div[data-baseweb="select"] div[class*="Value"],
div[data-baseweb="select"] div[class*="Placeholder"],
div[data-baseweb="select"] [data-baseweb="tag"] {
    color: #f8fafc !important;
}

/* Placeholder natif du input BaseWeb */
div[data-baseweb="select"] input::placeholder {
    color: #cbd5e1 !important;
    opacity: 1 !important;
}

/* Puces (tags) des valeurs sélectionnées : teinte verte translucide de la
   charte et texte clair, cohérents avec le mode sombre. */
div[data-baseweb="tag"] {
    background-color: rgba(16, 185, 129, 0.2) !important;
    border: 1px solid #10b981 !important;
    color: #ffffff !important;
}
div[data-baseweb="tag"] span { color: #ffffff !important; }

/* Compteur global de hadiths dans l'en-tête */
.app-counter {
  font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ui-accent); font-weight: 600; margin: 0.4rem 0 0.2rem;
  opacity: 0.9;
}
.app-counter strong {
  font-family: 'Lora', serif; font-size: 1.1rem; font-weight: 700;
  color: var(--ui-text); background: linear-gradient(90deg, var(--ui-accent), #f59e0b);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; padding: 0 0.2rem;
}

/* Supprime l'effet de focus blanc/clair de Streamlit. */
[data-baseweb="select"] > div:focus-within,
[data-baseweb="select"] > div:hover {
    border-color: #34d399 !important;
    box-shadow: 0 0 0 1px rgba(16, 185, 129, 0.35) !important;
}

/* Clair & Sépia — cadres volontairement VISIBLES (fond blanc/écru + fine
   bordure verte ou brune) : la régression du blanc reste ici assumée. */
</style>
"""

LIGHT_CSS = """
<style>
__FONTS__
* { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
body, .stApp { background: linear-gradient(180deg, #f6fbf8 0%, #eaf4ee 100%); color: #14261d; }
:root, .stApp {
  --ui-bg:#f6fbf8; --ui-surface:#ffffff; --ui-surface-2:#eef6f1; --ui-border:#d5e8dd;
  --ui-text:#14261d; --ui-muted:#5c7a6c; --ui-accent:#0f7a4d;
  --ui-tag-bg:#e9f6ee; --ui-tag-text:#0f7a4d;
  --ui-btn-bg:linear-gradient(180deg,#1f9d63,#178052); --ui-btn-bg-strong:linear-gradient(180deg,#12b76a,#0e8a52);
  --ui-btn-text:#ffffff;
  --ui-menu-bg:#e8f1ec; --ui-menu-text:#12261c; --ui-menu-hover:#d7e9df; --ui-menu-border:#c9e0d4;
  --ui-field-bg:#ffffff; --ui-field-border:#c6e0d2;
}
h1, h2, h3, h4 { color: #0f2419; letter-spacing: -0.01em; }

/* ---- En-tête ornemental (art islamique) ---- */
.app-header { text-align:center; padding:1.1rem 0 0.7rem; position:relative; }
.app-header::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 84px auto; background-position: top center; background-repeat: repeat;
  opacity:0.55; pointer-events:none; }
.app-header > * { position:relative; z-index:1; }
.app-title { font-family:'Amiri','Lora',serif; font-weight:700; font-size:3.05rem; line-height:1.15;
  margin:0.2rem 0 0; color:#10241a; letter-spacing:0.01em; }
.app-subtitle { font-size:0.92rem; letter-spacing:0.16em; text-transform:uppercase;
  color:#2f7d5b; margin-top:0.4rem; font-weight:600; }
.orn-row { display:flex; align-items:center; justify-content:center; gap:0.9rem; max-width:660px; margin:0.5rem auto; }
.orn-line { height:1px; flex:1; background: linear-gradient(90deg, transparent, __ACCENT__, transparent); }
.orn-star { color: __ACCENT__; font-size:1.35rem; line-height:1; }
.theme-switch-label { text-align:right; font-size:0.74rem; letter-spacing:0.14em; text-transform:uppercase;
  color:#3d8462; margin-bottom:0.3rem; font-weight:600; }

/* ---- Cartes de sélection ---- */
.theme-card { position: relative; overflow: hidden; border-radius: 16px; padding: 1.15rem 1.25rem 1.3rem;
  background: #ffffff; border: 1px solid #d5e8dd; color: #14261d;
  box-shadow: 0 2px 10px rgba(15,60,40,0.07); transition: transform .18s ease, box-shadow .18s ease; }
.theme-card:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(16,120,80,0.16); }
.theme-card::before { content:""; position:absolute; top:0; left:0; right:0; height:4px;
  background: linear-gradient(90deg, transparent, __ACCENT__, transparent); opacity:.85; }
.theme-card::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 96px auto; background-position: top right; background-repeat: repeat; }
.theme-card > * { position: relative; z-index: 1; }
.theme-card strong { display:block; font-family:'Lora', serif; font-size:1.06rem; line-height:1.5;
  margin-top:0.5rem; color:#0f2419; }
.theme-card div { position: relative; z-index: 1; }

/* ---- Badges ---- */
.badge { display:inline-block; padding:0.22rem 0.62rem; border-radius:8px; font-size:0.8rem; font-weight:500;
  border:1px solid #a7d7bb; background:#e9f6ee; color:#0f7a4d; margin:0 0.35rem 0.35rem 0; }

/* ---- Textes du hadith : traduction française en vedette ---- */
.matn-label { font-family:'Lora',serif; font-size:0.78rem; font-weight:600; letter-spacing:0.16em;
  text-transform:uppercase; color:__ACCENT__; margin:0 0 0.4rem 0.15rem; opacity:0.95; }
.translation-fr { font-family:'Lora',serif; font-size:1.22rem; line-height:2.1; color:#152a20;
  background:linear-gradient(180deg, #ffffff 0%, #f1f9f4 100%);
  border:1px solid #cfe6da; border-left:4px solid __ACCENT__;
  border-radius:14px; padding:1.35rem 1.6rem; margin:0 0 1.1rem 0;
  box-shadow:0 4px 14px rgba(15,60,40,0.08); }
.arabic-matn { font-family:'Amiri','Noto Sans Arabic',serif; font-size:1.7rem; line-height:2.6rem;
  text-align:right; direction:rtl; unicode-bidi:isolate; padding:1.35rem 1.7rem;
  background:#ffffff; border:1px solid #d5e8dd; border-left:4px solid __ACCENT__;
  border-radius:14px; color:#14261d; box-shadow:0 1px 3px rgba(15,60,40,0.06); }

/* ---- Boutons ---- */
.stButton, [data-testid="stButton"] { width: 100%; }
.stButton > button { width:100%; border-radius:10px; padding:0.56rem 0.9rem; font-weight:600;
  background: linear-gradient(180deg, #1f9d63, #178052); color:#ffffff; border: 1px solid rgba(16,122,77,0.35);
  cursor:pointer; transition: box-shadow .18s ease, filter .18s ease, background .18s ease; }
.stButton > button:hover { box-shadow: 0 6px 16px rgba(31,157,99,0.32); filter: brightness(1.06); }
.stButton > button:active { filter: brightness(0.95); }
.stButton > button[kind="primary"] { background: linear-gradient(180deg, #12b76a, #0e8a52);
  border-color: rgba(16,122,77,0.6);
  box-shadow: 0 0 0 1px rgba(18,183,106,0.45), 0 6px 16px rgba(31,157,99,0.3); }

/* ---- Légende dédiée du réseau ---- */
.chart-legend { display:flex; flex-wrap:wrap; align-items:center; gap:0.35rem 1.15rem;
  margin:0.2rem 0 0.9rem 0; padding:0.55rem 0.9rem; border-radius:10px; font-size:0.86rem;
  border:1px dashed #cfe6da; background:#f1f8f4; color:#2c4a3d; line-height:1.6; }
.chart-legend .dot { display:inline-block; width:13px; height:13px; border-radius:50%;
  margin-right:0.35rem; vertical-align:-2px; }
.chart-legend .legend-item { display:inline-flex; align-items:center; }

/* Compteur global de hadiths dans l'en-tête */
.app-counter {
  font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ui-accent); font-weight: 600; margin: 0.4rem 0 0.2rem;
  opacity: 0.9;
}
.app-counter strong {
  font-family: 'Lora', serif; font-size: 1.1rem; font-weight: 700;
  color: var(--ui-text); background: linear-gradient(90deg, var(--ui-accent), #f59e0b);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; padding: 0 0.2rem;
}

__SAFETY__
</style>
"""

SEPIA_CSS = """
<style>
__FONTS__
* { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
body, .stApp { background: radial-gradient(ellipse at top, #f8f3e3 0%, #efe6d0 100%); color: #4b3d29; }
:root, .stApp {
  --ui-bg:#f8f3e3; --ui-surface:#fffaf0; --ui-surface-2:#f5ecd7; --ui-border:rgba(139,115,85,0.35);
  --ui-text:#3a2f1e; --ui-muted:#7a6444; --ui-accent:#b98a44;
  --ui-tag-bg:rgba(249,240,214,0.9); --ui-tag-text:#6d5226;
  --ui-btn-bg:linear-gradient(180deg,#e2c184,#cba269); --ui-btn-bg-strong:linear-gradient(180deg,#d8b876,#b98a44);
  --ui-btn-text:#33271a;
  --ui-menu-bg:#f1ead6; --ui-menu-text:#33291a; --ui-menu-hover:#e6dcc2; --ui-menu-border:rgba(139,115,85,0.45);
  --ui-field-bg:#fffaf0; --ui-field-border:rgba(160,130,85,0.45);
}
h1, h2, h3, h4 { color: #3a2f1e; font-family: 'Lora', serif; letter-spacing: -0.01em; }

/* ---- En-tête ornemental (art islamique) ---- */
.app-header { text-align:center; padding:1.1rem 0 0.7rem; position:relative; }
.app-header::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 84px auto; background-position: top center; background-repeat: repeat;
  opacity:0.6; pointer-events:none; }
.app-header > * { position:relative; z-index:1; }
.app-title { font-family:'Amiri','Lora',serif; font-weight:700; font-size:3.05rem; line-height:1.15;
  margin:0.2rem 0 0; color:#33291a; letter-spacing:0.01em; }
.app-subtitle { font-size:0.92rem; letter-spacing:0.16em; text-transform:uppercase;
  color:#8a6d3b; margin-top:0.4rem; font-weight:600; }
.orn-row { display:flex; align-items:center; justify-content:center; gap:0.9rem; max-width:660px; margin:0.5rem auto; }
.orn-line { height:1px; flex:1; background: linear-gradient(90deg, transparent, __ACCENT__, transparent); }
.orn-star { color: __ACCENT__; font-size:1.35rem; line-height:1; }
.theme-switch-label { text-align:right; font-size:0.74rem; letter-spacing:0.14em; text-transform:uppercase;
  color:#8a6d3b; margin-bottom:0.3rem; font-weight:600; }

/* ---- Cartes de sélection ---- */
.theme-card { position: relative; overflow: hidden; border-radius: 16px; padding: 1.15rem 1.25rem 1.3rem;
  background: linear-gradient(180deg, #fdf7e7 0%, #f6ecD2 100%); border: 1px solid rgba(139,115,85,0.3);
  color: #3a2f1e; box-shadow: 0 2px 12px rgba(120,100,75,0.14); transition: transform .18s ease, box-shadow .18s ease; }
.theme-card:hover { transform: translateY(-3px); box-shadow: 0 10px 26px rgba(120,100,75,0.22); }
.theme-card::before { content:""; position:absolute; top:0; left:0; right:0; height:4px;
  background: linear-gradient(90deg, transparent, __ACCENT__, transparent); opacity:.9; }
.theme-card::after { content:""; position:absolute; inset:0; background-image: __ORNAMENT__;
  background-size: 96px auto; background-position: top right; background-repeat: repeat; }
.theme-card > * { position: relative; z-index: 1; }
.theme-card strong { display:block; font-family:'Lora', serif; font-size:1.06rem; line-height:1.5;
  margin-top:0.5rem; color:#3a2f1e; }
.theme-card div { position: relative; z-index: 1; }

/* ---- Badges ---- */
.badge { display:inline-block; padding:0.22rem 0.62rem; border-radius:8px; font-size:0.8rem; font-weight:500;
  border:1px solid rgba(185,138,68,0.45); background:rgba(249,240,214,0.9); color:#6d5226; margin:0 0.35rem 0.35rem 0; }

/* ---- Textes du hadith : traduction française en vedette ---- */
.matn-label { font-family:'Lora',serif; font-size:0.78rem; font-weight:600; letter-spacing:0.16em;
  text-transform:uppercase; color:__ACCENT__; margin:0 0 0.4rem 0.15rem; opacity:0.95; }
.translation-fr { font-family:'Lora',serif; font-size:1.22rem; line-height:2.1; color:#3a2c18;
  background:linear-gradient(180deg,#fffdf6 0%, #f7efd9 100%);
  border:1px solid rgba(139,115,85,0.35); border-left:4px solid __ACCENT__;
  border-radius:14px; padding:1.35rem 1.6rem; margin:0 0 1.1rem 0;
  box-shadow:0 4px 14px rgba(120,90,50,0.10); }
.arabic-matn { font-family:'Amiri','Noto Sans Arabic',serif; font-size:1.7rem; line-height:2.6rem;
  text-align:right; direction:rtl; unicode-bidi:isolate; padding:1.35rem 1.7rem;
  background:linear-gradient(180deg,#fffaf0 0%, #fdf6e3 100%); border:1px solid rgba(139,115,85,0.35);
  border-left:4px solid __ACCENT__; border-radius:14px; color:#3a2f1e; }

/* ---- Boutons (tons sablés / dorés, texte brun foncé lisible) ---- */
.stButton, [data-testid="stButton"] { width: 100%; }
.stButton > button { width:100%; border-radius:10px; padding:0.56rem 0.9rem; font-weight:700;
  background: linear-gradient(180deg, #e2c184, #cba269); color:#33271a; border: 1px solid rgba(139,115,85,0.55);
  cursor:pointer; transition: box-shadow .18s ease, filter .18s ease; }
.stButton > button:hover { box-shadow: 0 6px 16px rgba(139,115,85,0.35); filter: brightness(1.03); }
.stButton > button:active { filter: brightness(0.94); }
.stButton > button[kind="primary"] { background: linear-gradient(180deg, #d8b876, #b98a44);
  border-color: rgba(139,115,85,0.75);
  box-shadow: 0 0 0 1px rgba(185,138,68,0.5), 0 6px 16px rgba(139,115,85,0.3); }

/* ---- Légende dédiée du réseau ---- */
.chart-legend { display:flex; flex-wrap:wrap; align-items:center; gap:0.35rem 1.15rem;
  margin:0.2rem 0 0.9rem 0; padding:0.55rem 0.9rem; border-radius:10px; font-size:0.86rem;
  border:1px dashed rgba(139,115,85,0.5); background:rgba(250,245,230,0.85); color:#5b4a30; line-height:1.6; }
.chart-legend .dot { display:inline-block; width:13px; height:13px; border-radius:50%;
  margin-right:0.35rem; vertical-align:-2px; }
.chart-legend .legend-item { display:inline-flex; align-items:center; }

/* Compteur global de hadiths dans l'en-tête */
.app-counter {
  font-size: 0.78rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--ui-accent); font-weight: 600; margin: 0.4rem 0 0.2rem;
  opacity: 0.9;
}
.app-counter strong {
  font-family: 'Lora', serif; font-size: 1.1rem; font-weight: 700;
  color: var(--ui-text); background: linear-gradient(90deg, var(--ui-accent), #f59e0b);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; padding: 0 0.2rem;
}

__SAFETY__
</style>
"""

THEMES = {"Sombre": DARK_CSS, "Clair": LIGHT_CSS, "Sépia": SEPIA_CSS}
THEME_PLOT = {
    "Sombre": {
        "paper": "rgba(0,0,0,0)", "text": "#dcefe6", "edge": "#4f7d68", "madar": "#f472b6",
        "palette": {"thiqa": "#34d399", "hassan": "#eab308", "unknown": "#8fa89b",
                    "da'if": "#ef4444", "matrouk": "#b91c1c", "majhoul": "#a78bfa"},
    },
    "Clair": {
        "paper": "#ffffff", "text": "#14261d", "edge": "#9db8ac", "madar": "#db2777",
        "palette": {"thiqa": "#16a34a", "hassan": "#d97706", "unknown": "#8aa79a",
                    "da'if": "#dc2626", "matrouk": "#991b1b", "majhoul": "#7c3aed"},
    },
    "Sépia": {
        "paper": "#fdf6e3", "text": "#3e3426", "edge": "#a0784b", "madar": "#c2410c",
        "palette": {"thiqa": "#4d7c0f", "hassan": "#b45309", "unknown": "#a0896b",
                    "da'if": "#b91c1c", "matrouk": "#7f1d1d", "majhoul": "#7e22ce"},
    },
}


def theme_css(name):
    accent = _accent(name)
    return (THEMES[name].replace("__FONTS__", FONTS)
            .replace("__SAFETY__", SAFETY + WIDGET_CSS)
            .replace("__ACCENT__", accent)
            .replace("__ORNAMENT__", _ornament(accent)))


# ---------------------------------------------------------------------------
# 2b. Rendu réseau : disposition hiérarchique + figure Plotly
# ---------------------------------------------------------------------------
def layout_network(nodes, edges):
    """Disposition par niveaux (Compagnon en haut → Compilateur en bas),
    ordonnée par barycentre pour limiter les croisements de liens.
    Retourne {node_id: (x, y)} dans [0,1]."""
    if not nodes:
        return {}
    max_level = max((n["level"] for n in nodes), default=1) or 1

    levels = {}
    for n in nodes:
        levels.setdefault(n["level"], []).append(n)

    adjacency = {}
    for e in edges:
        adjacency.setdefault(e["source"], set()).add(e["target"])
        adjacency.setdefault(e["target"], set()).add(e["source"])

    idx = {}
    for lvl, ns in levels.items():
        ns.sort(key=lambda x: (-x["frequency"], -x["paths"]))
        for i, n in enumerate(ns):
            idx[n["id"]] = i

    # Quelques passes de barycentre pour aligner les nœuds liés.
    for _ in range(6):
        for lvl in sorted(levels):
            ns = levels[lvl]

            def bary(n):
                vals = [idx[m] for m in adjacency.get(n["id"], ()) if m in idx]
                return (sum(vals) / len(vals)) if vals else idx[n["id"]]

            ns.sort(key=bary)
            for i, n in enumerate(ns):
                idx[n["id"]] = i

    pos = {}
    for lvl, ns in levels.items():
        count = len(ns)
        y = (lvl / max_level) if max_level else 0.5
        for i, n in enumerate(ns):
            x = (i + 1) / (count + 1)
            pos[n["id"]] = (x, y)
    return pos


def build_network_figure(net, plot, highlight_madar, color_mode, mode="vertical"):
    """Figure Plotly du réseau complet des Turuq : tous les nœuds et liens,
    épaisseur/opacité des liens selon le poids (chemins), taille des nœuds
    selon la fréquence, couleur selon la fiabilité ou la fréquence."""
    nodes = net["nodes"]
    edges = net["edges"]
    pos = layout_network(nodes, edges, mode=mode)
    palette = plot["palette"]

    fig = go.Figure()

    # --- Liens regroupés en 5 paliers d'épaisseur (perf + lisibilité) ---
    max_w = max((e["weight"] for e in edges), default=1) or 1
    bucket_x = {i: [] for i in range(5)}
    bucket_y = {i: [] for i in range(5)}
    for e in edges:
        if e["source"] not in pos or e["target"] not in pos:
            continue
        x0, y0 = pos[e["source"]]
        x1, y1 = pos[e["target"]]
        b = min(4, int((e["weight"] / max_w) * 5))
        bucket_x[b] += [x0, x1, None]
        bucket_y[b] += [y0, y1, None]
    for b in range(5):
        if bucket_x[b]:
            fig.add_trace(go.Scatter(
                x=bucket_x[b], y=bucket_y[b], mode="lines",
                line=dict(width=0.8 + 1.35 * b, color=plot["edge"]),
                opacity=0.18 + 0.16 * b, hoverinfo="skip", showlegend=False,
            ))

    # --- Nœuds en une seule trace (tailles/couleurs par point) ---
    fmax = max((n["frequency"] for n in nodes), default=1) or 1
    xs, ys, sizes, colors, texts, hovers = [], [], [], [], [], []
    id_size = {}
    for n in nodes:
        if n["id"] not in pos:
            continue
        x, y = pos[n["id"]]
        size = 16 + min(28, 4 * n["frequency"])
        id_size[n["id"]] = size
        xs.append(x)
        ys.append(y)
        sizes.append(size)
        if color_mode == "Fréquence":
            t = n["frequency"] / fmax
            colors.append(f"rgb({int(56 + 199 * t)},{int(132 - 52 * t)},{int(255 - 215 * t)})")
        else:
            colors.append(palette.get(n["reliability"], palette["unknown"]))
        texts.append(n["label"])
        hovers.append(
            f"<b>{n['label']}</b><br>Fiabilité : {n.get('reliability_fr') or '—'}"
            f"<br>Tabaqa : {n.get('tabaqa') or 'N/A'}<br>Niveau : {n['level']}"
            f"<br>Fréquence : {n['frequency']} voie(s) • {n['paths']} chemins"
            + ("<br>★ Pivot (Madar)" if n.get("is_madar") else "")
        )
    fig.add_trace(go.Scatter(
        x=xs, y=ys, mode="markers+text",
        marker=dict(size=sizes, color=colors, line=dict(width=1.5, color=plot["text"])),
        text=texts, textposition="bottom center",
        textfont=dict(size=10, color=plot["text"]),
        hoverinfo="text", hovertext=hovers, showlegend=False,
    ))

    # --- Surbrillance des pivots (anneaux) ---
    if highlight_madar:
        mx = [pos[n["id"]][0] for n in nodes if n.get("is_madar") and n["id"] in pos]
        my = [pos[n["id"]][1] for n in nodes if n.get("is_madar") and n["id"] in pos]
        ms = [id_size[n["id"]] + 10 for n in nodes if n.get("is_madar") and n["id"] in pos]
        if mx:
            fig.add_trace(go.Scatter(
                x=mx, y=my, mode="markers",
                marker=dict(size=ms, color="rgba(0,0,0,0)",
                            line=dict(width=3, color=plot["madar"])),
                hoverinfo="skip", showlegend=False,
            ))

    # --- Légende : gérée en HTML (conteneur dédié, jamais superposée) ---

    fig.update_layout(
        paper_bgcolor=plot["paper"], plot_bgcolor=plot["paper"],
        font=dict(color=plot["text"]),
        hoverlabel=dict(bgcolor=plot["paper"], font=dict(color=plot["text"])),
        height=720, dragmode=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   range=[-0.05, 1.05], fixedrange=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                   range=[-0.09, 1.09], fixedrange=False),
        margin=dict(l=20, r=20, t=12, b=20),
    )
    return fig


def build_legend_html(plot, color_mode, highlight_madar):
    """Légende du réseau dans un conteneur HTML dédié (jamais superposée
    au texte ni au graphe : ligne séparée sous l'en-tête de section)."""
    palette = plot["palette"]
    if color_mode == "Fréquence":
        grad = "linear-gradient(90deg, #16a34a 0%, #eab308 50%, #dc2626 100%)"
        items = [
            f'<span class="legend-item"><span class="dot" style="background:{grad}"></span>'
            "Fréquence passerelle : faible → forte</span>"
        ]
    else:
        entries = [
            ("thiqa", "Fiable (Thiqa)"), ("hassan", "Bon (Hasan)"),
            ("unknown", "Inconnu"), ("da'if", "Faible (Da'if)"),
            ("matrouk", "Rejeté (Matrouk)"), ("majhoul", "Inconnu (Majhoul)"),
        ]
        items = [
            f'<span class="legend-item"><span class="dot" style="background:{palette.get(c, palette["unknown"])}"></span>{lab}</span>'
            for c, lab in entries
        ]
        if highlight_madar:
            items.append(
                f'<span class="legend-item"><span class="dot" '
                f'style="background:transparent;border:2.5px solid {plot["madar"]}"></span>'
                "Pivot (Madar)</span>"
            )
    return '<div class="chart-legend">' + "".join(items) + "</div>"


def _source_hits(source, text_lines):
    """Lignes texte (sources de hadith / de chaîne) qui référencent cette source."""
    toks = [t.lower() for t in source.get("tokens", [])]
    if not toks:
        return []
    return [l for l in text_lines if any(t in (l or "").lower() for t in toks)]


def _source_stats(source, hadiths, chains):
    """Lien de la source avec l'outil : nombre de hadiths et de chaînes la
    citant, familles thématiques associées."""
    n_had, n_ch = 0, 0
    cats = set()
    for h in hadiths:
        vhits = _source_hits(source, h.validation_sources or [])
        ch_hits = 0
        for voie in h.turuq or []:
            c = chains.get(voie.isnad_chain_id)
            if c and _source_hits(source, c.sources or []):
                ch_hits += 1
        if vhits or ch_hits:
            n_had += 1
            if h.thematic_category:
                cats.add(h.thematic_category)
        n_ch += ch_hits
    return n_had, n_ch, sorted(cats)[:3]


def render_sources_view(hadiths, chains):
    """Vue « Sources & Savants » : répertoire des recueils et compilateurs."""
    st.subheader("Sources & Savants du corpus")
    st.caption(
        "Répertoire des sources hadithiques mobilisées par l'outil — compilateurs, "
        "obédience, période du savant et contribution aux Turuq (voies de "
        "transmission) ainsi qu'aux hadiths référencés."
    )
    _ob_choices = ["Commun (Sunnite & Chiite)", "Sunnite", "Chiite"]
    with st.container():
        s1, s2, _ = st.columns([2.2, 1.4, 2.4])
        with s1:
            src_search = st.text_input(
                "Rechercher une source / un savant",
                key="src_search",
                placeholder="Nom du recueil ou du savant…",
            )
        with s2:
            src_ob = st.multiselect(
                "Obédience", _ob_choices, key="src_ob", default=[]
            )
    rows = []
    q = (src_search or "").strip().lower()
    for src in SOURCES:
        n_had, n_ch, cats = _source_stats(src, hadiths, chains)
        obey = obedience_fr(src["obedience"])
        if src_ob and obey not in set(src_ob):
            continue
        if q:
            hay = (
                f'{src["collection_fr"]} {src["scholar_fr"]} '
                f'{src["collection_ar"]} {src["scholar_ar"]}'
            ).lower()
            if q not in hay:
                continue
        rows.append((n_had + n_ch, n_had, n_ch, cats, src))
    rows.sort(key=lambda r: (-r[0], r[4]["collection_fr"].lower()))
    st.markdown(
        '<div style="font-size:0.8rem;color:var(--ui-muted);margin:0.2rem 0 0.6rem;">'
        f"{len(SOURCES)} sources répertoriées · {len(rows)} affichée(s) · "
        "tri : contribution décroissante</div>",
        unsafe_allow_html=True,
    )
    if not rows:
        st.info("Aucune source ne correspond à ces filtres.")
        return
    cols = st.columns(3)
    for i, (_score, n_had, n_ch, cats, src) in enumerate(rows):
        with cols[i % 3]:
            badge = f'<span class="badge">{obedience_fr(src["obedience"])}</span>'
            cats_html = " · ".join(cats) if cats else "référence transversale"
            st.markdown(
                f'<div class="source-card">'
                f"<div>{badge}</div>"
                f'<div class="sc-title">{src["collection_fr"]}</div>'
                f'<div class="sc-ar">{src["collection_ar"]}</div>'
                f'<div class="sc-scholar"><b>{src["scholar_fr"]}</b></div>'
                f'<div class="sc-dates">{src["dates_fr"]} · {src["century_hijri"]}</div>'
                f'<div class="sc-contribution">{src["contribution"]}</div>'
                f'<div class="sc-links">🔗 {n_had} hadith(s) · {n_ch} chaîne(s) · '
                f"🏷️ {cats_html}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )


# ---------------------------------------------------------------------------
# 3. En-tête + sélecteur de thème (boutons à icônes)
# ---------------------------------------------------------------------------
# Défilement fluide vers la section de lecture/détails au clic sur « Consulter ».
# __NONCE__ est remplacé à chaque sélection : le contenu du composant change, ce
# qui force Streamlit à recharger l'iframe et donc à ré-exécuter le script à
# CHAQUE clic (sinon le défilement ne se produirait qu'à la première sélection).
SCROLL_TO_DETAIL_JS = """
<script>
/* __NONCE__ */
(function () {
  function go() {
    var doc = window.parent.document;
    var el = doc.getElementById('detail-section');
    if (!el) { return false; }
    var sc = doc.querySelector('[data-testid="stMain"]') ||
             doc.querySelector('[data-testid="stAppViewContainer"]') ||
             doc.scrollingElement;
    if (sc && sc.scrollTo) {
      var top = el.getBoundingClientRect().top +
                (sc.scrollTop || 0) - 12;
      sc.scrollTo({ top: top, behavior: 'smooth' });
    } else {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    return true;
  }
  var tries = 0;
  var t = setInterval(function () {
    if (go() || ++tries > 12) { clearInterval(t); }
  }, 120);
})();
</script>
"""

# Bouton « Retour en haut » : n'apparaît qu'au défilement ; remontée fluide.
BACK_TO_TOP_JS = """
<script>
(function () {
  var doc = window.parent.document;
  if (doc.__bttInit) return;
  doc.__bttInit = true;

  function scroller() {
    return doc.querySelector('[data-testid="stMain"]') ||
           doc.querySelector('[data-testid="stAppViewContainer"]') ||
           doc.scrollingElement || doc.documentElement;
  }
  function pos() {
    var a = 0, sc = scroller();
    if (sc && typeof sc.scrollTop === 'number') a = Math.max(a, sc.scrollTop);
    var se = doc.scrollingElement;
    if (se && typeof se.scrollTop === 'number') a = Math.max(a, se.scrollTop);
    try { a = Math.max(a, window.parent.scrollY || 0); } catch (e) {}
    return a;
  }
  function refresh() {
    var b = doc.querySelector('.back-to-top');
    if (!b) return;
    if (pos() > 260) b.classList.add('visible');
    else b.classList.remove('visible');
  }
  doc.addEventListener('scroll', refresh, true);
  doc.addEventListener('wheel', refresh, { passive: true, capture: true });
  doc.addEventListener('touchmove', refresh, { passive: true, capture: true });
  doc.addEventListener('click', function (e) {
    var b = e.target && e.target.closest ? e.target.closest('.back-to-top') : null;
    if (!b) return;
    e.preventDefault();
    var s = scroller();
    if (s && s.scrollTo) s.scrollTo({ top: 0, behavior: 'smooth' });
    var se = doc.scrollingElement;
    if (se && se.scrollTo) se.scrollTo({ top: 0, behavior: 'smooth' });
    try { window.parent.scrollTo({ top: 0, behavior: 'smooth' }); } catch (err) {}
  }, true);
  try {
    new MutationObserver(refresh).observe(doc.body, { childList: true, subtree: true });
  } catch (e) {}
  setInterval(refresh, 800);
  refresh();
})();
</script>
"""

THEME_ICONS = [("Sombre", "🌙"), ("Clair", "☀️"), ("Sépia", "📜")]
if st.session_state.get("theme") not in ("Sombre", "Clair", "Sépia"):
    st.session_state.theme = "Sombre"

# Changement de thème via les icônes du sélecteur (paramètre d'URL).
_qp_theme = st.query_params.get("theme")
if _qp_theme in ("Sombre", "Clair", "Sépia"):
    st.session_state.theme = _qp_theme

theme = st.session_state.theme
st.markdown(theme_css(theme), unsafe_allow_html=True)
st.markdown('<div id="top"></div>', unsafe_allow_html=True)
st.markdown(
    '<a class="back-to-top" href="#top" title="Retour en haut" '
    'aria-label="Retour en haut">↑</a>',
    unsafe_allow_html=True,
)
st.iframe(BACK_TO_TOP_JS, height=1)
plot = THEME_PLOT[theme]

# Sélecteur d'ambiance : rangée compacte de boutons-icônes, alignée à droite.
# Un st.button déclenche un simple rerun (aucun rechargement de page) : le
# hadith sélectionné et le défilement sont donc préservés au changement de
# thème. Le paramètre d'URL ?theme=… reste supporté pour les liens directs.
_tl, _tr = st.columns([6, 2])
with _tr:
    with st.container(key="theme_switch"):
        for _name, _icon in THEME_ICONS:
            if st.button(
                _icon,
                key=f"theme_{_name}",
                help=f"Thème {_name}",
                type="primary" if _name == st.session_state.theme else "secondary",
            ):
                st.session_state.theme = _name
                st.rerun()

# En-tête principal ornementé (motifs géométriques islamiques).
total_hadiths = len(hadiths)
st.markdown(
    f"""
    <div class="app-header">
      <div class="orn-row">
        <span class="orn-line"></span><span class="orn-star">۞</span><span class="orn-line"></span>
      </div>
      <h1 class="app-title">Tawatur Hadith</h1>
      <div class="app-subtitle">Visualisation des Hadiths Mutawatir · Isnad & Turuq</div>
      <div class="app-counter">Nombre total de hadiths indexés : <strong>{total_hadiths}</strong></div>
      <div class="orn-row">
        <span class="orn-line"></span><span class="orn-star">❖</span><span class="orn-line"></span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# 3bis. Onglets de vue : Bibliothèque des Hadiths / Sources & Savants
# ---------------------------------------------------------------------------
if "view" not in st.session_state:
    st.session_state.view = "hadiths"
_view = st.session_state.view
with st.container(key="view_switch"):
    _tab1, _tab2, _tabx = st.columns([1, 1, 4])
    with _tab1:
        if st.button(
            "📖 La Bibliothèque",
            key="view_hadiths",
            type="primary" if _view == "hadiths" else "secondary",
            help="Parcourir, filtrer et consulter les hadiths mutawatir",
        ):
            st.session_state.view = "hadiths"
            st.rerun()
    with _tab2:
        if st.button(
            "📚 Sources & Savants",
            key="view_sources",
            type="primary" if _view == "sources" else "secondary",
            help="Répertoire des recueils et compilateurs mobilisés",
        ):
            st.session_state.view = "sources"
            st.rerun()

if _view == "sources":
    render_sources_view(hadiths, chains)
    st.markdown("---")
    st.caption("Corpus islamique d'étude comparative des hadiths mutawatir.")
    st.stop()


# ---------------------------------------------------------------------------
# 4. Filtres
# ---------------------------------------------------------------------------
_categories = sorted({h.thematic_category for h in hadiths if h.thematic_category})
with st.container():
    c1, c2, c3, c4 = st.columns([1.7, 1.2, 1.2, 1.3])
    with c1:
        search = st.text_input("Rechercher un hadith", placeholder="Mot-clé dans titre/traduction…")
    with c2:
        obedience_filter = st.multiselect("Obédience", ["Commun (Sunnite & Chiite)", "Sunnite", "Chiite"], default=[])
    with c3:
        tawatur_filter = st.multiselect(
            "Type de Tawatur",
            ["Mutawatir Lafzi (mot à mot)", "Mutawatir Ma'nawi (par le sens)"],
            default=[],
        )
    with c4:
        category_filter = st.multiselect("Catégorie thématique", _categories, default=[])

# --- Section : classification des rapporteurs & de la chaîne de transmission ---
_generations = sorted({r.tabaqa for r in rawis.values() if r.tabaqa})
st.markdown(
    '<div class="filter-section-label">Classification des rapporteurs '
    '&amp; de la chaîne de transmission</div>',
    unsafe_allow_html=True,
)
with st.container():
    q1, q2, q3, q4 = st.columns([1.35, 1.35, 1.35, 1.45])
    with q1:
        chain_quality_filter = st.multiselect(
            "Qualité de la chaîne", CHAIN_QUALITY_OPTIONS, default=[]
        )
    with q2:
        grandeur_filter = st.multiselect(
            "Grandeur de la transmission", CHAIN_GRANDEUR_OPTIONS, default=[]
        )
    with q3:
        generation_filter = st.multiselect(
            "Génération présente (Tabaqa)", _generations, default=[]
        )
    with q4:
        relevance_sort = st.selectbox(
            "Trier par pertinence", RELEVANCE_SORT_OPTIONS, index=0
        )

filtered = list(hadiths)
if search:
    s = search.lower()
    filtered = [
        h for h in filtered
        if s in (h.title_fr or "").lower()
        or (h.matn_translation_fr and s in h.matn_translation_fr.lower())
        or s in (h.matn or "").lower()
    ]
if obedience_filter:
    of = set(obedience_filter)
    filtered = [h for h in filtered if obedience_fr(h.obedience.value) in of]
if tawatur_filter:
    tf = set(tawatur_filter)
    filtered = [h for h in filtered if tawatur_fr(h.tawatur_type.value) in tf]
if category_filter:
    cf = set(category_filter)
    filtered = [h for h in filtered if (h.thematic_category or "") in cf]
if chain_quality_filter:
    cqf = set(chain_quality_filter)
    filtered = [h for h in filtered if chain_quality_tier(h) in cqf]
if grandeur_filter:
    gf = set(grandeur_filter)
    filtered = [h for h in filtered if chain_grandeur_tier(h) in gf]
if generation_filter:
    genf = set(generation_filter)
    filtered = [h for h in filtered if chain_generations(h) & genf]

# Tri par pertinence (tri stable : les ex æquo conservent l'ordre d'authenticité).
_sort_key = relevance_sort_key(relevance_sort)
if _sort_key is not None:
    filtered.sort(key=_sort_key, reverse=True)


# ---------------------------------------------------------------------------
# 5. Grille de sélection (cartes)
# ---------------------------------------------------------------------------
st.subheader("Sélection du Hadith")
if not filtered:
    st.info("Aucun hadith ne correspond aux filtres sélectionnés.")
else:
    grid = st.columns(3)
    for i, h in enumerate(filtered):
        with grid[i % 3]:
            chain = primary_chain(h)
            n_paths = chain.path_count if chain and chain.path_count else "N/A"
            excerpt = (h.matn_translation_fr or h.matn or "")
            excerpt = excerpt[:110] + "…" if len(excerpt) > 110 else excerpt
            summit = is_summit(h)
            card_cls = "theme-card golden" if summit else "theme-card"
            flag = ('<span class="golden-flag">✦ Sommet du Tawatur</span>'
                    if summit else "")
            with st.container(key=f"card_{h.id}"):
                st.markdown(
                    f'<div class="{card_cls}">'
                    f'<div><span class="badge">{obedience_fr(h.obedience.value)}</span>'
                    f'<span class="badge">{tawatur_fr(h.tawatur_type.value)}</span></div>'
                    f'<strong>{h.title_fr}</strong>'
                    f'<div style="font-size:0.92rem;margin-top:0.4rem;">{excerpt}</div>'
                    f'<div style="font-size:0.82rem;margin-top:0.5rem;opacity:0.8;">'
                    f'🔗 {n_paths} chemins &nbsp;•&nbsp; 🏷️ {h.id.upper()}</div>'
                    f'{flag}'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                opened = st.button(
                    f"Consulter : {h.title_fr}",
                    key=f"sel_{h.id}",
                )
            if opened:
                st.session_state.selected_hadith_id = h.id
                st.session_state.scroll_detail = True
                st.session_state.scroll_nonce = st.session_state.get("scroll_nonce", 0) + 1
                st.rerun()


# ---------------------------------------------------------------------------
# 6. Détail du hadith sélectionné (protégé)
# ---------------------------------------------------------------------------
sel_id = st.session_state.get("selected_hadith_id")
sel = next((h for h in hadiths if h.id == sel_id), None)

if sel:
    st.markdown('<div id="detail-section"></div>', unsafe_allow_html=True)
    if st.session_state.pop("scroll_detail", False):
        _nonce = st.session_state.get("scroll_nonce", 0)
        st.iframe(
            SCROLL_TO_DETAIL_JS.replace("__NONCE__", str(_nonce)),
            height=1,
        )
    st.markdown("---")

    # Recherche rapide : changer de hadith sans remonter au catalogue.
    _dq_raw = st.text_input(
        "Rechercher un autre hadith",
        key="detail_search",
        placeholder="Titre, texte arabe ou traduction…",
    )
    _dq = _dq_raw.strip().lower()
    if _dq:
        _matches = [
            h for h in hadiths
            if _dq in (h.title_fr or "").lower()
            or _dq in (h.matn or "")
            or _dq in (h.matn_translation_fr or "").lower()
        ][:9]
        if not _matches:
            st.caption("Aucun hadith correspondant.")
        else:
            _mc = st.columns(min(3, len(_matches)))
            for _i, _h in enumerate(_matches):
                with _mc[_i % len(_mc)]:
                    if st.button(_h.title_fr, key=f"dq_{_h.id}", width="stretch"):
                        st.session_state.selected_hadith_id = _h.id
                        st.session_state.scroll_detail = True
                        st.session_state.scroll_nonce = st.session_state.get("scroll_nonce", 0) + 1
                        st.rerun()

    try:
        st.header(sel.title_fr)
        if sel.title_ar:
            st.caption(sel.title_ar)

        m1, m2, m3, m4 = st.columns([1.2, 1.25, 2.4, 0.75])
        m1.metric("Obédience", obedience_fr(sel.obedience.value))
        m2.metric("Type de Tawatur", tawatur_fr(sel.tawatur_type.value))
        m3.metric("Degré", sel.degree_fr or "—")
        m4.metric("Nombre de voies", len(sel.turuq or []))

        st.subheader("Texte du Hadith")
        _matn_blocks = []
        if sel.matn_translation_fr:
            _matn_blocks.append('<div class="matn-label">Traduction française</div>')
            _matn_blocks.append(f'<div class="translation-fr">{sel.matn_translation_fr}</div>')
        if sel.matn:
            _matn_blocks.append('<div class="matn-label">Texte arabe</div>')
            _matn_blocks.append(f'<div class="arabic-matn">{sel.matn}</div>')
        st.markdown("".join(_matn_blocks), unsafe_allow_html=True)

        sources = sel.validation_sources or []
        if sources:
            st.markdown("**Sources de validation :** " + " • ".join(sources))
        if sel.thematic_category:
            st.markdown("**Catégorie thématique :** " + sel.thematic_category)

        # Voies (Turuq) → réseau exhaustif de TOUTES les chaînes
        if sel.turuq:
            st.subheader("Réseau global des voies de transmission (Turuq)")
            st.caption(
                "Toutes les ramifications sont affichées simultanément : Compagnons (haut) → "
                "Successeurs (Tabi'un) → Imams compilateurs (bas), jusqu'à la convergence du Tawatur."
            )

            max_path = max((chains.get(t.isnad_chain_id).path_count or 0
                            for t in sel.turuq if chains.get(t.isnad_chain_id)), default=0)
            ctrl1, ctrl2, ctrl3, ctrl4 = st.columns([3, 2, 2, 2])
            with ctrl1:
                min_paths = st.slider(
                    "Force minimale d'une voie (chemins déclarés)",
                    min_value=0, max_value=max(10, max_path), value=0,
                    step=max(1, max_path // 20 or 1),
                    help="Écarte les voies faibles pour désencombrer un réseau étendu.",
                )
            with ctrl2:
                highlight_madar = st.checkbox("Surligner les pivots (Madar)", value=True)
            with ctrl3:
                color_mode = st.radio("Couleur des nœuds", ["Fiabilité", "Fréquence"], horizontal=True)
            with ctrl4:
                graph_mode = st.radio(
                    "Mode de visualisation",
                    ["Standard / Vertical", "Radial / Soleil", "Hybride"],
                    index=0,
                    horizontal=True,
                    help="Standard : arborescence chronologique (haut→bas). "
                         "Radial : disposition circulaire concentrique. "
                         "Hybride : compromis fluide."
                )
                mode_map = {
                    "Standard / Vertical": "vertical",
                    "Radial / Soleil": "radial",
                    "Hybride": "hybrid",
                }

            net = build_turuq_network(sel, chains, rawis, min_paths=min_paths)
            stats = net["stats"]
            nodes = net["nodes"]
            edges = net["edges"]

            if not nodes:
                st.warning("Aucune voie ne correspond au seuil de force sélectionné.")
            else:
                k1, k2, k3, k4 = st.columns(4)
                k1.metric("Chaînes affichées", stats["n_chains"])
                k2.metric("Chemins cumulés", stats["total_paths"])
                k3.metric("Narrateurs (nœuds)", stats["n_nodes"])
                k4.metric("Liens de transmission", stats["n_edges"])

                st.markdown(build_legend_html(plot, color_mode, highlight_madar), unsafe_allow_html=True)

                fig = build_network_figure(net, plot, highlight_madar, color_mode, mode=mode_map[graph_mode])
                st.plotly_chart(
                    fig, width="stretch",
                    config={"scrollZoom": False, "displaylogo": False,
                            "modeBarButtons": [["zoomIn2d", "zoomOut2d", "resetScale2d"]]},
                )
                st.caption(
                    "💡 Zoom ↔ avec les boutons + / − • Défilement de la page libre "
                    "• Déplacement (pan/glisser) désactivé • Double-clic = réinitialiser. "
                    "Épaisseur des liens ∝ nombre de chemins ; taille des nœuds ∝ fréquence."
                )

                madar = [n["label"] for n in nodes if n.get("is_madar")]
                if madar:
                    st.markdown("**Pivots (Madar) — narrateurs structurants du réseau :** " + ", ".join(madar))

                # Détail linéaire d'une voie (repliable)
                with st.expander("Détail linéaire d'une voie (Turuq)"):
                    labels = [t.label for t in sel.turuq]
                    chosen = st.selectbox("Sélectionner une voie", labels)
                    voie = next((x for x in sel.turuq if x.label == chosen), sel.turuq[0])
                    chain = chains.get(voie.isnad_chain_id)
                    if chain is None:
                        st.warning("Chaîne d'Isnad introuvable pour cette voie.")
                    else:
                        st.markdown("**Chaîne d'Isnad :**")
                        st.code(format_isnad_text(chain))
                        if chain.path_count:
                            st.markdown(f"**Nombre de chemins rapportés :** {chain.path_count}")
                        if chain.sources:
                            st.markdown("**Sources de cette chaîne :** " + " • ".join(chain.sources))
                        if voie.description:
                            st.markdown("**Remarque sur cette voie :** " + voie.description)

                # Narrateurs (Jarh wa Ta'dil) — issus du réseau fusionné
                st.subheader("Détails des narrateurs (Jarh wa Ta'dil)")
                max_level_n = max((n["level"] for n in nodes), default=0)
                node_order = sorted(nodes, key=lambda x: (-x["level"], -x["frequency"]))
                rows = []
                network_rawis = []
                for n in node_order:
                    r = rawis.get(n["id"])
                    if not r:
                        continue
                    network_rawis.append((r, n))
                    rows.append({
                        "ID": r.id,
                        "Nom": r.name,
                        "Kunya": r.kunya or "—",
                        "Nisba": r.nisba or "—",
                        "Tabaqa": r.tabaqa or "—",
                        "Fiabilité": reliability_fr(r.reliability.value),
                        "Grade (Jarh wa Ta'dil)": r.notes or "—",
                        "Naissance": year_fr(r.birth_date),
                        "Décès": year_fr(r.death_date),
                        "Voies": n["frequency"],
                        "Chemins": n["paths"],
                        "Position": "Compagnon" if n["level"] >= max_level_n else f"Niveau {n['level']}",
                    })
                if rows:
                    st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)
                else:
                    st.info("Aucun narrateur identifié pour ce réseau.")

                # Fiche détaillée d'un maillon (Rijal) — choix interactif
                if network_rawis:
                    st.markdown("#### Fiche détaillée d'un maillon (Rijal)")
                    labels_r = [f"{r.name} · {r.id}" for r, _ in network_rawis]
                    choice_r = st.selectbox("Choisir un narrateur", labels_r, key="rijal_choice")
                    rawi_sel, node_sel = next(
                        (pair for pair, lab in zip(network_rawis, labels_r) if lab == choice_r),
                        network_rawis[0],
                    )
                    f1, f2, f3, f4 = st.columns(4)
                    f1.metric("Fiabilité", reliability_fr(rawi_sel.reliability.value))
                    f2.metric("Tabaqa", rawi_sel.tabaqa or "—")
                    f3.metric("Naissance", year_fr(rawi_sel.birth_date))
                    f4.metric("Décès", year_fr(rawi_sel.death_date))
                    st.markdown(f"**Grade (Jarh wa Ta'dil) :** {rawi_sel.notes or 'Non documenté'}")
                    if rawi_sel.kunya or rawi_sel.nisba:
                        st.caption(" · ".join(x for x in [rawi_sel.kunya, rawi_sel.nisba] if x))
                    position = ("Compagnon" if node_sel["level"] >= max_level_n
                                else f"Niveau {node_sel['level']}")
                    st.markdown(
                        f"**Présence dans le réseau :** {node_sel['frequency']} voie(s), "
                        f"{node_sel['paths']} chemin(s) cumulé(s) — Position : {position}"
                    )
                    if rawi_sel.sources:
                        st.markdown("**Références Rijal :** " + " • ".join(rawi_sel.sources))
                    else:
                        st.caption("Aucune référence Rijal renseignée pour ce narrateur.")

                # Références bibliographiques consolidées (hadith + chaînes + Rijal)
                with st.expander("Références bibliographiques consolidées"):
                    def _uniq(seq):
                        seen, out = set(), []
                        for s in seq:
                            if s and s not in seen:
                                seen.add(s)
                                out.append(s)
                        return out

                    hadith_refs = sel.validation_sources or []
                    chain_refs = []
                    for t in sel.turuq:
                        ch = chains.get(t.isnad_chain_id)
                        if ch and ch.sources:
                            chain_refs.extend(ch.sources)
                    rijal_refs = []
                    for r, _ in network_rawis:
                        rijal_refs.extend(r.sources or [])

                    if hadith_refs:
                        st.markdown("**Sources principales du hadith :**")
                        for s in _uniq(hadith_refs):
                            st.markdown(f"- {s}")
                    if chain_refs:
                        st.markdown("**Sources des chaînes (Turuq) :**")
                        for s in _uniq(chain_refs):
                            st.markdown(f"- {s}")
                    if rijal_refs:
                        st.markdown("**Ouvrages de Rijal cités :**")
                        for s in _uniq(rijal_refs):
                            st.markdown(f"- {s}")
        else:
            st.warning("Aucune voie de transmission (Turuq) définie pour ce hadith.")
    except Exception as exc:
        st.error("⚠️ **Erreur lors de l'affichage du hadith sélectionné.**")
        st.caption(f"**Détail :** `{exc}`")


# ---------------------------------------------------------------------------
# 7. Pied de page — épuré (copyright minimaliste)
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    '<div style="text-align:center;font-size:0.8rem;color:var(--ui-muted);'
    'padding-bottom:0.6rem;">© 2026 Tawatur Hadith — Corpus islamique de '
    "visualisation des hadiths mutawatir · Isnad &amp; Turuq</div>",
    unsafe_allow_html=True,
)
