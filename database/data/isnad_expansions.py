# -*- coding: utf-8 -*-
"""Chaînes de transmission détaillées ajoutées aux hadiths existants.

Chaque clé est un ``id`` de hadith ; la valeur est une liste de voies (Turuq)
au format identique à celui des specs de ``hadiths_data`` :

    {"label": ..., "path_count": ..., "sources": [...], "nodes": [(rawi_id, level), ...]}

Les ``nodes`` suivent : 4 = Compagnon, 2/3 = Tabi'i/Imam majeur, 1 = atba'
al-tabi'in / shaykh du compilateur, 0 = compilateur. Elles proviennent du
dépouillement des asanid des recueils (isnad complet tel qu'imprimé à la tête
de chaque tradition).

Sources consultées (asanid) : Sahih al-Bukhari, Sahih Muslim (numérotation
sunnah.com), Musnad Ahmad, Sunan (Abu Dawud, al-Tirmidhi, al-Nasa'i, Ibn Majah).
"""

ISNAD_EXPANSIONS = {
    # ==================================================================
    # Man kadhaba 'alayya — asanid d'al-Bukhari (110) et de Muslim (3)
    # ==================================================================
    "h_kadhib": [
        {
            "label": "Abu Hurayra → Abu Salih → Abu Hasin → Abu Awanah → Musa al-Minqari → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 110"],
            "nodes": [
                ("abu_hurayra", 4), ("abu_salih", 2), ("abu_hasin", 2),
                ("abu_awanah", 1), ("musa_minqari", 1), ("bukhari", 0),
            ],
        },
        {
            "label": "Abu Hurayra → Abu Salih → Abu Hasin → Abu Awanah → Muhammad ibn Ubayd al-Ghubari → Muslim",
            "path_count": 1,
            "sources": ["Sahih Muslim 3"],
            "nodes": [
                ("abu_hurayra", 4), ("abu_salih", 2), ("abu_hasin", 2),
                ("abu_awanah", 1), ("muh_ghubari", 1), ("muslim", 0),
            ],
        },
    ],

    # ==================================================================
    # Innamâ al-a'mâl bi-l-niyyât — asanid d'al-Bukhari (1) et Muslim (1907)
    # ==================================================================
    "h_niyyah": [
        {
            "label": "Omar → Alqama ibn Waqqas → Muhammad ibn Ibrahim al-Taymi → Yahya ibn Sa'id al-Ansari → Sufyan ibn Uyayna → Al-Humaydi → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 1"],
            "nodes": [
                ("umar", 4), ("alqama_waqqas", 2), ("muh_ibrahim_taymi", 2),
                ("yahya_ansari", 2), ("sufyan_uyayna", 1), ("humaydi", 1), ("bukhari", 0),
            ],
        },
        {
            "label": "Omar → Alqama ibn Waqqas → Muhammad ibn Ibrahim → Yahya ibn Sa'id al-Ansari → Malik → Abdullah ibn Maslama → Muslim",
            "path_count": 1,
            "sources": ["Sahih Muslim 1907"],
            "nodes": [
                ("umar", 4), ("alqama_waqqas", 2), ("muh_ibrahim_taymi", 2),
                ("yahya_ansari", 2), ("malik", 1), ("ibn_maslama", 1), ("muslim", 0),
            ],
        },
    ],

    # ==================================================================
    # Hadith al-Manzila — isnad d'al-Bukhari (4416)
    # ==================================================================
    "h_manzila": [
        {
            "label": "Sa'd → Mus'ab ibn Sa'd → Al-Hakam ibn Utayba → Shu'ba → Yahya al-Qattan → Musaddad → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 4416"],
            "nodes": [
                ("saad", 4), ("musab_saad", 2), ("al_hakam_utayba", 2),
                ("shuba", 1), ("yahya_qattan", 1), ("musaddad", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Hadith du Bassin (Al-Hawd) — isnad d'al-Bukhari (6579)
    # ==================================================================
    "h_hawd": [
        {
            "label": "Abdullah ibn Amr → Ibn Abi Mulayka → Nafi' ibn Umar → Sa'id ibn Abi Maryam → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 6579"],
            "nodes": [
                ("abdullah_amr", 4), ("ibn_abi_mulayka", 2),
                ("nafi_umar", 1), ("said_abi_maryam", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Raf' al-Yadayn — asanid d'al-Bukhari (735) et de Muslim (390)
    # ==================================================================
    "h_rafy": [
        {
            "label": "Ibn Umar → Salim → Al-Zuhri → Malik → Abdullah ibn Maslama → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 735"],
            "nodes": [
                ("abdullah_umar", 4), ("salim_umar", 2), ("al_zuhri", 2),
                ("malik", 1), ("ibn_maslama", 1), ("bukhari", 0),
            ],
        },
        {
            "label": "Ibn Umar → Salim → Al-Zuhri → Sufyan ibn Uyayna → Yahya ibn Yahya → Muslim",
            "path_count": 1,
            "sources": ["Sahih Muslim 390"],
            "nodes": [
                ("abdullah_umar", 4), ("salim_umar", 2), ("al_zuhri", 2),
                ("sufyan_uyayna", 1), ("yahya_tamimi", 1), ("muslim", 0),
            ],
        },
    ],

    # ==================================================================
    # Ghadir Khumm (man kuntu mawlâhu) — isnad d'al-Tirmidhi (3713)
    # ==================================================================
    "h_ghadir": [
        {
            "label": "Zayd ibn Arqam → Abu al-Tufayl → Salama ibn Kuhayl → Shu'ba → Muhammad ibn Ja'far → Muhammad ibn Bashshar → Al-Tirmidhi",
            "path_count": 1,
            "sources": ["Sunan al-Tirmidhi 3713"],
            "nodes": [
                ("zayd_arqam", 4), ("abu_tufayl", 2), ("salama_kuhayl", 2),
                ("shuba", 1), ("muh_jaafar", 1), ("muh_bashshar", 1), ("tirmidhi", 0),
            ],
        },
    ],

    # ==================================================================
    # Hadith al-Thaqalayn — asanid de Muslim (2408) et al-Tirmidhi (3788)
    # ==================================================================
    "h_thaqalayn": [
        {
            "label": "Zayd ibn Arqam → Yazid ibn Hayyan → Abu Hayyan → Ibn Ulayya → Zuhayr ibn Harb → Muslim",
            "path_count": 1,
            "sources": ["Sahih Muslim 2408"],
            "nodes": [
                ("zayd_arqam", 4), ("yazid_hayyan", 2), ("abu_hayyan", 2),
                ("ibn_ulayya", 1), ("zuhayr_harb", 1), ("muslim", 0),
            ],
        },
        {
            "label": "Zayd ibn Arqam → Habib ibn Abi Thabit → Al-A'mash → Muhammad ibn Fudayl → Ali ibn al-Mundhir → Al-Tirmidhi",
            "path_count": 1,
            "sources": ["Sunan al-Tirmidhi 3788"],
            "nodes": [
                ("zayd_arqam", 4), ("habib", 2), ("amash", 1),
                ("muh_fudayl", 1), ("ali_mundhir", 1), ("tirmidhi", 0),
            ],
        },
        {
            "label": "Abu Sa'id → Atiyya → Al-A'mash → Muhammad ibn Fudayl → Ali ibn al-Mundhir → Al-Tirmidhi",
            "path_count": 1,
            "sources": ["Sunan al-Tirmidhi 3788"],
            "nodes": [
                ("abu_saeed", 4), ("atiyya", 2), ("amash", 1),
                ("muh_fudayl", 1), ("ali_mundhir", 1), ("tirmidhi", 0),
            ],
        },
    ],

    # ==================================================================
    # Al-Mash 'ala al-Khuffayn — isnad d'al-Bukhari (206)
    # ==================================================================
    "h_mash": [
        {
            "label": "Al-Mughira → Urwa ibn al-Mughira → Al-Sha'bi → Zakariyya ibn Abi Za'ida → Abu Nu'aym → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 206"],
            "nodes": [
                ("mughira", 4), ("urwa_mughira", 2), ("shabi", 2),
                ("zakariyya", 1), ("abu_nuaym", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Ru'yat Allah — asanid d'al-Bukhari (7434), via Jarir
    # ==================================================================
    "h_ruyat": [
        {
            "label": "Jarir → Qays ibn Abi Hazim → Ismail ibn Abi Khalid → Hushaym → Amr ibn Awn → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 7434"],
            "nodes": [
                ("jarir", 4), ("qais", 2), ("ismail_abi_khalid", 2),
                ("hushaym", 1), ("amr_awn", 1), ("bukhari", 0),
            ],
        },
        {
            "label": "Jarir → Qais ibn Abi Hazim → Ismail ibn Abi Khalid → Khalid al-Tahhan → Amr ibn Awn → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 7434"],
            "nodes": [
                ("jarir", 4), ("qais", 2), ("ismail_abi_khalid", 2),
                ("khalid_tahhan", 1), ("amr_awn", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Ru'yat Allah — isnad d'al-Bukhari (7435), via Jarir
    # ==================================================================
    "h_ruya": [
        {
            "label": "Jarir → Qays ibn Abi Hazim → Ismail ibn Abi Khalid → Abu Shihab → Asim ibn Yusuf → Yusuf ibn Musa → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 7435"],
            "nodes": [
                ("jarir", 4), ("qais", 2), ("ismail_abi_khalid", 2),
                ("abu_shihab", 1), ("asim_yusuf", 1), ("yusuf_musa", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Nuzul Isa — isnad d'al-Bukhari (3448)
    # ==================================================================
    "h_nuzul_isa": [
        {
            "label": "Abu Hurayra → Sa'id ibn al-Musayyib → Al-Zuhri → Salih ibn Kaysan → Ibrahim ibn Sa'd → Ya'qub ibn Ibrahim → Ishaq ibn Rahawayh → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 3448"],
            "nodes": [
                ("abu_hurayra", 4), ("said_musayyib", 2), ("al_zuhri", 2),
                ("salih_kaysan", 1), ("ibrahim_saad", 1), ("yaqub_ibrahim", 1),
                ("ishaq_rahawayh", 1), ("bukhari", 0),
            ],
        },
    ],

    # ==================================================================
    # Al-Mahdi — asanid d'Abu Dawud (4282), tous par Asim → Zirr → Ibn Mas'ud
    # ==================================================================
    "h_mahdi": [
        {
            "label": "Ibn Mas'ud → Zirr ibn Hubaysh → Asim ibn Abi al-Nujud → Umar ibn Ubayd → Musaddad → Abu Dawud",
            "path_count": 1,
            "sources": ["Sunan Abi Dawud 4282"],
            "nodes": [
                ("ibn_masud", 4), ("zirr", 2), ("asim_nujud", 2),
                ("umar_ubayd", 1), ("musaddad", 1), ("abu_dawud", 0),
            ],
        },
        {
            "label": "Ibn Mas'ud → Zirr → Asim → Abu Bakr ibn Ayyash → Abu Kuraib → Abu Dawud",
            "path_count": 1,
            "sources": ["Sunan Abi Dawud 4282"],
            "nodes": [
                ("ibn_masud", 4), ("zirr", 2), ("asim_nujud", 2),
                ("abu_bakr_ayyash", 1), ("abu_kuraib", 1), ("abu_dawud", 0),
            ],
        },
        {
            "label": "Ibn Mas'ud → Zirr → Asim → Sufyan al-Thawri → Yahya al-Qattan → Musaddad → Abu Dawud",
            "path_count": 1,
            "sources": ["Sunan Abi Dawud 4282"],
            "nodes": [
                ("ibn_masud", 4), ("zirr", 2), ("asim_nujud", 2),
                ("sufyan_thawri", 1), ("yahya_qattan", 1), ("musaddad", 1), ("abu_dawud", 0),
            ],
        },
        {
            "label": "Ibn Mas'ud → Zirr → Asim → Za'ida → Ubaydullah ibn Musa → Ahmad ibn Ibrahim → Abu Dawud",
            "path_count": 1,
            "sources": ["Sunan Abi Dawud 4282"],
            "nodes": [
                ("ibn_masud", 4), ("zirr", 2), ("asim_nujud", 2),
                ("zaida", 1), ("ubaydullah_musa", 1), ("ahmad_dawraqi", 1), ("abu_dawud", 0),
            ],
        },
        {
            "label": "Ibn Mas'ud → Zirr → Asim → Fitr ibn Khalifa → Ubaydullah ibn Musa → Ahmad ibn Ibrahim → Abu Dawud",
            "path_count": 1,
            "sources": ["Sunan Abi Dawud 4282"],
            "nodes": [
                ("ibn_masud", 4), ("zirr", 2), ("asim_nujud", 2),
                ("fitr_khalifa", 1), ("ubaydullah_musa", 1), ("ahmad_dawraqi", 1), ("abu_dawud", 0),
            ],
        },
    ],

    # ==================================================================
    # Al-Shafa'a — asanid d'al-Bukhari (99) et (7474)
    # ==================================================================
    "h_shafaa": [
        {
            "label": "Abu Hurayra → Sa'id al-Maqburi → Amr ibn Abi Amr → Sulayman ibn Bilal → Abd al-Aziz al-Uwaysi → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 99"],
            "nodes": [
                ("abu_hurayra", 4), ("said_maqburi", 2), ("amr_abi_amr", 1),
                ("sulayman_bilal", 1), ("abdulaziz_uwaysi", 1), ("bukhari", 0),
            ],
        },
        {
            "label": "Abu Hurayra → Abu Salama → Al-Zuhri → Shu'ayb ibn Abi Hamza → Abu al-Yaman → Al-Bukhari",
            "path_count": 1,
            "sources": ["Sahih al-Bukhari 7474"],
            "nodes": [
                ("abu_hurayra", 4), ("abu_salama", 2), ("al_zuhri", 2),
                ("shuayb_zuhri", 1), ("abu_yaman", 1), ("bukhari", 0),
            ],
        },
    ],
}