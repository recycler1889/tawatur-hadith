# -*- coding: utf-8 -*-
"""Assemblage des données initiales du projet Tawatur Hadith.

Point d'entrée unique : ``create_seed_data()``.

Les données brutes sont séparées (package ``database.data``) pour rester
maintenables et extensibles, et agrégées par le catalogue central
(``database/data/catalog.py``) qui en pilote l'intégration progressive vers
le corpus complet des hadiths mutawatir validés par les savants (~300).

Registres de narrateurs :
- ``rawis_data_Rawis.RAWIS`` : registre des narrateurs (Rijal) ;
- ``rawis_data_extra.RAWIS_EXTRA`` : narrateurs additionnels (fusionnés) ;
- ``rawis_rijal.RAWIS_RIJAL`` : narrateurs intermédiaires (Tabi'un, atba'
  al-tabi'in, shuyukh des compilateurs) issus du dépouillement des asanid.

Registres de hadiths (vagues d'extension, voir le manifeste du catalogue) :
- ``hadiths_data.HADITHS``, ``hadiths_data_mw1.HADITHS_MW1``,
  ``hadiths_data_mw2.HADITHS_MW2``, ``hadiths_data_mw3.HADITHS_MW3``,
  ``hadiths_data_mw4.HADITHS_MW4`` : chacun porte ses voies (Turuq) avec la
  chaîne COMPLÈTE inline (Compagnon → Tabi'i/Imam → compilateur) ;
- ``isnad_expansions.ISNAD_EXPANSIONS`` : chaînes détaillées (narrateur par
  narrateur) ajoutées aux hadiths existants, d'après les asanid des recueils.

L'assembleur :
1. construit les modèles Pydantic (Rawiy, IsnadChain, Hadith) ;
2. transforme chaque voie inline en ``IsnadChain`` référencée ;
3. valide l'intégrité référentielle (narrateurs et turuq non vides) ;
4. trie les hadiths par ``rank`` (1 = plus haut degré d'authenticité).

Performance : l'ensemble (~100 hadiths, ~370 chaînes) se construit en quelques
dizaines de millisecondes et est mis en cache côté application Streamlit.
"""

from typing import Dict, List

from backend.models.hadith_models import (
    Hadith,
    IsnadChain,
    IsnadNode,
    IsnadTuruq,
    Rawiy,
)
from database.data.catalog import (
    ALL_HADITHS,
    ALL_RAWIS,
    MODULES,
    coverage_status,
)
from database.data.isnad_expansions import ISNAD_EXPANSIONS


class SeedDataError(ValueError):
    """Erreur d'intégrité des données de départ."""


def _build_rawis() -> Dict[str, Rawiy]:
    return {key: Rawiy(**value) for key, value in ALL_RAWIS.items()}


def _build_hadith(rawis: Dict[str, Rawiy], spec: Dict, chains: Dict[str, IsnadChain]) -> Hadith:
    hid = spec["id"]
    turuq: List[IsnadTuruq] = []

    voies = list(spec.get("turuq", [])) + list(ISNAD_EXPANSIONS.get(hid, []))
    for index, voie in enumerate(voies, start=1):
        cid = f"{hid}_c{index}"
        nodes: List[IsnadNode] = []
        for entry in voie["nodes"]:
            rawi_id, level = entry
            rawi = rawis.get(rawi_id)
            if rawi is None:
                raise SeedDataError(
                    f"Hadith '{hid}', voie {index} : narrateur inconnu '{rawi_id}'."
                )
            nodes.append(IsnadNode(rawi_id=rawi_id, rawi_name=rawi.name, level=level))
        if not nodes:
            raise SeedDataError(f"Hadith '{hid}', voie {index} : chaîne vide.")

        chains[cid] = IsnadChain(
            id=cid,
            nodes=nodes,
            path_count=voie.get("path_count"),
            sources=list(voie.get("sources", [])),
        )
        turuq.append(IsnadTuruq(
            id=f"t{index}",
            label=voie["label"],
            isnad_chain_id=cid,
            description=voie.get("description"),
        ))

    return Hadith(
        id=hid,
        matn=spec["matn"],
        matn_translation_fr=spec.get("matn_translation_fr"),
        title_fr=spec["title_fr"],
        title_ar=spec.get("title_ar"),
        tawatur_type=spec["tawatur_type"],
        obedience=spec["obedience"],
        degree_fr=spec["degree_fr"],
        turuq=turuq,
        validation_sources=list(spec.get("validation_sources", [])),
        thematic_category=spec.get("thematic_category"),
        keywords=list(spec.get("keywords", [])),
        rank=spec.get("rank"),
    )


def create_seed_data() -> Dict:
    """Retourne ``{rawis, isnad_chains, hadiths}`` prêt pour l'application."""
    rawis = _build_rawis()
    chains: Dict[str, IsnadChain] = {}
    hadiths: Dict[str, Hadith] = {}

    specs = sorted(ALL_HADITHS, key=lambda s: (s.get("rank", 1_000_000), s["id"]))
    seen = set()
    for spec in specs:
        if spec["id"] in seen:
            raise SeedDataError(f"Identifiant de hadith dupliqué : '{spec['id']}'.")
        seen.add(spec["id"])
        hadith = _build_hadith(rawis, spec, chains)
        hadiths[hadith.id] = hadith

    return {
        "rawis": {key: value.model_dump() for key, value in rawis.items()},
        "isnad_chains": {key: value.model_dump() for key, value in chains.items()},
        "hadiths": {key: value.model_dump() for key, value in hadiths.items()},
    }


if __name__ == "__main__":
    data = create_seed_data()
    cov = coverage_status()
    print(
        f"OK — {len(data['hadiths'])} hadiths, "
        f"{len(data['isnad_chains'])} chaînes, "
        f"{len(data['rawis'])} narrateurs."
    )
    print(
        f"Progression : {cov['current']}/{cov['target']} catalogués "
        f"({cov['validated']} validés), {cov['modules_validated']}/"
        f"{cov['modules']} modules VALIDATED, {cov['remaining']} restants."
    )
