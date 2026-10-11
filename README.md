# Tawatur Hadith Project

Un projet modulaire en Python pour répertorier, structurer et visualiser les hadiths Mutawatir avec leurs chaînes de transmission (Isnad) sous forme d'arbres généalogiques interactifs, en intégrant les perspectives sunnites et chiites.

## Architecture

Le projet suit une architecture propre et orientée données :

```
tawatur-hadith/
├── backend/
│   ├── api/           # API REST (future)
│   ├── graph/         # Outils de visualisation et traitement des graphes d'Isnad
│   ├── models/        # Modèles Pydantic/SQL
│   └── utils/         # Utilitaires backend
├── database/
│   ├── data/          # Registres (rawis_data) et catalogue (hadiths_data)
│   ├── seed_data.py   # Assembleur des données (hadiths + narrateurs)
│   └── save_seed.py   # Export vers data/seed_hadiths.json
├── frontend/
│   ├── app.py         # Interface Streamlit (thèmes Clair / Sépia / Sombre)
│   └── components/    # Composants UI
├── data/
│   ├── seed_hadiths.json      # Données au format JSON
│   └── example_isnad_tree.json # Exemple d'arbre d'Isnad
└── README.md
```

## Modèle de Données

### Entités principales

1. **Hadith** : Représente un hadith Mutawatir
   - Matn (texte arabe + traduction)
   - Type de Tawatur (Lafzi / Ma'nawi)
   - Obédience (Sunnite / Chiite / Commun)
   - Degré de tawatur et sources de validation
   - Chaînes d'Isnad associées

2. **Rawi (Narrateur)** : Biographie des transmetteurs
   - Identité (Nom, Kunya, Nisba, Tabaqa)
   - Fiabilité selon le Jarh wa Ta'dil
   - Dates (naissance/décès)

3. **IsnadChain** : Chaîne de transmission ordonnée
   - Noeuds ordonnés (Compagnon → ... → Compilateur)
   - Nombre de chemins de transmission (path_count)
   - Sources documentaires

## Données

Le catalogue regroupe **98 hadiths mutawatir** (rangs 1–98) répartis en
plusieurs vagues :

- `database/data/hadiths_data.py` : catalogue principal (rangs 1-50) ;
- `database/data/hadiths_data_mw1.py` / `hadiths_data_mw2.py` : vagues
  d'extension (rangs 51-70 et 71-98) ;
- `database/data/rawis_data.py` + `rawis_data_extra.py` : registre des
  narrateurs (Rijal), 105 profils (Sahaba, Tabi'un, Imams, compilateurs).

Chaque hadith porte ses voies (Turuq) avec une chaîne d'Isnad complète
(Compagnon → Tabi'i/Imam → compilateur). Le catalogue couvre les traditions
sunnite et chiite (obédiences « commun », « sunnite », « chiite »).

## Utilisation

### Générer/valider les données

```bash
cd C:\Users\decen\tawatur-hadith
python -m database.seed_data        # résumé de l'intégrité
python database/save_seed.py        # export data/seed_hadiths.json
```

### Lancer l'interface

```bash
streamlit run frontend/app.py
```

### Tester l'affichage des arbres d'Isnad

```bash
python test_isnad.py
```

Cela affichera les chaînes de transmission sous forme textuelle et générera un exemple JSON pour la visualisation graphique.

## Plan d'action pour l'import massif

L'intégration automatisée des hadiths mutawatir se fera par étapes :

### Phase 1 : Collecte et numérisation des corpus de référence
- **Al-Suyuti** (d. 911H) : *Al-Azhar al-Mutanasira fi al-Ahadith al-Mutawatira* - référence majeure sur les hadiths mutawatir
- **Al-Kattani** (d. 1907CE) : *Nazm al-Mutanathir min al-Hadith al-Mutawatir* - recensement systématique
- **Autres ouvrages** : *Qawa'id al-Tahdith* d'Ibn al-Salah, travaux de Mulla Ali al-Qari, etc.

### Phase 2 : Extraction et structuration
1. **OCR/Texte brut** : Convertir les ouvrages PDF/texte vers un format exploitable
2. **Parsing spécialisé** : Développer des parseurs pour extraire :
   - Matn (texte du hadith)
   - Isnad complet avec hiérarchie des narrateurs
   - Classification (Lafzi/Ma'nawi)
   - Approbations (Sunnite/Chiite/Commun)
3. **Normalisation** : Harmoniser les noms de narrateurs (résolution des variantes orthographiques)

### Phase 3 : Enrichissement des données biographiques (Ta'rikh al-Rijal)
- Intégration des dictionnaires : *Tahdhib al-Tahdhib*, *Al-Isabah*, *Mizan al-I'tidal*, *Rijal al-Kashshi*, etc.
- Mapping automatique des narrateurs pour compléter fiabilité, tabaqat, dates
- Résolution des ambiguïtés par algorithme de correspondance

### Phase 4 : Base de données et validation
- Migration vers SQLite/DuckDB avec schéma relationnel complet
- Validation croisée entre sources (Sunnite vs Chiite)
- Détection des chaînes communes et calcul des degrés de tawatur
- Qualité des données : tests, doublons, intégrité référentielle

### Phase 5 : Visualisation et API
- Interface web avec visualisation interactive des graphes (Cytoscape.js/D3.js)
- API REST pour requêtage (FastAPI)
- Interface Streamlit pour exploration rapide
- Export des données (JSON, GraphML, RDF)

### Phase 6 : Automatisation (CI/CD)
- Pipeline d'import incrémental
- Scripts de scraping/ingestion versionnés
- Suivi des sources et métadonnées (provenance)
- Tests d'intégration sur corpus

## Technologies envisagées

- **Backend** : FastAPI, Pydantic v2, SQLAlchemy
- **Base de données** : DuckDB (recommandé pour analytics + graphes) ou SQLite
- **Visualisation** : Cytoscape.js, PyVis, Plotly
- **Frontend** : Streamlit (MVP) → React/Vite + Cytoscape.js (v2)
- **Données** : NetworkX pour traitement des graphes
- **IA/Parsing** : LLM pour extraction assistée des textes arabes classiques

## Contribution

Ce projet vise à fournir une base scientifique et neutre pour l'étude comparative des hadiths mutawatir entre traditions sunnite et chiite.
