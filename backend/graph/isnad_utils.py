import math
from typing import Dict, List

import networkx as nx

from backend.models.hadith_models import IsnadChain, Rawiy, ReliabilityFR, TawaturTypeFR, ObedienceFR


def reliability_fr(code: str) -> str:
    return ReliabilityFR.MAP.get(code, code)


def tawatur_fr(code: str) -> str:
    return TawaturTypeFR.MAP.get(code, code)


def obedience_fr(code: str) -> str:
    return ObedienceFR.MAP.get(code, code)


def build_isnad_tree(isnad_chain: IsnadChain, rawis: Dict[str, Rawiy]) -> Dict:
    """Arbre linéaire d'UNE chaîne (rétro-compatibilité)."""
    tree = {"nodes": [], "edges": []}
    for i, node in enumerate(isnad_chain.nodes):
        rawi = rawis.get(node.rawi_id)
        tree["nodes"].append({
            "id": node.rawi_id,
            "label": node.rawi_name,
            "level": node.level,
            "reliability": rawi.reliability.value if rawi else "unknown",
            "reliability_fr": reliability_fr(rawi.reliability.value) if rawi else "Inconnu",
            "kunya": rawi.kunya if rawi else None,
            "tabaqa": rawi.tabaqa if rawi else None
        })
        if i < len(isnad_chain.nodes) - 1:
            next_node = isnad_chain.nodes[i + 1]
            tree["edges"].append({
                "source": node.rawi_id,
                "target": next_node.rawi_id,
                "type": "transmission"
            })
    return tree


def build_turuq_network(
    hadith,
    chains: Dict[str, IsnadChain],
    rawis: Dict[str, Rawiy],
    min_paths: int = 0,
) -> Dict:
    """Fusionne TOUTES les voies (Turuq) d'un hadith en un réseau unique.

    - Les narrateurs identiques sont fusionnés (nœud unique, dédupliqué par id).
    - Chaque nœud porte sa fréquence (nombre de voies le traversant) et le
      total de chemins qu'il accumule.
    - Chaque lien (transmission A -> B) porte un poids = somme des chemins.
    - Détection des pivots (Madar) : narrateurs présents dans la moitié ou plus
      des voies affichées (ou au moins 2 voies).

    Args:
        hadith: instance Hadith (attribut ``turuq`` = liste d'IsnadTuruq).
        chains: index id -> IsnadChain.
        rawis: index id -> Rawiy.
        min_paths: ne conserve que les voies dont ``path_count`` >= min_paths.

    Returns:
        dict {nodes, edges, stats, chains}
    """
    G = nx.DiGraph()
    try:
        node_map: Dict[str, Dict] = {}
        edge_map: Dict[tuple, Dict] = {}
        kept_chains: List[IsnadChain] = []

        for voie in (getattr(hadith, "turuq", None) or []):
            chain = chains.get(voie.isnad_chain_id)
            if chain is None or not chain.nodes:
                continue
            pc = chain.path_count or 1
            if pc < min_paths:
                continue
            kept_chains.append(chain)

            for node in chain.nodes:
                agg = node_map.get(node.rawi_id)
                if agg is None:
                    r = rawis.get(node.rawi_id)
                    agg = {
                        "id": node.rawi_id,
                        "label": node.rawi_name,
                        "level": node.level,
                        "reliability": r.reliability.value if r else "unknown",
                        "reliability_fr": reliability_fr(r.reliability.value) if r else "Inconnu",
                        "kunya": r.kunya if r else None,
                        "tabaqa": r.tabaqa if r else None,
                        "frequency": 0,
                        "paths": 0,
                    }
                    node_map[node.rawi_id] = agg
                agg["frequency"] += 1
                agg["paths"] += pc
                agg["level"] = max(agg["level"], node.level)

            for a, b in zip(chain.nodes, chain.nodes[1:]):
                key = (a.rawi_id, b.rawi_id)
                edge = edge_map.get(key)
                if edge is None:
                    edge = {"source": a.rawi_id, "target": b.rawi_id, "weight": 0, "chains": 0}
                    edge_map[key] = edge
                edge["weight"] += pc
                edge["chains"] += 1

        n_chains = len(kept_chains)
        nodes = list(node_map.values())
        pivot_threshold = max(2, 0.5 * n_chains)
        for nd in nodes:
            nd["is_madar"] = n_chains > 0 and nd["frequency"] >= pivot_threshold
            nd["is_compiler"] = nd["level"] == 0

        stats = {
            "n_chains": n_chains,
            "total_paths": sum((c.path_count or 0) for c in kept_chains),
            "n_nodes": len(nodes),
            "n_edges": len(edge_map),
            "n_madar": sum(1 for nd in nodes if nd["is_madar"]),
        }
        return {
            "nodes": nodes,
            "edges": list(edge_map.values()),
            "stats": stats,
            "chains": kept_chains,
        }
    except Exception:
        return {
            "nodes": [],
            "edges": [],
            "stats": {"n_chains": 0, "total_paths": 0, "n_nodes": 0, "n_edges": 0, "n_madar": 0},
            "chains": [],
        }


def format_isnad_text(isnad_chain: IsnadChain) -> str:
    names = [node.rawi_name for node in isnad_chain.nodes]
    return " → ".join(names)


def get_ancestry_path(isnad_chain: IsnadChain, start_idx: int = 0, end_idx: int = None) -> List[str]:
    if end_idx is None:
        end_idx = len(isnad_chain.nodes)
    return [n.rawi_name for n in isnad_chain.nodes[start_idx:end_idx]]


def layout_network(nodes, edges, *args, **kwargs):
    """Disposition hiérarchique verticale par strates (Tabaqat) — mode Standard."""
    return _layout_vertical(nodes, edges)


def _layout_vertical(nodes, edges):
    """Disposition verticale stricte par strates (Tabaqat).
    
    Niveaux Y :
      - Génération 0 (Compagnons)     : Y = 4.0
      - Génération 1 (Grands Tabi'un) : Y = 3.0
      - Génération 2 (Petits Tabi'un) : Y = 2.0
      - Génération 3 (Suivants)       : Y = 1.0
      - Génération 4 (Compilateurs)   : Y = 0.0
    
    Sur l'axe X : répartir équitablement les narrateurs de chaque niveau
    pour qu'ils ne se chevauchent jamais.
    """
    if not nodes:
        return {}
    max_level = max((n["level"] for n in nodes), default=1) or 1

    # Grouper par niveau (tabaqa)
    levels = {}
    for n in nodes:
        levels.setdefault(n["level"], []).append(n)

    pos = {}
    for lvl, ns in levels.items():
        count = len(ns)
        # Y position based on generation (stratum)
        # Génération 0 (Compagnons)   -> Y = 4.0
        # Génération 1 (Grands Tabi'un) -> Y = 3.0
        # Génération 2 (Petits Tabi'un) -> Y = 2.0
        # Génération 3 (Suivants)       -> Y = 1.0
        # Génération 4 (Compilateurs)   -> Y = 0.0
        y = 4.0 - float(lvl)

        # X: répartir équitablement pour éviter les chevauchements
        if count <= 1:
            x = 0.5
        else:
            margin = 0.1
            available = 1.0 - 2 * margin
            step = available / (count - 1)
            for i, n in enumerate(ns):
                x = margin + i * step
                pos[n["id"]] = (x, y)

    return pos
