# -*- coding: utf-8 -*-
"""Vague d'extension n.1 — hadiths mutawatir majeurs (rangs 51-70).

Mêmes conventions que ``hadiths_data`` : ``nodes`` = tuples (rawi_id, level),
4 = Compagnon, 3 = Imam/Tabi'i majeur, 2 = Tabi'i, 1 = intermédiaire,
0 = compilateur. Inscription d'après les inventaires classiques
(al-Azhar al-Mutanathira al-Suyuti, Nazm al-Mutanathir al-Kattani).
"""

HADITHS_MW1 = [
    # ------------------------------------------------------------------
    # 51. L'homme sera avec ceux qu'il aime
    # ------------------------------------------------------------------
    {
        "id": "h_mar",
        "rank": 51,
        "matn": "الْمَرْءُ مَعَ مَنْ أَحَبَّ",
        "matn_translation_fr": "L'homme sera avec celui qu'il aime.",
        "title_fr": "L'homme est avec celui qu'il aime (Al-Mar' ma'a man ahabb)",
        "title_ar": "المرء مع من أحب",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sahih al-Bukhari 6168", "Sahih Muslim 2640", "Sunan al-Tirmidhi 2634"],
        "thematic_category": "Foi & fraternité",
        "keywords": ["hubb", "amour", "akhira"],
        "turuq": [
            {"label": "Anas → Al-Bukhari", "path_count": 18, "sources": ["Sahih al-Bukhari 6168"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 15, "sources": ["Sahih Muslim 2640"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 10, "sources": ["Musnad Ahmad 2/468"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 52. Répandez le salut pour vous aimer
    # ------------------------------------------------------------------
    {
        "id": "h_tahabb",
        "rank": 52,
        "matn": "لَا تَدْخُلُونَ الْجَنَّةَ حَتَّى تُؤْمِنُوا، وَلَا تُؤْمِنُونَ حَتَّى تَحَابُّوا، أَفَلَا أَدُلُّكُمْ عَلَى مَا يُحَبِّبُكُمْ بَيْنَكُمْ؟ أَفْشُوا السَّلَامَ بَيْنَكُمْ",
        "matn_translation_fr": "Vous n'entrerez pas au Paradis tant que vous ne croirez pas, et vous ne croirez pas tant que vous ne vous aimerez pas. Vous indiquerai-je une chose qui, si vous la faites, vous fera vous aimer ? Répandez le salut entre vous.",
        "title_fr": "Répandez le salut (Afshu al-Salam)",
        "title_ar": "لا تدخلون الجنة حتى تؤمنوا وتتحابوا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Hurayra et Abu Musa",
        "validation_sources": ["Sahih Muslim 54", "Sunan al-Tirmidhi 2685", "Sunan Abi Dawud 5193"],
        "thematic_category": "Foi & fraternité",
        "keywords": ["salam", "paix", "hubb"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 16, "sources": ["Sahih Muslim 54"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 2685"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Abu Sa'id → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 5193"], "nodes": [("abu_saeed", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 53. J'ai reçu l'ordre de combattre les gens jusqu'à...
    # ------------------------------------------------------------------
    {
        "id": "h_umirtu",
        "rank": 53,
        "matn": "أُمِرْتُ أَنْ أُقَاتِلَ النَّاسَ حَتَّى يَشْهَدُوا أَنْ لَا إِلَهَ إِلَّا اللَّهُ، وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ، وَيُقِيمُوا الصَّلَاةَ، وَيُؤْتُوا الزَّكَاةَ، فَإِذَا فَعَلُوا ذَلِكَ عَصَمُوا مِنِّي دِمَاءَهُمْ وَأَمْوَالَهُمْ إِلَّا بِحَقِّ الْإِسْلَامِ، وَحِسَابُهُمْ عَلَى اللَّهِ",
        "matn_translation_fr": "J'ai reçu l'ordre de combattre les gens jusqu'à ce qu'ils attestent qu'il n'y a de divinité qu'Allah et que Muhammad est Son Messager, accomplissent la prière et s'acquittent de la zakat. Lorsqu'ils font cela, ils préservent de moi leurs vies et leurs biens, sauf en raison d'un droit de l'Islam, et leur compte revient à Allah.",
        "title_fr": "Le témoignage de foi (Umirtu an uqatil)",
        "title_ar": "أمرت أن أقاتل الناس حتى يشهدوا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 25", "Sahih Muslim 21", "Sunan al-Nasa'i 3974"],
        "thematic_category": "Dogme (Tawhid)",
        "keywords": ["tawhid", "shahada", "islam"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 25"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 16, "sources": ["Sahih Muslim 21"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Nasa'i", "path_count": 10, "sources": ["Sunan al-Nasa'i 3974"], "nodes": [("anass", 4), ("nasai", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 54. Honore son hôte
    # ------------------------------------------------------------------
    {
        "id": "h_dayf",
        "rank": 54,
        "matn": "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الْآخِرِ فَلْيُكْرِمْ ضَيْفَهُ",
        "matn_translation_fr": "Que celui qui croit en Allah et au Jour dernier honore son hôte.",
        "title_fr": "Honorer son hôte (Ikram al-Dayf)",
        "title_ar": "من كان يؤمن بالله واليوم الآخر فليكرم ضيفه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abu Shuraih, Abu Hurayra et d'autres",
        "validation_sources": ["Sahih al-Bukhari 6018", "Sahih Muslim 47", "Musnad Ahmad 4/31"],
        "thematic_category": "Hospitalité",
        "keywords": ["dayf", "hote", "ikram"],
        "turuq": [
            {"label": "Abu Shuraih → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 6018"], "nodes": [("abu_shurayh", 4), ("bukhari", 0)]},
            {"label": "Abu Shuraih → Muslim", "path_count": 10, "sources": ["Sahih Muslim 47"], "nodes": [("abu_shurayh", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 4/31"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 55. Qu'il dise du bien ou se taise
    # ------------------------------------------------------------------
    {
        "id": "h_khayr_samt",
        "rank": 55,
        "matn": "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ",
        "matn_translation_fr": "Que celui qui croit en Allah et au Jour dernier dise du bien ou se taise.",
        "title_fr": "Dire du bien ou se taire (Khayran aw liyasmut)",
        "title_ar": "فليقل خيرا أو ليصمت",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — une des règles de la parole",
        "validation_sources": ["Sahih al-Bukhari 6136", "Sahih Muslim 47", "Musnad Ahmad 4/31"],
        "thematic_category": "Éthique de la parole",
        "keywords": ["samt", "parole", "silence"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 14, "sources": ["Sahih al-Bukhari 6136"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 47"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Shuraih → Ahmad", "path_count": 6, "sources": ["Musnad Ahmad 4/31"], "nodes": [("abu_shurayh", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 56. Le jeûne est une protection
    # ------------------------------------------------------------------
    {
        "id": "h_siyam_2",
        "rank": 56,
        "matn": "الصِّيَامُ جُنَّةٌ",
        "matn_translation_fr": "Le jeûne est une protection (pour le croyant).",
        "title_fr": "Le jeûne est une protection (Al-Siyam Junna)",
        "title_ar": "الصيام جنة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Abu Hurayra et Abu Qatada",
        "validation_sources": ["Sahih al-Bukhari 1894", "Sahih Muslim 1151", "Sunan al-Tirmidhi 764"],
        "thematic_category": "Jeûne",
        "keywords": ["siyam", "jeune", "junna"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 18, "sources": ["Sahih al-Bukhari 1894"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 15, "sources": ["Sahih Muslim 1151"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 764"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 57. Le mauvais œil est réel
    # ------------------------------------------------------------------
    {
        "id": "h_ayn",
        "rank": 57,
        "matn": "الْعَيْنُ حَقٌّ",
        "matn_translation_fr": "Le mauvais œil est réel.",
        "title_fr": "Le mauvais œil existe (Al-'Ayn Haqq)",
        "title_ar": "العين حق",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 5740", "Sahih Muslim 2187", "Sunan al-Tirmidhi 2060"],
        "thematic_category": "Croyances & remèdes",
        "keywords": ["ayn", "mauvais oeil", "destination"],
        "turuq": [
            {"label": "Ibn Abbas → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 5740"], "nodes": [("ibn_abbas", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 10, "sources": ["Sahih Muslim 2187"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Jabir → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 2060"], "nodes": [("jabir", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 58. Celui qui facilite la besoin de son frère
    # ------------------------------------------------------------------
    {
        "id": "h_kafala",
        "rank": 58,
        "matn": "مَنْ كَانَ فِي حَاجَةِ أَخِيهِ كَانَ اللَّهُ فِي حَاجَتِهِ",
        "matn_translation_fr": "Celui qui aide son frère dans son besoin, Allah l'aide dans le sien.",
        "title_fr": "Le besoin du frère (Hajat al-Akh)",
        "title_ar": "من كان في حاجة أخيه",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — interdépendance et entraide",
        "validation_sources": ["Sahih al-Bukhari 2442", "Sahih Muslim 2580", "Sunan al-Tirmidhi 1930"],
        "thematic_category": "Solidarité",
        "keywords": ["hajat", "entraide", "akh"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 14, "sources": ["Sahih al-Bukhari 2442"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2580"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Jabir → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 1930"], "nodes": [("jabir", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 59. Le musulman est le frère du musulman
    # ------------------------------------------------------------------
    {
        "id": "h_akh_muslim",
        "rank": 59,
        "matn": "الْمُسْلِمُ أَخُو الْمُسْلِمِ لَا يَظْلِمُهُ وَلَا يَخْذُلُهُ وَلَا يَحْقِرُهُ",
        "matn_translation_fr": "Le musulman est le frère du musulman : il ne l'opprime pas, ne l'abandonne pas et ne le méprise pas.",
        "title_fr": "Fraternité musulmane (Al-Akh al-Muslim)",
        "title_ar": "المسلم أخو المسلم",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — droits du frère musulman",
        "validation_sources": ["Sahih al-Bukhari 2442", "Sahih Muslim 2564", "Sunan Abi Dawud 4880"],
        "thematic_category": "Solidarité",
        "keywords": ["fraternite", "droit du musulman", "zulm"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 14, "sources": ["Sahih al-Bukhari 2442"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 12, "sources": ["Sahih Muslim 2564"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Amr → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 4880"], "nodes": [("abdullah_amr", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 60. Nul préjudice, nul dommage réciproque
    # ------------------------------------------------------------------
    {
        "id": "h_darar",
        "rank": 60,
        "matn": "لَا ضَرَرَ وَلَا ضِرَارَ",
        "matn_translation_fr": "Nul préjudice, et nul dommage réciproque.",
        "title_fr": "Nul préjudice, nul dommage (La Darar wa la Dirar)",
        "title_ar": "لا ضرر ولا ضرار",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — règle juridique universelle",
        "validation_sources": ["Sunan Ibn Majah 2341", "Al-Muwatta' (Malik)", "Musnad Ahmad"],
        "thematic_category": "Jurisprudence (Fiqh)",
        "keywords": ["darar", "dommage", "fiqh"],
        "turuq": [
            {"label": "Abu Sa'id → Ibn Majah", "path_count": 12, "sources": ["Sunan Ibn Majah 2341"], "nodes": [("abu_saeed", 4), ("ibn_majah", 0)]},
            {"label": "Abu Sa'id → Malik", "path_count": 8, "sources": ["Al-Muwatta' (Malik)"], "nodes": [("abu_saeed", 4), ("malik", 0)]},
            {"label": "Abu Lubaba → Ahmad", "path_count": 6, "sources": ["Musnad Ahmad"], "nodes": [("abu_lubaba", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 61. Allah a prescrit l'excellence en toute chose
    # ------------------------------------------------------------------
    {
        "id": "h_ihsan",
        "rank": 61,
        "matn": "إِنَّ اللَّهَ كَتَبَ الْإِحْسَانَ عَلَى كُلِّ شَيْءٍ، فَإِذَا قَتَلْتُمْ فَأَحْسِنُوا الْقِتْلَةَ، وَإِذَا ذَبَحْتُمْ فَأَحْسِنُوا الذِّبْحَةَ، وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَهُ وَلْيُرِحْ ذَبِيحَتَهُ",
        "matn_translation_fr": "Allah a prescrit l'excellence en toute chose : si vous tuez, tuez avec excellence ; si vous égorgez, égorgez avec excellence, que l'un de vous aiguise sa lame et épargne à sa bête la souffrance.",
        "title_fr": "L'excellence en toute chose (Al-Ihsan)",
        "title_ar": "إن الله كتب الإحسان على كل شيء",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Shaddad ibn Aws et d'autres",
        "validation_sources": ["Sahih Muslim 1955", "Sunan Abi Dawud 2815", "Sunan al-Tirmidhi 1409"],
        "thematic_category": "Miséricorde envers les créatures",
        "keywords": ["ihsan", "excellence", "dhabiha"],
        "turuq": [
            {"label": "Shaddad → Muslim", "path_count": 15, "sources": ["Sahih Muslim 1955"], "nodes": [("shaddad", 4), ("muslim", 0)]},
            {"label": "Shaddad → Abu Dawud", "path_count": 10, "sources": ["Sunan Abi Dawud 2815"], "nodes": [("shaddad", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 8, "sources": ["Sunan al-Tirmidhi 1409"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 62. Ceux qui font miséricorde
    # ------------------------------------------------------------------
    {
        "id": "h_rahimun",
        "rank": 62,
        "matn": "الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمَنُ، ارْحَمُوا أَهْلَ الْأَرْضِ يَرْحَمْكُمْ أَهْلُ السَّمَاءِ",
        "matn_translation_fr": "Ceux qui font miséricorde recevront la miséricorde du Tout-Miséricordieux. Faites miséricorde à ceux qui sont sur terre, et Celui qui est au Ciel aura miséricorde de vous.",
        "title_fr": "Ceux qui font miséricorde (Al-Rahimun)",
        "title_ar": "الراحمون يرحمهم الرحمن",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — extrême importance de la miséricorde",
        "validation_sources": ["Sunan al-Tirmidhi 1924", "Sunan Abi Dawud 4941", "Mustadrak al-Hakim 7351"],
        "thematic_category": "Miséricorde",
        "keywords": ["rahma", "miséricorde", "ahl al-ard"],
        "turuq": [
            {"label": "Abdullah ibn Amr → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 1924"], "nodes": [("abdullah_amr", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 10, "sources": ["Sunan Abi Dawud 4941"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abdullah ibn Umar → Al-Hakim", "path_count": 7, "sources": ["Mustadrak al-Hakim 7351"], "nodes": [("abdullah_umar", 4), ("hakim", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 63. Le cure-dent (siwak) purifie la bouche
    # ------------------------------------------------------------------
    {
        "id": "h_siwak",
        "rank": 63,
        "matn": "السِّوَاكُ مَطْهَرَةٌ لِلْفَمِ مَرْضَاةٌ لِلرَّبِّ",
        "matn_translation_fr": "Le siwak purifie la bouche et est une cause d'agrément du Seigneur.",
        "title_fr": "Le siwak (Al-Siwak)",
        "title_ar": "السواك مطهرة للفم مرضاة للرب",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par Aisha et Abu Hurayra",
        "validation_sources": ["Sunan al-Nasa'i 5", "Sahih Ibn Khuzayma 141", "Sunan Ibn Majah 287"],
        "thematic_category": "Purification",
        "keywords": ["siwak", "hygiene", "tahara"],
        "turuq": [
            {"label": "Aisha → Al-Nasa'i", "path_count": 10, "sources": ["Sunan al-Nasa'i 5"], "nodes": [("aisha", 4), ("nasai", 0)]},
            {"label": "Aisha → Ibn Majah", "path_count": 8, "sources": ["Sunan Ibn Majah 287"], "nodes": [("aisha", 4), ("ibn_majah", 0)]},
            {"label": "Abu Hurayra → Ibn Khuzayma", "path_count": 7, "sources": ["Sahih Ibn Khuzayma 141"], "nodes": [("abu_hurayra", 4), ("ibn_khuzayma", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 64. Le meilleur de ma communauté est ma génération
    # ------------------------------------------------------------------
    {
        "id": "h_qarn",
        "rank": 64,
        "matn": "خَيْرُ أُمَّتِي قَرْنِي، ثُمَّ الَّذِينَ يَلُونَهُمْ، ثُمَّ الَّذِينَ يَلُونَهُمْ",
        "matn_translation_fr": "La meilleure génération de ma communauté est la mienne, puis celle qui la suit, puis celle qui suit celle-ci.",
        "title_fr": "La meilleure génération (Khayr Ummati Qarni)",
        "title_ar": "خير أمتي قرني",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 2650", "Sahih Muslim 2533", "Sunan al-Tirmidhi 3858"],
        "thematic_category": "Éloge des premières générations",
        "keywords": ["qarn", "generation", "salaf"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 18, "sources": ["Sahih al-Bukhari 2650"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Imran → Muslim", "path_count": 14, "sources": ["Sahih Muslim 2533"], "nodes": [("imran", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 10, "sources": ["Sunan al-Tirmidhi 3858"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 65. Priez comme vous m'avez vu prier
    # ------------------------------------------------------------------
    {
        "id": "h_salatu_kama",
        "rank": 65,
        "matn": "صَلُّوا كَمَا رَأَيْتُمُونِي أُصَلِّي",
        "matn_translation_fr": "Priez comme vous m'avez vu prier.",
        "title_fr": "La prière du Prophète (Sallu kama ra'aytumuni)",
        "title_ar": "صلوا كما رأيتموني أصلي",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — source de la description de la prière",
        "validation_sources": ["Sahih al-Bukhari", "Sunan Abi Dawud 403", "Sunan al-Tirmidhi 205"],
        "thematic_category": "Prière",
        "keywords": ["salat", "priere", "imitation du Prophete"],
        "turuq": [
            {"label": "Malik ibn al-Huwayrith → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari"], "nodes": [("malik_hu", 4), ("bukhari", 0)]},
            {"label": "Malik ibn al-Huwayrith → Abu Dawud", "path_count": 9, "sources": ["Sunan Abi Dawud 403"], "nodes": [("malik_hu", 4), ("abu_dawud", 0)]},
            {"label": "Malik ibn al-Huwayrith → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 205"], "nodes": [("malik_hu", 4), ("tirmidhi", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 66. Mort de l'ignorance (bai'a)
    # ------------------------------------------------------------------
    {
        "id": "h_mawt_jahil",
        "rank": 66,
        "matn": "مَنْ مَاتَ وَلَيْسَ فِي عُنُقِهِ بَيْعَةٌ مَاتَ مِيتَةً جَاهِلِيَّةً",
        "matn_translation_fr": "Quiconque meurt sans avoir fait acte d'allégeance meurt de la mort de l'ignorance.",
        "title_fr": "L'allégeance (Bay'a)",
        "title_ar": "من مات وليس في عنقه بيعة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par Abdullah ibn Umar et Mu'awiya",
        "validation_sources": ["Sahih Muslim 1851", "Sunan Abi Dawud 4756", "Musnad Ahmad"],
        "thematic_category": "Politique & communauté",
        "keywords": ["bay'a", "allegeance", "jama'a"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 12, "sources": ["Sahih Muslim 1851"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Mu'awiya → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 4756"], "nodes": [("muawiya", 4), ("abu_dawud", 0)]},
            {"label": "Abdullah ibn Amr → Ahmad", "path_count": 7, "sources": ["Musnad Ahmad 2/159"], "nodes": [("abdullah_amr", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 67. Entre l'homme et le polythéisme, l'abandon de la prière
    # ------------------------------------------------------------------
    {
        "id": "h_bayna",
        "rank": 67,
        "matn": "بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالْكُفْرِ تَرْكُ الصَّلَاةِ",
        "matn_translation_fr": "Entre l'homme et le polythéisme et la mécréance, il y a l'abandon de la prière.",
        "title_fr": "L'abandon de la prière (Tark al-Salat)",
        "title_ar": "بين الرجل وبين الشرك والكفر ترك الصلاة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sahih Muslim 82", "Sunan Ibn Majah 1078", "Musnad Ahmad"],
        "thematic_category": "Prière",
        "keywords": ["salat", "kufr", "shirk"],
        "turuq": [
            {"label": "Jabir → Muslim", "path_count": 14, "sources": ["Sahih Muslim 82"], "nodes": [("jabir", 4), ("muslim", 0)]},
            {"label": "Anas → Ibn Majah", "path_count": 9, "sources": ["Sunan Ibn Majah 1078"], "nodes": [("anass", 4), ("ibn_majah", 0)]},
            {"label": "Abdullah ibn Amr → Ahmad", "path_count": 8, "sources": ["Musnad Ahmad 2/197"], "nodes": [("abdullah_amr", 4), ("ahmad", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 68. Ne voyagez que vers trois mosquées
    # ------------------------------------------------------------------
    {
        "id": "h_rihal",
        "rank": 68,
        "matn": "لَا تُشَدُّ الرِّحَالُ إِلَّا إِلَى ثَلَاثَةِ مَسَاجِدَ: الْمَسْجِدِ الْحَرَامِ، وَمَسْجِدِ الرَّسُولِ، وَالْمَسْجِدِ الْأَقْصَى",
        "matn_translation_fr": "On ne se déplace avec motivation que vers trois mosquées : la Mosquée sacrée, la mosquée du Messager et la mosquée al-Aqsa.",
        "title_fr": "Les trois mosquées (La tushadd al-Rihal)",
        "title_ar": "لا تشد الرحال إلا إلى ثلاثة مساجد",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs Compagnons",
        "validation_sources": ["Sahih al-Bukhari 1189", "Sahih Muslim 1397", "Sunan Abi Dawud 2028"],
        "thematic_category": "Lieux saints",
        "keywords": ["masjids", "rihal", "voyage"],
        "turuq": [
            {"label": "Abu Sa'id → Al-Bukhari", "path_count": 12, "sources": ["Sahih al-Bukhari 1189"], "nodes": [("abu_saeed", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 10, "sources": ["Sahih Muslim 1397"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Jabir → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 2028"], "nodes": [("jabir", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 69. La voie vers la science mène au Paradis
    # ------------------------------------------------------------------
    {
        "id": "h_ilm_tariq",
        "rank": 69,
        "matn": "مَنْ سَلَكَ طَرِيقًا يَلْتَمِسُ فِيهِ عِلْمًا سَهَّلَ اللَّهُ لَهُ بِهِ طَرِيقًا إِلَى الْجَنَّةِ",
        "matn_translation_fr": "Quiconque emprunte un chemin en quête de science, Allah lui facilite par cela un chemin vers le Paradis.",
        "title_fr": "La quête de la science (Salak tariqan)",
        "title_ar": "من سلك طريقا يلتمس فيه علما",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — mérites de la quête du savoir",
        "validation_sources": ["Sahih Muslim 2699", "Sunan Abi Dawud 3641", "Sunan al-Tirmidhi 2646"],
        "thematic_category": "Science",
        "keywords": ["ilm", "science", "janna"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 14, "sources": ["Sahih Muslim 2699"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 9, "sources": ["Sunan al-Tirmidhi 2646"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Abu Ayyub → Abu Dawud", "path_count": 7, "sources": ["Sunan Abi Dawud 3641"], "nodes": [("abu_ayyub", 4), ("abu_dawud", 0)]},
        ],
    },

    # ------------------------------------------------------------------
    # 70. La sérénité descend sur les assembleurs du Coran
    # ------------------------------------------------------------------
    {
        "id": "h_dhikr_jama",
        "rank": 70,
        "matn": "وَمَا اجْتَمَعَ قَوْمٌ فِي بَيْتٍ مِنْ بُيُوتِ اللَّهِ يَتْلُونَ كِتَابَ اللَّهِ وَيَتَدَارَسُونَهُ بَيْنَهُمْ إِلَّا نَزَلَتْ عَلَيْهِمُ السَّكِينَةُ، وَغَشِيَتْهُمُ الرَّحْمَةُ، وَحَفَّتْهُمُ الْمَلَائِكَةُ، وَذَكَرَهُمُ اللَّهُ فِيمَنْ عِنْدَهُ",
        "matn_translation_fr": "Aucune assemblée ne se réunit dans une maison d'Allah, récitant le Livre d'Allah et l'étudiant entre eux, sans que la sérénité ne descende sur eux, que la miséricorde ne les enveloppe, que les anges ne les entourent et qu'Allah ne les mentionne auprès de ceux qui sont auprès de Lui.",
        "title_fr": "La sérénité des assembleurs du Coran (Al-Sakina)",
        "title_ar": "ما اجتمع قوم في بيت من بيوت الله...",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — mérites des cercles de savoir",
        "validation_sources": ["Sahih Muslim 2699", "Sunan Abi Dawud 1455", "Sunan al-Tirmidhi 2945"],
        "thematic_category": "Science & invocation",
        "keywords": ["dhikr", "sakina", "cercles de savoir"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 14, "sources": ["Sahih Muslim 2699"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Abu Dawud", "path_count": 8, "sources": ["Sunan Abi Dawud 1455"], "nodes": [("abu_saeed", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 7, "sources": ["Sunan al-Tirmidhi 2945"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },
]