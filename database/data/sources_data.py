"""Répertoire des sources hadithiques mobilisées par l'outil Tawatur Hadith.

Chaque entrée décrit un recueil, son compilateur, son obédience, la période du
savant et sa contribution au corpus (types de hadiths, chaînes/Turuq soutenues).
Le champ ``tokens`` sert au « lien avec l'outil » : sous-chaînes (insensibles à
la casse) recherchées dans les ``validation_sources`` des hadiths et dans les
``sources`` des chaînes pour compter les correspondances réelles dans la base.

Codes d'obédience : "sunnite", "chiite", "commun" (cf. ObedienceFR).
"""

SOURCES = [
    {
        "id": "bukhari",
        "collection_fr": "Sahih al-Bukhari",
        "collection_ar": "صحيح البخاري",
        "scholar_fr": "Muhammad ibn Isma'il al-Bukhari",
        "scholar_ar": "محمد بن إسماعيل البخاري",
        "obedience": "sunnite",
        "dates_fr": "194-256 AH / vers 810-870",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sahih al-bukhari", "al-bukhari"],
        "contribution": "Le recueil le plus référencé du corpus : confirme la "
                        "transmission large (Lafzi et Ma'nawi) de la majorité des "
                        "hadiths — passages sur l'eau, le repentir, le miracle, "
                        "l'ablution, le voyage.",
    },
    {
        "id": "muslim",
        "collection_fr": "Sahih Muslim",
        "collection_ar": "صحيح مسلم",
        "scholar_fr": "Muslim ibn al-Hajjaj al-Naysaburi",
        "scholar_ar": "مسلم بن الحجاج النيسابوري",
        "obedience": "sunnite",
        "dates_fr": "204-261 AH / vers 817-875",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sahih muslim", "muslim 1/", "muslim 2/"],
        "contribution": "Complément systématique d'al-Bukhari sur les mêmes "
                        "hadiths : alourdit le compte des chaînes et la "
                        "concordance des voies.",
    },
    {
        "id": "abu_dawud",
        "collection_fr": "Sunan Abi Dawud",
        "collection_ar": "سنن أبي داود",
        "scholar_fr": "Abu Dawud al-Sijistani",
        "scholar_ar": "أبو داود السجستاني",
        "obedience": "sunnite",
        "dates_fr": "202-275 AH / vers 817-889",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sunan abi dawud"],
        "contribution": "Recueil de Sunan : fournit des voies complémentaires "
                        "(salem, répudiation, trop de épreuves, mirais) qui "
                        "renforcent la multiplicité des Turuq.",
    },
    {
        "id": "tirmidhi",
        "collection_fr": "Sunan al-Tirmidhi",
        "collection_ar": "سنن الترمذي",
        "scholar_fr": "Muhammad ibn 'Isa al-Tirmidhi",
        "scholar_ar": "محمد بن عيسى الترمذي",
        "obedience": "sunnite",
        "dates_fr": "209-279 AH / vers 824-892",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sunan al-tirmidhi", "al-tirmidhi"],
        "contribution": "Le Sunan le plus souvent cité dans les "
                        "validation_sources ; appuie des hadiths à forte charge "
                        "théologique (Ghadir, quitter le monde, le sang d'Ali).",
    },
    {
        "id": "nasai",
        "collection_fr": "Sunan al-Nasa'i",
        "collection_ar": "سنن النسائي",
        "scholar_fr": "Ahmad ibn Shu'ayb al-Nasa'i",
        "scholar_ar": "أحمد بن شعيب النسائي",
        "obedience": "sunnite",
        "dates_fr": "215-303 AH / vers 830-915",
        "century_hijri": "4e siècle hégirien",
        "tokens": ["sunan al-nasa'i", "al-nasa'i"],
        "contribution": "Sunan des rites et de la justice ; intervient sur les "
                        "hadiths de l'ablution et de la prière en voyage.",
    },
    {
        "id": "ibn_majah",
        "collection_fr": "Sunan Ibn Majah",
        "collection_ar": "سنن ابن ماجه",
        "scholar_fr": "Ibn Majah al-Qazwini",
        "scholar_ar": "ابن ماجه القزويني",
        "obedience": "sunnite",
        "dates_fr": "209-273 AH / vers 824-887",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sunan ibn majah"],
        "contribution": "Sixième des Kutub al-Sittah ; ses voies élargissent "
                        "l'assise des hadiths communs (Ghadir, la justice).",
    },
    {
        "id": "ahmad",
        "collection_fr": "Musnad Ahmad",
        "collection_ar": "مسند أحمد",
        "scholar_fr": "Ahmad ibn Hanbal",
        "scholar_ar": "أحمد بن حنبل",
        "obedience": "sunnite",
        "dates_fr": "164-241 AH / vers 780-855",
        "century_hijri": "2e-3e siècle hégirien",
        "tokens": ["musnad ahmad"],
        "contribution": "Le Musnad le plus mobilisé par les chaînes : nombreuses "
                        "voies via Abu Hurayra, Jabir, Ibn Abbas, Ali — pilier de "
                        "la multiplicité des Turuq (ex. Ghadir via 3 Compagnons).",
    },
    {
        "id": "malik",
        "collection_fr": "Al-Muwatta'",
        "collection_ar": "الموطأ",
        "scholar_fr": "Malik ibn Anas",
        "scholar_ar": "مالك بن أنس",
        "obedience": "sunnite",
        "dates_fr": "93-179 AH / vers 711-795",
        "century_hijri": "2e siècle hégirien",
        "tokens": ["al-muwatta", "muwatta", "muwata"],
        "contribution": "Le plus ancien recueil cité : donne des hadiths "
                        "transmis par l'école médinoise (gosière du voyageur).",
    },
    {
        "id": "darimi",
        "collection_fr": "Sunan al-Darimi",
        "collection_ar": "سنن الدارمي",
        "scholar_fr": "'Abd Allah ibn 'Abd al-Rahman al-Darimi",
        "scholar_ar": "عبد الله بن عبد الرحمن الدارمي",
        "obedience": "sunnite",
        "dates_fr": "181-255 AH / vers 797-869",
        "century_hijri": "3e siècle hégirien",
        "tokens": ["sunan al-darimi"],
        "contribution": "Recueil du Khurasan : voie complémentaire (ex. la "
                        "toucher de l'Arabie, la foi par le cœur).",
    },
    {
        "id": "hakim",
        "collection_fr": "Al-Mustadrak 'ala al-Sahihayn",
        "collection_ar": "المستدرك على الصحيحين",
        "scholar_fr": "al-Hakim al-Naysaburi",
        "scholar_ar": "الحاكم النيسابوري",
        "obedience": "sunnite",
        "dates_fr": "321-405 AH / vers 933-1014",
        "century_hijri": "4e-5e siècle hégirien",
        "tokens": ["mustadrak al-hakim", "al-mustadrak"],
        "contribution": "Recueil de hadiths répondant aux conditions de "
                        "Bukhari/Muslim : voie décisive pour Ghadir (3/109) et "
                        "les mérites d'Ali (3/118).",
    },
    {
        "id": "bayhaqi",
        "collection_fr": "Al-Sunan al-Kubra",
        "collection_ar": "السنن الكبرى",
        "scholar_fr": "al-Bayhaqi",
        "scholar_ar": "البيهقي",
        "obedience": "sunnite",
        "dates_fr": "384-458 AH / vers 994-1066",
        "century_hijri": "4e-5e siècle hégirien",
        "tokens": ["sunan al-kubra", "al-bayhaqi"],
        "contribution": "Compilation juridique monumentale ; a séparé les voies "
                        "et les silencieux pour les hadiths de la foi.",
    },
    {
        "id": "ibn_abi_shayba",
        "collection_fr": "Al-Musannaf",
        "collection_ar": "المصنف",
        "scholar_fr": "Ibn Abi Shayba",
        "scholar_ar": "ابن أبي شيبة",
        "obedience": "sunnite",
        "dates_fr": "159-235 AH / vers 776-889",
        "century_hijri": "2e-3e siècle hégirien",
        "tokens": ["ibn abi shayba", "musannaf"],
        "contribution": "Source précoce de la transmission médinoise et "
                        "kufienne : élargit le bassin des narrateurs.",
    },
    {
        "id": "tabarani",
        "collection_fr": "Al-Mu'jam al-Kabir",
        "collection_ar": "المعجم الكبير",
        "scholar_fr": "al-Tabarani",
        "scholar_ar": "الطبراني",
        "obedience": "sunnite",
        "dates_fr": "260-360 AH / vers 874-971",
        "century_hijri": "3e-4e siècle hégirien",
        "tokens": ["al-mu'jam al-kabir", "al-mu'ajam al-kabir", "al-tabarani"],
        "contribution": "Recueil des Compagnons : fournit de nombreuses voies "
                        "complémentaires aux hadiths communs.",
    },
    {
        "id": "mizzi",
        "collection_fr": "Tuhfat al-Ashraf",
        "collection_ar": "تحفة الأشراف",
        "scholar_fr": "Jamal al-Din al-Mizzi",
        "scholar_ar": "جمال الدين المزي",
        "obedience": "sunnite",
        "dates_fr": "654-742 AH / vers 1256-1341",
        "century_hijri": "7e-8e siècle hégirien",
        "tokens": ["tuhfat al-ashraf"],
        "contribution": "Index systématique des narrateurs des grandes "
                        "collections ; sert à l'audit des chaînes.",
    },
    {
        "id": "muttaqi",
        "collection_fr": "Kanz al-Ummal",
        "collection_ar": "كنز العمال",
        "scholar_fr": "al-Muttaqi al-Hindi",
        "scholar_ar": "المتقي الهندي",
        "obedience": "sunnite",
        "dates_fr": "885-975 AH / vers 1480-1567",
        "century_hijri": "9e-10e siècle hégirien",
        "tokens": ["kanz al-ummal"],
        "contribution": "Compilation exhaustive des hadiths de la masse : "
                        "appuie la convergence des voies (Lafzi).",
    },
    {
        "id": "suyuti",
        "collection_fr": "Al-Azhar al-Mutanathira fi al-Ahadith al-Mutawatira",
        "collection_ar": "الأزهار المتناثرة في الأحاديث المتواترة",
        "scholar_fr": "Jalal al-Din al-Suyuti",
        "scholar_ar": "جلال الدين السيوطي",
        "obedience": "sunnite",
        "dates_fr": "849-911 AH / vers 1445-1505",
        "century_hijri": "9e-10e siècle hégirien",
        "tokens": ["al-azhar al-mutanathira"],
        "contribution": "Inventaire canonique des Mutawatir (Lafzi) — boussole "
                        "théorique du projet (cf. définitions du degré).",
    },
    {
        "id": "kattani",
        "collection_fr": "Nazm al-Mutanathir min al-Hadith al-Mutawatir",
        "collection_ar": "نظم المتناثر من الحديث المتواتر",
        "scholar_fr": "'Abd al-Hayy al-Kattani",
        "scholar_ar": "عبد الحي الكتاني",
        "obedience": "sunnite",
        "dates_fr": "1273-1345 AH / vers 1856-1927",
        "century_hijri": "13e-14e siècle hégirien",
        "tokens": ["nazm al-mutanathir"],
        "contribution": "Répertoire méthodologique du tawatur praticable : "
                        "définit les seuils de voies et de Compagnons utilisés "
                        "par les degrés (Turuq ≥ 4/5/6 Compagnons).",
    },
    {
        "id": "kulayni",
        "collection_fr": "Al-Kafi",
        "collection_ar": "الكافي",
        "scholar_fr": "Muhammad ibn Ya'qub al-Kulayni",
        "scholar_ar": "محمد بن يعقوب الكليني",
        "obedience": "chiite",
        "dates_fr": "vers 250-329 AH / vers 864-941",
        "century_hijri": "3e-4e siècle hégirien",
        "tokens": ["al-kafi"],
        "contribution": "Le recueil chiite le plus cité (Ghadir 1/295, mérites "
                        "d'Ali 1/294, le sang 8/106) : assure la concordance "
                        "inter-communautaire du corpus (Commun).",
    },
    {
        "id": "saduq",
        "collection_fr": "Man la yahduruhu al-Faqih (+ al-Amali)",
        "collection_ar": "من لا يحضره الفقيه وأمالي الصدوق",
        "scholar_fr": "Ibn Babawayh al-Saduq",
        "scholar_ar": "ابن بابويه الصدوق",
        "obedience": "chiite",
        "dates_fr": "305-381 AH / vers 918-991",
        "century_hijri": "4e siècle hégirien",
        "tokens": ["man la yahduruhu al-faqih", "al-amali", "a-al-amali"],
        "contribution": "Un des Quatre Livres (al-Kutub al-Arba'a) ; les "
                        "sources d'hommes et ses Amali complètent la base "
                        "chiite des hadiths communs.",
    },
    {
        "id": "tusi",
        "collection_fr": "Tahdhib al-Ahkam (+ al-Istibsar)",
        "collection_ar": "تهذيب الأحكام والاستبصار",
        "scholar_fr": "al-Shaykh al-Tusi",
        "scholar_ar": "الشيخ الطوسي",
        "obedience": "chiite",
        "dates_fr": "385-460 AH / vers 995-1067",
        "century_hijri": "4e-5e siècle hégirien",
        "tokens": ["tahdhib al-ahkam", "al-istibsar"],
        "contribution": "Les deux autres des Quatre Livres ; rigueur de chaîne "
                        "équivalente à la Sunna pour les mêmes hadiths.",
    },
    {
        "id": "nasai_khasa",
        "collection_fr": "Khasa'is Amir al-Mu'minin",
        "collection_ar": "خصائص أمير المؤمنين",
        "scholar_fr": "al-Nasa'i (recueil dédié aux mérites d'Ali)",
        "scholar_ar": "النسائي - الخصائص",
        "obedience": "commun",
        "dates_fr": "215-303 AH / vers 830-915",
        "century_hijri": "4e siècle hégirien",
        "tokens": ["khasa'is", "khassais"],
        "contribution": "Recueil dédié de l'imam sunnite sur les mérites "
                        "particuliers d'Ali — mobilisé dans le hadith du sang et "
                        "la mesure après Ghadir ; OBÉDIENCE commune.",
    },
    {
        "id": "amini",
        "collection_fr": "Kitab al-Ghadir",
        "collection_ar": "كتاب الغدير",
        "scholar_fr": "'Abd al-Husayn al-Amini",
        "scholar_ar": "عبد الحسين الأميني",
        "obedience": "chiite",
        "dates_fr": "1305-1390 AH / vers 1887-1970",
        "century_hijri": "14e siècle hégirien",
        "tokens": ["kitab al-ghadir", "al-ghadir"],
        "contribution": "Enquête moderne : compile 110 Compagnons et 360 "
                        "narrateurs du texte de Ghadir — référence transversale "
                        "fondamentale pour le degré maximum du corpus.",
    },
]

# Identifiants uniques garantis (utile pour l'audit).
SOURCE_IDS = [s["id"] for s in SOURCES]