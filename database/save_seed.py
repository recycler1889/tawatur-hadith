import json
import os
import sys

# Ajout du chemin racine
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from .seed_data import create_seed_data


def save_seed_data(filepath: str):
    data = create_seed_data()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    print(f"Données sauvegardées dans {filepath}")


if __name__ == "__main__":
    save_seed_data(os.path.join(ROOT, "data", "seed_hadiths.json"))
    print("Terminé.")
