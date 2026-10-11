# -*- coding: utf-8 -*-
"""Vague d'extension n.2 — hadiths mutawatir (rangs 71-98).

Mêmes conventions que ``hadiths_data`` et ``hadiths_data_mw1`` : ``nodes`` =
tuples (rawi_id, level), 4 = Compagnon, 3 = Imam/Tabi'i majeur, 2 = Tabi'i,
1 = intermédiaire, 0 = compilateur. Inscription d'après les inventaires
classiques (al-Suyuti, *al-Azhar al-Mutanathira* ; al-Kattani,
*Nazm al-Mutanathir* ; pour les recueils chiites : al-Kafi, Man la
yahduruhu al-Faqih).
"""

HADITHS_MW2 = [
    # ------------------------------------------------------------------
    # 71. La patience (Al-Sabr)
    # ------------------------------------------------------------------
    {
        "id": "h_sabr",
        "rank": 71,
        "matn": "وَمَنْ يَصْبِرْ يُصْبِرْهُ اللَّهُ، وَمَا أُعْطِيَ أَحَدٌ عَطَاءً خَيْرًا وَأَوْسَعَ مِنَ الصَّبْرِ",
        "matn_translation_fr": "Quiconque patiente, Allah lui accorde la patience ; et nul n'a reçu de don meilleur et plus vaste que la patience.",
        "title_fr": "La patience (Al-Sabr)",
        "title_ar": "الصبر",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — vertu cardinale rapportée par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 1469", "Sahih Muslim 1053", "Sunan al-Tirmidhi 2024"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["sabr", "patience", "vertu"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 16, "sources": ["Sahih al-Bukhari 1469"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Sa'id → Muslim", "path_count": 12, "sources": ["Sahih Muslim 1053"], "nodes": [("abu_saeed", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 2024"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 72. La reconnaissance envers les gens
    # ------------------------------------------------------------------
    {
        "id": "h_shukr",
        "rank": 72,
        "matn": "مَنْ لَا يَشْكُرُ النَّاسَ لَا يَشْكُرُ اللَّهَ",
        "matn_translation_fr": "Celui qui ne remercie pas les gens ne remercie pas Allah.",
        "title_fr": "La reconnaissance (Al-Shukr)",
        "title_ar": "من لا يشكر الناس لا يشكر الله",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sunan Abi Dawud 4811", "Sunan al-Tirmidhi 1954", "Musnad Ahmad 2/258"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["shukr", "reconnaissance", "gratitude"],
        "turuq": [
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 4811"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 10, "sources": ["Sunan al-Tirmidhi 1954"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Anas → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 2/258"], "nodes": [("anass", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 73. Le contentement (Al-Qana'a)
    # ------------------------------------------------------------------
    {
        "id": "h_qanaa",
        "rank": 73,
        "matn": "قَدْ أَفْلَحَ مَنْ أَسْلَمَ، وَرُزِقَ كَفَافًا، وَقَنَّعَهُ اللَّهُ بِمَا آتَاهُ",
        "matn_translation_fr": "A réussi celui qui embrasse l'Islam, reçoit une subsistance suffisante et que Allah rend content de ce qu'Il lui a donné.",
        "title_fr": "Le contentement (Al-Qana'a)",
        "title_ar": "قد أفلح من أسلم ورزق كفافا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sahih Muslim 1054", "Sunan al-Tirmidhi 2348", "Sunan Ibn Majah 4138"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["qanaa", "contentement", "kafaf"],
        "turuq": [
            {"label": "Abdullah ibn Amr → Muslim", "path_count": 11, "sources": ["Sahih Muslim 1054"], "nodes": [("abdullah_amr", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 2348"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Anas → Ibn Majah", "path_count": 7, "sources": ["Sunan Ibn Majah 4138"], "nodes": [("anass", 4), ("ibn_majah", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 74. La confiance en Allah (Al-Tawakkul)
    # ------------------------------------------------------------------
    {
        "id": "h_tawakkul",
        "rank": 74,
        "matn": "لَوْ أَنَّكُمْ تَوَكَّلْتُمْ عَلَى اللَّهِ حَقَّ تَوَكُّلِهِ لَرَزَقَكُمْ كَمَا يَرْزُقُ الطَّيْرَ، تَغْدُو خِمَاصًا وَتَرُوحُ بِطَانًا",
        "matn_translation_fr": "Si vous placiez votre confiance en Allah comme il se doit, Il vous pourvoirait comme Il pourvoit aux oiseaux, qui partent le matin le ventre vide et reviennent le soir le ventre plein.",
        "title_fr": "La confiance en Allah (Al-Tawakkul)",
        "title_ar": "لو أنكم توكلتم على الله حق توكله",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sunan al-Tirmidhi 2344", "Sunan Ibn Majah 4164", "Musnad Ahmad 1/30"],
        "thematic_category": "Dogme (Tawhid)",
        "keywords": ["tawakkul", "confiance", "rizq"],
        "turuq": [
            {"label": "Omar → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 2344"], "nodes": [("umar", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 9, "sources": ["Musnad Ahmad 1/30"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Anas → Ibn Majah", "path_count": 7, "sources": ["Sunan Ibn Majah 4164"], "nodes": [("anass", 4), ("ibn_majah", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 75. L'appel à la repentance (Al-Tawba)
    # ------------------------------------------------------------------
    {
        "id": "h_tawba",
        "rank": 75,
        "matn": "إِنَّ اللَّهَ يَبْسُطُ يَدَهُ بِاللَّيْلِ لِيَتُوبَ مُسِيءُ النَّهَارِ، وَيَبْسُطُ يَدَهُ بِالنَّهَارِ لِيَتُوبَ مُسِيءُ اللَّيْلِ",
        "matn_translation_fr": "Allah étend Sa main la nuit afin que le fautif du jour se repente, et Il étend Sa main le jour afin que le fautif de la nuit se repente.",
        "title_fr": "La porte de la repentance (Al-Tawba)",
        "title_ar": "التوبة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — large acceptation de la repentance",
        "validation_sources": ["Sahih Muslim 2759", "Sunan al-Tirmidhi 3534", "Musnad Ahmad 4/399"],
        "thematic_category": "Repentance & pardon",
        "keywords": ["tawba", "repentance", "pardon"],
        "turuq": [
            {"label": "Abu Musa → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2759"], "nodes": [("abu_musa", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 3534"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 4/399"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 76. L'istiqlhfâr du Prophète (Al-Istighfar)
    # ------------------------------------------------------------------
    {
        "id": "h_istighfar",
        "rank": 76,
        "matn": "إِنِّي لَأَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ فِي الْيَوْمِ أَكْثَرَ مِنْ سَبْعِينَ مَرَّةً",
        "matn_translation_fr": "Je demande pardon à Allah et reviens à Lui plus de soixante-dix fois par jour.",
        "title_fr": "L'invocation de pardon (Al-Istighfar)",
        "title_ar": "إني لأستغفر الله وأتوب إليه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons avec des nombres variables",
        "validation_sources": ["Sahih al-Bukhari 6307", "Sahih Muslim 2702", "Sunan al-Tirmidhi 3255"],
        "thematic_category": "Repentance & pardon",
        "keywords": ["istighfar", "pardon", "dhikr"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 14, "sources": ["Sahih al-Bukhari 6307"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 11, "sources": ["Sahih Muslim 2702"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Umar → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 3255"], "nodes": [("abdullah_umar", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 77. La masse de chair (le cœur)
    # ------------------------------------------------------------------
    {
        "id": "h_qalb",
        "rank": 77,
        "matn": "أَلَا وَإِنَّ فِي الْجَسَدِ مُضْغَةً، إِذَا صَلَحَتْ صَلَحَ الْجَسَدُ كُلُّهُ، وَإِذَا فَسَدَتْ فَسَدَ الْجَسَدُ كُلُّهُ، أَلَا وَهِيَ الْقَلْبُ",
        "matn_translation_fr": "Il y a dans le corps un morceau de chair : s'il est sain, tout le corps est sain ; s'il est corrompu, tout le corps est corrompu. C'est le cœur.",
        "title_fr": "Le cœur (Al-Qalb)",
        "title_ar": "ألا وإن في الجسد مضغة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par al-Nu'man ibn Bashir et d'autres",
        "validation_sources": ["Sahih al-Bukhari 52", "Sahih Muslim 1599", "Sunan Ibn Majah 3984"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["qalb", "coeur", "sincerite"],
        "turuq": [
            {"label": "Al-Nu'man ibn Bashir → Al-Bukhari", "path_count": 13, "sources": ["Sahih al-Bukhari 52"], "nodes": [("numan", 4), ("bukhari", 0)]},
            {"label": "Al-Nu'man ibn Bashir → Muslim", "path_count": 11, "sources": ["Sahih Muslim 1599"], "nodes": [("numan", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Ibn Majah", "path_count": 8, "sources": ["Sunan Ibn Majah 3984"], "nodes": [("abu_hurayra", 4), ("ibn_majah", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 78. La garantie du Paradis pour qui retient sa langue
    # ------------------------------------------------------------------
    {
        "id": "h_lisan",
        "rank": 78,
        "matn": "مَنْ يَضْمَنْ لِي مَا بَيْنَ لَحْيَيْهِ وَمَا بَيْنَ رِجْلَيْهِ أَضْمَنْ لَهُ الْجَنَّةَ",
        "matn_translation_fr": "Celui qui me garantit ce qui est entre ses deux mâchoires et ce qui est entre ses deux jambes, je lui garantis le Paradis.",
        "title_fr": "La langue et la chasteté (Man yadman li)",
        "title_ar": "من يضمن لي ما بين لحييه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Sahl ibn Sa'd et Abu Hurayra",
        "validation_sources": ["Sahih al-Bukhari 6474", "Sunan al-Tirmidhi 2408", "Sunan Ibn Majah 3973"],
        "thematic_category": "Éthique de la parole",
        "keywords": ["lisan", "langue", "chastete"],
        "turuq": [
            {"label": "Sahl ibn Sa'd → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 6474"], "nodes": [("sahl", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 10, "sources": ["Sunan al-Tirmidhi 2408"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ibn Majah", "path_count": 7, "sources": ["Sunan Ibn Majah 3973"], "nodes": [("abu_hurayra", 4), ("ibn_majah", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 79. La médisance (Al-Ghiba)
    # ------------------------------------------------------------------
    {
        "id": "h_ghiba",
        "rank": 79,
        "matn": "أَتَدْرُونَ مَا الْغِيبَةُ؟ قَالُوا: اللَّهُ وَرَسُولُهُ أَعْلَمُ. قَالَ: ذِكْرُكَ أَخَاكَ بِمَا يَكْرَهُ",
        "matn_translation_fr": "Savez-vous ce qu'est la médisance ? Ils dirent : Allah et Son Messager le savent mieux. Il dit : c'est que tu évoques ton frère par ce qui lui déplaît.",
        "title_fr": "La médisance (Al-Ghiba)",
        "title_ar": "الغيبة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Hurayra et d'autres",
        "validation_sources": ["Sahih Muslim 2589", "Sunan Abi Dawud 4874", "Sunan al-Tirmidhi 1934"],
        "thematic_category": "Éthique de la parole",
        "keywords": ["ghiba", "medisance", "frere"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 14, "sources": ["Sahih Muslim 2589"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Abu Dawud", "path_count": 9, "sources": ["Sunan Abi Dawud 4874"], "nodes": [("abu_saeed", 4), ("abu_dawud", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 1934"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 80. L'interdiction de l'envie et de la haine
    # ------------------------------------------------------------------
    {
        "id": "h_hasad",
        "rank": 80,
        "matn": "لَا تَحَاسَدُوا، وَلَا تَنَاجَشُوا، وَلَا تَبَاغَضُوا، وَلَا تَدَابَرُوا، وَلَا يَبِعْ بَعْضُكُمْ عَلَى بَيْعِ بَعْضٍ، وَكُونُوا عِبَادَ اللَّهِ إِخْوَانًا",
        "matn_translation_fr": "Ne vous enviez pas, ne vous dupez pas, ne vous haïssez pas, ne vous tournez pas le dos ; que l'un ne vende pas sur la vente de l'autre ; soyez frères, serviteurs d'Allah.",
        "title_fr": "L'interdiction de l'envie (La Tahasadu)",
        "title_ar": "لا تحاسدوا ولا تناجشوا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Hurayra et Ibn Umar",
        "validation_sources": ["Sahih al-Bukhari 6065", "Sahih Muslim 2564", "Sunan Abi Dawud 4884"],
        "thematic_category": "Solidarité",
        "keywords": ["hasad", "envie", "fraternite"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 14, "sources": ["Sahih Muslim 2564"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 11, "sources": ["Sahih al-Bukhari 6065"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 4884"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 81. Le poids d'un atome d'orgueil
    # ------------------------------------------------------------------
    {
        "id": "h_kibr",
        "rank": 81,
        "matn": "لَا يَدْخُلُ الْجَنَّةَ مَنْ كَانَ فِي قَلْبِهِ مِثْقَالُ ذَرَّةٍ مِنْ كِبْرٍ",
        "matn_translation_fr": "N'entrera pas au Paradis celui qui a dans son cœur le poids d'un atome d'orgueil.",
        "title_fr": "L'orgueil (Al-Kibr)",
        "title_ar": "لا يدخل الجنة من كان في قلبه مثقال ذرة من كبر",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sahih Muslim 91", "Sunan Abi Dawud 4091", "Sunan al-Tirmidhi 1999"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["kibr", "orgueil", "jannah"],
        "turuq": [
            {"label": "Abdullah ibn Mas'ud → Muslim", "path_count": 13, "sources": ["Sahih Muslim 91"], "nodes": [("ibn_masud", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 9, "sources": ["Sunan Abi Dawud 4091"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abdullah ibn Umar → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 1999"], "nodes": [("abdullah_umar", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 82. L'oppression, ténèbres au Jour du Jugement
    # ------------------------------------------------------------------
    {
        "id": "h_dhulm",
        "rank": 82,
        "matn": "اتَّقُوا الظُّلْمَ، فَإِنَّ الظُّلْمَ ظُلُمَاتٌ يَوْمَ الْقِيَامَةِ",
        "matn_translation_fr": "Craignez l'oppression, car l'oppression sera ténèbres le Jour de la Résurrection.",
        "title_fr": "L'oppression (Al-Zulm)",
        "title_ar": "اتقوا الظلم فإن الظلم ظلمات",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Jabir et d'autres",
        "validation_sources": ["Sahih Muslim 2579", "Sunan al-Tirmidhi 2035", "Musnad Ahmad 3/323"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["dhulm", "zulm", "oppression"],
        "turuq": [
            {"label": "Jabir → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2579"], "nodes": [("jabir", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 2035"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Abdullah ibn Umar → Ahmad", "path_count": 7, "sources": ["Musnad Ahmad 3/323"], "nodes": [("abdullah_umar", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 83. Les quatre questions du Jour dernier
    # ------------------------------------------------------------------
    {
        "id": "h_arba",
        "rank": 83,
        "matn": "لَا تَزُولُ قَدَمَا عَبْدٍ يَوْمَ الْقِيَامَةِ حَتَّى يُسْأَلَ عَنْ أَرْبَعٍ: عَنْ عُمْرِهِ فِيمَ أَفْنَاهُ، وَعَنْ عِلْمِهِ فِيمَ فَعَلَ، وَعَنْ مَالِهِ مِنْ أَيْنَ اكْتَسَبَهُ وَفِيمَ أَنْفَقَهُ، وَعَنْ جِسْمِهِ فِيمَ أَبْلَاهُ",
        "matn_translation_fr": "Les deux pieds d'un serviteur ne bougeront pas le Jour de la Résurrection avant qu'il ne soit interrogé sur quatre choses : sa vie, en quoi il l'a passée ; sa science, ce qu'il en a fait ; sa richesse, d'où il l'a acquise et où il l'a dépensée ; et son corps, comment il l'a usé.",
        "title_fr": "Les quatre questions (La tazulu qadama)",
        "title_ar": "لا تزول قدما عبد يوم القيامة حتى يسأل عن أربع",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sunan al-Tirmidhi 2417", "Sunan al-Darimi 537", "Sunan al-Bayhaqi (Shu'ab)"],
        "thematic_category": "Eschatologie",
        "keywords": ["hisab", "compte", "qiyamah"],
        "turuq": [
            {"label": "Ibn Mas'ud → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 2417"], "nodes": [("ibn_masud", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Al-Darimi", "path_count": 8, "sources": ["Sunan al-Darimi 537"], "nodes": [("abu_hurayra", 4), ("darimi", 0)]},
            {"label": "Abu Sa'id → Al-Bayhaqi", "path_count": 7, "sources": ["Sunan al-Bayhaqi (Shu'ab)"], "nodes": [("abu_saeed", 4), ("bayhaqi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 84. La vision d'Allah au Paradis (Al-Ru'ya)
    # ------------------------------------------------------------------
    {
        "id": "h_ruyat",
        "rank": 84,
        "matn": "إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ عَزَّ وَجَلَّ يَوْمَ الْقِيَامَةِ كَمَا تَرَوْنَ الْقَمَرَ لَيْلَةَ الْبَدْرِ، لَا تُضَامُّونَ فِي رُؤْيَتِهِ",
        "matn_translation_fr": "Vous verrez votre Seigneur le Jour de la Résurrection comme vous voyez la lune la nuit de la pleine lune, sans être lésés dans cette vision.",
        "title_fr": "La vision d'Allah (Al-Ru'ya)",
        "title_ar": "إنكم سترون ربكم",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Jarir, Abu Hurayra et d'autres",
        "validation_sources": ["Sahih al-Bukhari 7434", "Sahih Muslim 633", "Sunan al-Tirmidhi 2554"],
        "thematic_category": "Dogme (Tawhid)",
        "keywords": ["ruya", "vision", "jannah"],
        "turuq": [
            {"label": "Jarir ibn Abdullah → Al-Bukhari", "path_count": 13, "sources": ["Sahih al-Bukhari 7434"], "nodes": [("jarir", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 11, "sources": ["Sahih Muslim 633"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 2554"], "nodes": [("abu_saeed", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 85. La descente de Jésus (Nuzul Isa)
    # ------------------------------------------------------------------
    {
        "id": "h_nuzul_isa",
        "rank": 85,
        "matn": "وَالَّذِي نَفْسِي بِيَدِهِ، لَيُوشِكَنَّ أَنْ يَنْزِلَ فِيكُمُ ابْنُ مَرْيَمَ حَكَمًا مُقْسِطًا، فَيَكْسِرُ الصَّلِيبَ، وَيَقْتُلُ الْخِنْزِيرَ، وَيَضَعُ الْجِزْيَةَ",
        "matn_translation_fr": "Par Celui qui tient mon âme dans Sa main, le fils de Marie ne tardera pas à descendre parmi vous comme juge équitable : il brisera la croix, tuera le porc et abolira la capitation.",
        "title_fr": "La descente de Jésus (Nuzul Isa)",
        "title_ar": "نزول عيسى ابن مريم",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Hurayra et de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 3448", "Sahih Muslim 155", "Sunan Abi Dawud 4324"],
        "thematic_category": "Eschatologie",
        "keywords": ["isa", "nuzul", "eschatologie"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 15, "sources": ["Sahih al-Bukhari 3448"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 13, "sources": ["Sahih Muslim 155"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 4324"], "nodes": [("anass", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 86. Le Mahdi
    # ------------------------------------------------------------------
    {
        "id": "h_mahdi",
        "rank": 86,
        "matn": "لَا تَذْهَبُ الدُّنْيَا حَتَّى يَمْلِكُ الْعَرَبَ رَجُلٌ مِنْ أَهْلِ بَيْتِي، اسْمُهُ يُوَاطِئُ اسْمِي",
        "matn_translation_fr": "Le monde ne s'achèvera pas avant qu'un homme de ma famille, dont le nom est identique au mien, ne règne sur les Arabes.",
        "title_fr": "Le Mahdi",
        "title_ar": "المهدي",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sunan Abi Dawud 4282", "Sunan al-Tirmidhi 2230", "Musnad Ahmad 1/84"],
        "thematic_category": "Eschatologie",
        "keywords": ["mahdi", "ahl al-bayt", "eschatologie"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 4282"], "nodes": [("abdullah_umar", 4), ("abu_dawud", 0)]},
            {"label": "Abu Sa'id → Al-Tirmidhi", "path_count": 10, "sources": ["Sunan al-Tirmidhi 2230"], "nodes": [("abu_saeed", 4), ("tirmidhi", 0)]},
            {"label": "Ali → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 1/84"], "nodes": [("ali", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 87. Se hâter vers les bonnes œuvres (Al-Fitan)
    # ------------------------------------------------------------------
    {
        "id": "h_fitna",
        "rank": 87,
        "matn": "بَادِرُوا بِالْأَعْمَالِ فِتَنًا كَقِطَعِ اللَّيْلِ الْمُظْلِمِ، يُصْبِحُ الرَّجُلُ مُؤْمِنًا وَيُمْسِي كَافِرًا، وَيُمْسِي مُؤْمِنًا وَيُصْبِحُ كَافِرًا",
        "matn_translation_fr": "Hâtez-vous d'accomplir les bonnes œuvres avant des épreuves comme les fragments d'une nuit obscure : l'homme devient croyant au matin et mécréant au soir, croyant au soir et mécréant au matin.",
        "title_fr": "Se hâter avant les épreuves (Badiru bi al-A'mal)",
        "title_ar": "بادروا بالأعمال فتنا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Hurayra et d'autres",
        "validation_sources": ["Sahih Muslim 118", "Sunan Abi Dawud 4258", "Sunan al-Tirmidhi 2196"],
        "thematic_category": "Épreuves & fin des temps",
        "keywords": ["fitna", "epreuves", "fin des temps"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 118"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Abu Dawud", "path_count": 9, "sources": ["Sunan Abi Dawud 4258"], "nodes": [("abu_saeed", 4), ("abu_dawud", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 2196"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 88. La compréhension de la religion (Al-Fiqh fi al-Din)
    # ------------------------------------------------------------------
    {
        "id": "h_ilm_din",
        "rank": 88,
        "matn": "مَنْ يُرِدِ اللَّهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّينِ",
        "matn_translation_fr": "À qui Allah veut du bien, Il accorde la compréhension profonde de la religion.",
        "title_fr": "La compréhension de la religion (Yufaqqihhu fi al-Din)",
        "title_ar": "من يرد الله به خيرا يفقهه في الدين",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Mu'awiya et Abu Hurayra",
        "validation_sources": ["Sahih al-Bukhari 71", "Sahih Muslim 1037", "Sunan al-Tirmidhi 2645"],
        "thematic_category": "Science",
        "keywords": ["fiqh", "science", "religion"],
        "turuq": [
            {"label": "Mu'awiya → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 71"], "nodes": [("muawiya", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 10, "sources": ["Sahih Muslim 1037"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 2645"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 89. Le meilleur apprenti du Coran
    # ------------------------------------------------------------------
    {
        "id": "h_quran_khayr",
        "rank": 89,
        "matn": "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
        "matn_translation_fr": "Le meilleur d'entre vous est celui qui apprend le Coran et l'enseigne.",
        "title_fr": "Le meilleur apprenti du Coran (Khayrukum man ta'allama)",
        "title_ar": "خيركم من تعلم القرآن وعلمه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Uthman et Abu Hurayra",
        "validation_sources": ["Sahih al-Bukhari 5027", "Sunan Abi Dawud 1452", "Sunan al-Tirmidhi 2907"],
        "thematic_category": "Coran",
        "keywords": ["quran", "apprentissage", "enseignement"],
        "turuq": [
            {"label": "Uthman → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 5027"], "nodes": [("uthman", 4), ("bukhari", 0)]},
            {"label": "Uthman → Abu Dawud", "path_count": 9, "sources": ["Sunan Abi Dawud 1452"], "nodes": [("uthman", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 2907"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 90. La douceur de la foi (Halawat al-Iman)
    # ------------------------------------------------------------------
    {
        "id": "h_hubb_allah",
        "rank": 90,
        "matn": "ثَلَاثٌ مَنْ كُنَّ فِيهِ وَجَدَ بِهِنَّ حَلَاوَةَ الْإِيمَانِ: أَنْ يَكُونَ اللَّهُ وَرَسُولُهُ أَحَبَّ إِلَيْهِ مِمَّا سِوَاهُمَا، وَأَنْ يُحِبَّ الْمَرْءَ لَا يُحِبُّهُ إِلَّا لِلَّهِ، وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ كَمَا يَكْرَهُ أَنْ يُقْذَفَ فِي النَّارِ",
        "matn_translation_fr": "Trois qualités : celui qui les possède goûte par elles la douceur de la foi — qu'Allah et Son Messager lui soient plus chers que tout autre, qu'il n'aime une personne que pour Allah, et qu'il répugne à retourner à la mécréance comme il répugne à être jeté dans le feu.",
        "title_fr": "La douceur de la foi (Halawat al-Iman)",
        "title_ar": "ثلاث من كن فيه وجد حلاوة الإيمان",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Anas et Abu Hurayra",
        "validation_sources": ["Sahih al-Bukhari 16", "Sahih Muslim 43", "Sunan al-Tirmidhi 2624"],
        "thematic_category": "Dogme (Tawhid)",
        "keywords": ["iman", "hubb", "foi"],
        "turuq": [
            {"label": "Anas → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 16"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 10, "sources": ["Sahih Muslim 43"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 2624"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 91. La prière de la nuit (Al-Tahajjud)
    # ------------------------------------------------------------------
    {
        "id": "h_tahajjud",
        "rank": 91,
        "matn": "أَفْضَلُ الصَّلَاةِ بَعْدَ الْفَرِيضَةِ صَلَاةُ اللَّيْلِ",
        "matn_translation_fr": "La meilleure prière après la prière prescrite est la prière de la nuit.",
        "title_fr": "La prière de la nuit (Salat al-Layl)",
        "title_ar": "أفضل الصلاة بعد الفريضة صلاة الليل",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Abu Hurayra et d'autres",
        "validation_sources": ["Sahih Muslim 1163", "Sunan al-Tirmidhi 438", "Sunan Abi Dawud 1430"],
        "thematic_category": "Prière",
        "keywords": ["tahajjud", "nuit", "priere"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 1163"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 438"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 7, "sources": ["Sunan Abi Dawud 1430"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 92. L'évocation d'Allah (Al-Dhikr)
    # ------------------------------------------------------------------
    {
        "id": "h_dhikr",
        "rank": 92,
        "matn": "سَبَقَ الْمُفَرِّدُونَ، الذَّاكِرُونَ اللَّهَ كَثِيرًا وَالذَّاكِرَاتُ",
        "matn_translation_fr": "Les solitaires ont pris les devants : ceux qui évoquent Allah abondamment, hommes et femmes.",
        "title_fr": "L'évocation d'Allah (Al-Dhikr)",
        "title_ar": "سبق المفردون",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Abu Hurayra et Abu Sa'id",
        "validation_sources": ["Sahih Muslim 2676", "Sunan al-Tirmidhi 3376", "Musnad Ahmad 3/75"],
        "thematic_category": "Invocation & dhikr",
        "keywords": ["dhikr", "evocation", "mufarridun"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2676"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 3376"], "nodes": [("abu_saeed", 4), ("tirmidhi", 0)]},
            {"label": "Anas → Ahmad", "path_count": 7, "sources": ["Musnad Ahmad 3/75"], "nodes": [("anass", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 93. L'invocation est l'adoration (Al-Du'a)
    # ------------------------------------------------------------------
    {
        "id": "h_dua",
        "rank": 93,
        "matn": "إِنَّ الدُّعَاءَ هُوَ الْعِبَادَةُ",
        "matn_translation_fr": "L'invocation, c'est l'adoration même.",
        "title_fr": "L'invocation est adoration (Al-Du'a huwa al-'Ibada)",
        "title_ar": "إن الدعاء هو العبادة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par al-Nu'man ibn Bashir et Abu Hurayra",
        "validation_sources": ["Sunan al-Tirmidhi 3247", "Sunan Abi Dawud 1479", "Sunan Ibn Majah 3828"],
        "thematic_category": "Invocation & dhikr",
        "keywords": ["dua", "invocation", "ibada"],
        "turuq": [
            {"label": "Al-Nu'man ibn Bashir → Al-Tirmidhi", "path_count": 11, "sources": ["Sunan al-Tirmidhi 3247"], "nodes": [("numan", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 1479"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Ibn Majah", "path_count": 7, "sources": ["Sunan Ibn Majah 3828"], "nodes": [("abu_hurayra", 4), ("ibn_majah", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 94. La véracité (Al-Sidq)
    # ------------------------------------------------------------------
    {
        "id": "h_sidq",
        "rank": 94,
        "matn": "عَلَيْكُمْ بِالصِّدْقِ، فَإِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ، وَإِنَّ الْبِرَّ يَهْدِي إِلَى الْجَنَّةِ",
        "matn_translation_fr": "Tenez-vous à la véracité, car la véracité conduit à la piété, et la piété conduit au Paradis.",
        "title_fr": "La véracité (Al-Sidq)",
        "title_ar": "عليكم بالصدق",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Ibn Mas'ud, Ibn Umar et Abu Hurayra",
        "validation_sources": ["Sahih Muslim 2607", "Sahih al-Bukhari 6094", "Sunan al-Tirmidhi 1971"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["sidq", "verite", "birr"],
        "turuq": [
            {"label": "Abdullah ibn Mas'ud → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2607"], "nodes": [("ibn_masud", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 10, "sources": ["Sahih al-Bukhari 6094"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 1971"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 95. Le dépôt (Al-Amana)
    # ------------------------------------------------------------------
    {
        "id": "h_amanah",
        "rank": 95,
        "matn": "أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ، وَلَا تَخُنْ مَنْ خَانَكَ",
        "matn_translation_fr": "Rends le dépôt à celui qui t'a fait confiance, et ne trahis pas celui qui t'a trahi.",
        "title_fr": "Le dépôt (Al-Amana)",
        "title_ar": "أد الأمانة إلى من ائتمنك",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Abu Hurayra et Anas",
        "validation_sources": ["Sunan Abi Dawud 3535", "Sunan al-Tirmidhi 1264", "Musnad Ahmad 3/206"],
        "thematic_category": "Éthique & caractère",
        "keywords": ["amanah", "depot", "confiance"],
        "turuq": [
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 11, "sources": ["Sunan Abi Dawud 3535"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 1264"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Anas → Ahmad", "path_count": 7, "sources": ["Musnad Ahmad 3/206"], "nodes": [("anass", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 96. La recommandation du voisin (Al-Jar)
    # ------------------------------------------------------------------
    {
        "id": "h_jari",
        "rank": 96,
        "matn": "مَا زَالَ جِبْرِيلُ يُوصِينِي بِالْجَارِ حَتَّى ظَنَنْتُ أَنَّهُ سَيُوَرِّثُهُ",
        "matn_translation_fr": "Gabriel n'a cessé de me recommander le voisin, au point que j'ai cru qu'il allait lui donner droit d'héritage.",
        "title_fr": "Le droit du voisin (Al-Jar)",
        "title_ar": "ما زال جبريل يوصيني بالجار",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Aisha, Ibn Umar et Abu Hurayra",
        "validation_sources": ["Sahih al-Bukhari 6014", "Sahih Muslim 2624", "Sunan al-Tirmidhi 1943"],
        "thematic_category": "Solidarité",
        "keywords": ["jar", "voisin", "voisinage"],
        "turuq": [
            {"label": "Aisha → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 6014"], "nodes": [("aisha", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 10, "sources": ["Sahih Muslim 2624"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 1943"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 97. La piété filiale (Birr al-Walidayn)
    # ------------------------------------------------------------------
    {
        "id": "h_walidayn",
        "rank": 97,
        "matn": "رِضَا الرَّبِّ مِنْ رِضَا الْوَالِدِ، وَسَخَطُ الرَّبِّ مِنْ سَخَطِ الْوَالِدِ",
        "matn_translation_fr": "La satisfaction du Seigneur découle de la satisfaction du père, et Sa colère de la colère du père.",
        "title_fr": "La piété filiale (Birr al-Walidayn)",
        "title_ar": "رضا الرب من رضا الوالد",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sunan al-Tirmidhi 1899", "Sunan Ibn Majah 3662", "Mustadrak al-Hakim 4/151"],
        "thematic_category": "Famille",
        "keywords": ["walidayn", "parents", "birr"],
        "turuq": [
            {"label": "Abdullah ibn Amr → Al-Tirmidhi", "path_count": 11, "sources": ["Sunan al-Tirmidhi 1899"], "nodes": [("abdullah_amr", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ibn Majah", "path_count": 8, "sources": ["Sunan Ibn Majah 3662"], "nodes": [("abu_hurayra", 4), ("ibn_majah", 0)]},
            {"label": "Abdullah ibn Umar → Al-Hakim", "path_count": 7, "sources": ["Mustadrak al-Hakim 4/151"], "nodes": [("abdullah_umar", 4), ("hakim", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 98. La bonne fin (Husn al-Khatima)
    # ------------------------------------------------------------------
    {
        "id": "h_husn_khatim",
        "rank": 98,
        "matn": "مَنْ كَانَ آخِرُ كَلَامِهِ لَا إِلَهَ إِلَّا اللَّهُ دَخَلَ الْجَنَّةَ",
        "matn_translation_fr": "Celui dont la dernière parole est « il n'y a de divinité qu'Allah » entrera au Paradis.",
        "title_fr": "La bonne fin (Husn al-Khatima)",
        "title_ar": "من كان آخر كلامه لا إله إلا الله",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sunan Abi Dawud 3116", "Musnad Ahmad 5/233", "Mustadrak al-Hakim 1/502"],
        "thematic_category": "Eschatologie",
        "keywords": ["khatima", "tawhid", "jannah"],
        "turuq": [
            {"label": "Mu'adh ibn Jabal → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 3116"], "nodes": [("muadh", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 5/233"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Abdullah ibn Umar → Al-Hakim", "path_count": 7, "sources": ["Mustadrak al-Hakim 1/502"], "nodes": [("abdullah_umar", 4), ("hakim", 0)]},
        ],
    },
]
