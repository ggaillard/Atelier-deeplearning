# Phase 2 : Amélioration des performances et intégration (1h30)

![Amélioration des performances](https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=1000&h=300)

## Introduction aux techniques d'optimisation (30 min)

**Objectif**: Comprendre les différentes techniques d'optimisation des modèles de Deep Learning pour les environnements à ressources limitées et les applications en production.

### Pourquoi optimiser les modèles ?

Dans un contexte d'entreprise, l'optimisation des modèles est essentielle pour plusieurs raisons :

- **Coûts d'infrastructure** : Réduire les besoins en ressources matérielles
- **Latence** : Améliorer le temps de réponse pour une meilleure expérience utilisateur
- **Énergie** : Diminuer la consommation énergétique (crucial pour les appareils mobiles)
- **Accessibilité** : Permettre l'exécution sur des appareils à ressources limitées

### Panorama des techniques d'optimisation

#### 1. Quantification

<img src="quantification-weights-optimization.svg" alt="Schéma de quantification" width="800" height="400">

La quantification consiste à réduire la précision des poids du modèle (par exemple, passer de float32 à int8). Cette technique peut réduire la taille du modèle par 4 et accélérer l'inférence, avec une perte de précision souvent négligeable.

**Comment ça marche :**
- Les poids du modèle, initialement stockés en nombres à virgule flottante 32 bits (float32), sont convertis en entiers 8 bits (int8)
- Une table de correspondance est créée pour convertir les valeurs lors de l'inférence
- Les opérations mathématiques sont effectuées sur des entiers plutôt que sur des flottants, ce qui est beaucoup plus rapide sur la plupart des processeurs

**Avantages :**
- Modèles 3-4 fois plus petits
- Inférence 2-4 fois plus rapide sur CPU
- Consommation d'énergie réduite

**Inconvénients :**
- Légère baisse de précision possible (1-2%)
- Plus sensible aux valeurs extrêmes

#### 2. Élagage (Pruning)

<img src="pruning-network-optimization.svg" alt="Schéma d'élagage" width="800" height="400">

L'élagage consiste à supprimer les connexions (poids) les moins importantes du réseau. Cette technique peut réduire la taille du modèle et accélérer l'inférence sans impact significatif sur les performances.

**Comment ça marche :**
- Pendant ou après l'entraînement, on identifie les poids qui contribuent le moins aux prédictions
- Ces poids sont mis à zéro ou complètement supprimés de la structure du réseau
- Le modèle peut être réentraîné après élagage pour récupérer une partie de la précision perdue
- Deux approches principales : élagage structuré (éliminer des neurones entiers) ou non structuré (éliminer des connexions individuelles)

**Avantages :**
- Peut réduire la taille du modèle de 75-90%
- Améliore les performances sur des appareils à mémoire limitée
- Maintient la précision si fait correctement

**Inconvénients :**
- Nécessite souvent un réentraînement après élagage
- L'accélération réelle dépend du matériel et des bibliothèques

#### 3. Distillation de connaissances

<img src="knowledge-distillation-process.svg" alt="Schéma de distillation" width="800" height="400">

La distillation consiste à entraîner un modèle plus petit (élève) à imiter un modèle plus grand et plus performant (enseignant).

