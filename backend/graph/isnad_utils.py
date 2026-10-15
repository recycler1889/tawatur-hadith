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


def format_isnad_text(isnad_chain: IsnadChain) -> str:
    names = [node.rawi_name for node in isnad_chain.nodes]
    return " → ".join(names)


def get_ancestry_path(isnad_chain: IsnadChain, start_idx: int = 0, end_idx: int = None) -> List[str]:
    if end_idx is None:
        end_idx = len(isnad_chain.nodes)
    return [n.rawi_name for n in isnad_chain.nodes[start_idx:end_idx]]


# --- Layouts alternatifs ---

def layout_radial(nodes, edges, max_level=None):
    """Disposition radiale / « Soleil » : noyau central (compilateur niveau 0),
    expansion concentrique vers les Compagnons (niveaux supérieurs).
    Retourne {node_id: (x, y)} dans [0,1]."""
    if not nodes:
        return {}
    
    if max_level is None:
        max_level = max((n["level"] for n in nodes), default=1) or 1
    
    # Grouper les nœuds par niveau
    levels = {}
    for n in nodes:
        levels.setdefault(n["level"], []).append(n)
    
    # Trier chaque niveau par fréquence décroissante
    for lvl in levels:
        levels[lvl].sort(key=lambda x: (-x["frequency"], -x["paths"]))
    
    # Construire l'adjacence pour le barycentre
    adjacency = {}
    for e in edges:
        adjacency.setdefault(e["source"], set()).add(e["target"])
        adjacency.setdefault(e["target"], set()).add(e["source"])
    
    pos = {}
    center_x, center_y = 0.5, 0.5
    
    # Le compilateur (niveau 0) au centre
    if 0 in levels:
        for n in levels[0]:
            pos[n["id"]] = (center_x, center_y)
    
    # Niveaux concentriques
    max_radius = 0.45
    for lvl in sorted(levels.keys()):
        if lvl == 0:
            continue
        ns = levels[lvl]
        count = len(ns)
        radius = (lvl / max_level) * max_radius
        for i, n in enumerate(ns):
            angle = (2 * math.pi * i) / count
            # Décalage léger pour éviter la superposition parfaite
            angle += 0.1 * (n.get("frequency", 1) % 3)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pos[n["id"]] = (x, y)
    
    return pos


def layout_hybrid(nodes, edges, max_level=None):
    """Disposition hybride : arbre vertical pour la structure principale,
    avec les sous-branches déployées en éventail radial.
    Compromis entre lisibilité chronologique et compacité."""
    if not nodes:
        return {}
    
    if max_level is None:
        max_level = max((n["level"] for n in nodes), default=1) or 1
    
    # Grouper par niveau
    levels = {}
    for n in nodes:
        levels.setdefault(n["level"], []).append(n)
    
    for lvl in levels:
        levels[lvl].sort(key=lambda x: (-x["frequency"], -x["paths"]))
    
    adjacency = {}
    for e in edges:
        adjacency.setdefault(e["source"], set()).add(e["target"])
        adjacency.setdefault(e["target"], set()).add(e["source"])
    
    idx = {}
    for lvl, ns in levels.items():
        for i, n in enumerate(ns):
            idx[n["id"]] = i
    
    # Barycentre comme layout vertical
    for _ in range(4):
        for lvl in sorted(levels):
            ns = levels[lvl]
            def bary(n):
                vals = [idx[m] for m in adjacency.get(n["id"], ()) if m in idx]
                return (sum(vals) / len(vals)) if vals else idx[n["id"]]
            ns.sort(key=bary)
            for i, n in enumerate(ns):
                idx[n["id"]] = i
    
    pos = {}
    # Niveaux principaux en vertical (haut -> bas)
    # Mais avec un écartement horizontal plus large (éventail)
    for lvl in sorted(levels.keys()):
        ns = levels[lvl]
        count = len(ns)
        # y : vertical (0 = haut = Compagnons, 1 = bas = Compilateur)
        y = 1.0 - (lvl / max_level) if max_level else 0.5
        # x : éventail centré, plus large que le layout vertical standard
        if count == 1:
            pos[ns[0]["id"]] = (0.5, y)
        else:
            # Espacement dynamique selon le niveau
            spread = 0.8 if lvl > 0 else 0.6
            start = 0.5 - spread / 2
            for i, n in enumerate(ns):
                x = start + (i + 0.5) * spread / count
                pos[n["id"]] = (x, y)
    
    return pos


def layout_network(nodes, edges, mode="Standard", **kwargs):
    """Disposition du réseau selon le mode choisi.

    Args:
        mode: string, l'un de : "Standard", "Radial", "Soleil", "Hybride".
              Insensible à la casse. Les arguments supplémentaires sont transmis
              à la fonction layout via **kwargs (évite les TypeError).
    """
    m = str(mode).lower()
    try:
        # Construire un graphe networkx à partir des nœuds / arêtes
        G = nx.DiGraph()
        for n in nodes:
            node_id = n.get("id") if isinstance(n, dict) else n
            G.add_node(str(node_id))
        for e in edges:
            src = e.get("source") if isinstance(e, dict) else e[0]
            tgt = e.get("target") if isinstance(e, dict) else e[1]
            G.add_edge(str(src), str(tgt))

        if "radial" in m or "soleil" in m:
            # Mode Radial / Soleil : disposition circulaire concentrique
            try:
                return nx.circular_layout(G, **kwargs)
            except Exception:
                return {n: (0.0, float(i)) for i, n in enumerate(G.nodes())}
        elif "hybride" in m:
            # Mode Hybride : force-directed étendu
            try:
                return nx.spring_layout(G, k=0.8, iterations=60, seed=42, **kwargs)
            except Exception:
                return {n: (0.0, float(i)) for i, n in enumerate(G.nodes())}
        else:
            # Mode Standard (vertical / hiérarchique par génération / Tabaqa)
            try:
                return nx.spring_layout(G, k=0.4, iterations=40, seed=42, **kwargs)
            except Exception:
                return {n: (0.0, float(i)) for i, n in enumerate(G.nodes())}
    except Exception:
        return {n: (0.0, float(i)) for i, n in enumerate(G.nodes())}


def _layout_vertical(nodes, edges):
    """Layout vertical original (renommé pour éviter la collision)."""
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
