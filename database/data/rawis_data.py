# -*- coding: utf-8 -*-
"""Registre des narrateurs (Rijal) — Sahaba, Tabi'un, Imams, compilateurs.

Chaque entrée est un dictionnaire prêt pour ``Rawiy(**entry)``.
Les dates sont données en années hégiriennes (AH), approximatives.

Chaque narrateur porte :
- ``notes``  : le grade (Jarh wa Ta'dil) tel qu'attesté dans la littérature ;
- ``sources``: les ouvrages de Rijal classiques qui traitent de ce narrateur
  (référence AUX ŒUVRES, sans pagination inventée).

Convention de grade : Sahaba = « 'adala générale » (ta'dil d'ensemble) ;
Shia = sources Rijal imamites (al-Najashi, al-Kashi, al-Tusi, al-Hilli).
"""

SAHABA_SRC = [
    "Al-Isaba fi Tamyiz al-Sahaba (Ibn Hajar)",
    "Al-Isti'ab fi Ma'rifat al-Ashab (Ibn Abd al-Barr)",
    "Usd al-Ghaba (Ibn al-Athir)",
]

SUNNI_RIJAL = [
    "Tahdhib al-Tahdhib (Ibn Hajar)",
    "Taqrib al-Tahdhib (Ibn Hajar)",
    "Siyar A'lam al-Nubala' (al-Dhahabi)",
]

SHIA_RIJAL = [
    "Rijal al-Najashi",
    "Rijal al-Tusi",
    "Rijal al-Kashi",
    "Fihrist al-Tusi",
]

TAFSIR_RIJAL = [
    "Tahdhib al-Tahdhib (Ibn Hajar)",
    "Taqrib al-Tahdhib (Ibn Hajar)",
    "Siyar A'lam al-Nubala' (al-Dhahabi)",
    "Al-Tabaqat al-Kubra (Ibn Sa'd)",
]


def _r(id, name, kunya=None, nisba=None, tabaqa=None,
       reliability="thiqa", birth=None, death=None,
       grade=None, sources=None):
    return id, {
        "id": id,
        "name": name,
        "kunya": kunya,
        "nisba": nisba,
        "tabaqa": tabaqa,
        "reliability": reliability,
        "birth_date": birth,
        "death_date": death,
        "sources": list(sources) if sources else [],
        "notes": grade,
    }


COMPANION = "Compagnon (Sahaba) — 'adala générale (ta'dil d'ensemble)"
COMPANION_F = "Compagnonne (Sahabiyya) — 'adala générale (ta'dil d'ensemble)"


