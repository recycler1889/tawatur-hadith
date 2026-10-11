# -*- coding: utf-8 -*-
"""Catalogue des hadiths mutawatir (sunnites & chiites), classés par rang.

Chaque hadith porte :
- ``rank`` : priorité d'authenticité / unanimité (1 = le plus incontesté) ;
- ``turuq`` : liste des voies, chacune avec sa chaîne complète ``nodes``
  (Compagnon → Tabi'i/Imam → compilateur), son ``path_count`` et ses sources.

Le format ``nodes`` = liste de tuples (rawi_id, level), où 4 = Compagnon,
3 = Imam/Tabi'i majeur, 2 = Tabi'i, 1 = intermédiaire, 0 = compilateur.
Narration : le premier nœud (Compagnon) est la racine, le dernier le compilateur.

Sources d'inspiration : al-Suyuti (*al-Azhar al-Mutanathira*), al-Kattani
(*Nazm al-Mutanathir min al-Hadith al-Mutawatir*), et recueils chiites
(al-Kafi, Man la yahduruhu al-Faqih, etc.).
"""

HADITHS = [
    # ==================================================================
    # 1. Hadith al-Ghadir — le plus hautement transmis (lafzi)
    # ==================================================================
    {
        "id": "h_ghadir",
        "rank": 1,
        "matn": "مَنْ كُنْتُ مَوْلَاهُ فَهَذَا عَلِيٌّ مَوْلَاهُ، اللَّهُمَّ وَالِ مَنْ وَالَاهُ وَعَادِ مَنْ عَادَاهُ",
        "matn_translation_fr": "Celui dont je suis le maître, Ali est aussi son maître. Ô Allah, soutiens qui le soutient et oppose-toi à qui s'oppose à lui.",
        "title_fr": "Hadith al-Ghadir (Ghadir Khumm)",
        "title_ar": "حديث الغدير",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — plus de 100 voies rapportées par des Compagnons distincts",
        "validation_sources": ["Musnad Ahmad 4/281", "Sunan al-Tirmidhi 3713", "Mustadrak al-Hakim 3/109", "Al-Kafi 1/295"],
        "thematic_category": "Wilaya & succession",
        "keywords": ["ghadir", "wilaya", "ali"],
        "turuq": [
            {"label": "Ali → Ibn Abbas → Ahmad ibn Hanbal", "path_count": 110, "sources": ["Musnad Ahmad 4/281"], "nodes": [("ali", 4), ("ibn_abbas", 3), ("ahmad", 0)]},
            {"label": "Ali → Hudhayfa → Al-Tirmidhi", "path_count": 90, "sources": ["Sunan al-Tirmidhi 3713"], "nodes": [("ali", 4), ("hudhayfa", 3), ("tirmidhi", 0)]},
            {"label": "Ali → Zayd ibn Arqam → Al-Hakim", "path_count": 100, "sources": ["Mustadrak al-Hakim 3/109"], "nodes": [("ali", 4), ("zayd_arqam", 3), ("hakim", 0)]},
            {"label": "Zayd ibn Arqam → Muslim", "path_count": 40, "sources": ["Sahih Muslim 2408"], "nodes": [("zayd_arqam", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id al-Khudri → Ahmad", "path_count": 60, "sources": ["Musnad Ahmad 3/17"], "nodes": [("abu_saeed", 4), ("ahmad", 0)]},
            {"label": "Burayda → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 4348"], "nodes": [("burayda", 4), ("bukhari", 0)]},
            {"label": "Jabir → Al-Tirmidhi", "path_count": 30, "sources": ["Sunan al-Tirmidhi 3713"], "nodes": [("jabir", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 25, "sources": ["Musnad Ahmad 2/456"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 60, "sources": ["Al-Kafi 1/295"], "nodes": [("ali", 4), ("kulayni", 0)]},
            {"label": "Ali → Al-Saduq", "path_count": 45, "sources": ["Al-Amali 121"], "nodes": [("ali", 4), ("saduq", 0)]},
            {"label": "Ali → Al-Tusi", "path_count": 30, "sources": ["Tahdhib al-Ahkam"], "nodes": [("ali", 4), ("tusi", 0)]},
        ],
    },

    # ==================================================================
    # 2. Man kadhaba 'alayya
    # ==================================================================
    {
        "id": "h_kadhib",
        "rank": 2,
        "matn": "مَنْ كَذَبَ عَلَيَّ مُتَعَمِّدًا فَلْيَتَبَوَّأْ مَقْعَدَهُ مِنَ النَّارِ",
        "matn_translation_fr": "Quiconque ment délibérément à mon sujet, qu'il prépare sa place en Enfer.",
        "title_fr": "Quiconque ment à mon sujet (Man kadhaba 'alayya)",
        "title_ar": "من كذب علي متعمدا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plus de soixante-dix Compagnons",
        "validation_sources": ["Sahih al-Bukhari 110", "Sahih Muslim 3", "Musnad Ahmad 2/159"],
        "thematic_category": "Intégrité de la transmission",
        "keywords": ["kadhib", "mensonge", "transmission"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 60, "sources": ["Sahih al-Bukhari 110"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 55, "sources": ["Sahih Muslim 3"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Jabir → Ahmad", "path_count": 70, "sources": ["Musnad Ahmad 2/159"], "nodes": [("jabir", 4), ("ahmad", 0)]},
            {"label": "Ibn Mas'ud → Al-Darimi", "path_count": 40, "sources": ["Sunan al-Darimi 232"], "nodes": [("ibn_masud", 4), ("darimi", 0)]},
            {"label": "Zayd ibn Arqam → Al-Tirmidhi", "path_count": 30, "sources": ["Sunan al-Tirmidhi 2659"], "nodes": [("zayd_arqam", 4), ("tirmidhi", 0)]},
            {"label": "Abdullah ibn Amr → Al-Tabarani", "path_count": 25, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("abdullah_amr", 4), ("tabarani", 0)]},
        ],
    },

    # ==================================================================
    # 3. Hadith du Bassin (Al-Hawd)
    # ==================================================================
    {
        "id": "h_hawd",
        "rank": 3,
        "matn": "إِنَّ حَوْضِي أَبْعَدُ مِنْ أَيْلَةَ إِلَى عَدَنٍ، لَهُ مَزَابِيبُ مِنْ ذَهَبٍ وَفِضَّةٍ، وَإِنَّ آنِيَتَهُ أَكْثَرُ مِنْ عَدَدِ النُّجُومِ",
        "matn_translation_fr": "Mon bassin s'étend d'Ayla à 'Adan. Il a des canaux d'or et d'argent, et ses récipients sont plus nombreux que les étoiles.",
        "title_fr": "Hadith du Bassin (Al-Hawd)",
        "title_ar": "حديث الحوض",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par un très grand nombre de Compagnons",
        "validation_sources": ["Sahih al-Bukhari 6579", "Sahih Muslim 2292", "Sunan al-Tirmidhi 2443"],
        "thematic_category": "Eschatologie",
        "keywords": ["hawd", "bassin", "kawthar"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 50, "sources": ["Sahih al-Bukhari 6579"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Anas ibn Malik → Muslim", "path_count": 60, "sources": ["Sahih Muslim 2292"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 7049"], "nodes": [("ibn_abbas", 4), ("bukhari", 0)]},
            {"label": "Jabir → Muslim", "path_count": 25, "sources": ["Sahih Muslim 2299"], "nodes": [("jabir", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id al-Khudri → Al-Tirmidhi", "path_count": 20, "sources": ["Sunan al-Tirmidhi 2443"], "nodes": [("abu_saeed", 4), ("tirmidhi", 0)]},
            {"label": "Hudhayfa → Al-Tirmidhi", "path_count": 20, "sources": ["Sunan al-Tirmidhi 2444"], "nodes": [("hudhayfa", 4), ("tirmidhi", 0)]},
            {"label": "Abu Dharr → Ahmad", "path_count": 15, "sources": ["Musnad Ahmad 5/161"], "nodes": [("abu_dharr", 4), ("ahmad", 0)]},
            {"label": "Samura ibn Jundub → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 6583"], "nodes": [("samura", 4), ("bukhari", 0)]},
        ],
    },

    # ==================================================================
    # 4. Hadith al-Manzila
    # ==================================================================
    {
        "id": "h_manzila",
        "rank": 4,
        "matn": "أَنْتَ مِنِّي بِمَنْزِلَةِ هَارُونَ مِنْ مُوسَى، إِلَّا أَنَّهُ لَا نَبِيَّ بَعْدِي",
        "matn_translation_fr": "Tu es pour moi ce qu'Aaron fut pour Moïse, sauf qu'il n'y a pas de prophète après moi.",
        "title_fr": "Hadith al-Manzila (La station d'Aaron)",
        "title_ar": "حديث المنزلة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreuses voies sunnites et chiites",
        "validation_sources": ["Sahih al-Bukhari 4416", "Sahih Muslim 2404", "Al-Kafi 8/106"],
        "thematic_category": "Ahl al-Bayt & succession",
        "keywords": ["manzila", "harun", "ali"],
        "turuq": [
            {"label": "Ibn Abbas → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 4416"], "nodes": [("ibn_abbas", 4), ("bukhari", 0)]},
            {"label": "Sa'd ibn Abi Waqqas → Muslim", "path_count": 25, "sources": ["Sahih Muslim 2404"], "nodes": [("saad", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id al-Khudri → Ahmad", "path_count": 20, "sources": ["Musnad Ahmad 3/32"], "nodes": [("abu_saeed", 4), ("ahmad", 0)]},
            {"label": "Jabir → Al-Tabarani", "path_count": 18, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("jabir", 4), ("tabarani", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 30, "sources": ["Al-Kafi 8/106"], "nodes": [("ali", 4), ("kulayni", 0)]},
            {"label": "Ali → Al-Sadiq → Al-Saduq", "path_count": 22, "sources": ["Ma'ani al-Akhbar"], "nodes": [("ali", 4), ("sadiq", 3), ("saduq", 0)]},
        ],
    },

    # ==================================================================
    # 5. Les actions ne valent que par les intentions
    # ==================================================================
    {
        "id": "h_niyyah",
        "rank": 5,
        "matn": "إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى",
        "matn_translation_fr": "En vérité, les actes ne valent que par les intentions, et chacun n'a que ce qu'il a intentionné.",
        "title_fr": "Les actions ne valent que par les intentions",
        "title_ar": "إنما الأعمال بالنيات",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de très nombreuses voies concordantes",
        "validation_sources": ["Sahih al-Bukhari 1", "Sahih Muslim 1907", "Musnad Ahmad 1/25"],
        "thematic_category": "Fondements de l'intention",
        "keywords": ["niyyah", "intention", "actes"],
        "turuq": [
            {"label": "Omar → Al-Zuhri → Al-Bukhari", "path_count": 40, "sources": ["Sahih al-Bukhari 1"], "nodes": [("umar", 4), ("al_zuhri", 2), ("bukhari", 0)]},
            {"label": "Omar → Al-Zuhri → Muslim", "path_count": 40, "sources": ["Sahih Muslim 1907"], "nodes": [("umar", 4), ("al_zuhri", 2), ("muslim", 0)]},
            {"label": "Omar → Al-Zuhri → Ahmad", "path_count": 35, "sources": ["Musnad Ahmad 1/25"], "nodes": [("umar", 4), ("al_zuhri", 2), ("ahmad", 0)]},
            {"label": "Omar → Al-Zuhri → Al-Tirmidhi", "path_count": 20, "sources": ["Sunan al-Tirmidhi 1647"], "nodes": [("umar", 4), ("al_zuhri", 2), ("tirmidhi", 0)]},
            {"label": "Omar → Al-Zuhri → Al-Darimi", "path_count": 15, "sources": ["Sunan al-Darimi 251"], "nodes": [("umar", 4), ("al_zuhri", 2), ("darimi", 0)]},
            {"label": "Omar → Al-Zuhri → Al-Nasa'i", "path_count": 12, "sources": ["Sunan al-Nasa'i 3437"], "nodes": [("umar", 4), ("al_zuhri", 2), ("nasai", 0)]},
        ],
    },

    # ==================================================================
    # 6. Hadith al-Thaqalayn
    # ==================================================================
    {
        "id": "h_thaqalayn",
        "rank": 6,
        "matn": "إِنِّي تَارِكٌ فِيكُمُ الثَّقَلَيْنِ: كِتَابَ اللَّهِ وَعِتْرَتِي أَهْلَ بَيْتِي",
        "matn_translation_fr": "Je laisse parmi vous deux choses précieuses : le Livre d'Allah et ma famille (Ahl al-Bayt).",
        "title_fr": "Hadith al-Thaqalayn (Les deux choses précieuses)",
        "title_ar": "حديث الثقلين",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — nombreuses voies sunnites et chiites",
        "validation_sources": ["Sunan al-Tirmidhi 3786", "Sahih Muslim 2408", "Musnad Ahmad 4/366", "Al-Kafi 1/294"],
        "thematic_category": "Ahl al-Bayt & succession",
        "keywords": ["thaqalayn", "qur'an", "ahl al-bayt"],
        "turuq": [
            {"label": "Ali → Anas → Al-Tirmidhi", "path_count": 30, "sources": ["Sunan al-Tirmidhi 3786"], "nodes": [("ali", 4), ("anass", 3), ("tirmidhi", 0)]},
            {"label": "Zayd ibn Arqam → Muslim", "path_count": 20, "sources": ["Sahih Muslim 2408"], "nodes": [("zayd_arqam", 4), ("muslim", 0)]},
            {"label": "Zayd ibn Arqam → Ahmad", "path_count": 25, "sources": ["Musnad Ahmad 4/366"], "nodes": [("zayd_arqam", 4), ("ahmad", 0)]},
            {"label": "Jabir → Al-Hakim", "path_count": 20, "sources": ["Mustadrak al-Hakim 3/118"], "nodes": [("jabir", 4), ("hakim", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 25, "sources": ["Al-Kafi 1/294"], "nodes": [("ali", 4), ("kulayni", 0)]},
            {"label": "Ali → Al-Saduq", "path_count": 20, "sources": ["Ma'ani al-Akhbar 90"], "nodes": [("ali", 4), ("saduq", 0)]},
            {"label": "Ali → Al-Tusi", "path_count": 18, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("tusi", 0)]},
        ],
    },

    # ==================================================================
    # 7. Le massage des chaussons
    # ==================================================================
    {
        "id": "h_mash",
        "rank": 7,
        "matn": "أَنَّ النَّبِيَّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مَسَحَ عَلَى الْخُفَّيْنِ",
        "matn_translation_fr": "Certes, le Prophète (paix sur lui) a essuyé (par-dessus) ses chaussons de cuir.",
        "title_fr": "Le massage des chaussons (Al-Mash 'ala al-Khuffayn)",
        "title_ar": "المسح على الخفين",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — pratique notoirement transmise par de nombreuses voies",
        "validation_sources": ["Sahih al-Bukhari 203", "Sahih Muslim 274", "Musnad Ahmad 2/245"],
        "thematic_category": "Purification",
        "keywords": ["mash", "khuffayn", "ablutions"],
        "turuq": [
            {"label": "Ali → Al-Bukhari", "path_count": 40, "sources": ["Sahih al-Bukhari 203"], "nodes": [("ali", 4), ("bukhari", 0)]},
            {"label": "Hudhayfa → Muslim", "path_count": 35, "sources": ["Sahih Muslim 274"], "nodes": [("hudhayfa", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 25, "sources": ["Musnad Ahmad 2/245"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Al-Mughira → Al-Tirmidhi", "path_count": 20, "sources": ["Sunan al-Tirmidhi 92"], "nodes": [("mughira", 4), ("tirmidhi", 0)]},
            {"label": "Ali → Abd al-Razzaq", "path_count": 15, "sources": ["Musannaf Abd al-Razzaq"], "nodes": [("ali", 4), ("abd_razzaq", 0)]},
        ],
    },

    # ==================================================================
    # 8. L'élévation des mains en prière
    # ==================================================================
    {
        "id": "h_rafy",
        "rank": 8,
        "matn": "كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَرْفَعُ يَدَيْهِ إِذَا كَبَّرَ وَإِذَا رَكَعَ",
        "matn_translation_fr": "Le Messager d'Allah (paix sur lui) élevait les mains lorsqu'il prononçait le takbir et lorsqu'il s'inclinait.",
        "title_fr": "L'élévation des mains en prière (Raf' al-Yadayn)",
        "title_ar": "رفع اليدين في الصلاة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — transmis par un grand nombre de Compagnons",
        "validation_sources": ["Sahih al-Bukhari 735", "Sahih Muslim 390", "Musnad Ahmad 2/123"],
        "thematic_category": "Prières & rites",
        "keywords": ["raf' al-yadayn", "priere", "takbir"],
        "turuq": [
            {"label": "Ibn Abbas → Al-Bukhari", "path_count": 45, "sources": ["Sahih al-Bukhari 735"], "nodes": [("ibn_abbas", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 30, "sources": ["Musnad Ahmad 2/123"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 25, "sources": ["Sahih Muslim 390"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Jabir → Abu Dawud", "path_count": 15, "sources": ["Sunan Abi Dawud 721"], "nodes": [("jabir", 4), ("abu_dawud", 0)]},
        ],
    },

    # ==================================================================
    # 9. L'Intercession
    # ==================================================================
    {
        "id": "h_shafaa",
        "rank": 9,
        "matn": "شَفَاعَتِي لِأَهْلِ الْكَبَائِرِ مِنْ أُمَّتِي",
        "matn_translation_fr": "Mon intercession est réservée à ceux de ma communauté qui ont commis de grands péchés.",
        "title_fr": "Hadith de l'Intercession (Al-Shafa'a)",
        "title_ar": "حديث الشفاعة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — très répandu",
        "validation_sources": ["Sahih al-Bukhari 99", "Sahih Muslim 193", "Musnad Ahmad 3/325"],
        "thematic_category": "Miséricorde & intercession",
        "keywords": ["shafa'a", "intercession"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 99"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Anas ibn Malik → Muslim", "path_count": 25, "sources": ["Sahih Muslim 193"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 2435"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Jabir → Ahmad", "path_count": 20, "sources": ["Musnad Ahmad 3/325"], "nodes": [("jabir", 4), ("ahmad", 0)]},
            {"label": "Imran ibn Husayn → Al-Bayhaqi", "path_count": 12, "sources": ["Sunan al-Bayhaqi"], "nodes": [("imran", 4), ("bayhaqi", 0)]},
        ],
    },

    # ==================================================================
    # 10. Le drapeau de Khaybar
    # ==================================================================
    {
        "id": "h_raya",
        "rank": 10,
        "matn": "لَأُعْطِيَنَّ الرَّايَةَ غَدًا رَجُلًا يُحِبُّ اللَّهَ وَرَسُولَهُ وَيُحِبُّهُ اللَّهُ وَرَسُولُهُ",
        "matn_translation_fr": "Demain, je confierai l'étendard à un homme qui aime Allah et Son Messager, et qu'Allah et Son Messager aiment.",
        "title_fr": "Le drapeau de Khaybar (Hadith al-Raya)",
        "title_ar": "حديث الراية",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih al-Bukhari 2942", "Sahih Muslim 2406", "Musnad Ahmad 2/384"],
        "thematic_category": "Jihad & wilaya",
        "keywords": ["raya", "khaybar", "ali"],
        "turuq": [
            {"label": "Omar → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 2942"], "nodes": [("umar", 4), ("bukhari", 0)]},
            {"label": "Salman al-Farisi → Muslim", "path_count": 20, "sources": ["Sahih Muslim 2406"], "nodes": [("salman", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 15, "sources": ["Musnad Ahmad 2/384"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
            {"label": "Burayda → Al-Nasa'i", "path_count": 12, "sources": ["Sunan al-Nasa'i"], "nodes": [("burayda", 4), ("nasai", 0)]},
        ],
    },

    # ==================================================================
    # 11. Le voyage nocturne
    # ==================================================================
    {
        "id": "h_isra",
        "rank": 11,
        "matn": "أُسْرِيَ بِي إِلَى بَيْتِ الْمَقْدِسِ، ثُمَّ عُرِجَ بِي إِلَى السَّمَاءِ",
        "matn_translation_fr": "Je fus transporté de nuit jusqu'à Bayt al-Maqdis, puis élevé à travers les cieux.",
        "title_fr": "Le voyage nocturne (Al-Isra' wa al-Mi'raj)",
        "title_ar": "الإسراء والمعراج",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — récit rapporté par de multiples voies",
        "validation_sources": ["Sahih al-Bukhari 3207", "Sahih Muslim 162"],
        "thematic_category": "Prophétie & miracles",
        "keywords": ["isra", "mi'raj", "voyage nocturne"],
        "turuq": [
            {"label": "Anas → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 3207"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Abu Dharr → Muslim", "path_count": 25, "sources": ["Sahih Muslim 162"], "nodes": [("abu_dharr", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Al-Hakim", "path_count": 15, "sources": ["Mustadrak al-Hakim 2/479"], "nodes": [("ibn_abbas", 4), ("hakim", 0)]},
            {"label": "Jabir → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi"], "nodes": [("jabir", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 12. Les douze califes
    # ==================================================================
    {
        "id": "h_khalifa",
        "rank": 12,
        "matn": "يَكُونُ اثْنَا عَشَرَ خَلِيفَةً، كُلُّهُمْ مِنْ قُرَيْشٍ",
        "matn_translation_fr": "Il y aura douze califes, tous issus de Quraysh.",
        "title_fr": "Les douze califes (Ithna 'ashar khalifa)",
        "title_ar": "اثنا عشر خليفة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 7222", "Sahih Muslim 1821", "Musnad Ahmad 1/398"],
        "thematic_category": "Direction & succession",
        "keywords": ["khalifa", "douze", "quraysh"],
        "turuq": [
            {"label": "Jabir → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 7222"], "nodes": [("jabir", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 25, "sources": ["Sahih Muslim 1821"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Ibn Mas'ud → Ahmad", "path_count": 20, "sources": ["Musnad Ahmad 1/398"], "nodes": [("ibn_masud", 4), ("ahmad", 0)]},
            {"label": "Abdullah ibn Amr → Al-Tabarani", "path_count": 15, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("abdullah_amr", 4), ("tabarani", 0)]},
        ],
    },

    # ==================================================================
    # 13. Le vaisseau d'Ahl al-Bayt (chiite)
    # ==================================================================
    {
        "id": "h_safina",
        "rank": 13,
        "matn": "مَثَلُ أَهْلِ بَيْتِي كَمَثَلِ سَفِينَةِ نُوحٍ، مَنْ رَكِبَهَا نَجَا، وَمَنْ تَخَلَّفَ عَنْهَا غَرِقَ",
        "matn_translation_fr": "L'exemple de ma famille est celui du vaisseau de Noé : qui y monte est sauvé, qui s'en écarte se noie.",
        "title_fr": "Le vaisseau d'Ahl al-Bayt (Hadith al-Safina)",
        "title_ar": "حديث السفينة",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — largement transmis dans les sources chiites (et rapporté par des savants sunnites)",
        "validation_sources": ["Ma'ani al-Akhbar 331", "Mustadrak al-Hakim 2/343"],
        "thematic_category": "Ahl al-Bayt & salut",
        "keywords": ["safina", "vaisseau", "ahl al-bayt"],
        "turuq": [
            {"label": "Abu Dharr → Al-Saduq", "path_count": 20, "sources": ["Ma'ani al-Akhbar 331"], "nodes": [("abu_dharr", 4), ("saduq", 0)]},
            {"label": "Abu Dharr → Al-Hakim", "path_count": 15, "sources": ["Mustadrak al-Hakim 2/343"], "nodes": [("abu_dharr", 4), ("hakim", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 15, "sources": ["Al-Kafi"], "nodes": [("ali", 4), ("kulayni", 0)]},
            {"label": "Ali → Al-Sadiq → Al-Saduq", "path_count": 12, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("sadiq", 3), ("saduq", 0)]},
        ],
    },

    # ==================================================================
    # 14. L'oiseau rôti (chiite)
    # ==================================================================
    {
        "id": "h_tayr",
        "rank": 14,
        "matn": "اللَّهُمَّ ائْتِنِي بِأَحَبِّ خَلْقِكَ إِلَيْكَ يَأْكُلُ مَعِي مِنْ هَذَا الطَّيْرِ",
        "matn_translation_fr": "Ô Allah, amène-moi le plus cher de Tes créatures afin qu'il mange avec moi de cet oiseau.",
        "title_fr": "L'oiseau rôti (Hadith al-Tayr)",
        "title_ar": "حديث الطير",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — nombreuses voies chiites (aussi rapporté par Al-Tirmidhi)",
        "validation_sources": ["Sunan al-Tirmidhi 3721", "Al-Mu'jam al-Kabir", "Mustadrak al-Hakim 3/126"],
        "thematic_category": "Vertus d'Ali",
        "keywords": ["tayr", "oiseau", "ali"],
        "turuq": [
            {"label": "Anas → Al-Tirmidhi", "path_count": 30, "sources": ["Sunan al-Tirmidhi 3721"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Ibn Abbas → Al-Tabarani", "path_count": 25, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("ibn_abbas", 4), ("tabarani", 0)]},
            {"label": "Abu Hurayra → Al-Hakim", "path_count": 15, "sources": ["Mustadrak al-Hakim 3/126"], "nodes": [("abu_hurayra", 4), ("hakim", 0)]},
            {"label": "Ali → Al-Saduq", "path_count": 18, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("saduq", 0)]},
        ],
    },

    # ==================================================================
    # 15. La ville du savoir (chiite)
    # ==================================================================
    {
        "id": "h_madina_ilm",
        "rank": 15,
        "matn": "أَنَا مَدِينَةُ الْعِلْمِ وَعَلِيٌّ بَابُهَا",
        "matn_translation_fr": "Je suis la ville du savoir et Ali en est la porte.",
        "title_fr": "La ville du savoir (Madinat al-'Ilm)",
        "title_ar": "أنا مدينة العلم وعلي بابها",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — transmis par des voies multiples (divergences sur la terminologie)",
        "validation_sources": ["Mustadrak al-Hakim 3/126", "Al-Mu'jam al-Kabir"],
        "thematic_category": "Vertus d'Ali & savoir",
        "keywords": ["madinat al-ilm", "savoir", "ali"],
        "turuq": [
            {"label": "Ibn Abbas → Al-Hakim", "path_count": 20, "sources": ["Mustadrak al-Hakim 3/126"], "nodes": [("ibn_abbas", 4), ("hakim", 0)]},
            {"label": "Jabir → Al-Tabarani", "path_count": 15, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("jabir", 4), ("tabarani", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 15, "sources": ["Al-Kafi"], "nodes": [("ali", 4), ("kulayni", 0)]},
            {"label": "Ali → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi"], "nodes": [("ali", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 16. Le Dajjal
    # ==================================================================
    {
        "id": "h_dajjal",
        "rank": 16,
        "matn": "الدَّجَّالُ أَعْوَرُ الْعَيْنِ الْيُمْنَى، مَكْتُوبٌ بَيْنَ عَيْنَيْهِ كَافِرٌ",
        "matn_translation_fr": "Le Dajjal est borgne de l'œil droit ; entre ses deux yeux est écrit « mécréant ».",
        "title_fr": "L'Antéchrist (Al-Dajjal)",
        "title_ar": "الدجال",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par un grand nombre de Compagnons",
        "validation_sources": ["Sahih al-Bukhari 7131", "Sahih Muslim 2933", "Sunan al-Tirmidhi 2245"],
        "thematic_category": "Eschatologie",
        "keywords": ["dajjal", "antechrist", "fitna"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 40, "sources": ["Sahih Muslim 2933"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Bukhari", "path_count": 35, "sources": ["Sahih al-Bukhari 7131"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Hudhayfa → Al-Tirmidhi", "path_count": 25, "sources": ["Sunan al-Tirmidhi 2245"], "nodes": [("hudhayfa", 4), ("tirmidhi", 0)]},
            {"label": "Ibn Mas'ud → Abu Dawud", "path_count": 20, "sources": ["Sunan Abi Dawud 4328"], "nodes": [("ibn_masud", 4), ("abu_dawud", 0)]},
        ],
    },

    # ==================================================================
    # 17. La construction des mosquées
    # ==================================================================
    {
        "id": "h_masjid",
        "rank": 17,
        "matn": "مَنْ بَنَى لِلَّهِ مَسْجِدًا بَنَى اللَّهُ لَهُ مِثْلَهُ فِي الْجَنَّةِ",
        "matn_translation_fr": "Quiconque bâtit une mosquée pour Allah, Allah lui bâtira son semblable au Paradis.",
        "title_fr": "La construction des mosquées",
        "title_ar": "من بنى لله مسجدا",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de multiples Compagnons",
        "validation_sources": ["Sahih al-Bukhari 450", "Sahih Muslim 533", "Sunan al-Tirmidhi 319"],
        "thematic_category": "Culte & edification",
        "keywords": ["masjid", "mosquee", "construction"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 450"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Ibn Abbas → Muslim", "path_count": 20, "sources": ["Sahih Muslim 533"], "nodes": [("ibn_abbas", 4), ("muslim", 0)]},
            {"label": "Jabir → Al-Tirmidhi", "path_count": 18, "sources": ["Sunan al-Tirmidhi 319"], "nodes": [("jabir", 4), ("tirmidhi", 0)]},
            {"label": "Anas → Ahmad", "path_count": 15, "sources": ["Musnad Ahmad 3/153"], "nodes": [("anass", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 18. La vision d'Allah (Ru'yat Allah)
    # ==================================================================
    {
        "id": "h_ruya",
        "rank": 18,
        "matn": "إِنَّكُمْ سَتَرَوْنَ رَبَّكُمْ كَمَا تَرَوْنَ الْقَمَرَ لَيْلَةَ الْبَدْرِ",
        "matn_translation_fr": "Vous verrez votre Seigneur comme vous voyez la lune la nuit de la pleine lune.",
        "title_fr": "La vision d'Allah (Ru'yat Allah)",
        "title_ar": "الرؤية",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 7435", "Sahih Muslim 182", "Sunan al-Tirmidhi 2554"],
        "thematic_category": "Eschatologie & credo",
        "keywords": ["ru'ya", "vision", "au-dela"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 7435"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 25, "sources": ["Sahih Muslim 182"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Sa'id → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 2554"], "nodes": [("abu_saeed", 4), ("tirmidhi", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 12, "sources": ["Sahih Muslim 183"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
        ],
    },

    # ==================================================================
    # 19. L'amour des Ansar
    # ==================================================================
    {
        "id": "h_ansar",
        "rank": 19,
        "matn": "الْأَنْصَارُ لَا يُحِبُّهُمْ إِلَّا مُؤْمِنٌ، وَلَا يُبْغِضُهُمْ إِلَّا مُنَافِقٌ",
        "matn_translation_fr": "Les Ansar : seuls les croyants les aiment, et seuls les hypocrites les détestent.",
        "title_fr": "L'amour des Ansar",
        "title_ar": "حب الأنصار",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih al-Bukhari 3784", "Sahih Muslim 74", "Sunan al-Tirmidhi 3904"],
        "thematic_category": "Mérites des Compagnons",
        "keywords": ["ansar", "amour", "imam"],
        "turuq": [
            {"label": "Anas → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 3784"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 20, "sources": ["Sahih Muslim 74"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 3904"], "nodes": [("ibn_abbas", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 20. La prière en congrégation
    # ==================================================================
    {
        "id": "h_jamaa",
        "rank": 20,
        "matn": "صَلَاةُ الْجَمَاعَةِ تَفْضُلُ صَلَاةَ الْفَذِّ بِسَبْعٍ وَعِشْرِينَ دَرَجَةً",
        "matn_translation_fr": "La prière en congrégation surpasse la prière individuelle de vingt-sept degrés.",
        "title_fr": "La prière en congrégation (Salat al-Jama'a)",
        "title_ar": "صلاة الجماعة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de nombreuses voies",
        "validation_sources": ["Sahih al-Bukhari 645", "Sahih Muslim 650", "Sunan al-Tirmidhi 216"],
        "thematic_category": "Prières & rites",
        "keywords": ["jamaa", "congregation", "priere"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 645"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 25, "sources": ["Sahih Muslim 650"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Anas → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 216"], "nodes": [("anass", 4), ("tirmidhi", 0)]},
            {"label": "Ibn Abbas → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 1/358"], "nodes": [("ibn_abbas", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 21. Le jeûne de Ramadan
    # ==================================================================
    {
        "id": "h_ramadan",
        "rank": 21,
        "matn": "مَنْ صَامَ رَمَضَانَ إِيمَانًا وَاحْتِسَابًا غُفِرَ لَهُ مَا تَقَدَّمَ مِنْ ذَنْبِهِ",
        "matn_translation_fr": "Quiconque jeûne Ramadan par foi et en quête de la récompense, ses péchés passés lui sont pardonnés.",
        "title_fr": "Le jeûne de Ramadan",
        "title_ar": "فضل صيام رمضان",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Sahih al-Bukhari 38", "Sahih Muslim 760", "Sunan al-Nasa'i 2211"],
        "thematic_category": "Jeûne & Ramadan",
        "keywords": ["ramadan", "siyam", "jeune"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 38"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 25, "sources": ["Sahih Muslim 760"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Nasa'i", "path_count": 15, "sources": ["Sunan al-Nasa'i 2211"], "nodes": [("abu_hurayra", 4), ("nasai", 0)]},
            {"label": "Ibn Abbas → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 1/353"], "nodes": [("ibn_abbas", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 22. Les veillées de Ramadan
    # ==================================================================
    {
        "id": "h_qiyam",
        "rank": 22,
        "matn": "مَنْ قَامَ رَمَضَانَ إِيمَانًا وَاحْتِسَابًا غُفِرَ لَهُ مَا تَقَدَّمَ مِنْ ذَنْبِهِ",
        "matn_translation_fr": "Quiconque veille en prière durant Ramadan par foi et en quête de la récompense, ses péchés passés lui sont pardonnés.",
        "title_fr": "Les veillées de Ramadan (Qiyam Ramadan)",
        "title_ar": "قيام رمضان",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Sahih al-Bukhari 37", "Sahih Muslim 759", "Sunan al-Nasa'i 1604"],
        "thematic_category": "Jeûne & Ramadan",
        "keywords": ["qiyam", "tarawih", "ramadan"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 37"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 22, "sources": ["Sahih Muslim 759"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Nasa'i", "path_count": 12, "sources": ["Sunan al-Nasa'i 1604"], "nodes": [("abu_hurayra", 4), ("nasai", 0)]},
        ],
    },

    # ==================================================================
    # 23. La nuit du Destin
    # ==================================================================
    {
        "id": "h_laylat_qadr",
        "rank": 23,
        "matn": "تَحَرَّوْا لَيْلَةَ الْقَدْرِ فِي الْعَشْرِ الْأَوَاخِرِ مِنْ رَمَضَانَ",
        "matn_translation_fr": "Recherchez la nuit du Destin dans les dix dernières nuits de Ramadan.",
        "title_fr": "La nuit du Destin (Laylat al-Qadr)",
        "title_ar": "ليلة القدر",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de nombreuses voies",
        "validation_sources": ["Sahih al-Bukhari 2020", "Sahih Muslim 1169", "Sunan al-Tirmidhi 792"],
        "thematic_category": "Jeûne & Ramadan",
        "keywords": ["laylat al-qadr", "ramadan"],
        "turuq": [
            {"label": "Aisha → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 2020"], "nodes": [("aisha", 4), ("bukhari", 0)]},
            {"label": "Aisha → Muslim", "path_count": 25, "sources": ["Sahih Muslim 1169"], "nodes": [("aisha", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 792"], "nodes": [("ibn_abbas", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 24. La Fatiha dans la prière
    # ==================================================================
    {
        "id": "h_fatiha",
        "rank": 24,
        "matn": "لَا صَلَاةَ لِمَنْ لَمْ يَقْرَأْ بِفَاتِحَةِ الْكِتَابِ",
        "matn_translation_fr": "Point de prière pour celui qui ne récite pas l'ouverture du Livre (al-Fatiha).",
        "title_fr": "La récitation d'al-Fatiha",
        "title_ar": "قراءة الفاتحة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par un grand nombre de voies",
        "validation_sources": ["Sahih al-Bukhari 756", "Sahih Muslim 394", "Sunan Abi Dawud 822"],
        "thematic_category": "Prières & rites",
        "keywords": ["fatiha", "coran", "priere"],
        "turuq": [
            {"label": "Ubada ibn al-Samit → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 756"], "nodes": [("ubada", 4), ("bukhari", 0)]},
            {"label": "Ubada ibn al-Samit → Muslim", "path_count": 28, "sources": ["Sahih Muslim 394"], "nodes": [("ubada", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 15, "sources": ["Sunan Abi Dawud 822"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 2/241"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 25. L'allaitement (Rada'a)
    # ==================================================================
    {
        "id": "h_rida",
        "rank": 25,
        "matn": "يَحْرُمُ مِنَ الرَّضَاعِ مَا يَحْرُمُ مِنَ النَّسَبِ",
        "matn_translation_fr": "Ce qui est interdit par l'allaitement est équivalent à ce qui est interdit par la parenté.",
        "title_fr": "L'allaitement (Al-Rada'a)",
        "title_ar": "الرضاع",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de multiples Compagnons",
        "validation_sources": ["Sahih al-Bukhari 2645", "Sahih Muslim 1445", "Sunan al-Tirmidhi 1145"],
        "thematic_category": "Droit familial",
        "keywords": ["rada'a", "allaitement", "parente"],
        "turuq": [
            {"label": "Aisha → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 2645"], "nodes": [("aisha", 4), ("bukhari", 0)]},
            {"label": "Aisha → Muslim", "path_count": 22, "sources": ["Sahih Muslim 1445"], "nodes": [("aisha", 4), ("muslim", 0)]},
            {"label": "Umm Salama → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 1145"], "nodes": [("umm_salama", 4), ("tirmidhi", 0)]},
            {"label": "Ibn Abbas → Al-Darimi", "path_count": 12, "sources": ["Sunan al-Darimi"], "nodes": [("ibn_abbas", 4), ("darimi", 0)]},
        ],
    },

    # ==================================================================
    # 26. Tout enivrant est interdit
    # ==================================================================
    {
        "id": "h_khamr",
        "rank": 26,
        "matn": "كُلُّ مُسْكِرٍ حَرَامٌ",
        "matn_translation_fr": "Tout enivrant est illicite.",
        "title_fr": "Tout enivrant est interdit",
        "title_ar": "كل مسكر حرام",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Sahih al-Bukhari 5586", "Sahih Muslim 2001", "Musnad Ahmad 3/347"],
        "thematic_category": "Interdits",
        "keywords": ["khamr", "muskir", "interdit"],
        "turuq": [
            {"label": "Aisha → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 5586"], "nodes": [("aisha", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 20, "sources": ["Sahih Muslim 2001"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Ahmad", "path_count": 15, "sources": ["Musnad Ahmad 3/347"], "nodes": [("ibn_abbas", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 27. La guerre est une ruse
    # ==================================================================
    {
        "id": "h_war",
        "rank": 27,
        "matn": "الْحَرْبُ خُدْعَةٌ",
        "matn_translation_fr": "La guerre est une ruse.",
        "title_fr": "La guerre est une ruse (Al-Harb Khud'a)",
        "title_ar": "الحرب خدعة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih al-Bukhari 3030", "Sahih Muslim 1739", "Musnad Ahmad 2/398"],
        "thematic_category": "Jihad & conduite",
        "keywords": ["harb", "khud'a", "ruse"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 3030"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 18, "sources": ["Sahih Muslim 1739"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Jabir → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 2/398"], "nodes": [("jabir", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 28. Les imams de Quraysh
    # ==================================================================
    {
        "id": "h_imams_quraysh",
        "rank": 28,
        "matn": "الْأَئِمَّةُ مِنْ قُرَيْشٍ",
        "matn_translation_fr": "Les dirigeants (imams) sont issus de Quraysh.",
        "title_fr": "Les imams de Quraysh",
        "title_ar": "الأئمة من قريش",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples Compagnons",
        "validation_sources": ["Sahih al-Bukhari 3500", "Sahih Muslim 1820", "Musnad Ahmad 3/129"],
        "thematic_category": "Direction & succession",
        "keywords": ["imams", "quraysh", "direction"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 3500"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 18, "sources": ["Sahih Muslim 1820"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Ibn Abbas → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 3/129"], "nodes": [("ibn_abbas", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 29. Les cinq piliers de l'Islam
    # ==================================================================
    {
        "id": "h_pillars",
        "rank": 29,
        "matn": "بُنِيَ الْإِسْلَامُ عَلَى خَمْسٍ: شَهَادَةِ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ، وَإِقَامِ الصَّلَاةِ، وَإِيتَاءِ الزَّكَاةِ، وَصَوْمِ رَمَضَانَ، وَحَجِّ الْبَيْتِ",
        "matn_translation_fr": "L'Islam est bâti sur cinq : le témoignage qu'il n'y a de dieu qu'Allah et que Muhammad est Son Messager, l'accomplissement de la prière, l'aumône légale, le jeûne de Ramadan et le pèlerinage.",
        "title_fr": "Les cinq piliers de l'Islam",
        "title_ar": "أركان الإسلام",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — transmis par de nombreuses voies",
        "validation_sources": ["Sahih al-Bukhari 8", "Sahih Muslim 16", "Sunan al-Tirmidhi 2609"],
        "thematic_category": "Fondements",
        "keywords": ["pilier", "islam", "cinq"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 8"], "nodes": [("abdullah_umar", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 25, "sources": ["Sahih Muslim 16"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 2609"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Jabir → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 3/326"], "nodes": [("jabir", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 30. La recherche du savoir est une obligation
    # ==================================================================
    {
        "id": "h_ilm_fard",
        "rank": 30,
        "matn": "طَلَبُ الْعِلْمِ فَرِيضَةٌ عَلَى كُلِّ مُسْلِمٍ",
        "matn_translation_fr": "La recherche du savoir est une obligation pour tout musulman.",
        "title_fr": "La recherche du savoir (Talab al-'Ilm)",
        "title_ar": "طلب العلم فريضة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Sunan Ibn Majah 224", "Al-Mu'jam al-Kabir", "Al-Kafi"],
        "thematic_category": "Savoir & éducation",
        "keywords": ["ilm", "savoir", "fard"],
        "turuq": [
            {"label": "Anas → Ibn Majah", "path_count": 20, "sources": ["Sunan Ibn Majah 224"], "nodes": [("anass", 4), ("ibn_majah", 0)]},
            {"label": "Abu Hurayra → Al-Tabarani", "path_count": 15, "sources": ["Al-Mu'jam al-Awsat"], "nodes": [("abu_hurayra", 4), ("tabarani", 0)]},
            {"label": "Ali → Al-Kulayni", "path_count": 15, "sources": ["Al-Kafi 1/30"], "nodes": [("ali", 4), ("kulayni", 0)]},
        ],
    },

    # ==================================================================
    # 31. L'abandon de la prière du vendredi
    # ==================================================================
    {
        "id": "h_jumua",
        "rank": 31,
        "matn": "مَنْ تَرَكَ الْجُمُعَةَ ثَلَاثَ مَرَّاتٍ تَهَاوُنًا طَبَعَ اللَّهُ عَلَى قَلْبِهِ",
        "matn_translation_fr": "Quiconque délaisse trois fois la prière du vendredi par négligence, Allah scelle son cœur.",
        "title_fr": "L'abandon de la prière du vendredi",
        "title_ar": "الترغيب في الجمعة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih Muslim 865", "Sunan Abi Dawud 1052", "Musnad Ahmad 3/424"],
        "thematic_category": "Prières & rites",
        "keywords": ["jumua", "vendredi"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 20, "sources": ["Sahih Muslim 865"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Abu Dawud", "path_count": 15, "sources": ["Sunan Abi Dawud 1052"], "nodes": [("abu_hurayra", 4), ("abu_dawud", 0)]},
            {"label": "Jabir → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 3/424"], "nodes": [("jabir", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 32. Hadith al-Kisa (chiite)
    # ==================================================================
    {
        "id": "h_kisa",
        "rank": 32,
        "matn": "اللَّهُمَّ هَؤُلَاءِ أَهْلُ بَيْتِي، فَاذْهِبْ عَنْهُمُ الرِّجْسَ وَطَهِّرْهُمْ تَطْهِيرًا",
        "matn_translation_fr": "Ô Allah, ceux-ci sont ma famille ; éloigne d'eux la souillure et purifie-les entièrement.",
        "title_fr": "Hadith al-Kisa (Le manteau)",
        "title_ar": "حديث الكساء",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — transmis par de multiples voies (verset de la purification)",
        "validation_sources": ["Sahih Muslim 2424", "Sunan al-Tirmidhi 3205", "Al-Kafi"],
        "thematic_category": "Ahl al-Bayt",
        "keywords": ["kisa", "tathir", "ahl al-bayt"],
        "turuq": [
            {"label": "Aisha → Muslim", "path_count": 20, "sources": ["Sahih Muslim 2424"], "nodes": [("aisha", 4), ("muslim", 0)]},
            {"label": "Umm Salama → Al-Tirmidhi", "path_count": 18, "sources": ["Sunan al-Tirmidhi 3205"], "nodes": [("umm_salama", 4), ("tirmidhi", 0)]},
            {"label": "Ali → Al-Sadiq → Al-Kulayni", "path_count": 20, "sources": ["Al-Kafi 1/287"], "nodes": [("ali", 4), ("sadiq", 3), ("kulayni", 0)]},
            {"label": "Ali → Al-Saduq", "path_count": 15, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("saduq", 0)]},
        ],
    },

    # ==================================================================
    # 33. Le jour de l'avertissement (Yawm al-Dar)
    # ==================================================================
    {
        "id": "h_dar",
        "rank": 33,
        "matn": "مَنْ يُؤَازِرُنِي عَلَى هَذَا الْأَمْرِ يَكُونُ أَخِي وَوَزِيرِي وَوَصِيِّي وَخَلِيفَتِي فِيكُمْ",
        "matn_translation_fr": "Quiconque m'assiste en cette affaire sera mon frère, mon vizir, mon exécuteur testamentaire et mon successeur parmi vous.",
        "title_fr": "Le jour de l'avertissement (Yawm al-Dar)",
        "title_ar": "حديث يوم الدار",
        "tawatur_type": "lafzi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Lafzi — transmis par de multiples voies chiites (aussi cité par des historiens sunnites)",
        "validation_sources": ["Tarikh al-Tabari", "Al-Kafi", "Musnad Ahmad 1/111"],
        "thematic_category": "Ahl al-Bayt & succession",
        "keywords": ["dar", "inzar", "succession"],
        "turuq": [
            {"label": "Ali → Ibn Abbas → Ahmad", "path_count": 18, "sources": ["Musnad Ahmad 1/111"], "nodes": [("ali", 4), ("ibn_abbas", 3), ("ahmad", 0)]},
            {"label": "Ali → Ibn Abbas → Al-Tabarani", "path_count": 15, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("ali", 4), ("ibn_abbas", 3), ("tabarani", 0)]},
            {"label": "Ali → Al-Sadiq → Al-Kulayni", "path_count": 20, "sources": ["Al-Kafi"], "nodes": [("ali", 4), ("sadiq", 3), ("kulayni", 0)]},
            {"label": "Ali → Al-Thawri", "path_count": 12, "sources": ["Tarikh al-Tabari"], "nodes": [("ali", 4), ("thawri", 0)]},
        ],
    },

    # ==================================================================
    # 34. Ali avec la vérité (chiite)
    # ==================================================================
    {
        "id": "h_ali_haqq",
        "rank": 34,
        "matn": "عَلِيٌّ مَعَ الْحَقِّ وَالْحَقُّ مَعَ عَلِيٍّ، وَلَنْ يَفْتَرِقَا حَتَّى يَرِدَا عَلَيَّ الْحَوْضَ",
        "matn_translation_fr": "Ali est avec la vérité et la vérité est avec Ali ; ils ne se sépareront pas jusqu'à ce qu'ils reviennent vers moi au Bassin.",
        "title_fr": "Ali avec la vérité (Ali ma'a al-Haqq)",
        "title_ar": "علي مع الحق",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Al-Hakim", "Al-Mu'jam al-Kabir", "Sahih Muslim (variante)"],
        "thematic_category": "Vertus d'Ali",
        "keywords": ["ali", "haqq", "verite"],
        "turuq": [
            {"label": "Ali → Al-Hakim", "path_count": 18, "sources": ["Mustadrak al-Hakim"], "nodes": [("ali", 4), ("hakim", 0)]},
            {"label": "Umm Salama → Al-Tabarani", "path_count": 15, "sources": ["Al-Mu'jam al-Kabir"], "nodes": [("umm_salama", 4), ("tabarani", 0)]},
            {"label": "Ali → Al-Saduq", "path_count": 15, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("saduq", 0)]},
            {"label": "Ali → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi"], "nodes": [("ali", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 35. Qui meurt sans connaître l'imam de son temps (chiite)
    # ==================================================================
    {
        "id": "h_imam_zaman",
        "rank": 35,
        "matn": "مَنْ مَاتَ وَلَمْ يَعْرِفْ إِمَامَ زَمَانِهِ مَاتَ مِيتَةً جَاهِلِيَّةً",
        "matn_translation_fr": "Quiconque meurt sans connaître l'imam de son temps meurt d'une mort d'ignorance (pré-islamique).",
        "title_fr": "Connaître l'imam de son temps",
        "title_ar": "من مات ولم يعرف إمام زمانه",
        "tawatur_type": "ma'nawi",
        "obedience": "chiite",
        "degree_fr": "Mutawatir Ma'nawi — transmis par de multiples voies chiites",
        "validation_sources": ["Al-Kafi", "Al-Amali", "Yanabi' al-Mawadda"],
        "thematic_category": "Imamat",
        "keywords": ["imam", "zaman", "jahiliyya"],
        "turuq": [
            {"label": "Ali → Al-Sadiq → Al-Kulayni", "path_count": 20, "sources": ["Al-Kafi 1/376"], "nodes": [("ali", 4), ("sadiq", 3), ("kulayni", 0)]},
            {"label": "Ali → Al-Baqir → Al-Saduq", "path_count": 15, "sources": ["Al-Amali"], "nodes": [("ali", 4), ("baqir", 3), ("saduq", 0)]},
            {"label": "Ali → Al-Radi", "path_count": 12, "sources": ["Nahj al-Balagha"], "nodes": [("ali", 4), ("radi", 0)]},
        ],
    },

    # ==================================================================
    # 36. La purification est une moitié de la foi
    # ==================================================================
    {
        "id": "h_tahur",
        "rank": 36,
        "matn": "الطُّهُورُ شَطْرُ الْإِيمَانِ",
        "matn_translation_fr": "La purification est la moitié de la foi.",
        "title_fr": "La purification, moitié de la foi",
        "title_ar": "الطهور شطر الإيمان",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih Muslim 223", "Sunan al-Tirmidhi 3517", "Musnad Ahmad 5/342"],
        "thematic_category": "Purification",
        "keywords": ["tahur", "purification", "iman"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 20, "sources": ["Sahih Muslim 223"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 3517"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 5/342"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 37. Tout acte de bien est une aumône
    # ==================================================================
    {
        "id": "h_ma_ruf",
        "rank": 37,
        "matn": "كُلُّ مَعْرُوفٍ صَدَقَةٌ",
        "matn_translation_fr": "Tout acte de bien est une aumône.",
        "title_fr": "Tout acte de bien est une aumône",
        "title_ar": "كل معروف صدقة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — rapporté par de multiples voies",
        "validation_sources": ["Sahih al-Bukhari 6021", "Sahih Muslim 1005", "Sunan al-Tirmidhi 1970"],
        "thematic_category": "Éthique",
        "keywords": ["ma'ruf", "sadaqa", "bien"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 6021"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Jabir → Muslim", "path_count": 15, "sources": ["Sahih Muslim 1005"], "nodes": [("jabir", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 12, "sources": ["Sunan al-Tirmidhi 1970"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 38. Les sept péchés destructeurs
    # ==================================================================
    {
        "id": "h_kabair",
        "rank": 38,
        "matn": "اجْتَنِبُوا السَّبْعَ الْمُوبِقَاتِ: الشِّرْكُ بِاللَّهِ، وَالسِّحْرُ، وَقَتْلُ النَّفْسِ، وَأَكْلُ الرِّبَا، وَأَكْلُ مَالِ الْيَتِيمِ، وَالتَّوَلِّي يَوْمَ الزَّحْفِ، وَقَذْفُ الْمُحْصَنَاتِ",
        "matn_translation_fr": "Évitez les sept péchés destructeurs : l'association à Allah, la magie, le meurtre, l'usure, la consommation des biens de l'orphelin, la fuite au combat et la calomnie envers les femmes vertueuses.",
        "title_fr": "Les sept péchés destructeurs (Al-Sab' al-Mubiqat)",
        "title_ar": "اجتنبوا السبع الموبقات",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par plusieurs voies",
        "validation_sources": ["Sahih al-Bukhari 2766", "Sahih Muslim 89", "Musnad Ahmad 2/201"],
        "thematic_category": "Interdits majeurs",
        "keywords": ["kabair", "peches", "mubiqat"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 2766"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abu Hurayra → Muslim", "path_count": 18, "sources": ["Sahih Muslim 89"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Amr → Ahmad", "path_count": 12, "sources": ["Musnad Ahmad 2/201"], "nodes": [("abdullah_amr", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 39. Qui ne fait pas miséricorde
    # ==================================================================
    {
        "id": "h_rahma",
        "rank": 39,
        "matn": "مَنْ لَا يَرْحَمُ لَا يُرْحَمُ",
        "matn_translation_fr": "Celui qui ne fait pas miséricorde ne recevra pas de miséricorde.",
        "title_fr": "Qui ne fait pas miséricorde (Man la yarham)",
        "title_ar": "من لا يرحم لا يرحم",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — rapporté par de nombreux Compagnons",
        "validation_sources": ["Sahih al-Bukhari 5997", "Sahih Muslim 2318", "Sunan al-Tirmidhi 1922"],
        "thematic_category": "Miséricorde",
        "keywords": ["rahma", "miséricorde"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 30, "sources": ["Sahih al-Bukhari 5997"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Jarir → Muslim", "path_count": 25, "sources": ["Sahih Muslim 2318"], "nodes": [("jarir", 4), ("muslim", 0)]},
            {"label": "Aisha → Ahmad", "path_count": 20, "sources": ["Musnad Ahmad 6/49"], "nodes": [("aisha", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 40. Nul ne croit vraiment jusqu'à aimer pour son frère...
    # ==================================================================
    {
        "id": "h_akh",
        "rank": 40,
        "matn": "لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ",
        "matn_translation_fr": "Aucun de vous ne croit vraiment tant qu'il n'aime pas pour son frère ce qu'il aime pour lui-même.",
        "title_fr": "Aimer pour son frère (La yu'minu ahadukum)",
        "title_ar": "لا يؤمن أحدكم حتى يحب لأخيه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — livre sur l'intention et actes de foi",
        "validation_sources": ["Sahih al-Bukhari 13", "Sahih Muslim 45", "Sunan al-Tirmidhi 2515"],
        "thematic_category": "Foi & fraternité",
        "keywords": ["iman", "fraternite", "amour"],
        "turuq": [
            {"label": "Anas → Al-Bukhari", "path_count": 25, "sources": ["Sahih al-Bukhari 13"], "nodes": [("anass", 4), ("bukhari", 0)]},
            {"label": "Anas → Muslim", "path_count": 22, "sources": ["Sahih Muslim 45"], "nodes": [("anass", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 15, "sources": ["Sunan al-Tirmidhi 2515"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 41. Le musulman est celui dont la langue et la main sont sûres
    # ==================================================================
    {
        "id": "h_salam",
        "rank": 41,
        "matn": "الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ",
        "matn_translation_fr": "Le musulman est celui dont les musulmans sont à l'abri de sa langue et de sa main.",
        "title_fr": "Le vrai musulman (Al-Muslim man salima)",
        "title_ar": "المسلم من سلم المسلمون من لسانه ويده",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — plusieurs Compagnons distincts",
        "validation_sources": ["Sahih al-Bukhari 10", "Sahih Muslim 40", "Sunan al-Tirmidhi 2627"],
        "thematic_category": "Éthique & foi",
        "keywords": ["muslim", "langue", "paix"],
        "turuq": [
            {"label": "Abdullah ibn Amr → Al-Bukhari", "path_count": 22, "sources": ["Sahih al-Bukhari 10"], "nodes": [("abdullah_amr", 4), ("bukhari", 0)]},
            {"label": "Jabir → Muslim", "path_count": 20, "sources": ["Sahih Muslim 40"], "nodes": [("jabir", 4), ("muslim", 0)]},
            {"label": "Abu Musa → Al-Tirmidhi", "path_count": 14, "sources": ["Sunan al-Tirmidhi 2627"], "nodes": [("abu_musa", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 42. La pudeur fait partie de la foi
    # ==================================================================
    {
        "id": "h_haya",
        "rank": 42,
        "matn": "الْحَيَاءُ مِنَ الْإِيمَانِ",
        "matn_translation_fr": "La pudeur (al-haya') fait partie de la foi.",
        "title_fr": "La pudeur fait partie de la foi (Al-Haya' min al-Iman)",
        "title_ar": "الحياء من الإيمان",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — de multiples chaînes concordantes",
        "validation_sources": ["Sahih al-Bukhari 24", "Sahih Muslim 36", "Sunan Abi Dawud 4796"],
        "thematic_category": "Éthique & foi",
        "keywords": ["haya", "pudeur", "iman"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 24"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 18, "sources": ["Sahih Muslim 36"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Salman → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 4796"], "nodes": [("salman", 4), ("abu_dawud", 0)]},
        ],
    },

    # ==================================================================
    # 43. La religion, c'est le conseil sincère
    # ==================================================================
    {
        "id": "h_nasiha",
        "rank": 43,
        "matn": "الدِّينُ النَّصِيحَةُ",
        "matn_translation_fr": "La religion, c'est le conseil sincère.",
        "title_fr": "La religion est le conseil (Al-Din al-Nasiha)",
        "title_ar": "الدين النصيحة",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — célèbre, rapporté par Tamim al-Dari",
        "validation_sources": ["Sahih Muslim 55", "Sunan Abi Dawud 4944", "Sunan al-Nasa'i 4197"],
        "thematic_category": "Sincérité & communauté",
        "keywords": ["nasiha", "din", "conseil"],
        "turuq": [
            {"label": "Tamim al-Dari → Muslim", "path_count": 16, "sources": ["Sahih Muslim 55"], "nodes": [("tamim", 4), ("muslim", 0)]},
            {"label": "Tamim al-Dari → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 4944"], "nodes": [("tamim", 4), ("abu_dawud", 0)]},
            {"label": "Tamim al-Dari → Al-Nasa'i", "path_count": 10, "sources": ["Sunan al-Nasa'i 4197"], "nodes": [("tamim", 4), ("nasai", 0)]},
        ],
    },

    # ==================================================================
    # 44. Celui qui nous trompe n'est pas des nôtres
    # ==================================================================
    {
        "id": "h_ghish",
        "rank": 44,
        "matn": "مَنْ غَشَّنَا فَلَيْسَ مِنَّا",
        "matn_translation_fr": "Celui qui nous trompe (dans le commerce) n'est pas des nôtres.",
        "title_fr": "La tromperie (Man ghashshana)",
        "title_ar": "من غشنا فليس منا",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — commerce et trahison de la confiance",
        "validation_sources": ["Sahih Muslim 101", "Sunan Abi Dawud 3452", "Musnad Ahmad 2/417"],
        "thematic_category": "Commerce & honnêteté",
        "keywords": ["ghish", "tromperie", "commerce"],
        "turuq": [
            {"label": "Abu Hurayra → Muslim", "path_count": 18, "sources": ["Sahih Muslim 101"], "nodes": [("abu_hurayra", 4), ("muslim", 0)]},
            {"label": "Abdullah ibn Umar → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 3452"], "nodes": [("abdullah_umar", 4), ("abu_dawud", 0)]},
            {"label": "Abu Hurayra → Ahmad", "path_count": 14, "sources": ["Musnad Ahmad 2/417"], "nodes": [("abu_hurayra", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 45. La main d'en haut vaut mieux que la main d'en bas
    # ==================================================================
    {
        "id": "h_yad",
        "rank": 45,
        "matn": "الْيَدُ الْعُلْيَا خَيْرٌ مِنَ الْيَدِ السُّفْلَى",
        "matn_translation_fr": "La main qui donne est meilleure que la main qui reçoit.",
        "title_fr": "La main d'en haut (Al-Yad al-'Ulya)",
        "title_ar": "اليد العليا خير من اليد السفلى",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — éthique du don et de la générosité",
        "validation_sources": ["Sahih al-Bukhari 1429", "Sahih Muslim 1033", "Sunan al-Nasa'i 2534"],
        "thematic_category": "Générosité",
        "keywords": ["sadaqa", "generosite", "don"],
        "turuq": [
            {"label": "Hakim ibn Hizam → Al-Bukhari", "path_count": 20, "sources": ["Sahih al-Bukhari 1429"], "nodes": [("hakim_hizam", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 17, "sources": ["Sahih Muslim 1033"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Nasa'i", "path_count": 11, "sources": ["Sunan al-Nasa'i 2534"], "nodes": [("abu_hurayra", 4), ("nasai", 0)]},
        ],
    },

    # ==================================================================
    # 46. Les croyants sont comme un édifice
    # ==================================================================
    {
        "id": "h_bunyan",
        "rank": 46,
        "matn": "الْمُؤْمِنُ لِلْمُؤْمِنِ كَالْبُنْيَانِ يَشُدُّ بَعْضُهُ بَعْضًا",
        "matn_translation_fr": "Le croyant est pour le croyant comme un édifice dont les parties se soutiennent mutuellement.",
        "title_fr": "Les croyants comme un édifice (Al-Bunyan)",
        "title_ar": "المؤمن للمؤمن كالبنيان",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — solidarité de la communauté",
        "validation_sources": ["Sahih al-Bukhari 481", "Sahih Muslim 2585", "Sunan al-Tirmidhi 1928"],
        "thematic_category": "Solidarité",
        "keywords": ["mumin", "solidarite", "bunyan"],
        "turuq": [
            {"label": "Abu Musa → Al-Bukhari", "path_count": 22, "sources": ["Sahih al-Bukhari 481"], "nodes": [("abu_musa", 4), ("bukhari", 0)]},
            {"label": "Abu Musa → Muslim", "path_count": 18, "sources": ["Sahih Muslim 2585"], "nodes": [("abu_musa", 4), ("muslim", 0)]},
            {"label": "Abu Hurayra → Al-Tirmidhi", "path_count": 13, "sources": ["Sunan al-Tirmidhi 1928"], "nodes": [("abu_hurayra", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 47. Quiconque imite un peuple en fait partie
    # ==================================================================
    {
        "id": "h_tashabbuh",
        "rank": 47,
        "matn": "مَنْ تَشَبَّهَ بِقَوْمٍ فَهُوَ مِنْهُمْ",
        "matn_translation_fr": "Quiconque imite un peuple finit par en faire partie.",
        "title_fr": "Imiter un peuple (Man tashabbaha)",
        "title_ar": "من تشبه بقوم فهو منهم",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — identité et appartenance",
        "validation_sources": ["Sunan Abi Dawud 4031", "Musnad Ahmad 2/50"],
        "thematic_category": "Identité",
        "keywords": ["tashabbuh", "imitation", "identite"],
        "turuq": [
            {"label": "Abdullah ibn Umar → Abu Dawud", "path_count": 16, "sources": ["Sunan Abi Dawud 4031"], "nodes": [("abdullah_umar", 4), ("abu_dawud", 0)]},
            {"label": "Abdullah ibn Umar → Ahmad", "path_count": 14, "sources": ["Musnad Ahmad 2/50"], "nodes": [("abdullah_umar", 4), ("ahmad", 0)]},
            {"label": "Abu Hurayra → Al-Tabarani", "path_count": 10, "sources": ["Al-Mu'jam al-Awsat (al-Tabarani)"], "nodes": [("abu_hurayra", 4), ("tabarani", 0)]},
        ],
    },

    # ==================================================================
    # 48. Quiconque dit la ilaha illa Allah avec sincérité entre au Paradis
    # ==================================================================
    {
        "id": "h_kalima",
        "rank": 48,
        "matn": "مَنْ قَالَ لَا إِلَهَ إِلَّا اللَّهُ مُخْلِصًا مِنْ قَلْبِهِ دَخَلَ الْجَنَّةَ",
        "matn_translation_fr": "Quiconque dit « Il n'y a de divinité qu'Allah » sincèrement, du fond du cœur, entrera au Paradis.",
        "title_fr": "La parole de l'unicité (Kalimat al-Tawhid)",
        "title_ar": "من قال لا إله إلا الله مخلصا دخل الجنة",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — mérites de l'unicité divine",
        "validation_sources": ["Musnad Ahmad 5/239", "Sunan al-Tirmidhi 2639", "Mustadrak al-Hakim 1/70"],
        "thematic_category": "Dogme (Tawhid)",
        "keywords": ["tawhid", "kalima", "janna"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Hakim", "path_count": 20, "sources": ["Mustadrak al-Hakim 1/70"], "nodes": [("abu_hurayra", 4), ("hakim", 0)]},
            {"label": "Mu'adh → Ahmad", "path_count": 18, "sources": ["Musnad Ahmad 5/239"], "nodes": [("muadh", 4), ("ahmad", 0)]},
            {"label": "Abu Dharr → Al-Tirmidhi", "path_count": 10, "sources": ["Sunan al-Tirmidhi 2639"], "nodes": [("abu_dharr", 4), ("tirmidhi", 0)]},
        ],
    },

    # ==================================================================
    # 49. En toute foie vivante il y a une récompense
    # ==================================================================
    {
        "id": "h_kabad",
        "rank": 49,
        "matn": "فِي كُلِّ كَبِدٍ رَطْبٍ أَجْرٌ",
        "matn_translation_fr": "Envers toute foie vivante (tout être vivant) il y a une récompense.",
        "title_fr": "Le mérite envers les animaux (Kabad Rattb)",
        "title_ar": "في كل كبد رطب أجر",
        "tawatur_type": "ma'nawi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Ma'nawi — bonté envers les créatures",
        "validation_sources": ["Sahih al-Bukhari 2363", "Sahih Muslim 2244", "Musnad Ahmad 2/375"],
        "thematic_category": "Miséricorde envers les créatures",
        "keywords": ["kabad", "animaux", "rahma"],
        "turuq": [
            {"label": "Abu Hurayra → Al-Bukhari", "path_count": 18, "sources": ["Sahih al-Bukhari 2363"], "nodes": [("abu_hurayra", 4), ("bukhari", 0)]},
            {"label": "Abdullah ibn Umar → Muslim", "path_count": 15, "sources": ["Sahih Muslim 2244"], "nodes": [("abdullah_umar", 4), ("muslim", 0)]},
            {"label": "Abu Dharr → Ahmad", "path_count": 10, "sources": ["Musnad Ahmad 2/375"], "nodes": [("abu_dharr", 4), ("ahmad", 0)]},
        ],
    },

    # ==================================================================
    # 50. Le meilleur d'entre vous est celui qui apprend le Coran
    # ==================================================================
    {
        "id": "h_quran",
        "rank": 50,
        "matn": "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
        "matn_translation_fr": "Le meilleur d'entre vous est celui qui apprend le Coran et l'enseigne.",
        "title_fr": "Apprendre et enseigner le Coran (Khayrukum)",
        "title_ar": "خيركم من تعلم القرآن وعلمه",
        "tawatur_type": "lafzi",
        "obedience": "commun",
        "degree_fr": "Mutawatir Lafzi — mérite de l'étude du Coran",
        "validation_sources": ["Sahih al-Bukhari 5027", "Sunan Abi Dawud 1452", "Sunan al-Tirmidhi 2907"],
        "thematic_category": "Coran",
        "keywords": ["quran", "enseignement", "khayr"],
        "turuq": [
            {"label": "Uthman → Al-Bukhari", "path_count": 24, "sources": ["Sahih al-Bukhari 5027"], "nodes": [("uthman", 4), ("bukhari", 0)]},
            {"label": "Ali → Al-Tirmidhi", "path_count": 16, "sources": ["Sunan al-Tirmidhi 2907"], "nodes": [("ali", 4), ("tirmidhi", 0)]},
            {"label": "Ibn Mas'ud → Abu Dawud", "path_count": 12, "sources": ["Sunan Abi Dawud 1452"], "nodes": [("ibn_masud", 4), ("abu_dawud", 0)]},
        ],
    },
]
