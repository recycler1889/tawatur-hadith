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
│   ├── schema.sql     # Schéma de base de données (à venir)
│   └── seed_data.py   # Données d'exemple (hadiths mutawatir)
├── frontend/
│   ├── app.py         # Interface Streamlit (à venir)
│   └── components/    # Composants UI
├── data/
│   ├── seed_hadiths.json      # Données d'exemple au format JSON
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

## Données d'exemple

Le projet inclut 3 hadiths mutawatir majeurs incontestés :

1. **Hadith 001** - *Innamā al-a'mālu bin-niyyāt* (Actions sont jugées par les intentions)
   - Type : Mutawatir Ma'nawi
   - Obédience : Commun (Sunnite + Chiite)
   - Source : Al-Bukhari, Muslim

2. **Hadith 002** - *Hadith al-Thaqalayn* (Les deux choses lourdes)
   - Type : Mutawatir Lafzi
   - Obédience : Commun
   - Source : Al-Kafi, Sunan al-Tirmidhi, Musnad Ahmad

3. **Hadith 003** - *Hadith al-Ghadir* (Jour de Ghadir Khumm)
   - Type : Mutawatir Lafzi
   - Obédience : Commun
   - Source : Musnad Ahmad, al-Tirmidhi, al-Hakim

## Utilisation

### Générer les données d'exemple

```bash
cd C:\Users\decen\tawatur-hadith
python database/seed_data.py
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