**Comment ça marche :**
- Un grand modèle pré-entraîné (l'enseignant) génère des prédictions sur un ensemble de données
- Un modèle plus petit (l'élève) est entraîné à reproduire ces prédictions
- L'élève apprend non seulement les bonnes réponses finales, mais aussi les "probabilités douces" du modèle enseignant
- La fonction de perte combine généralement l'erreur de classification traditionnelle et l'erreur entre les distributions de probabilité de l'enseignant et de l'élève

**Avantages :**
- Modèles plus petits avec des performances proches du grand modèle
- Flexibilité dans le choix de l'architecture de l'élève
- Transfert des "incertitudes" du modèle enseignant qui contiennent une information précieuse

**Inconvénients :**
- Nécessite deux phases : entraînement de l'enseignant puis distillation vers l'élève
- Le choix de la fonction de perte de distillation est délicat

#### 4. Architectures efficientes

<img src="efficient-architectures-comparison.svg" alt="Comparaison d'architectures" width="800" height="400">

Utiliser des architectures spécialement conçues pour l'efficience comme MobileNet, EfficientNet ou SqueezeNet.

**Comment ça marche :**
- Les architectures efficientes utilisent des blocs de construction optimisés :
  - **Convolutions séparables en profondeur** (MobileNet) : séparent une convolution standard en deux opérations plus légères
  - **Scaling composé** (EfficientNet) : équilibre optimal entre largeur, profondeur et résolution du réseau
  - **Stratégie Fire** (SqueezeNet) : remplace les gros filtres par des couches squeeze (1x1) suivies de couches expand (1x1 et 3x3)

**Avantages :**
- Optimisées pour des dispositifs spécifiques (mobile, embarqué)
- Bon équilibre performance/taille
- Souvent disponibles comme modèles pré-entraînés

**Inconvénients :**
- Performance légèrement inférieure aux grandes architectures
- Peut nécessiter plus d'époques d'entraînement

## TP : Intégration de modèles pré-entraînés dans des applications (45 min)

### Mise en contexte : Stage en entreprise pour BTS SIO

**Scénario professionnel :**  
Vous êtes stagiaire en développement dans une boutique de commerce électronique spécialisée dans les vêtements et accessoires. L'entreprise souhaite améliorer l'expérience client avec une fonction de recherche visuelle. Le responsable technique vous demande de développer un prototype permettant aux clients de prendre une photo d'un vêtement pour trouver des articles similaires dans le catalogue.

Ce projet répond à plusieurs compétences du référentiel BTS SIO :
- **B1.3** - Développer la présence en ligne de l'organisation
- **B2.2** - Concevoir une solution applicative
- **B2.3** - Développer des composants logiciels
- **B3.1** - Tester et déployer une solution applicative

### Objectif du TP
Explorer et comprendre une application qui intègre un modèle de deep learning optimisé pour la classification de vêtements.

### Téléchargement et exploration du projet

1. [Téléchargez le projet API de recherche visuelle (ZIP)](https://example.com/download/api-vetements-ia.zip)
2. Extrayez le contenu et examinez l'arborescence du projet

### Architecture de l'application

L'application est structurée selon une architecture en couches, avec une séparation claire des responsabilités :

```
api-vetements-ia/
├── app.py                  # Point d'entrée de l'application
├── config.py               # Configuration centralisée
├── models/                 # Couche modèle et logique métier
├── utils/                  # Utilitaires et fonctions d'aide
├── static/                 # Ressources statiques (CSS, JS, images)
└── templates/              # Templates HTML pour l'interface
```

#### Principaux mécanismes à comprendre

1. **Chargement optimisé du modèle**
   - Dans `models/classifier.py`, le modèle est chargé une seule fois au démarrage de l'application
   - Un pattern singleton est utilisé pour éviter les rechargements multiples
   - Le mécanisme de "lazy loading" permet de ne charger le modèle que lorsqu'il est nécessaire

2. **Pipeline de prétraitement des images**
   - Dans `utils/image_utils.py`, on trouve les fonctions de prétraitement des images
   - Le redimensionnement, la normalisation et la standardisation sont appliqués avant l'inférence
   - La détection et gestion de différents formats d'entrée (fichier, base64) simplifie l'intégration

3. **Optimisations de performance**
   - Dans `utils/model_utils.py`, plusieurs techniques d'optimisation sont appliquées :
     - Quantification des poids pour réduire la taille du modèle
     - Fusion des opérations de batch normalization avec les couches convolutives
     - Optimisations spécifiques à TensorFlow pour l'inférence

4. **Architecture API REST**
   - L'application expose une API REST pour permettre l'intégration avec différents clients
   - Le endpoint principal `/api/predict` accepte des images en entrée et retourne les prédictions
   - Le endpoint de santé `/api/health` permet de vérifier que l'API est opérationnelle

5. **Interface utilisateur progressive**
   - L'interface web utilise JavaScript pour offrir une expérience fluide sans rechargement
   - La caméra peut être utilisée sur les appareils mobiles pour capturer directement des images
   - Des indicateurs visuels (spinner, barres de progression) informent l'utilisateur sur l'état du traitement

### Points clés à explorer dans le code

#### 1. Chargement et optimisation du modèle (`models/classifier.py`)

Le chargement du modèle est une opération coûteuse qui ne devrait être effectuée qu'une seule fois. Examinez comment :

- La classe `ClothingClassifier` implémente un pattern singleton pour partager une instance du modèle
- Le système gère un modèle de repli en cas d'échec du chargement du modèle principal
- La méthode `optimize_model_for_inference` améliore les performances d'inférence

#### 2. Prétraitement des images (`utils/image_utils.py`)

Le prétraitement correct des images est crucial pour obtenir de bonnes prédictions. Analysez comment :

- Les images sont normalisées et redimensionnées aux dimensions attendues par le modèle
- Différents formats d'entrée (fichiers, URLs, base64) sont gérés de manière transparente
- Le recadrage centré permet d'améliorer la qualité des prédictions

#### 3. API REST Flask (`app.py`)

L'API REST est le point d'entrée principal pour l'intégration. Observez comment :

- Les requêtes avec différents formats de données sont traitées
- Les erreurs sont gérées et communiquées au client de manière claire
- Les informations de performance (temps de traitement) sont mesurées et incluses dans la réponse

#### 4. Interface progressive (`static/js/app.js` et `templates/index.html`)

L'interface utilisateur est conçue pour être réactive et informative. Examinez comment :

- La capture d'image via la caméra est gérée
- L'interface affiche clairement la progression et les résultats
- Les exemples prédéfinis permettent de tester rapidement le système

### Exercices pratiques

1. **Exploration du code**
   - Parcourez les différents fichiers du projet pour comprendre leur rôle
   - Identifiez où les techniques d'optimisation vues précédemment sont appliquées
   - Repérez les mécanismes de gestion d'erreurs et de fallback

2. **Comprendre le flux de données**
   - Tracez le parcours d'une image depuis son upload jusqu'à l'affichage des prédictions
   - Identifiez les transformations appliquées à l'image
   - Repérez comment les prédictions du modèle sont converties en résultats exploitables

3. **Optimisations potentielles**
   - Réfléchissez à d'autres optimisations qui pourraient être appliquées
   - Comment améliorer encore le temps de réponse de l'API ?
   - Quelles fonctionnalités supplémentaires pourraient enrichir cette application ?

## Bonnes pratiques pour l'intégration de modèles dans des applications web (15 min)

À travers ce projet, nous avons exploré plusieurs approches pour optimiser et intégrer des modèles de Deep Learning. Résumons les bonnes pratiques essentielles à retenir:

### 1. Choix du modèle

- **Privilégier les architectures efficientes**: MobileNet, EfficientNet, SqueezeNet
- **Évaluer le compromis taille/précision**: Un petit modèle moins précis est souvent préférable à un modèle lourd inutilisable
- **Adapter la complexité au cas d'usage**: La classification d'images simples ne nécessite pas un ResNet152

### 2. Techniques d'optimisation

- **Quantification**: Toujours essayer la quantification post-entraînement
- **Élagage**: Pour les modèles plus grands, envisager l'élagage pendant l'entraînement
- **Distillation**: Pour des cas plus avancés, envisager la distillation de connaissances
- **Combinaison des techniques**: Utiliser plusieurs techniques peut donner les meilleurs résultats

### 3. Intégration côté serveur

- **Mise en cache**: Éviter de recharger le modèle pour chaque requête
- **Traitement par lot**: Regrouper les requêtes quand c'est possible
- **Gestion asynchrone**: Utiliser des files d'attente pour les requêtes intensives
- **Surveillance des performances**: Mettre en place des métriques (temps d'inférence, utilisation mémoire)

### 4. Intégration côté client

- **Prétraitement efficace**: Redimensionner les images côté client quand c'est possible
- **Feedback utilisateur**: Toujours indiquer que le traitement est en cours
- **Dégradation gracieuse**: Prévoir un comportement de repli en cas d'échec de l'IA
- **Conservation de contexte**: Limiter les allers-retours avec le serveur

### 5. Documentation et maintenance

- **Versionnement des modèles**: Suivre les versions des modèles déployés
- **Tests A/B**: Comparer les performances des différentes optimisations
- **Journalisation des erreurs**: Capturer les cas où le modèle échoue
- **Mise à jour progressive**: Planifier des améliorations incrémentales

## Conclusion et transition

Dans cette phase, nous avons exploré des techniques d'optimisation essentielles pour rendre les modèles de Deep Learning utilisables dans des applications réelles. Nous avons vu comment réduire la taille des modèles, accélérer leur inférence et les intégrer dans des applications web.

Nous avons également examiné un projet concret qui met en œuvre ces concepts dans un contexte professionnel de stage BTS SIO. En comprenant comment structurer une application qui intègre un modèle de deep learning optimisé, vous êtes maintenant mieux préparés pour développer votre propre chatbot pédagogique.

Dans la prochaine phase, nous allons nous concentrer sur la préparation spécifique du projet de chatbot, en explorant l'API Mistral AI et en définissant le cahier des charges complet.

[Retour au Module 3](index.md){ .md-button }
[Continuer vers la préparation du projet](preparation-projet.md){ .md-button .md-button--primary }