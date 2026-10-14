# -*- coding: utf-8 -*-
"""Troisième vague d'extension du catalogue (intégration progressive vers ~300).

MODÈLE DE DÉPART — MODULE EN COURS D'INTÉGRATION
=================================================
Ce module contient les hadiths mutawatir supplémentaires qui entreront dans le
catalogue au fil de la validation par les savants. Le registre ``HADITHS_MW4``
est volontairement VIDE tant qu'aucune entrée n'a été validée article par
article (herméneutique : le matn exact, les Turuq et leurs chaînes doivent
être corroborés chez au moins une référence classique avant intégration).

LE MODÈLE DE DONNÉES (s'abstient de toute complétion approximative) :
------------------------------------------------------------------------
Chaque entrée est un dict conforme au schéma du catalogue (voir
``database/data/hadiths_data.py`` pour la référence complète et détaillée) :

    {
        # ``id`` : identifiant unique, préfixe "h_" + slug court (kebab-case).
        "id": "h_<slug>",
        # ``rank`` : priorité d'authenticité / unanimité (1 = le plus incontesté).
        # IMPORTANT : les rangs doivent rester UNIQUES sur tout le catalogue —
        # décaler les rangs existants avant de fixer un nouveau rang.
        "rank": 1_000_000,
        "matn": "النص العربي…",
        "matn_translation_fr": "Traduction française rigoureuse.",
        "title_fr": "Titre français",
        "title_ar": "العنوان العربي",
        "tawatur_type": "lafzi",            # ou "ma'nawi"
        "obedience": "commun",              # ou "sunnite" / "chiite"
        "degree_fr": "Degré de tawatur explicité en français.",
        "validation_sources": ["Recueil classique, tome/page", …],
        "thematic_category": "Catégorie thématique",
        "keywords": ["mot_cle", …],
        # ``turuq`` : AU MOINS une voie ; chaque nœud référence un narrateur du
        # registre (RAWIS / RAWIS_EXTRA / RAWIS_RIJAL). Niveau : 4 = Compagnon,
        # 3 = Imam/Tabi'i majeur, 2 = Tabi'i, 1 = intermédiaire, 0 = compilateur.
        "turuq": [
            {
                "label": "Compagnon → Imam → Compilateur",
                "path_count": 1,
                "sources": ["Recueil classique, tome/page"],
                "nodes": [("rawi_id", 4), ("rawi_id", 1), ("rawi_id", 0)],
            },
        ],
    }

PROCÉDURE D'INTÉGRATION D'UNE ENTRÉE VALIDÉE :
-----------------------------------------------
1. Ajouter l'entrée au tableau ``HADITHS_MW4`` ci-dessous (respecter le schéma) ;
2. Si un narrateur n'existe pas encore, l'ajouter à ``database/data/rawis_rijal.py``
   (ou ``rawis_data_extra.py``) ;
3. Lancer l'audit : ``python database/check_data.py`` (ajouter ``--strict`` en CI) ;
4. Lorsque le groupe d'entrées est validé par les savants, passer le statut du
   module de ``DRAFT`` à ``VALIDATED`` dans ``database/data/catalog.py``.

Les chaînes de détail longues (narrateur par narrateur) peuvent aussi être
déclarées dans ``database/data/isnad_expansions.py`` sous la clé ``h_<slug>``
au lieu d'être inline — le catalogue les fusionne automatiquement.
"""

HADITHS_MW4: list = [
    # …
]