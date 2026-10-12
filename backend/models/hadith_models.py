from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class TawaturType(str, Enum):
    """Type de tawatur"""
    LAFZI = "lafzi"  # Mutawatir Lafzi
    MA_NAWI = "ma'nawi"  # Mutawatir Ma'nawi


class Obedience(str, Enum):
    """Appartenance doctrinale"""
    SUNNITE = "sunnite"
    CHIITE = "chiite"
    COMMUN = "commun"


class Reliability(str, Enum):
    """Classification Jarh wa Ta'dil"""
    THIQA = "thiqa"
    HASSAN = "hassan"
    UNKNOWN = "unknown"
    DA_IF = "da'if"
    MATROUK = "matrouk"
    MAJHOUL = "majhoul"


class ReliabilityFR:
    """Traductions françaises des statuts de fiabilité"""
    MAP = {
        "thiqa": "Fiable (Thiqa)",
        "hassan": "Bon (Hasan)",
        "unknown": "Inconnu",
        "da'if": "Faible (Da'if)",
        "matrouk": "Rejeté (Matrouk)",
        "majhoul": "Inconnu (Majhoul)"
    }


class TawaturTypeFR:
    MAP = {
        "lafzi": "Mutawatir Lafzi (mot à mot)",
        "ma'nawi": "Mutawatir Ma'nawi (par le sens)"
    }


class ObedienceFR:
    MAP = {
        "sunnite": "Sunnite",
        "chiite": "Chiite",
        "commun": "Commun (Sunnite & Chiite)"
    }


class Rawiy(BaseModel):
    """Narrateur (Rawi)"""
    id: str = Field(..., description="Identifiant unique du narrateur")
    name: str = Field(..., description="Nom principal du narrateur")
    kunya: Optional[str] = Field(None, description="Kunya (titre honorifique)")
    nisba: Optional[str] = Field(None, description="Nisba (origine/gentilé)")
    tabaqa: Optional[str] = Field(None, description="Tabaqa (niveau générationnel)")
    reliability: Reliability = Field(default=Reliability.UNKNOWN, description="Statut selon Jarh wa Ta'dil")
    birth_date: Optional[int] = Field(None, description="Année de naissance approximative")
    death_date: Optional[int] = Field(None, description="Année de décès approximative")
    sources: List[str] = Field(default_factory=list)
    notes: Optional[str] = Field(None)


class IsnadNode(BaseModel):
    """Nœud dans une chaîne d'Isnad"""
    rawi_id: str = Field(..., description="Identifiant du narrateur")
    rawi_name: str = Field(..., description="Nom du narrateur")
    level: int = Field(..., description="Position (0 = compilateur, niveau max = Compagnon)")


class IsnadChain(BaseModel):
    """Chaîne d'Isnad complète (du Compagnon au Compilateur)"""
    id: str = Field(..., description="Identifiant unique de la chaîne")
    nodes: List[IsnadNode] = Field(..., description="Liste ordonnée (premier = Compagnon, dernier = Compilateur)")
    path_count: Optional[int] = Field(None, description="Nombre de voies de transmission")
    sources: List[str] = Field(default_factory=list)
    description: Optional[str] = Field(None)


class IsnadTuruq(BaseModel):
    """Variante/Voie de transmission (Tariq/Turuq)"""
    id: str = Field(..., description="Identifiant de la voie")
    label: str = Field(..., description="Libellé explicite de la voie (ex. Voie 1 via Al-Humaidi)")
    isnad_chain_id: str = Field(..., description="Référence vers la chaîne d'Isnad")
    description: Optional[str] = Field(None, description="Détails complémentaires sur cette voie")


class Hadith(BaseModel):
    """Hadith Mutawatir avec support multi-voies"""
    id: str = Field(..., description="Identifiant unique du hadith")
    matn: str = Field(..., description="Texte arabe original (Matn)")
    matn_translation_fr: Optional[str] = Field(None, description="Traduction française rigoureuse du Matn")
    title_fr: str = Field(..., description="Titre français du hadith")
    title_ar: Optional[str] = Field(None, description="Titre arabe éventuel")
    tawatur_type: TawaturType = Field(..., description="Type de tawatur")
    obedience: Obedience = Field(..., description="Appartenance (Sunnite/Chiite/Commun)")
    degree_fr: str = Field(..., description="Degré de tawatur explicité en français")
    rank: Optional[int] = Field(None, description="Priorité d'authenticité/unanimite (1 = plus haut)")
    turuq: List[IsnadTuruq] = Field(default_factory=list, description="Liste des voies de transmission")
    validation_sources: List[str] = Field(default_factory=list, description="Sources classiques validant le tawatur")
    thematic_category: Optional[str] = Field(None, description="Catégorie thématique")
    keywords: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    notes: Optional[str] = Field(None)
