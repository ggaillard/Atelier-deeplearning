# Module 3 : Pratique TensorFlow/Keras pour BTS SIO

## Introduction

Ce module est entièrement axé sur la pratique et conçu spécifiquement pour des étudiants de BTS SIO. Vous allez apprendre à utiliser TensorFlow/Keras à travers des exercices concrets, avec deux options disponibles :
- Version Google Colab (aucune installation requise)
- Version locale (pour ceux qui souhaitent installer les outils sur leur machine)

## Prérequis

### Pour la version Google Colab
- Un compte Google
- Navigateur web récent
- Aucune installation requise

### Pour la version locale
- Python 3.7 ou supérieur installé
- Pip (gestionnaire de paquets Python)
- Éditeur de code (VS Code recommandé)

## Partie 1 : Premier modèle avec TensorFlow/Keras (1h30)

### Objectifs
- Comprendre les bases de TensorFlow/Keras
- Créer et entraîner un modèle simple
- Visualiser les résultats

### Version Google Colab

1. **Accès au notebook**
   - Cliquez sur ce lien pour ouvrir le notebook : [TensorFlow Débutant - Colab](https://colab.research.google.com/drive/...)
   - Faites une copie dans votre Drive en cliquant sur "Fichier > Enregistrer une copie dans Drive"

2. **Contenu du notebook**
   - Introduction à TensorFlow/Keras
   - Chargement du dataset MNIST (chiffres manuscrits)
   - Création d'un modèle de base
   - Entraînement et évaluation
   - Visualisation des résultats

3. **Exercices pratiques dans le notebook**
   - Modifier le nombre de neurones
   - Changer la fonction d'activation
   - Ajouter des couches supplémentaires
   - Observer l'impact sur la précision

### Version locale

1. **Installation**
   ```bash
   # Créer un environnement virtuel
   python -m venv tf_env
   
   # Activer l'environnement
   # Pour Windows
   tf_env\Scripts\activate
   # Pour macOS/Linux
   source tf_env/bin/activate
   
   # Installer les paquets nécessaires
   pip install tensorflow numpy matplotlib jupyter
   ```

2. **Téléchargement du script**
   - Téléchargez [tf_debutant.py](lien_vers_script) 
   - Placez-le dans votre dossier de travail

3. **Exécution du script**
   ```bash
   python tf_debutant.py
   ```

4. **Exercices pratiques**
   Le script contient des sections commentées avec "EXERCICE" où vous devrez:
   - Modifier les hyperparamètres
   - Ajouter des couches au modèle
   - Changer les fonctions d'activation
   - Exécuter le script après chaque modification et observer les résultats

## Partie 2 : Reconnaissance d'images en pratique (1h30)

### Objectifs
- Utiliser un modèle plus avancé pour la reconnaissance d'images
- Comprendre le concept de modèle pré-entraîné
- Créer une interface simple pour tester le modèle

### Version Google Colab

1. **Accès au notebook**
   - Ouvrez ce notebook : [Reconnaissance d'images - Colab](https://colab.research.google.com/drive/...)
   - Faites une copie dans votre Drive

2. **Contenu du notebook**
   - Chargement d'un modèle pré-entraîné (MobileNetV2)
   - Prétraitement d'images
   - Classification d'images test
   - Création d'une interface avec les widgets Colab

3. **Exercices pratiques**
   - Tester le modèle avec vos propres images
   - Modifier les paramètres de prétraitement
   - Comparer différents modèles pré-entraînés
   - Créer un tableau de résultats comparatifs

### Version locale

1. **Installation des dépendances supplémentaires**
   ```bash
   pip install pillow matplotlib
   ```

2. **Téléchargement des fichiers**
   - Téléchargez [image_classifier.zip](api-vetements-ia.zip)
   - Décompressez l'archive dans votre dossier de travail

3. **Structure du projet**
   ```
   image_classifier/
   ├── classifier.py         # Script principal
   ├── images/               # Dossier pour vos images test
   │   ├── sample1.jpg
   │   ├── sample2.jpg
   │   └── ...
   └── utils/                # Utilitaires Python
       ├── model_loader.py   # Chargement du modèle
       └── preprocessing.py  # Prétraitement des images
   ```

4. **Exécution du script**
   ```bash
   cd image_classifier
   python classifier.py
   ```
   
   Le script vous demandera de sélectionner une image dans le dossier images/ et affichera les résultats dans une fenêtre graphique avec matplotlib.

5. **Exercices pratiques**
   - Compléter les fonctions marquées "TODO" dans classifier.py
   - Ajouter une fonction pour afficher le top 5 des prédictions
   - Créer une fonction pour comparer plusieurs images côte à côte
   - Implémenter un système simple de batch processing pour traiter plusieurs images

## Partie 3 : Mini-projet - Classificateur d'images personnalisé (1h)

### Objectifs
- Adapter un modèle pré-entraîné à vos propres données
- Comprendre le concept de transfer learning
- Créer un classificateur personnalisé

### Version Google Colab

1. **Accès au notebook**
   - Ouvrez ce notebook : [Classificateur personnalisé - Colab](https://colab.research.google.com/drive/...)
   - Faites une copie dans votre Drive

2. **Contenu du notebook**
   - Préparation d'un petit dataset personnalisé (fourni)
   - Application du transfer learning sur MobileNetV2
   - Entraînement du modèle adapté
   - Test et évaluation des performances

3. **Dataset fourni**
   Le notebook télécharge automatiquement un petit dataset contenant 3 catégories:
   - Téléphones portables
   - Ordinateurs portables
   - Tablettes

4. **Exercices pratiques**
   - Adapter le code pour utiliser votre propre petit dataset (10-15 images par classe)
   - Modifier les paramètres d'entraînement
   - Expérimenter avec différents modèles de base
   - Créer une matrice de confusion pour analyser les erreurs

### Version locale

1. **Téléchargement des ressources**
   - Téléchargez [mini_projet_classificateur.zip](lien_vers_archive)
   - Décompressez l'archive dans votre dossier de travail

2. **Structure des fichiers**
   ```
   mini_projet_classificateur/
   ├── custom_classifier.py      # Script principal
   ├── data_loader.py            # Chargement des données
   ├── visualization.py          # Visualisations
   ├── dataset/                  # Dataset à télécharger
   │   ├── telephones/           # 15 images
   │   ├── ordinateurs/          # 15 images
   │   └── tablettes/            # 15 images
   └── README.md                 # Instructions détaillées
   ```

3. **Exécution du projet**
   ```bash
   cd mini_projet_classificateur
   python custom_classifier.py
   ```

   Le script vous guidera à travers les étapes de transfer learning avec une interface en ligne de commande.

4. **Exercices pratiques**
   - Compléter les parties manquantes dans custom_classifier.py
   - Modifier les fonctions de data augmentation pour améliorer la généralisation
   - Implémenter une visualisation avec matplotlib des résultats d'entraînement
   - Ajouter un mode de test pour évaluer le modèle sur de nouvelles images

## Évaluation des compétences

À la fin de ce module pratique, vous serez évalué sur:

1. **Compréhension technique**
   - Capacité à modifier et adapter les modèles
   - Compréhension des concepts clés (couches, fonctions d'activation, etc.)

2. **Réalisation pratique**
   - Fonctionnalité des exercices complétés
   - Qualité du code produit
   - Interface utilisateur (pour la version locale)

3. **Analyse et amélioration**
   - Pertinence des modifications apportées
   - Analyse des résultats
   - Propositions d'amélioration

## Ressources supplémentaires

### Documentation officielle
- [TensorFlow pour débutants](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [Guide Keras](https://keras.io/guides/)

### Tutoriels vidéo
- [Premiers pas avec TensorFlow](https://www.youtube.com/watch?v=...)
- [Transfer Learning expliqué simplement](https://www.youtube.com/watch?v=...)

### Aide en cas de problème
- Forum d'entraide: [forum.bts-sio.net](http://forum.bts-sio.net)
- Canal Discord de la classe

## Conclusion

Ce module pratique vous a permis de mettre en œuvre les concepts du Deep Learning avec TensorFlow/Keras. Vous avez créé et adapté des modèles, les avez testés sur des données réelles et avez développé des interfaces pour les utiliser. Ces compétences pratiques sont directement transférables en milieu professionnel, notamment pour des stages en développement d'applications ou en analyse de données.