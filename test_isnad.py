import json
import sys
sys.path.append("C:\\Users\\decen\\tawatur-hadith")

from backend.graph.isnad_utils import build_isnad_tree, format_isnad_text
from backend.models.hadith_models import Hadith, IsnadChain, Rawiy
from database.seed_data import create_seed_data


def display_isnad_example():
    """Display example of isnad tree representation."""
    data = create_seed_data()
    
    print("=" * 60)
    print("TAWATUR HADITH PROJECT - ISNAD TREE DEMONSTRATION")
    print("=" * 60)
    print()
    
    rawis_dict = {k: Rawiy(**v) for k, v in data["rawis"].items()}
    
    for hadith_id, hadith_data in data["hadiths"].items():
        hadith = Hadith(**hadith_data)
        print(f"HADITH: {hadith.title}")
        print(f"ID: {hadith_id}")
        print(f"Tawatur: {hadith.tawatur_type} | Obedience: {hadith.obedience}")
        print()
        print(f"MATN: {hadith.matn}")
        if hadith.matn_translation:
            print(f"Translation: {hadith.matn_translation}")
        print()
        
        chain_id = hadith.isnad_chain_id
        chain = IsnadChain(**data["isnad_chains"][chain_id])
        print(f"ISNAD ({chain_id}):")
        print(f"  {format_isnad_text(chain)}")
        print()
        print("Tree Structure:")
        tree = build_isnad_tree(chain, rawis_dict)
        for node in tree['nodes']:
            level = node['level']
            indent = "  " * (max(0, 5 - level)) if level > 0 else "  "
            rel = f"[{node['reliability']}]"
            print(f"  {indent}├─ {node['label']} {rel}")
        print()
        print("-" * 60)
        print()
    
    # Save example tree
    chain_3 = IsnadChain(**data["isnad_chains"]["isnad_003"])
    example_tree = build_isnad_tree(chain_3, rawis_dict)
    with open("C:\\Users\\decen\\tawatur-hadith\\data\\example_isnad_tree.json", 'w', encoding='utf-8') as f:
        json.dump(example_tree, f, ensure_ascii=False, indent=2)
    print("Example tree saved to data/example_isnad_tree.json")


if __name__ == "__main__":
    display_isnad_example()