RAWIS = dict([
    # ------------------------------------------------------------------
    # Compagnons (Sahaba) — niveau terminal des chaînes
    # ------------------------------------------------------------------
    _r("umar", "Omar ibn al-Khattab", "Abu Hafs", "Al-Qurashi", "Sahaba", death=23, grade=COMPANION, sources=SAHABA_SRC),
    _r("ali", "Ali ibn Abi Talib", "Abu al-Hasan", "Al-Hashimi", "Sahaba", death=40, grade=COMPANION + " ; Imam et 4e calife", sources=SAHABA_SRC),
    _r("aisha", "Aisha bint Abi Bakr", "Umm Abdullah", None, "Sahabiyat", death=58, grade=COMPANION_F + " ; référence majeure du fiqh et du hadith", sources=SAHABA_SRC),
    _r("abu_bakr", "Abu Bakr al-Siddiq", "Abu Bakr", "Al-Qurashi", "Sahaba", death=13, grade=COMPANION + " ; 1er calife", sources=SAHABA_SRC),
    _r("uthman", "Uthman ibn Affan", "Abu Amr", "Al-Umawi", "Sahaba", death=35, grade=COMPANION + " ; 3e calife", sources=SAHABA_SRC),
    _r("ibn_abbas", "Abdullah ibn Abbas", "Abu al-Abbas", "Al-Qurashi", "Sahaba", death=68, grade=COMPANION + " ; 'Tarjuman al-Qur'an', maître du tafsir", sources=SAHABA_SRC),
    _r("abu_hurayra", "Abu Hurayra al-Dawsi", "Abu Hurayra", "Al-Dawsi", "Sahaba", death=59, grade=COMPANION + " ; le plus prolifique des transmetteurs", sources=SAHABA_SRC),
    _r("anass", "Anas ibn Malik", "Abu Hamza", "Al-Ansari", "Sahaba", death=93, grade=COMPANION + " ; dernier des grands Compagnons de Bassora", sources=SAHABA_SRC),
    _r("hudhayfa", "Hudhayfa ibn al-Yaman", "Abu Abdullah", "Al-Absi", "Sahaba", death=36, grade=COMPANION + " ; dépositaire des traditions sur les épreuves (fitan)", sources=SAHABA_SRC),
    _r("ibn_masud", "Abdullah ibn Mas'ud", "Abu Abd al-Rahman", "Al-Hudhali", "Sahaba", death=32, grade=COMPANION + " ; grand récitateur et juriste de Koufa", sources=SAHABA_SRC),
    _r("jabir", "Jabir ibn Abdullah", "Abu Abdullah", "Al-Ansari", "Sahaba", death=78, grade=COMPANION + " ; dernière autorité de Médine", sources=SAHABA_SRC),
    _r("abu_saeed", "Abu Sa'id al-Khudri", "Abu Sa'id", "Al-Khudri", "Sahaba", death=74, grade=COMPANION, sources=SAHABA_SRC),
    _r("zayd_arqam", "Zayd ibn Arqam", "Abu Ammar", "Al-Ansari", "Sahaba", death=66, grade=COMPANION, sources=SAHABA_SRC),
    _r("burayda", "Burayda ibn al-Husayb", "Abu al-Husayb", "Al-Aslami", "Sahaba", death=63, grade=COMPANION, sources=SAHABA_SRC),
    _r("abu_dharr", "Abu Dharr al-Ghifari", "Abu Dharr", "Al-Ghifari", "Sahaba", death=31, grade=COMPANION + " ; ascète (zahid) célèbre", sources=SAHABA_SRC),
    _r("salman", "Salman al-Farisi", "Abu Abdullah", "Al-Farisi", "Sahaba", death=33, grade=COMPANION, sources=SAHABA_SRC),
    _r("saad", "Sa'd ibn Abi Waqqas", "Abu Ishaq", "Al-Qurashi", "Sahaba", death=55, grade=COMPANION + " ; un des dix promis au Paradis", sources=SAHABA_SRC),
    _r("abdullah_umar", "Abdullah ibn Umar", "Abu Abd al-Rahman", "Al-Qurashi", "Sahaba", death=73, grade=COMPANION + " ; référence en fiqh et ascèse", sources=SAHABA_SRC),
    _r("abu_musa", "Abu Musa al-Ash'ari", "Abu Musa", "Al-Ash'ari", "Sahaba", death=44, grade=COMPANION, sources=SAHABA_SRC),
    _r("mughira", "Al-Mughira ibn Shu'ba", "Abu Isa", "Al-Thaqafi", "Sahaba", death=50, grade=COMPANION, sources=SAHABA_SRC),
    _r("irbad", "Irbad ibn Sariya", "Abu al-Najm", "Al-Sulami", "Sahaba", death=75, grade=COMPANION + " ; connu pour le hadith al-maw'iza", sources=SAHABA_SRC),
    _r("thawban", "Thawban ibn Bujdud", "Abu Abdullah", None, "Sahaba", death=54, grade=COMPANION + " ; affranchi du Prophète", sources=SAHABA_SRC),
    _r("abu_umama", "Abu Umama al-Bahili", "Abu Umama", "Al-Bahili", "Sahaba", death=86, grade=COMPANION, sources=SAHABA_SRC),
    _r("muadh", "Mu'adh ibn Jabal", "Abu Abd al-Rahman", "Al-Ansari", "Sahaba", death=18, grade=COMPANION + " ; envoyé au Yémen, grand juriste", sources=SAHABA_SRC),
    _r("ubada", "Ubada ibn al-Samit", "Abu al-Walid", "Al-Ansari", "Sahaba", death=34, grade=COMPANION, sources=SAHABA_SRC),
    _r("abu_ayyub", "Abu Ayyub al-Ansari", "Abu Ayyub", "Al-Ansari", "Sahaba", death=52, grade=COMPANION, sources=SAHABA_SRC),
    _r("abdullah_amr", "Abdullah ibn Amr ibn al-As", "Abu Muhammad", "Al-Qurashi", "Sahaba", death=65, grade=COMPANION + " ; détenteur d'un codex écrit (al-Sahifa al-sadiqa)", sources=SAHABA_SRC),
    _r("wathila", "Wathila ibn al-Asqa", "Abu al-Asqa", "Al-Laythi", "Sahaba", death=85, grade=COMPANION, sources=SAHABA_SRC),
    _r("imran", "Imran ibn Husayn", "Abu Nujayd", "Al-Khuza'i", "Sahaba", death=52, grade=COMPANION, sources=SAHABA_SRC),
    _r("abu_qatada", "Abu Qatada al-Ansari", "Abu Qatada", "Al-Ansari", "Sahaba", death=54, grade=COMPANION, sources=SAHABA_SRC),
    _r("sahl", "Sahl ibn Sa'd al-Sa'idi", "Abu Abbas", "Al-Ansari", "Sahaba", death=91, grade=COMPANION, sources=SAHABA_SRC),
    _r("umm_atiyya", "Umm Atiyya al-Ansariyya", "Umm Atiyya", "Al-Ansari", "Sahabiyat", death=70, grade=COMPANION_F, sources=SAHABA_SRC),
    _r("umm_salama", "Umm Salama", "Umm Salama", "Al-Makhzumiyya", "Sahabiyat", death=62, grade=COMPANION_F + " ; épouse du Prophète", sources=SAHABA_SRC),
    _r("samura", "Samura ibn Jundub", "Abu Sulayman", "Al-Fazari", "Sahaba", death=60, grade=COMPANION, sources=SAHABA_SRC),
    _r("abu_barza", "Abu Barza al-Aslami", "Abu Barza", "Al-Aslami", "Sahaba", death=65, grade=COMPANION, sources=SAHABA_SRC),
    _r("rafi_bin_khadij", "Rafi' ibn Khadij", "Abu Khadij", "Al-Ansari", "Sahaba", death=74, grade=COMPANION, sources=SAHABA_SRC),
    _r("abu_lubaba", "Abu Lubaba al-Ansari", "Abu Lubaba", "Al-Ansari", "Sahaba", death=40, grade=COMPANION, sources=SAHABA_SRC),
    _r("tamim", "Tamim ibn Aws al-Dari", "Abu Ruqayya", "Al-Dari", "Sahaba", death=40, grade=COMPANION + " ; narrateur du hadith al-nasiha", sources=SAHABA_SRC),
    _r("hakim_hizam", "Hakim ibn Hizam", "Abu Khaled", "Al-Qurashi", "Sahaba", death=54, grade=COMPANION, sources=SAHABA_SRC),
    _r("jarir", "Jarir ibn Abdullah al-Bajali", "Abu Amr", "Al-Bajali", "Sahaba", death=51, grade=COMPANION, sources=SAHABA_SRC),

    # ------------------------------------------------------------------
    # Tabi'un et générations suivantes (intermédiaires)
    # ------------------------------------------------------------------
    _r("al_zuhri", "Muhammad ibn Muslim al-Zuhri", "Abu Bakr", "Al-Zuhri", "Tabi' al-Tabi'in", death=124, grade="Thiqa, faqih hafiz, imam — codificateur du hadith", sources=SUNNI_RIJAL),
    _r("qatada", "Qatada ibn Di'ama", "Abu al-Khattab", "Al-Sadusi", "Tabi'in", death=117, grade="Thiqa, hafiz ; savant de Bassora ; connu pour al-tadlis", sources=SUNNI_RIJAL),
    _r("hassan_basri", "Al-Hassan al-Basri", "Abu Sa'id", "Al-Basri", "Tabi'in", death=110, grade="Thiqa, imam, faqih ; connu pour al-irsal et al-tadlis", sources=SUNNI_RIJAL),
    _r("nafi", "Nafi' mawla Ibn Umar", "Abu Abdullah", None, "Tabi'in", death=117, grade="Thiqa, imam ; chaîne de Nafi' < Ibn Umar (la 'chaîne d'or')", sources=SUNNI_RIJAL),
    _r("urwa", "Urwa ibn al-Zubayr", "Abu Abdullah", "Al-Asadi", "Tabi'in", death=94, grade="Thiqa, faqih ; un des sept juristes de Médine", sources=SUNNI_RIJAL),
    _r("amr_dinar", "Amr ibn Dinar", "Abu Muhammad", "Al-Makki", "Tabi'in", death=126, grade="Thiqa, hafiz", sources=SUNNI_RIJAL),
    _r("amash", "Sulayman ibn Mihran al-A'mash", "Abu Muhammad", "Al-Asadi", "Tabi'in", death=148, grade="Thiqa, hafiz, imam ; réputé pour al-tadlis", sources=SUNNI_RIJAL),
    _r("ataa", "Ata' ibn Abi Rabah", "Abu Muhammad", "Al-Makki", "Tabi'in", death=114, grade="Thiqa, faqih, mufassir ; grand mufti de La Mecque", sources=SUNNI_RIJAL),
    _r("mujahid", "Mujahid ibn Jabr", "Abu al-Hajjaj", "Al-Makki", "Tabi'in", death=104, grade="Thiqa, imam en tafsir", sources=TAFSIR_RIJAL),
    _r("abu_ishaq_sabii", "Abu Ishaq al-Sabi'i", "Abu Ishaq", "Al-Hamdani", "Tabi'in", death=127, grade="Thiqa, hafiz ; ikhtilat en fin de vie et al-tadlis", sources=SUNNI_RIJAL),
    _r("shabi", "Al-Sha'bi", "Abu Amr", "Al-Hamdani", "Tabi'in", death=103, grade="Thiqa, faqih, hafiz ; grand savant de Koufa", sources=SUNNI_RIJAL),
    _r("ibn_sirin", "Muhammad ibn Sirin", "Abu Bakr", "Al-Basri", "Tabi'in", death=110, grade="Thiqa, imam ; connu pour al-irsal et sa science de l'interprétation des rêves", sources=SUNNI_RIJAL),
    _r("yahya_ansari", "Yahya ibn Sa'id al-Ansari", "Abu Sa'id", "Al-Ansari", "Tabi'in", death=143, grade="Thiqa, hafiz ; qadi de Médine", sources=SUNNI_RIJAL),
    _r("awzai", "Al-Awza'i", "Abu Amr", "Al-Dimashqi", "Tabi' al-Tabi'in", death=157, grade="Thiqa, imam ; faqih du Levant", sources=SUNNI_RIJAL),
    _r("thawri", "Sufyan al-Thawri", "Abu Abdullah", "Al-Thawri", "Tabi' al-Tabi'in", death=161, grade="Thiqa, hafiz — 'Amir al-Mu'minin fi al-Hadith'", sources=SUNNI_RIJAL),
    _r("laith", "Al-Layth ibn Sa'd", "Abu al-Harith", "Al-Fahmi", "Tabi' al-Tabi'in", death=175, grade="Thiqa, imam, faqih d'Égypte", sources=SUNNI_RIJAL),
    _r("shuba", "Shu'ba ibn al-Hajjaj", "Abu Bistam", "Al-Ataki", "Tabi' al-Tabi'in", death=160, grade="Thiqa, hafiz — 'Amir al-Mu'minin fi al-Hadith' ; fondateur de la critique des Rijal", sources=SUNNI_RIJAL),
    _r("bakr_muzani", "Bakr ibn Abdullah al-Muzani", "Abu Abdullah", "Al-Muzani", "Tabi'in", death=106, grade="Thiqa, faqih ; autorité en dogme", sources=SUNNI_RIJAL),
    _r("mansur", "Mansur ibn al-Mu'tamir", "Abu al-Hasan", "Al-Kufi", "Tabi' al-Tabi'in", death=132, grade="Thiqa, hafiz", sources=SUNNI_RIJAL),
    _r("habib", "Habib ibn Abi Thabit", "Abu Yahya", "Al-Kufi", "Tabi'in", death=119, grade="Thiqa ; ikhtilat tardif et al-tadlis", sources=SUNNI_RIJAL),
    _r("qais", "Qays ibn Abi Hazim", "Abu Abd Allah", "Al-Bajali", "Tabi'in", death=120, grade="Thiqa", sources=SUNNI_RIJAL),
    _r("makhul", "Makhul al-Shami", "Abu Abdullah", "Al-Dimashqi", "Tabi'in", death=112, grade="Thiqa, faqih ; al-tadlis et irsal sur l'identification des Compagnons", sources=SUNNI_RIJAL),
    _r("said_musayyib", "Sa'id ibn al-Musayyib", "Abu Muhammad", "Al-Makhzumi", "Tabi'in", death=94, grade="Thiqa, imam ; chef des sept juristes de Médine", sources=SUNNI_RIJAL),
    _r("ibrahim_nakhai", "Ibrahim al-Nakha'i", "Abu Imran", "Al-Nakha'i", "Tabi'in", death=96, grade="Thiqa, faqih de Koufa ; transmet surtout en mursal", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Imams chiites (intermédiaires majeurs pour les asanid chiites)
    # ------------------------------------------------------------------
    _r("zayd_ali", "Zayd ibn Ali", "Abu al-Husayn", "Al-Hashimi", "Imam", death=122, grade="Thiqa selon les deux écoles ; Imam fondateur du zaydisme", sources=SHIA_RIJAL),
    _r("baqir", "Muhammad al-Baqir", "Abu Ja'far", "Al-Hashimi", "Imam", death=114, grade="Imam ; thiqa (ma'sum pour les imamites), respecté par les sunnites", sources=SHIA_RIJAL),
    _r("sadiq", "Ja'far al-Sadiq", "Abu Abdullah", "Al-Hashimi", "Imam", death=148, grade="Imam ; thiqa ; immense autorité, maître d'Abu Hanifa et Malik", sources=SHIA_RIJAL),
    _r("kazim", "Musa al-Kazim", "Abu al-Hasan", "Al-Hashimi", "Imam", death=183, grade="Imam ; thiqa", sources=SHIA_RIJAL),
    _r("rida", "Ali al-Rida", "Abu al-Hasan", "Al-Hashimi", "Imam", death=203, grade="Imam ; thiqa", sources=SHIA_RIJAL),

    # ------------------------------------------------------------------
    # Compilateurs sunnites
    # ------------------------------------------------------------------
    _r("bukhari", "Muhammad ibn Ismail al-Bukhari", "Abu Abdullah", "Al-Bukhari", "Muhaddith", birth=194, death=256, grade="Imam, hafiz — 'Amir al-Mu'minin fi al-Hadith'", sources=SUNNI_RIJAL),
    _r("muslim", "Muslim ibn al-Hajjaj", "Abu al-Husayn", "Al-Naysaburi", "Muhaddith", birth=204, death=261, grade="Imam, hafiz", sources=SUNNI_RIJAL),
    _r("abu_dawud", "Abu Dawud al-Sijistani", "Abu Dawud", "Al-Sijistani", "Muhaddith", birth=202, death=275, grade="Imam, hafiz ; auteur des Sunan", sources=SUNNI_RIJAL),
    _r("tirmidhi", "Abu Isa al-Tirmidhi", "Abu Isa", "Al-Tirmidhi", "Muhaddith", birth=209, death=279, grade="Imam, hafiz ; auteur de la Jami' (Sunan)", sources=SUNNI_RIJAL),
    _r("nasai", "Ahmad ibn Shu'ayb al-Nasa'i", "Abu Abd al-Rahman", "Al-Nasa'i", "Muhaddith", birth=215, death=303, grade="Imam, hafiz ; auteur des Sunan", sources=SUNNI_RIJAL),
    _r("ibn_majah", "Muhammad ibn Yazid Ibn Majah", "Abu Abdullah", "Al-Qazwini", "Muhaddith", birth=209, death=273, grade="Hafiz ; quelques critiques sur la Sunan (la plus faible des six)", sources=SUNNI_RIJAL),
    _r("ahmad", "Ahmad ibn Hanbal", "Abu Abdullah", "Al-Shaybani", "Imam", birth=164, death=241, grade="Imam, hafiz ; fondateur du madhhab hanbalite", sources=SUNNI_RIJAL),
    _r("darimi", "Al-Darimi", "Abu Muhammad", "Al-Samarqandi", "Muhaddith", birth=181, death=255, grade="Imam, hafiz ; auteur du Musnad al-Darimi", sources=SUNNI_RIJAL),
    _r("malik", "Malik ibn Anas", "Abu Abdullah", "Al-Asbahi", "Imam", birth=93, death=179, grade="Imam — 'Imam Dar al-Hijra' ; fondateur du madhhab malikite", sources=SUNNI_RIJAL),
    _r("hakim", "Al-Hakim al-Naysaburi", "Abu Abdullah", "Al-Naysaburi", "Muhaddith", birth=321, death=405, grade="Imam, hafiz ; connu pour sa tolérance (tasahhul) dans le Mustadrak", sources=SUNNI_RIJAL),
    _r("tabarani", "Al-Tabarani", "Abu al-Qasim", "Al-Lakhmi", "Muhaddith", birth=260, death=360, grade="Imam, hafiz ; auteur des trois Mu'jam", sources=SUNNI_RIJAL),
    _r("bayhaqi", "Al-Bayhaqi", "Abu Bakr", "Al-Bayhaqi", "Muhaddith", birth=384, death=458, grade="Imam, hafiz ; auteur des Sunan al-Kubra", sources=SUNNI_RIJAL),
    _r("shafii", "Muhammad ibn Idris al-Shafi'i", "Abu Abdullah", "Al-Shafi'i", "Imam", birth=150, death=204, grade="Imam ; fondateur du madhhab shafi'ite", sources=SUNNI_RIJAL),
    _r("humaydi", "Al-Humaydi", "Abu Bakr", "Al-Makki", "Muhaddith", death=219, grade="Thiqa, hafiz ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
    _r("ishaq_rahawayh", "Ishaq ibn Rahawayh", "Abu Ya'qub", "Al-Marwazi", "Muhaddith", birth=161, death=238, grade="Imam, hafiz", sources=SUNNI_RIJAL),
    _r("abd_razzaq", "Abd al-Razzaq al-San'ani", "Abu Bakr", "Al-San'ani", "Muhaddith", birth=126, death=211, grade="Thiqa, hafiz ; ikhtilat tardif", sources=SUNNI_RIJAL),
    _r("ibn_abi_shayba", "Ibn Abi Shayba", "Abu Bakr", "Al-Kufi", "Muhaddith", birth=159, death=235, grade="Thiqa, hafiz ; auteur du Musannaf", sources=SUNNI_RIJAL),
    _r("waki", "Waki' ibn al-Jarrah", "Abu Sufyan", "Al-Kufi", "Muhaddith", birth=129, death=197, grade="Thiqa, hafiz, imam ; professeur d'Ahmad ibn Hanbal", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Compilateurs chiites
    # ------------------------------------------------------------------
    _r("kulayni", "Muhammad ibn Ya'qub al-Kulayni", "Abu Ja'far", "Al-Razi", "Muhaddith", birth=258, death=329, grade="Thiqa, imam ; compilateur du al-Kafi", sources=SHIA_RIJAL),
    _r("saduq", "Ibn Babawayh al-Qummi (Al-Saduq)", "Abu Ja'far", "Al-Qummi", "Muhaddith", birth=306, death=381, grade="Thiqa, hafiz ; auteur de Man la yahduruhu al-Faqih", sources=SHIA_RIJAL),
    _r("tusi", "Al-Shaykh al-Tusi", "Abu Ja'far", "Al-Tusi", "Muhaddith", birth=385, death=460, grade="Imam ; auteur de Tahdhib al-Ahkam et Istibsar et des deux Rijal", sources=SHIA_RIJAL),
    _r("mufid", "Al-Shaykh al-Mufid", "Abu Abdullah", "Al-Baghdadi", "Mujtahid", birth=336, death=413, grade="Faqih, mutakallim ; juriste bagdadien", sources=SHIA_RIJAL),
    _r("ayyashi", "Al-Ayyashi", "Abu al-Nadr", "Al-Samarqandi", "Muhaddith", death=320, grade="Thiqa ; auteur du Tafsir et Basa'ir al-Darajat", sources=SHIA_RIJAL),
    _r("qummi", "Ali ibn Ibrahim al-Qummi", "Abu al-Hasan", "Al-Qummi", "Muhaddith", death=307, grade="Thiqa ; auteur du Tafsir al-Qummi", sources=SHIA_RIJAL),
    _r("numani", "Ibn Abi Zaynab al-Nu'mani", "Abu Abdullah", "Al-Nu'mani", "Muhaddith", death=360, grade="Thiqa ; auteur de al-Ghayba (al-Nu'mani)", sources=SHIA_RIJAL),
    _r("radi", "Al-Sharif al-Radi", "Abu al-Hasan", "Al-Musawi", "Muhaddith", birth=359, death=406, grade="Compilateur du Nahj al-Balagha ; Sharif de Bagdad", sources=SHIA_RIJAL),
])
