import json
import os
import sys

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.graph.isnad_utils import build_isnad_tree, format_isnad_text
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data

st.set_page_config(
    page_title="Tawatur Hadith - Isnad Tree Visualizer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Tawatur Hadith - Visualisation des Hadiths Mutawatir")
st.markdown("""
Cet outil permet de visualiser les hadiths Mutawatir et leurs chaînes de transmission (Isnad)
sous forme d'arbres généalogiques interactifs, en intégrant les perspectives sunnites et chiites.
""")


@st.cache_data
def load_data():
    data = create_seed_data()
    hadiths = [Hadith(**h) for h in data["hadiths"].values()]
    rawis = {k: Rawiy(**v) for k, v in data["rawis"].items()}
    chains = {k: IsnadChain(**v) for k, v in data["isnad_chains"].items()}
    return hadiths, rawis, chains


hadiths, rawis, chains = load_data()

# Sidebar
st.sidebar.header("Sélection du Hadith")
hadith_dict = {f"{h.id} - {h.title}": h for h in hadiths}
selected = st.sidebar.selectbox("Choisir un hadith", list(hadith_dict.keys()))
selected_hadith = hadith_dict[selected]

# Display hadith info
col1, col2 = st.columns(2)

with col1:
    st.header("Informations du Hadith")
    st.markdown(f"**ID :** {selected_hadith.id}")
    st.markdown(f"**Titre :** {selected_hadith.title}")
    st.markdown(f"**Type de Tawatur :** {selected_hadith.tawatur_type}")
    st.markdown(f"**Obédience :** {selected_hadith.obedience}")
    st.markdown(f"**Degré :** {selected_hadith.degree}")
    st.markdown("**Matn (Texte arabe) :**")
    st.markdown(f"``` {selected_hadith.matn} ```")
    if selected_hadith.matn_translation:
        st.markdown("**Traduction :**")
        st.markdown(f"*{selected_hadith.matn_translation}*")
    st.markdown(f"**Catégorie thématique :** {selected_hadith.thematic_category}")
    st.markdown(f"**Sources de validation :** {', '.join(selected_hadith.validation_sources)}")

with col2:
    st.header("Chaîne de Transmission (Isnad)")
    chain = chains[selected_hadith.isnad_chain_id]
    st.markdown(f"**ID Isnad :** {chain.id}")
    st.markdown(f"**Format textuel :**")
    st.code(format_isnad_text(chain))
    st.markdown(f"**Nombre de chemins :** {chain.path_count or 'N/A'}")
    st.markdown(f"**Sources :** {', '.join(chain.sources)}")

# Tree visualization
st.header("Arbre Généalogique de l'Isnad")
tree = build_isnad_tree(chain, rawis)

# Create Plotly figure
fig = go.Figure()

# Build positions (simple hierarchical layout)
nodes = tree["nodes"]
edges = tree["edges"]

# Assign y positions by level
level_counts = {}
for node in nodes:
    level = node["level"]
    level_counts[level] = level_counts.get(level, 0) + 1

# Calculate positions
pos = {}
y_step = 1.0 / (max(level_counts.keys()) + 1) if level_counts else 0.5
for node in nodes:
    level = node["level"]
    # x spread
    idx = list(n["id"] for n in nodes if n["level"] == level).index(node["id"])
    x_step = 1.0 / (level_counts[level] + 1)
    x = (idx + 1) * x_step
    y = 1.0 - level * y_step if level > 0 else 0.1  # compiler at top? or reverse - adjust
    # Reverse: companion (high level) at top, compiler at bottom
    max_level = max(level_counts.keys())
    y = level / max_level if max_level > 0 else 0.5

# Better layout: higher level numbers (companions) at top
max_level = max(n["level"] for n in nodes) if nodes else 0
level_positions = {}
for lvl in range(max_level + 1):
    nodes_at_lvl = [n for n in nodes if n["level"] == lvl]
    for i, n in enumerate(nodes_at_lvl):
        x = (i + 1) / (len(nodes_at_lvl) + 1)
        y = (max_level - lvl) / max_level if max_level > 0 else 0.5
        pos[n["id"]] = (x, y)

# Draw edges
for edge in edges:
    src = edge["source"]
    tgt = edge["target"]
    if src in pos and tgt in pos:
        x0, y0 = pos[src]
        x1, y1 = pos[tgt]
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode="lines",
            line=dict(width=2, color="#888"),
            hoverinfo="none",
            showlegend=False
        ))

# Draw nodes
for node in nodes:
    nid = node["id"]
    if nid in pos:
        x, y = pos[nid]
        color = "#1f77b4" if node["reliability"] == "thiqa" else "#ff7f0e"
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode="markers+text",
            marker=dict(size=20, color=color, line=dict(width=2, color="DarkSlateGrey")),
            text=node["label"],
            textposition="bottom center",
            hoverinfo="text",
            hovertext=f"<b>{node['label']}</b><br>"
                      f"Kunya: {node.get('kunya') or 'N/A'}<br>"
                      f"Tabaqa: {node.get('tabaqa') or 'N/A'}<br>"
                      f"Reliability: {node['reliability']}<br>"
                      f"Level: {node['level']}",
            showlegend=False
        ))

fig.update_layout(
    title="Arbre d'Isnad Interactif",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=500,
    plot_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

# Data tables
st.header("Détails des Narrateurs")
narrators_list = []
for node in nodes:
    r = rawis.get(node["id"])
    if r:
        narrators_list.append({
            "ID": r.id,
            "Nom": r.name,
            "Kunya": r.kunya or "-",
            "Nisba": r.nisba or "-",
            "Tabaqa": r.tabaqa or "-",
            "Fiabilité": r.reliability,
            "Naissance": r.birth_date or "-",
            "Décès": r.death_date or "-"
        })
df = pd.DataFrame(narrators_list)
st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Tawatur Hadith Project** - Structure modulaire pour l'étude comparative des hadiths mutawatir")
