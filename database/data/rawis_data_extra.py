# -*- coding: utf-8 -*-
"""Narrateurs additionnels (Rijal) pour la vague d'extension du catalogue.

Même conventions que ``rawis_data`` (helper ``_r``, grades + ouvrages Rijal).
Ce lot est fusionné dans ``RAWIS`` par l'assembleur ``seed_data``.
"""

from database.data.rawis_data import _r, SAHABA_SRC, SUNNI_RIJAL, COMPANION

RAWIS_EXTRA = dict([
    # ------------------------------------------------------------------
    # Compagnons additionnels
    # ------------------------------------------------------------------
    _r("abu_shurayh", "Abu Shuraih al-Khuza'i", "Abu Shuraih", "Al-Khuza'i", "Sahaba", death=68,
       grade=COMPANION + " ; narrateur des hadiths sur l'hôte (dayf) et le voisin", sources=SAHABA_SRC),
    _r("shaddad", "Shaddad ibn Aws", "Abu Yazan", "Al-Ansari", "Sahaba", death=58,
       grade=COMPANION + " ; narrateur du hadith al-ihsan", sources=SAHABA_SRC),
    _r("muawiya", "Mu'awiya ibn Abi Sufyan", "Abu Abd al-Rahman", "Al-Umawi", "Sahaba", death=60,
       grade=COMPANION + " ; scribe de la révélation", sources=SAHABA_SRC),
    _r("malik_hu", "Malik ibn al-Huwayrith al-Laythi", "Abu Sulayman", "Al-Laythi", "Sahaba", death=74,
       grade=COMPANION + " ; narrateur de 'Valinyu-llah bi as-salat'", sources=SAHABA_SRC),
    _r("adi_hatim", "'Adi ibn Hatim al-Ta'i", "Abu Tarif", "Al-Ta'i", "Sahaba", death=68,
       grade=COMPANION, sources=SAHABA_SRC),
    _r("numan", "Al-Nu'man ibn Bashir", "Abu Abd Allah", "Al-Ansari", "Sahaba", death=64,
       grade=COMPANION + " ; narrateur du hadith al-halal wa al-haram", sources=SAHABA_SRC),
    _r("ubayy", "Ubayy ibn Ka'b", "Abu al-Mundhir", "Al-Ansari", "Sahaba", death=30,
       grade=COMPANION + " ; maître des récitateurs", sources=SAHABA_SRC),
    _r("abdullah_zubayr", "Abdullah ibn al-Zubayr", "Abu Bakr", "Al-Qurashi", "Sahaba", death=73,
       grade=COMPANION, sources=SAHABA_SRC),

    # ------------------------------------------------------------------
    # Muhaddithun additionnels
    # ------------------------------------------------------------------
    _r("ibn_khuzayma", "Ibn Khuzayma al-Naysaburi", "Abu Bakr", "Al-Naysaburi", "Muhaddith",
       birth=223, death=311, grade="Imam, hafiz — auteur du Sahih", sources=SUNNI_RIJAL),
    _r("alqama", "'Alqama ibn Qays", "Abu Shibl", "Al-Nakha'i", "Tabi'in", death=62,
       grade="Thiqa, hafiz ; grand faqih de Koufa", sources=SUNNI_RIJAL),
])