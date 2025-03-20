
```markdown
# Instructions d'intégration pour les scripts de Deep Learning

Ce guide détaille l'installation, la configuration et l'utilisation des scripts d'intégration de Deep Learning fournis dans le cadre du cours. Ces scripts vous permettent d'explorer l'intégration des modèles de Deep Learning dans des applications web et des API.

## 1. Intégration avec l'API Mistral (`api-integration.py`)

Ce script permet d'interagir avec l'API Mistral AI pour générer des explications sur les concepts de Deep Learning.

### Prérequis

- Python 3.7 ou supérieur
- Compte sur la plateforme Mistral AI avec une clé API

### Installation

1. **Installer les dépendances requises**:

   ```bash
   pip install flask requests python-dotenv
   ```

2. **Configurer la clé API**:

   - Créez un fichier `.env` dans le même répertoire que le script
   - Ajoutez votre clé API Mistral:
     ```
     MISTRAL_API_KEY=votre_clé_api_réelle
     ```

### Utilisation

1. **Lancer l'application**:

   ```bash
   python api-integration.py
   ```

2. **Accéder à l'application web**:

   - Ouvrez votre navigateur et accédez à `http://localhost:5000`
   - Entrez un concept de Deep Learning à expliquer
   - Sélectionnez le niveau de difficulté
   - Cliquez sur "Expliquer" pour obtenir une explication générée par Mistral AI

### Fonctionnalités principales

- **Saisie de concepts**: Permet d'entrer n'importe quel concept lié au Deep Learning
- **Niveaux de difficulté**: Propose des explications adaptées à différents niveaux (débutant, intermédiaire, avancé)
- **Interface utilisateur simple**: Facilite l'interaction avec l'API Mistral

### Structure du code

- **Fonction `mistral_chat_completion()`**: Gère l'appel à l'API Mistral
- **Fonction `explain_deep_learning_concept()`**: Crée un prompt structuré pour obtenir des explications pédagogiques
- **App Flask**: Fournit une interface web pour interagir avec l'API

## 2. Intégration d'un CNN dans une application web (`web-integration.py`)

Ce script démontre comment intégrer un modèle CNN entraîné dans une application web Flask pour la reconnaissance de chiffres manuscrits.

### Prérequis

- Python 3.7 ou supérieur
- TensorFlow 2.x

### Installation

1. **Installer les dépendances requises**:

   ```bash
   pip install flask tensorflow pillow matplotlib numpy
   ```

2. **Préparation du modèle**:

   - Idéalement, utilisez un modèle `cnn_mnist_model.h5` généré à partir du notebook CNN
   - Si non disponible, le script créera automatiquement un modèle simple

### Utilisation

1. **Lancer l'application**:

   ```bash
   python web-integration.py
   ```

2. **Accéder à l'application web**:

   - Ouvrez votre navigateur et accédez à `http://localhost:5001`
   - Uploadez une image de chiffre manuscrit (ou utilisez la fonction glisser-déposer)
   - Cliquez sur "Analyser l'image" pour obtenir la prédiction
   - Consultez la visualisation et les détails techniques

### Fonctionnalités principales

- **Upload d'images**: Supporte l'upload et le glisser-déposer d'images
- **Prétraitement automatique**: Convertit et normalise les images pour le modèle CNN
- **Visualisation**: Affiche les probabilités de prédiction pour chaque chiffre
- **Métriques de performance**: Indique le temps d'inférence et le niveau de confiance

### Structure du code

- **Fonction `preprocess_image()`**: Prépare les images pour le modèle
- **Fonction `generate_prediction_visualization()`**: Crée des visualisations des prédictions
- **Route `/predict`**: API REST pour soumettre des images et obtenir des prédictions
- **Interface utilisateur**: Frontend en HTML/CSS/JavaScript pour interagir avec l'API

## Exercices d'extension

### Pour l'API Mistral

1. **Historique de conversation**:
   - Modifiez le script pour maintenir un contexte de conversation
   - Permettez au modèle de se référer aux questions précédentes

2. **Amélioration des prompts**:
   - Expérimentez avec différentes structures de prompts
   - Mesurez l'impact sur la qualité et la pertinence des explications

3. **Fonctionnalités pédagogiques avancées**:
   - Ajoutez une option pour générer des quiz sur les concepts
   - Implémentez un système de niveaux d'apprentissage progressifs

### Pour l'intégration web CNN

1. **Outil de dessin**:
   - Ajoutez un canvas HTML5 permettant de dessiner des chiffres directement
   - Intégrez la conversion du dessin en image pour l'analyse

2. **Comparaison de modèles**:
   - Ajoutez la possibilité de charger différents modèles CNN
   - Créez une interface permettant de comparer leurs performances

3. **Feedback utilisateur**:
   - Implémentez un mécanisme pour signaler les prédictions incorrectes
   - Créez un système de collecte de données pour améliorer le modèle

## Résolution des problèmes courants

### API Mistral

| Problème | Solution |
|----------|----------|
| "Clé API invalide" | Vérifiez que la clé est correctement copiée dans le fichier `.env` |
| Timeout de la requête | Augmentez le timeout dans `requests.post()` ou réduisez `max_tokens` |
| Erreur "model not found" | Vérifiez que le nom du modèle est correct (mistral-tiny, mistral-small, etc.) |

### Application Web CNN

| Problème | Solution |
|----------|----------|
| "Modèle non trouvé" | Vérifiez le chemin vers le fichier `.h5` ou laissez le modèle par défaut se créer |
| Image non reconnue | Assurez-vous que l'image est en noir et blanc avec un bon contraste |
| Application lente | Réduisez la taille du modèle ou optimisez le prétraitement des images |

## Bonnes pratiques pour l'intégration de modèles

1. **Séparation des préoccupations**:
   - Séparez le code du modèle, du prétraitement et de l'interface utilisateur
   - Utilisez des classes et des modules pour organiser votre code

2. **Gestion de l'environnement**:
   - Utilisez des variables d'environnement pour les clés et configurations
   - Documentez clairement les dépendances requises

3. **Retour utilisateur**:
   - Fournissez des feedback visuels pendant le chargement/traitement
   - Proposez des messages d'erreur clairs et des suggestions de résolution

4. **Performances**:
   - Optimisez le chargement du modèle (chargez-le une seule fois au démarrage)
   - Utilisez du caching pour les opérations répétitives

## Lien avec le projet chatbot pédagogique

Ces scripts d'intégration constituent des briques fondamentales pour le développement du chatbot pédagogique:

- **API Mistral**: Servira de moteur de génération pour les explications pédagogiques
- **Intégration web**: Fournit un modèle pour l'interface utilisateur du chatbot
- **Patterns d'API REST**: Démontre comment structurer les échanges client-serveur

En maîtrisant ces scripts, vous acquerrez les compétences nécessaires pour développer efficacement le projet fil rouge du chatbot pédagogique sur le Deep Learning.
```

Ce document complet fournit toutes les informations nécessaires pour que les étudiants puissent installer, configurer et utiliser les scripts d'intégration. Il inclut également des exercices d'extension, des conseils pour la résolution des problèmes courants et établit clairement le lien avec le projet de chatbot pédagogique.