# Kit de démarrage pour le projet chatbot (4h)

Ce kit contient tous les éléments essentiels pour développer rapidement un chatbot pédagogique fonctionnel dans le cadre d'une séance de 4 heures. Choisissez la version correspondant à votre option (SISR ou SLAM).

## Structure du kit

kit-demarrage-[sisr/slam]/
├── frontend/
│   ├── index.html         # Interface du chatbot
│   ├── css/
│   │   └── style.css      # Styles pré-configurés
│   └── js/
│       └── app.js         # Logique côté client
│
├── backend/
│   ├── app.py             # Serveur Flask et intégration API
│   ├── knowledge_base.py  # Gestion de la base de connaissances
│   └── prompt_utils.py    # Utilities pour l'enrichissement des prompts
│
├── knowledge/
│   ├── base_structure.json  # Structure JSON vide à compléter
│   └── examples/
│       ├── dl_general.json  # Exemple pour concept général
│       └── concept_[sisr/slam].json  # Exemple spécifique à l'option
│
└── README.md              # Instructions d'utilisation


## Guide de démarrage rapide

1. **Configuration**
   - Placez votre clé API Mistral dans le fichier `backend/config.py`
   - Exécutez `pip install -r requirements.txt` pour installer les dépendances

2. **Lancement**
   - Démarrez le backend : `python backend/app.py`
   - Ouvrez `frontend/index.html` avec Live Server ou équivalent

3. **Développement rapide**
   - **Frontend** : L'interface est déjà fonctionnelle, modifiez seulement l'apparence
   - **Backend** : Les fonctions sont pré-implémentées, ajoutez votre logique spécifique
   - **Base de connaissances** : Complétez les fichiers JSON dans le dossier `knowledge/`

## Points de personnalisation

Dans chaque fichier, vous trouverez des commentaires `TODO` indiquant les sections à modifier pour votre projet.

### Spécificités SISR

Pour l'option SISR, concentrez-vous sur :
- Le système d'arbre de décision dans `backend/diagnostic_tree.py`
- Les réponses adaptées aux problèmes réseau dans `knowledge/concept_sisr.json`

### Spécificités SLAM

Pour l'option SLAM, concentrez-vous sur :
- Le système d'authentification simple dans `frontend/js/auth.js`
- La persistance locale dans `frontend/js/storage.js`
- Les concepts de développement dans `knowledge/concept_slam.json`