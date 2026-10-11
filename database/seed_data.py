import json
import os
from typing import Dict

from backend.models.hadith_models import (
    Hadith,
    IsnadChain,
    IsnadNode,
    Obedience,
    Rawiy,
    Reliability,
    TawaturType
)


def create_seed_data() -> Dict:
    """Create seed data with 2-3 major mutawatir hadiths."""
    
    rawis = {
        # Common narrators for major hadiths
        "rawi_001": Rawiy(
            id="rawi_001",
            name="Umar ibn al-Khattab",
            kunya="Abu Hafs",
            nisba="Al-Qurashi",
            tabaqa="Sahaba",
            reliability=Reliability.THIQA,
            death_date=23
        ),
        "rawi_002": Rawiy(
            id="rawi_002",
            name="Al-Hafiz al-Bukhari",
            kunya="Abu Abdullah",
            nisba="Al-Bukhari",
            tabaqa="Compiler",
            reliability=Reliability.THIQA,
            birth_date=194,
            death_date=256
        ),
        "rawi_003": Rawiy(
            id="rawi_003",
            name="Al-Hafiz Muslim",
            kunya="Abu al-Husayn",
            nisba="Al-Naysaburi",
            tabaqa="Compiler",
            reliability=Reliability.THIQA,
            birth_date=204,
            death_date=261
        ),
        "rawi_004": Rawiy(
            id="rawi_004",
            name="Imam Ali ibn Abi Talib",
            kunya="Abu al-Hasan",
            nisba="Al-Hayawi",
            tabaqa="Sahaba",
            reliability=Reliability.THIQA,
            death_date=40
        ),
        "rawi_005": Rawiy(
            id="rawi_005",
            name="Al-Shaykh al-Kulayni",
            kunya="Abu Ja'far",
            nisba="Al-Kulayni",
            tabaqa="Compiler",
            reliability=Reliability.THIQA,
            birth_date=864,
            death_date=941
        ),
        "rawi_006": Rawiy(
            id="rawi_006",
            name="Muhammad ibn Ya'qub al-Kulayni",
            kunya=None,
            tabaqa="Shi'i Hadith Scholar",
            reliability=Reliability.THIQA
        )
    }
    
    # 1. Hadith: Innamā al-a'mālu bin-niyyāt (Actions are by intentions)
    isnad_1 = IsnadChain(
        id="isnad_001",
        nodes=[
            IsnadNode(rawi_id="rawi_001", rawi_name="Umar ibn al-Khattab", level=5),
            IsnadNode(rawi_id="rawi_002", rawi_name="Al-Bukhari", level=0),  # simplified chain
        ],
        path_count=40,  # widely transmitted
        sources=["Sahih al-Bukhari", "Sahih Muslim"]
    )
    
    hadith_1 = Hadith(
        id="hadith_001",
        title="Actions are Judged by Intentions",
        matn="إنما الأعمال بالنيات، وإنما لكل امرئ ما نوى",
        matn_translation="Verily, actions are only by intentions, and every person will only have that which they intended.",
        tawatur_type=TawaturType.MA_NAWI,
        obedience=Obedience.COMMUN,
        degree="Mutawatir Ma'nawi - Widely transmitted",
        isnad_chain_id="isnad_001",
        validation_sources=["Al-Bukhari (1)", "Muslim (1907)", "Ibn Hibban", "Al-Daraqutni"],
        thematic_category="Aqida",
        keywords=["intentions", "niyyah", "actions"]
    )
    
    # 2. Hadith al-Thaqalayn (The Two Weighty Things)
    isnad_2 = IsnadChain(
        id="isnad_002",
        nodes=[
            IsnadNode(rawi_id="rawi_004", rawi_name="Imam Ali ibn Abi Talib", level=5),
            IsnadNode(rawi_id="rawi_005", rawi_name="Al-Kulayni", level=0),
        ],
        path_count=30,
        sources=["Al-Kafi", "Sunan al-Tirmidhi", "Musnad Ahmad"]
    )
    
    hadith_2 = Hadith(
        id="hadith_002",
        title="Hadith al-Thaqalayn",
        matn="إني تارك فيكم الثقلين: كتاب الله وعترتي، ما إن تمسكتم بهما لن تضلوا بعدي أبدا",
        matn_translation="I am leaving among you two weighty things: the Book of Allah and my Ahl al-Bayt. If you hold fast to them, you will never go astray after me.",
        tawatur_type=TawaturType.LAFZI,
        obedience=Obedience.COMMUN,
        degree="Mutawatir Lafzi",
        isnad_chain_id="isnad_002",
        alternative_chains=["isnad_003"],
        validation_sources=["Sunan al-Tirmidhi", "Musnad Ahmad", "Al-Kafi"],
        thematic_category="Imamah/Ahl al-Bayt",
        keywords=["thaqalayn", "ahli bayt", "quran"]
    )
    
    # 3. Hadith al-Ghadir (The Day of Ghadir Khumm)
    isnad_3 = IsnadChain(
        id="isnad_003",
        nodes=[
            IsnadNode(rawi_id="rawi_004", rawi_name="Imam Ali ibn Abi Talib", level=5),
            IsnadNode(rawi_id="rawi_003", rawi_name="Muslim", level=0),
        ],
        path_count=110,  # very widely transmitted
        sources=["Musnad Ahmad", "Sunan al-Tirmidhi", "Mustadrak al-Hakim"]
    )
    
    hadith_3 = Hadith(
        id="hadith_003",
        title="Hadith al-Ghadir",
        matn="من كنت مولاه فهذا علي مولاه، اللهم وال من والاه وعاد من عاداه",
        matn_translation="Whomsoever I am his master, Ali is his master. O Allah, befriend whoever befriends him and be hostile to whoever is hostile to him.",
        tawatur_type=TawaturType.LAFZI,
        obedience=Obedience.COMMUN,
        degree="Mutawatir Lafzi by majority",
        isnad_chain_id="isnad_003",
        validation_sources=["Musnad Ahmad", "Tirmidhi", "Nasai", "Ibn Majah", "Al-Hakim"],
        thematic_category="Wilayah/Imamah",
        keywords=["ghadir", "wilayah", "mawla"]
    )
    
    return {
        "rawis": {k: v.model_dump() for k, v in rawis.items()},
        "isnad_chains": {
            "isnad_001": isnad_1.model_dump(),
            "isnad_002": isnad_2.model_dump(),
            "isnad_003": isnad_3.model_dump()
        },
        "hadiths": {
            "hadith_001": hadith_1.model_dump(),
            "hadith_002": hadith_2.model_dump(),
            "hadith_003": hadith_3.model_dump()
        }
    }


def save_seed_data(filepath: str):
    """Save seed data to JSON file."""
    data = create_seed_data()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    print(f"Seed data saved to {filepath}")


if __name__ == "__main__":
    save_seed_data("C:\\Users\\decen\\tawatur-hadith\\data\\seed_hadiths.json")
    print("Seed data generation complete.")
