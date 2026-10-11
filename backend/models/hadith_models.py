from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class TawaturType(str, Enum):
    """Type of tawatur classification."""
    LAFZI = "lafzi"  # Mutawatir Lafzi
    MA_NAWI = "ma'nawi"  # Mutawatir Ma'nawi


class Obedience(str, Enum):
    """Religious school/obedience classification."""
    SUNNITE = "sunnite"
    CHIITE = "chiite"
    COMMUN = "commun"  # Shared between both


class Reliability(str, Enum):
    """Jarh wa Ta'dil reliability classification."""
    THIQA = "thiqa"  # Trustworthy
    HASSAN = "hassan"  # Good
    UNKNOWN = "unknown"
    DA_IF = "da'if"  # Weak (for reference, though mutawatir usually strong)
    MATROUK = "matrouk"  # Abandoned


class Rawiy(BaseModel):
    """Narrator (Rawi) model."""
    id: str = Field(..., description="Unique identifier for narrator")
    name: str = Field(..., description="Primary name of narrator")
    kunya: Optional[str] = Field(None, description="Honorific name (Kunya)")
    nisba: Optional[str] = Field(None, description="Attributed origin (Nisba)")
    tabaqa: Optional[str] = Field(None, description="Generational level (Tabaqat)")
    reliability: Reliability = Field(default=Reliability.UNKNOWN, description="Reliability per Jarh wa Ta'dil")
    birth_date: Optional[int] = Field(None, description="Approximate birth year (Hijri/CE context)")
    death_date: Optional[int] = Field(None, description="Approximate death year")
    sources: List[str] = Field(default_factory=list, description="Sources of biographical info")
    notes: Optional[str] = Field(None, description="Additional notes")


class IsnadNode(BaseModel):
    """Individual node in isnad chain."""
    rawi_id: str = Field(..., description="ID of narrator")
    rawi_name: str = Field(..., description="Name of narrator for readability")
    level: int = Field(..., description="Position in chain (0 = compiler, n = companion)")


class IsnadChain(BaseModel):
    """Full isnad chain ordered from companion to compiler."""
    id: str = Field(..., description="Unique identifier for isnad chain")
    nodes: List[IsnadNode] = Field(..., description="Ordered list of narrators (first=companion, last=compiler)")
    path_count: Optional[int] = Field(None, description="Number of transmission paths (for mutawatir)")
    sources: List[str] = Field(default_factory=list, description="Sources documenting this chain")


class Hadith(BaseModel):
    """Hadith model focusing on mutawatir narrations."""
    id: str = Field(..., description="Unique identifier for hadith")
    matn: str = Field(..., description="Arabic text of hadith (Matn)")
    matn_translation: Optional[str] = Field(None, description="Translation of matn")
    title: str = Field(..., description="Short descriptive title")
    tawatur_type: TawaturType = Field(..., description="Lafzi or Ma'nawi")
    obedience: Obedience = Field(..., description="Sunnite/Chiite/Commun")
    degree: str = Field(..., description="Degree of tawatur (e.g., 'Mutawatir by consensus')")
    isnad_chain_id: str = Field(..., description="Reference to primary isnad chain")
    alternative_chains: List[str] = Field(default_factory=list, description="Additional isnad chain IDs")
    validation_sources: List[str] = Field(default_factory=list, description="Classical sources validating tawatur")
    thematic_category: Optional[str] = Field(None, description="Thematic category (beliefs, rituals, etc.)")
    keywords: List[str] = Field(default_factory=list, description="Search keywords")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    notes: Optional[str] = Field(None, description="Additional notes")
