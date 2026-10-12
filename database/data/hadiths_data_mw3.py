# -*- coding: utf-8 -*-
"""Vague 3 : mutawatir supplémentaires sourcés (asanid détaillés inclus).

Ces traditions figurent parmi les mutawatir recensés par al-Suyuti
(*al-Azhar al-Mutanathira*) et al-Kattani (*Nazm al-Mutanathir*). Chaque voie
porte la chaîne complète telle qu'imprimée à la tête de la tradition dans le
recueil cité (dépouillement des asanid).

Format identique aux autres vagues (``hadiths_data``).
"""

HADITHS_MW3 = [
    # ==================================================================
    # 99. Interdiction de prier après l'aube et après l'Asr (lafzi)
    # ==================================================================
    {
        "id": "h_salat_baad",
        "rank": 99,
        "matn": "لَا صَلَاةَ بَعْدَ الصُّبْحِ حَتَّى تَرْتَفِعَ الشَّمْسُ، وَلَا صَلَاةَ بَعْدَ الْعَصْرِ حَتَّى تَغِيبَ الشَّمْسُ",
        "matn_translation_fr": "Il n'y a pas de prière après celle de l'aube jusqu'à ce que le soleil se lève, ni de prière après celle de l'Asr jusqu'à ce que le soleil se couche.",
        "title_fr": "Interdiction de prier après l'aube et après l'Asr",
        "title_ar": "النهي عن الصلاة بعد الفجر وبعد العصر",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons (Abu Sa'id, Ibn Abbas, Abu Hurayra, Umar, Abu Barza...)",
        "validation_sources": ["Sahih al-Bukhari 586", "Sahih Muslim 827", "Sunan Abi Dawud 1276"],
        "thematic_category": "Prières & rites",
        "keywords": ["salat", "awqat", "fajr", "asr", "prohibition"],
        "turuq": [
            {
                "label": "Abu Sa'id → Ata ibn Yazid → Al-Zuhri → Salih ibn Kaysan → Ibrahim ibn Sa'd → Abd al-Aziz → Al-Bukhari",
                "path_count": 1,
                "sources": ["Sahih al-Bukhari 586"],
                "nodes": [
                    ("abu_saeed", 4), ("ata_yazid", 2), ("al_zuhri", 2),
                    ("salih_kaysan", 1), ("ibrahim_saad", 1), ("abdulaziz_umawi", 1),
                    ("bukhari", 0),
                ],
            },
            {
                "label": "Abu Sa'id → Ata ibn Yazid → Al-Zuhri → Yunus → Ibn Wahb → Harmala → Muslim",
                "path_count": 1,
                "sources": ["Sahih Muslim 827"],
                "nodes": [
                    ("abu_saeed", 4), ("ata_yazid", 2), ("al_zuhri", 2),
                    ("yunus_ayli", 1), ("ibn_wahb", 1), ("harmala", 1),
                    ("muslim", 0),
                ],
            },
        ],
    },

    # ==================================================================
    # 100. Le Coran révélé selon sept ahruf (lafzi)
    # ==================================================================
    {
        "id": "h_ahruf",
        "rank": 100,
        "matn": "إِنَّ هَذَا الْقُرْآنَ أُنْزِلَ عَلَى سَبْعَةِ أَحْرُفٍ، فَاقْرَءُوا مَا تَيَسَّرَ مِنْهُ",
        "matn_translation_fr": "En vérité, ce Coran a été révélé selon sept modes (ahruf) ; récitez donc ce qui vous en est facile.",
        "title_fr": "La révélation du Coran selon sept ahruf",
        "title_ar": "إن هذا القرآن أنزل على سبعة أحرف",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons (Umar, Ubayy, Ibn Mas'ud, Hudhayfa...)",
        "validation_sources": ["Sahih al-Bukhari 4992", "Sahih Muslim 818", "Sunan al-Tirmidhi 2944"],
        "thematic_category": "Coran",
        "keywords": ["quran", "ahruf", "sept", "recitation"],
        "turuq": [
            {
                "label": "Omar → Abd al-Rahman ibn Abd al-Qari → Urwa → Al-Zuhri → Uqayl → Al-Layth → Sa'id ibn Ufayr → Al-Bukhari",
                "path_count": 1,
                "sources": ["Sahih al-Bukhari 4992"],
                "nodes": [
                    ("umar", 4), ("abdulrahman_qari", 2), ("urwa", 2),
                    ("al_zuhri", 2), ("uqayl", 1), ("laith", 1),
                    ("said_ufayr", 1), ("bukhari", 0),
                ],
            },
            {
                "label": "Omar → Abd al-Rahman ibn Abd al-Qari → Urwa → Al-Zuhri → Malik → Yahya ibn Yahya → Muslim",
                "path_count": 1,
                "sources": ["Sahih Muslim 818"],
                "nodes": [
                    ("umar", 4), ("abdulrahman_qari", 2), ("urwa", 2),
                    ("al_zuhri", 2), ("malik", 1), ("yahya_tamimi", 1),
                    ("muslim", 0),
                ],
            },
        ],
    },
]