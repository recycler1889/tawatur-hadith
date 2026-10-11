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

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.graph.isnad_utils import (
    build_turuq_network,
    format_isnad_text,
    obedience_fr,
    reliability_fr,
    tawatur_fr,
)
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data

st.set_page_config(
    page_title="Tawatur Hadith | Visualisation des Hadiths Mutawatir",
    page_icon="📚",
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


def year_fr(value):
    if value is None or value == "":
        return "—"
    return f"{value} (env.)"


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
  background-color: var(--ui-surface) !important;
  border-color: var(--ui-border) !important;
}
.stApp input, .stApp textarea, .stApp select {
  background-color: var(--ui-surface) !important;
  color: var(--ui-text) !important;
  caret-color: var(--ui-accent) !important;
}
.stApp input::placeholder, .stApp textarea::placeholder {
  color: var(--ui-muted) !important; opacity: 1 !important;
}
[data-baseweb="select"] { color: var(--ui-text) !important; }
[data-baseweb="select"] [data-baseweb="tag"] {
  background-color: var(--ui-tag-bg) !important; color: var(--ui-tag-text) !important;
  border: 1px solid var(--ui-border) !important;
}
[data-baseweb="select"] [data-baseweb="tag"] span { color: var(--ui-tag-text) !important; }
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
  border-radius: 12px !important; padding: 0.6rem 0.8rem !important;
}
[data-testid="stMetricLabel"] p, [data-testid="stMetricValue"] { color: var(--ui-text) !important; }

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
body, .stApp { background: radial-gradient(ellipse at top, #0b1a17 0%, #050d0b 100%); color: #dcefe6; }
:root, .stApp {
  --ui-bg:#0b1a17; --ui-surface:#0f251e; --ui-surface-2:#123027; --ui-border:rgba(52,211,153,0.25);
  --ui-text:#dcefe6; --ui-muted:#93b7a8; --ui-accent:#34d399;
  --ui-tag-bg:rgba(16,185,129,0.16); --ui-tag-text:#a7f3d0;
  --ui-btn-bg:linear-gradient(180deg,#1f9d63,#0f7a4d); --ui-btn-bg-strong:linear-gradient(180deg,#18a06b,#0f7d54);
  --ui-btn-text:#ffffff;
  --ui-menu-bg:#0a1c17; --ui-menu-text:#e6f4ec; --ui-menu-hover:#143a2c; --ui-menu-border:rgba(52,211,153,0.30);
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

/* ---- Textes du hadith ---- */
.arabic-matn { font-family: 'Amiri','Noto Sans Arabic',serif; font-size: 1.7rem; line-height: 2.5rem;
  text-align: right; direction: rtl; unicode-bidi: isolate; padding: 1.4rem 1.75rem;
  background: linear-gradient(180deg, rgba(6,30,24,0.92) 0%, rgba(3,15,12,0.92) 100%);
  border: 1px solid rgba(52,211,153,0.22); border-left: 4px solid __ACCENT__; border-radius: 12px;
  color: #f1f5f9; box-shadow: inset 0 2px 8px rgba(0,0,0,0.4); }
.translation-fr { font-size: 1.02rem; line-height: 1.8rem; color: #cbd5e1; background: rgba(6,30,24,0.7);
  border-left: 3px solid __ACCENT__; padding: 1rem 1.25rem; border-radius: 10px; margin-top: 0.75rem; }

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

/* ---- Textes du hadith ---- */
.arabic-matn { font-family: 'Amiri','Noto Sans Arabic',serif; font-size: 1.7rem; line-height: 2.5rem;
  text-align: right; direction: rtl; unicode-bidi: isolate; padding: 1.4rem 1.75rem;
  background: #ffffff; border: 1px solid #d5e8dd; border-left: 4px solid __ACCENT__; border-radius: 12px;
  color: #14261d; box-shadow: 0 1px 3px rgba(15,60,40,0.06); }
.translation-fr { font-size: 1.02rem; line-height: 1.8rem; color: #2c4238; background: #eff7f2;
  border-left: 3px solid __ACCENT__; padding: 1rem 1.25rem; border-radius: 10px; margin-top: 0.75rem; }

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

/* ---- Textes du hadith ---- */
.arabic-matn { font-family: 'Amiri','Noto Sans Arabic',serif; font-size: 1.7rem; line-height: 2.5rem;
  text-align: right; direction: rtl; unicode-bidi: isolate; padding: 1.4rem 1.75rem;
  background: linear-gradient(180deg, #fffaf0 0%, #fdf6e3 100%); border: 1px solid rgba(139,115,85,0.35);
  border-left: 4px solid __ACCENT__; border-radius: 12px; color: #3a2f1e;
  box-shadow: inset 0 1px 4px rgba(160,120,75,0.08); }
.translation-fr { font-size: 1.02rem; line-height: 1.8rem; color: #5b4a30; background: rgba(250,245,230,0.92);
  border-left: 3px solid __ACCENT__; padding: 1rem 1.25rem; border-radius: 10px; margin-top: 0.75rem; }

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


def build_network_figure(net, plot, highlight_madar, color_mode):
    """Figure Plotly du réseau complet des Turuq : tous les nœuds et liens,
    épaisseur/opacité des liens selon le poids (chemins), taille des nœuds
    selon la fréquence, couleur selon la fiabilité ou la fréquence."""
    nodes = net["nodes"]
    edges = net["edges"]
    pos = layout_network(nodes, edges)
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
        height=720, dragmode="pan",
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


# ---------------------------------------------------------------------------
# 3. En-tête + sélecteur de thème (boutons à icônes)
# ---------------------------------------------------------------------------
# Défilement fluide vers la section de lecture/détails au clic sur « Consulter ».
SCROLL_TO_DETAIL_JS = """
<script>
(function () {
  function go() {
    var el = window.parent.document.getElementById('detail-section');
    if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  }
  setTimeout(go, 120);
  setTimeout(go, 450);
})();
</script>
"""

THEME_ICONS = [("Sombre", "🌙"), ("Clair", "☀️"), ("Sépia", "📜")]
if st.session_state.get("theme") not in ("Sombre", "Clair", "Sépia"):
    st.session_state.theme = "Sombre"

theme = st.session_state.theme
st.markdown(theme_css(theme), unsafe_allow_html=True)
plot = THEME_PLOT[theme]

# Barre d'ambiance : boutons à icônes, alignés à droite.
_tl, _tr = st.columns([5, 3])
with _tr:
    st.markdown('<div class="theme-switch-label">Ambiance visuelle</div>', unsafe_allow_html=True)
    _tcols = st.columns(3)
    for _col, (_name, _icon) in zip(_tcols, THEME_ICONS):
        with _col:
            _active = (st.session_state.theme == _name)
            if st.button(_icon, key=f"theme_{_name}", help=_name,
                         type=("primary" if _active else "secondary"), width="stretch"):
                st.session_state.theme = _name
                st.rerun()

# En-tête principal ornementé (motifs géométriques islamiques).
st.markdown(
    """
    <div class="app-header">
      <div class="orn-row">
        <span class="orn-line"></span><span class="orn-star">۞</span><span class="orn-line"></span>
      </div>
      <h1 class="app-title">Tawatur Hadith</h1>
      <div class="app-subtitle">Visualisation des Hadiths Mutawatir · Isnad &amp; Turuq</div>
      <div class="orn-row">
        <span class="orn-line"></span><span class="orn-star">❖</span><span class="orn-line"></span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# 4. Filtres
# ---------------------------------------------------------------------------
with st.container():
    c1, c2, c3 = st.columns(3)
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
            st.markdown(
                f"""<div class="theme-card">
                <div><span class="badge">{obedience_fr(h.obedience.value)}</span>
                <span class="badge">{tawatur_fr(h.tawatur_type.value)}</span></div>
                <strong>{h.title_fr}</strong>
                <div style="font-size:0.92rem;margin-top:0.4rem;">{excerpt}</div>
                <div style="font-size:0.82rem;margin-top:0.5rem;opacity:0.8;">
                🔗 {n_paths} chemins &nbsp;•&nbsp; 🏷️ {h.id.upper()}</div>
                </div>""",
                unsafe_allow_html=True,
            )
            if st.button("Consulter", key=f"sel_{h.id}", width="stretch"):
                st.session_state.sel_id = h.id
                st.session_state.scroll_detail = True


# ---------------------------------------------------------------------------
# 6. Détail du hadith sélectionné (protégé)
# ---------------------------------------------------------------------------
sel_id = st.session_state.get("sel_id")
sel = next((h for h in hadiths if h.id == sel_id), None)

if sel:
    st.markdown('<div id="detail-section"></div>', unsafe_allow_html=True)
    if st.session_state.pop("scroll_detail", False):
        components.html(SCROLL_TO_DETAIL_JS, height=0, width=0)
    st.markdown("---")
    try:
        st.header(sel.title_fr)
        if sel.title_ar:
            st.caption(sel.title_ar)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Obédience", obedience_fr(sel.obedience.value))
        m2.metric("Type de Tawatur", tawatur_fr(sel.tawatur_type.value))
        m3.metric("Degré", sel.degree_fr or "—")
        m4.metric("Nombre de voies", len(sel.turuq or []))

        st.subheader("Texte du Hadith")
        st.markdown(f'<div class="arabic-matn">{sel.matn}</div>', unsafe_allow_html=True)
        if sel.matn_translation_fr:
            st.markdown(f'<div class="translation-fr">{sel.matn_translation_fr}</div>', unsafe_allow_html=True)

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
            ctrl1, ctrl2, ctrl3 = st.columns([3, 2, 2])
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

                fig = build_network_figure(net, plot, highlight_madar, color_mode)
                st.plotly_chart(
                    fig, width="stretch",
                    config={"scrollZoom": True, "displaylogo": False,
                            "modeBarButtonsToAdd": ["pan2d", "zoomIn2d", "zoomOut2d", "resetScale2d"]},
                )
                st.caption(
                    "💡 Molette = zoom • Glisser = déplacer • Double-clic = réinitialiser. "
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
# 7. Pied de page
# ---------------------------------------------------------------------------
st.markdown("---")
st.caption(
    "Tawatur Hadith Project • Navigation sans barre latérale, thèmes Clair/Sombre/Sépia "
    "et support multi-voies (Turuq)."
)
