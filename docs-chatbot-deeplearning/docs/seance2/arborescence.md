seance2/
│
├── index.md                                       # Page principale de la séance 2
│
├── atelier1-reconnaissance-images/                # Atelier 1
│   ├── guide-atelier1.md                          # Guide de travail pratique
│   ├── notebooks/
│   │   ├── 00_workshop_intro.ipynb                # Introduction à l'atelier
│   │   ├── 01_model_exploration.ipynb             # Exploration du modèle pré-entraîné
│   │   ├── 02_model_adaptation.ipynb              # Adaptation du modèle au catalogue
│   │   └── 03_business_adaptation.ipynb           # Configuration des seuils et cas spéciaux
│   ├── api_project/
│   │   ├── app.py                                 # Squelette de l'API Flask
│   │   ├── requirements.txt                       # Dépendances Python
│   │   └── Dockerfile                             # Template pour la conteneurisation
│   ├── api_docs/
│   │   └── openapi.yaml                           # Documentation OpenAPI/Swagger
│   └── data/
│       ├── examples/                              # Images d'exemple pour les tests
│       └── techretail/                            # Dataset client (images + métadonnées)
│
├── atelier2-assistant-virtuel/                    # Atelier 2
│   ├── guide-atelier2.md                          # Guide de travail pratique
│   ├── notebooks/
│   │   ├── 01_data_exploration.ipynb              # Analyse du dataset de tickets
│   │   ├── 02_data_preparation.ipynb              # Prétraitement du texte
│   │   ├── 03_model_setup.ipynb                   # Configuration du modèle NLP
│   │   └── 04_model_training.ipynb                # Entraînement et évaluation
│   ├── knowledge_base/                            # Base de connaissances pour l'assistant
│   │   ├── common_issues.json                     # Problèmes fréquents
│   │   ├── hardware_issues.json                   # Problèmes matériels
│   │   ├── software_issues.json                   # Problèmes logiciels
│   │   └── network_issues.json                    # Problèmes réseau
│   ├── assistant_api/
│   │   ├── app.py                                 # Serveur Flask pour l'assistant
│   │   └── utils/                                 # Fonctions utilitaires
│   ├── chat_interface/
│   │   ├── index.html                             # Interface web de chat
│   │   ├── styles.css                             # Styles CSS
│   │   └── script.js                              # Script JavaScript à compléter
│   ├── routing_system.py                          # Système de routage des demandes
│   └── test_assistant.py                          # Outil de test
│
├── atelier3-optimisation-deploiement/              # Atelier 3
│   ├── guide-atelier3.md                          # Guide de travail pratique
│   ├── notebooks/
│   │   ├── 01_performance_analysis.ipynb          # Analyse des performances
│   │   ├── 02_quantization.ipynb                  # Techniques de quantification
│   │   └── 03_inference_optimization.ipynb        # Optimisation des opérations d'inférence
│   ├── image_recognition_service/                 # Service de reconnaissance d'images
│   │   ├── Dockerfile                             # Template à compléter
│   │   └── app/                                   # Code source du service
│   ├── assistant_service/                         # Service d'assistant virtuel
│   │   ├── Dockerfile                             # Template à compléter
│   │   └── app/                                   # Code source du service
│   ├── monitoring/                                # Configuration du monitoring
│   │   ├── prometheus/                            # Configuration Prometheus
│   │   └── grafana/                               # Dashboards Grafana
│   ├── docker-compose.yml                         # Configuration multi-services
│   ├── deploy.sh                                  # Script de déploiement
│   └── health_check.sh                            # Script de vérification
│
└── ressources/                                    # Ressources communes
    ├── guides/
    │   ├── bonnes_pratiques_api.md                # Guide des bonnes pratiques API REST
    │   ├── conteneurisation_ml.md                 # Guide de conteneurisation pour ML
    │   └── optimisation_modeles.md                # Guide d'optimisation des modèles
    ├── templates/
    │   ├── compte_rendu.md                        # Template de compte-rendu
    │   └── documentation_technique.md             # Template de documentation technique
    └── evaluation/
        └── grille_evaluation.md                   # Grille d'évaluation détaillée