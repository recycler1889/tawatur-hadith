# -*- coding: utf-8 -*-
"""Narrateurs intermédiaires (Rijal) issus du dépouillement des asanid.

Ce registre complète ``rawis_data`` et ``rawis_data_extra``. Il rassemble les
transmetteurs intermédiaires (Tabi'un, atba' al-tabi'in, shuyukh des
compilateurs) apparaissant dans les chaînes détaillées consignées dans
``isnad_expansions``.

Conventions identiques à ``rawis_data`` (helper ``_r``, grades + ouvrages
Rijal). Les dates sont en années hégiriennes (AH).
"""

from database.data.rawis_data import _r, SUNNI_RIJAL, TAFSIR_RIJAL

RAWIS_RIJAL = dict([
    # ------------------------------------------------------------------
    # Tabi'un (Tabi'in) — maillons intermédiaires des asanid
    # ------------------------------------------------------------------
    _r("abu_salih", "Abu Salih Dhakwan al-Samman", "Abu Salih", "Al-Madani", "Tabi'in", death=101,
       grade="Thiqa, thabt ; serviteur de Juwairiya, narrateur de nombreuses traditions d'Abu Hurayra",
       sources=SUNNI_RIJAL),
    _r("abu_hasin", "Abu Hasin Uthman ibn Asim al-Asadi", "Abu Hasin", "Al-Asadi", "Tabi'in", death=127,
       grade="Thiqa ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("alqama_waqqas", "Alqama ibn Waqqas al-Laythi", "Abu Muhammad", "Al-Laythi", "Tabi'in", death=86,
       grade="Thiqa ; oncle de Yahya ibn Sa'id al-Ansari", sources=SUNNI_RIJAL),
    _r("muh_ibrahim_taymi", "Muhammad ibn Ibrahim ibn al-Harith al-Taymi", "Abu Abdullah", "Al-Taymi", "Tabi'in", death=120,
       grade="Thiqa, faqih de Médine ; un des juristes de Médine", sources=SUNNI_RIJAL),
    _r("al_hakam_utayba", "Al-Hakam ibn Utayba al-Kindi", "Abu Muhammad", "Al-Kindi", "Tabi'in", death=115,
       grade="Thiqa, faqih, hafiz ; grand juriste de Koufa", sources=SUNNI_RIJAL),
    _r("musab_saad", "Mus'ab ibn Sa'd ibn Abi Waqqas", "Abu Zayd", "Al-Qurashi", "Tabi'in", death=103,
       grade="Thiqa ; fils de Sa'd ibn Abi Waqqas", sources=SUNNI_RIJAL),
    _r("ibn_abi_mulayka", "Abdullah ibn Ubaydullah ibn Abi Mulayka", "Abu Bakr", "Al-Taymi", "Tabi'in", death=117,
       grade="Thiqa, faqih ; qadi de La Mecque", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Atba' al-Tabi'in et shuyukh des compilateurs (intermédiaires)
    # ------------------------------------------------------------------
    _r("abu_awanah", "Abu Awanah al-Waddah ibn Abdullah al-Yashkuri", "Abu Awanah", "Al-Yashkuri",
       "Atba' al-Tabi'in", death=175,
       grade="Thiqa, hafiz ; savant de Wasit et Bassora", sources=SUNNI_RIJAL),
    _r("sufyan_uyayna", "Sufyan ibn Uyayna al-Hilali", "Abu Muhammad", "Al-Hilali", "Tabi' al-Tabi'in", death=198,
       grade="Thiqa, hafiz, imam ; muhaddith de La Mecque", sources=SUNNI_RIJAL),
    _r("yahya_qattan", "Yahya ibn Sa'id al-Qattan", "Abu Sa'id", "Al-Basri", "Tabi' al-Tabi'in", death=198,
       grade="Thiqa, hafiz ; critique renommé des Rijal", sources=SUNNI_RIJAL),
    _r("nafi_umar", "Nafi' ibn Umar ibn Abdullah al-Jumahi", "Abu Abdullah", "Al-Jumahi", "Tabi' al-Tabi'in", death=169,
       grade="Thiqa ; neveu d'Ibn Abi Mulayka", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Shuyukh des compilateurs (maillons précédant le recueil)
    # ------------------------------------------------------------------
    _r("muh_ghubari", "Muhammad ibn Ubayd al-Ghubari", "Abu Abdullah", "Al-Ghubari", "Muhaddith", death=247,
       grade="Thiqa ; shaykh de Muslim", sources=SUNNI_RIJAL),
    _r("musa_minqari", "Musa ibn Ismail al-Minqari", "Abu Salama", "Al-Minqari", "Muhaddith", death=223,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("musaddad", "Musaddad ibn Musarhad al-Asadi", "Abu al-Hasan", "Al-Asadi", "Muhaddith", birth=131, death=228,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("ibn_maslama", "Abdullah ibn Maslama al-Qa'nabi", "Abu Abd al-Rahman", "Al-Harithi", "Muhaddith", death=221,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
    _r("said_abi_maryam", "Sa'id ibn Abi Maryam al-Jumahi", "Abu Muhammad", "Al-Misri", "Muhaddith", death=224,
       grade="Thiqa ; shaykh d'al-Bukhari, qadi d'Égypte", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Tabi'un supplémentaires (révélés par les asanid dépouillés)
    # ------------------------------------------------------------------
    _r("ata_yazid", "Ata ibn Yazid al-Laythi al-Jundai", "Abu Muhammad", "Al-Jundai", "Tabi'in", death=105,
       grade="Thiqa ; narrateur d'Abu Sa'id al-Khudri", sources=SUNNI_RIJAL),
    _r("salim_umar", "Salim ibn Abdullah ibn Umar", "Abu Umar", "Al-Qurashi", "Tabi'in", death=106,
       grade="Thiqa, faqih ; un des sept juristes de Médine, fils d'Ibn Umar", sources=SUNNI_RIJAL),
    _r("abdulrahman_qari", "Abd al-Rahman ibn Abd al-Qari", "Abu Muhammad", "Al-Qari", "Tabi'in", death=80,
       grade="Thiqa ; narrateur de la tradition des ahruf", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Atba' al-tabi'in supplémentaires
    # ------------------------------------------------------------------
    _r("salih_kaysan", "Salih ibn Kaysan al-Madani", "Abu Muhammad", "Al-Madani", "Tabi' al-Tabi'in", death=140,
       grade="Thiqa, hafiz ; autorité sur les traditions d'al-Zuhri", sources=SUNNI_RIJAL),
    _r("ibrahim_saad", "Ibrahim ibn Sa'd ibn Ibrahim ibn Abd al-Rahman ibn Awf", "Abu Ishaq", "Al-Qurashi", "Tabi' al-Tabi'in", death=184,
       grade="Thiqa, hafiz ; shaykh de Médine", sources=SUNNI_RIJAL),
    _r("yunus_ayli", "Yunus ibn Yazid al-Ayli", "Abu Yazid", "Al-Ayli", "Atba' al-Tabi'in", death=159,
       grade="Thiqa ; principal transmetteur d'Ibn Shihab d'Égypte", sources=SUNNI_RIJAL),
    _r("uqayl", "Uqayl ibn Khalid al-Ayli", "Abu Khalid", "Al-Ayli", "Tabi' al-Tabi'in", death=144,
       grade="Thiqa, thabt ; parmi les plus fiables sur al-Zuhri", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Shuyukh de compilateurs supplémentaires
    # ------------------------------------------------------------------
    _r("abdulaziz_umawi", "Abd al-Aziz ibn Abdullah al-Umawi", "Abu al-Qasim", "Al-Madani", "Muhaddith", death=197,
       grade="Thiqa ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("ibn_wahb", "Abdullah ibn Wahb al-Misri", "Abu Muhammad", "Al-Fihri", "Muhaddith", birth=125, death=197,
       grade="Thiqa, faqih ; imam d'Égypte", sources=SUNNI_RIJAL),
    _r("harmala", "Harmala ibn Yahya al-Tujibi", "Abu Hafs", "Al-Misri", "Muhaddith", death=244,
       grade="Thiqa ; shaykh de Muslim", sources=SUNNI_RIJAL),
    _r("said_ufayr", "Sa'id ibn Ufayr al-Misri", "Abu Uthman", "Al-Misri", "Muhaddith", death=199,
       grade="Thiqa ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("yahya_tamimi", "Yahya ibn Yahya al-Tamimi al-Naysaburi", "Abu Zakariyya", "Al-Naysaburi", "Muhaddith", birth=142, death=226,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
    _r("said_mansur", "Sa'id ibn Mansur al-Khurasani", "Abu Uthman", "Al-Marwazi", "Muhaddith", death=227,
       grade="Thiqa, hafiz ; auteur du Sunan", sources=SUNNI_RIJAL),
    _r("amr_naqid", "Amr ibn Muhammad al-Naqid", "Abu Uthman", "Al-Baghdadi", "Muhaddith", death=232,
       grade="Thiqa ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
    _r("zuhayr_harb", "Zuhayr ibn Harb al-Abdi", "Abu Khaythama", "Al-Nasa'i", "Muhaddith", birth=160, death=234,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Deuxième vague — asanid du Ghadir, Thaqalayn, Mash, Ru'ya, Shafa'a
    # ------------------------------------------------------------------
    # Tabi'un et Compagnons intermédiaires
    _r("abu_tufayl", "Amir ibn Wathila al-Laythi al-Kinani", "Abu al-Tufayl", "Al-Kinani", "Tabi'in",
       birth=3, death=110,
       grade="Thiqa ; dernier Compagnon survivant, témoin de Ghadir Khumm", sources=SUNNI_RIJAL),
    _r("salama_kuhayl", "Salama ibn Kuhayl al-Hadrami", "Abu Yahya", "Al-Hadrami", "Tabi'in", death=121,
       grade="Thiqa, thabt ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("shabi", "Amir ibn Shurahbil al-Sha'bi", "Abu Amr", "Al-Hamdani", "Tabi'in", death=104,
       grade="Thiqa, faqih de Koufa ; grand successeur (tabi'i)", sources=SUNNI_RIJAL),
    _r("urwa_mughira", "Urwa ibn al-Mughira ibn Shu'ba", "Abu Ya'fur", "Al-Thaqafi", "Tabi'in", death=60,
       grade="Thiqa ; fils d'al-Mughira ibn Shu'ba", sources=SUNNI_RIJAL),
    _r("abu_salama", "Abu Salama ibn Abd al-Rahman ibn Awf", "Abu Salama", "Al-Qurashi", "Tabi'in", death=94,
       grade="Thiqa, faqih ; un des sept juristes de Médine", sources=SUNNI_RIJAL),
    _r("yazid_hayyan", "Yazid ibn Hayyan al-Taymi", "Abu Hayyan", "Al-Taymi", "Tabi'in", death=90,
       grade="Thiqa ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("abu_hayyan", "Yahya ibn Sa'id ibn Hayyan al-Taymi", "Abu Hayyan", "Al-Taymi", "Tabi'in", death=145,
       grade="Thiqa ; qadi de Koufa", sources=SUNNI_RIJAL),
    _r("atiyya", "Atiyya ibn Sa'd ibn Junada al-Awfi", "Abu al-Hasan", "Al-Awfi", "Tabi'in", death=111,
       grade="Saduq ; chiite, parfois mu'dal (récit de la famille), auteur du tafsir attribué", sources=SUNNI_RIJAL),
    _r("qais", "Qays ibn Abi Hazim al-Bajali", "Abu Abdullah", "Al-Bajali", "Tabi'in", death=97,
       grade="Thiqa ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("ismail_abi_khalid", "Ismail ibn Abi Khalid al-Bajali", "Abu Abdullah", "Al-Bajali", "Tabi'in", death=146,
       grade="Thiqa ; narrateur de Koufa", sources=SUNNI_RIJAL),

    # Atba' al-Tabi'in et shuyukh des compilateurs
    _r("muh_jaafar", "Muhammad ibn Ja'far al-Hudhali", "Abu Abdullah", "Al-Hudhali", "Muhaddith", death=192,
       grade="Thiqa ; surnommé Ghundar, shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("muh_bashshar", "Muhammad ibn Bashshar al-Abdi", "Abu Bakr", "Al-Abdi", "Muhaddith", birth=152, death=252,
       grade="Thiqa, hafiz ; surnommé Bundar, shaykh des six recueils", sources=SUNNI_RIJAL),
    _r("ibn_ulayya", "Ismail ibn Ibrahim ibn Muqsim al-Asadi", "Abu Bishr", "Al-Asadi", "Muhaddith", birth=110,
       death=193,
       grade="Thiqa, hafiz ; Ibn Ulayya, shaykh des deux Sahih", sources=SUNNI_RIJAL),
    _r("hushaym", "Hushaym ibn Bashir al-Wasiti", "Abu Muawiya", "Al-Wasiti", "Muhaddith", birth=104, death=183,
       grade="Thiqa, hafiz ; mugalliq (tadlis connu)", sources=SUNNI_RIJAL),
    _r("muh_fudayl", "Muhammad ibn Fudayl ibn Ghazwan al-Dabbi", "Abu Abd al-Rahman", "Al-Dabbi", "Muhaddith",
       death=195,
       grade="Saduq ; chiite modéré, nombreux hadiths", sources=SUNNI_RIJAL),
    _r("ali_mundhir", "Ali ibn al-Mundhir al-Tawari", "Abu al-Hasan", "Al-Kufi", "Muhaddith", death=256,
       grade="Thiqa ; shaykh d'al-Tirmidhi", sources=SUNNI_RIJAL),
    _r("abu_nuaym", "Al-Fadl ibn Dukayn al-Mula'i", "Abu Nu'aym", "Al-Kufi", "Muhaddith", birth=130, death=219,
       grade="Thiqa, hafiz, thabt ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("zakariyya", "Zakariyya ibn Abi Za'ida al-Hamdani", "Abu Yahya", "Al-Hamdani", "Muhaddith", death=147,
       grade="Thiqa, hafiz ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("khalid_tahhan", "Khalid ibn Mihran al-Hadhdha", "Abu al-Mundhir", "Al-Tahhan", "Muhaddith", birth=110,
       death=183,
       grade="Thiqa, hafiz ; shaykh des deux Sahih", sources=SUNNI_RIJAL),
    _r("amr_awn", "Amr ibn Awn ibn Aus al-Bajali", "Abu Uthman", "Al-Baghdadi", "Muhaddith", death=225,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("shuayb_zuhri", "Shu'ayb ibn Abi Hamza al-Qurashi", "Abu Bishr", "Al-Himsi", "Muhaddith", death=162,
       grade="Thiqa, faqih ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
    _r("abu_yaman", "Al-Hakam ibn Nafi' al-Bahrani", "Abu al-Yaman", "Al-Himsi", "Muhaddith", birth=150, death=222,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),

    # ------------------------------------------------------------------
    # Troisième vague — asanid de la Ru'ya (7435), Nuzul Isa (3448),
    # Mahdi (Abu Dawud 4282) et Shafa'a (Bukhari 99)
    # ------------------------------------------------------------------
    _r("said_maqburi", "Sa'id ibn Abi Sa'id Kaysan al-Maqburi", "Abu Sa'd", "Al-Maqburi", "Tabi' al-Tabi'in",
       death=123, grade="Thiqa ; mourut à Médine, narrateur d'Abu Hurayra", sources=SUNNI_RIJAL),
    _r("amr_abi_amr", "Amr ibn Abi Amr al-Qurashi", "Abu Uthman", "Al-Madani", "Tabi' al-Tabi'in", death=144,
       grade="Thiqa ; mawla al-Muttalib", sources=SUNNI_RIJAL),
    _r("sulayman_bilal", "Sulayman ibn Bilal al-Qurashi", "Abu Muhammad", "Al-Taymi", "Muhaddith", death=172,
       grade="Thiqa ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("abdulaziz_uwaysi", "Abd al-Aziz ibn Abdullah ibn Yahya al-Uwaysi", "Abu al-Qasim", "Al-Madani", "Muhaddith",
       birth=120, death=234, grade="Thiqa ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("abu_shihab", "Abd Rabbih ibn Nafi' al-Hanafi", "Abu Shihab", "Al-Kinani", "Tabi' al-Tabi'in", death=172,
       grade="Saduq ; narrateur de Koufa doté d'erreurs", sources=SUNNI_RIJAL),
    _r("asim_yusuf", "Asim ibn Yusuf al-Yarbu'i", "Abu Amr", "Al-Yarbu'i", "Muhaddith", death=210,
       grade="Thiqa ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("yusuf_musa", "Yusuf ibn Musa al-Qattan al-Razi", "Abu Ya'qub", "Al-Razi", "Muhaddith", birth=162, death=253,
       grade="Thiqa, hafiz ; shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("yaqub_ibrahim", "Ya'qub ibn Ibrahim ibn Sa'd al-Zuhri", "Abu Yusuf", "Al-Madani", "Muhaddith", birth=117,
       death=208, grade="Thiqa ; fils d'Ibrahim ibn Sa'd", sources=SUNNI_RIJAL),
    _r("ishaq_rahawayh", "Ishaq ibn Ibrahim al-Hanzali al-Marwazi", "Abu Ya'qub", "Al-Marwazi", "Muhaddith",
       birth=161, death=238, grade="Thiqa, hafiz, imam ; Ibn Rahawayh, shaykh d'al-Bukhari", sources=SUNNI_RIJAL),
    _r("asim_nujud", "Asim ibn Abi al-Nujud Bahdala al-Asadi", "Abu Bakr", "Al-Asadi", "Tabi' al-Tabi'in",
       death=127, grade="Thiqa ; un des sept récitants, lecteur de Koufa", sources=SUNNI_RIJAL),
    _r("zirr", "Zirr ibn Hubaysh ibn Hubasha al-Asadi", "Abu Maryam", "Al-Asadi", "Tabi'in", death=81,
       grade="Thiqa ; grand narrateur de Koufa, rapporta d'Ibn Mas'ud", sources=SUNNI_RIJAL),
    _r("umar_ubayd", "Umar ibn Ubayd al-Tanafisi al-Tanafisi", "Abu Hafs", "Al-Kufi", "Muhaddith", death=185,
       grade="Thiqa ; shaykh autodidacte de Koufa", sources=SUNNI_RIJAL),
    _r("abu_bakr_ayyash", "Abu Bakr ibn Ayyash al-Asadi", "Abu Bakr", "Al-Asadi", "Muhaddith", birth=95, death=193,
       grade="Thiqa, hafiz ; dernier grand mouqri de Koufa", sources=SUNNI_RIJAL),
    _r("sufyan_thawri", "Sufyan ibn Sa'id ibn Masruq al-Thawri", "Abu Abdullah", "Al-Thawri", "Muhaddith",
       birth=97, death=161, grade="Thiqa, hafiz ; amir al-mu'minin fi al-hadith", sources=SUNNI_RIJAL),
    _r("ubaydullah_musa", "Ubaydullah ibn Musa al-Absi", "Abu Muhammad", "Al-Absi", "Muhaddith", birth=120,
       death=213, grade="Thiqa, hafiz ; shaykh de Koufa", sources=SUNNI_RIJAL),
    _r("zaida", "Za'ida ibn Qudama al-Thaqafi", "Abu al-Salt", "Al-Thaqafi", "Muhaddith", birth=110, death=161,
       grade="Thiqa, hafiz ; narrateur de Koufa", sources=SUNNI_RIJAL),
    _r("fitr_khalifa", "Fitr ibn Khalifa al-Makhzumi", "Abu Bakr", "Al-Makhzumi", "Muhaddith", death=153,
       grade="Saduq ; chiite, ses hadiths sont acceptés", sources=SUNNI_RIJAL),
    _r("abu_kuraib", "Muhammad ibn al-Ala ibn Kuraib al-Hamdani", "Abu Kuraib", "Al-Hamdani", "Muhaddith",
       birth=161, death=248, grade="Thiqa, hafiz ; shaykh des six recueils", sources=SUNNI_RIJAL),
    _r("ahmad_dawraqi", "Ahmad ibn Ibrahim al-Dawraqi al-Abdi", "Abu Abdullah", "Al-Baghdadi", "Muhaddith",
       birth=168, death=246, grade="Thiqa, hafiz ; shaykh d'al-Bukhari et Muslim", sources=SUNNI_RIJAL),
])