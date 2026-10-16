import re

with open('backend/graph/isnad_utils.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_func = '''def layout_network(nodes, edges, **kwargs):
    import networkx as nx
    G = nx.DiGraph()
    try:
        if isinstance(nodes, dict):
            for n in nodes.keys(): G.add_node(n)
        elif isinstance(nodes, (list, tuple, set)):
            for n in nodes:
                nid = n.get("id", n.get("name", str(n))) if isinstance(n, dict) else n
                G.add_node(nid)
        if isinstance(edges, (list, tuple, set)):
            for e in edges:
                src = e.get("source") if isinstance(e, dict) else e[0]
                tgt = e.get("target") if isinstance(e, dict) else e[1]
                if src and tgt: G.add_edge(src, tgt)
        if len(G.nodes) == 0: return {}

        roots = [n for n in G.nodes() if G.in_degree(n) == 0] or list(G.nodes())[:1]
        levels = {}
        for n in G.nodes():
            d = 0
            for r in roots:
                if nx.has_path(G, r, n):
                    p = len(nx.shortest_path(G, r, n)) - 1
                    if p > d: d = p
            levels[n] = d

        layers = {}
        for n, l in levels.items(): layers.setdefault(l, []).append(n)

        pos = {}
        for l in sorted(layers.keys()):
            nds = layers[l]
            count = len(nds)
            for i, n in enumerate(nds):
                x = (i - (count - 1) / 2.0) * 2.5
                y = -float(l) * 3.0
                pos[n] = (float(x), float(y))
        return pos
    except Exception:
        return {str(n): (float(i * 2), 0.0) for i, n in enumerate(G.nodes())}
'''

# Match from def layout_network to end of function (next def or end of file)
pattern = r'def layout_network\(nodes, edges, \*\*kwargs\).*?(?=\n\ndef |\nclass |\Z)'
# Replace - but need to be careful: the pattern needs to capture the whole function
# Let's just replace the specific lines we know

# Simpler: just replace the entire function by matching its exact start and end markers
old_marker = "def layout_network(nodes, edges, **kwargs):"
# Find the function and replace it
start = content.find(old_marker)
if start >= 0:
    # Find end: next top-level def or end
    remaining = content[start:]
    # Find next "def " at line start
    end = remaining.find("\n\ndef ")
    if end == -1:
        # Check for class
        end2 = remaining.find("\n\nclass ")
        if end2 == -1:
            end = len(content)
        else:
            end = start + end2
    else:
        end = start + end
    
    new_content = content[:start] + new_func + "\n" + content[end:]
    with open('backend/graph/isnad_utils.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced layout_network function successfully")
else:
    print("Could not find layout_network function start")