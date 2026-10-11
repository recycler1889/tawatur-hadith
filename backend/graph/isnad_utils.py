from typing import Dict, List, Optional

from backend.models.hadith_models import Hadith, IsnadChain, Rawiy


def build_isnad_tree(isnad_chain: IsnadChain, rawis: Dict[str, Rawiy]) -> Dict:
    """
    Build a tree structure representation of an isnad chain for visualization.
    
    Returns a dictionary suitable for graph visualization (e.g., Plotly, NetworkX, Cytoscape).
    """
    tree = {
        "nodes": [],
        "edges": []
    }
    
    # Build nodes and edges from chain (companion -> compiler order)
    for i, node in enumerate(isnad_chain.nodes):
        rawi = rawis.get(node.rawi_id)
        tree["nodes"].append({
            "id": node.rawi_id,
            "label": node.rawi_name,
            "level": node.level,
            "reliability": rawi.reliability.value if rawi else "unknown",
            "kunya": rawi.kunya if rawi else None,
            "tabaqa": rawi.tabaqa if rawi else None
        })
        # Add edge to next in chain
        if i < len(isnad_chain.nodes) - 1:
            next_node = isnad_chain.nodes[i + 1]
            tree["edges"].append({
                "source": node.rawi_id,
                "target": next_node.rawi_id,
                "type": "transmission"
            })
    
    return tree


def format_isnad_text(isnad_chain: IsnadChain) -> str:
    """Format isnad chain as readable text."""
    names = [node.rawi_name for node in isnad_chain.nodes]
    return " -> ".join(names)


def get_ancestry_path(isnad_chain: IsnadChain, start_idx: int = 0, end_idx: Optional[int] = None) -> List[str]:
    """Get a subpath of the isnad chain."""
    if end_idx is None:
        end_idx = len(isnad_chain.nodes)
    return [n.rawi_name for n in isnad_chain.nodes[start_idx:end_idx]]
