# Phase 1 : Mini-projet CNN pour la vision par ordinateur

![CNN Architecture](https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la phase

Dans cette phase, vous allez :

- Comprendre les principes fondamentaux des réseaux de neurones convolutifs (CNN)
- Implémenter un CNN pour la classification d'images avec TensorFlow/Keras
- Visualiser et interpréter les filtres et feature maps d'un CNN
- Intégrer un modèle CNN dans une application web simple

## Partie 1: Principes des CNN (20 min)

### Architecture d'un CNN

Les réseaux de neurones convolutifs (CNN) sont spécialement conçus pour traiter des données structurées en grille, comme les images. Leur architecture s'inspire du cortex visuel biologique et comprend plusieurs types de couches spécialisées :

1. **Couches de convolution** : appliquent des filtres qui glissent sur l'image pour détecter des motifs locaux (contours, textures, etc.)
2. **Couches de pooling** : réduisent la dimension spatiale pour diminuer le nombre de paramètres
3. **Couches fully connected** : combinent les caractéristiques extraites pour la classification finale

Avantages majeurs pour un développeur d'applications :

- Réduction significative du nombre de paramètres (partage de poids)
- Invariance à la translation (détection de motifs quelle que soit leur position)
- Capacité d'extraire automatiquement des caractéristiques pertinentes

## Partie 2: Implémentation d'un CNN pour MNIST (40 min)

### Instructions

1. Ouvrez le notebook Jupyter [cnn-classification](ressources/cnn-classification.md) dans Google Colab
2. Suivez les instructions étape par étape pour implémenter un CNN pour la classification des chiffres manuscrits (MNIST)
3. Exécutez chaque cellule et observez les résultats
4. Portez une attention particulière aux sections suivantes :
   - Architecture du modèle CNN
   - Processus d'entraînement
   - Visualisation des filtres et feature maps
   - Analyse des performances et des erreurs

### Points clés à explorer

- Comment les couches de convolution extraient-elles des caractéristiques de plus en plus abstraites ?
- Quel est l'impact du nombre de filtres et de couches sur les performances ?
- Comment les feature maps révèlent-elles ce que "voit" le réseau ?
- Quelles sont les limites du modèle face à des données bruitées ou déformées ?

## Partie 3: Intégration dans une application web (30 min)

Dans cette partie, vous allez découvrir comment intégrer un modèle CNN pré-entraîné dans une application web interactive.

### Étape 1: Préparation de l'environnement

1.  **Sauvegarde du modèle CNN** :
    * Assurez-vous que votre modèle CNN entraîné lors de la Partie 2 est correctement sauvegardé. Utilisez le code Python suivant pour le sauvegarder :

    ```python
    cnn_model.save('mnist_cnn_model.h5')
    ```

    * Ce code créera un fichier nommé `mnist_cnn_model.h5` contenant les poids et l'architecture de votre modèle.
    * **Note importante :** Vérifiez que le fichier `mnist_cnn_model.h5` est bien créé dans le même répertoire que votre script Python.
    * Si vous travaillez dans Google Colab : Après avoir sauvegardé le modèle, vous devez télécharger le fichier sur votre ordinateur local. Exécutez ce code supplémentaire :
```
from google.colab import files
files.download('mnist_cnn_model.h5')
```


2.  **Téléchargement des fichiers de l'application web** :
    * Téléchargez les fichiers suivants nécessaires à l'application web et placez-les dans les dossiers indiqués :
        * [web-integration.py](code-app-web/web-integration.py) - Script principal de l'application Flask.
        * [templates/index.html](code-app-web/index.html) - Template HTML pour l'interface utilisateur.
        * [static/css/style.css](code-app-web/style.css) - Feuille de style CSS.
        * [static/js/app.js](code-app-web/app.js) - Script JavaScript pour l'interactivité.

3.  **Structure des dossiers** :

   *Assurez-vous que votre structure de dossiers est la suivante:
   
   ```
   votre_dossier_de_travail/
   ├── mnist_cnn_model.h5      # Votre modèle sauvegardé ou le modèle fourni
   ├── web-integration.py      # Script principal Flask
   ├── templates/              # Dossier pour les templates HTML
   │   └── index.html
   └── static/                 # Dossier pour CSS, JS, images
       ├── css/
       │   └── style.css
       └── js/
           └── app.js
   ```

### Étape 2: Installation des dépendances requises

Ouvrez un terminal et exécutez:

```bash
pip install flask tensorflow pillow matplotlib numpy
```
Note pour Windows: Si vous rencontrez des problèmes avec TensorFlow, essayez pip install tensorflow==2.9.0.
### Étape 3: Exécution de l'application web

1. Dans le terminal, naviguez vers votre dossier de travail
2. Exécutez la commande:
   ```bash
   python web-integration.py
   ```
3. Vous devriez voir un message indiquant que l'application est en cours d'exécution
4. Ouvrez votre navigateur et accédez à: http://localhost:5001

### Étape 4: Test de l'application

1. L'interface vous permet de:
   - Dessiner un chiffre manuellement ou uploader une image
   - Soumettre l'image pour prédiction
   - Voir la prédiction du modèle
   - Explorer les visualisations des feature maps

2. Testez l'application en dessinant différents chiffres

### Étape 5: Analyse du code source

Ouvrez le fichier [web-integration.py](../ressources/code/web-integration.py) et examinez:

1. **Chargement du modèle**: Identifiez la section où le modèle CNN est chargé
   ```python
   # Recherchez un code similaire à:
   model = load_model('mnist_cnn_model.h5')
   ```

2. **Prétraitement des images**: Examinez comment les images sont prétraitées
   ```python
   # Recherchez la fonction qui fait le prétraitement:
   def preprocess_image(image_data):
       # ...
   ```

3. **API Flask**: Identifiez les routes Flask et leur fonction
   ```python
   # Routes comme:
   @app.route('/predict', methods=['POST'])
   def predict():
       # ...
   ```

4. **Interaction frontend-backend**: Ouvrez `static/js/app.js` et examinez comment les requêtes sont envoyées au serveur
  
### Étape 6 : Défis et questions à ajouter

Pour approfondir l'apprentissage, ajoutez ces défis:

### Défis à réaliser (pour les plus rapides)

1. **Amélioration de l'interface**: Modifiez le fichier HTML/CSS pour améliorer l'expérience utilisateur
   
2. **Ajout de fonctionnalités**: Implémentez une de ces fonctionnalités supplémentaires:
   - Historique des prédictions
   - Visualisation de la matrice de confusion en temps réel
   - Option pour appliquer des transformations à l'image (rotation, flou)
   
3. **Optimisation du modèle**: Modifiez le code pour charger un modèle plus léger (quantifié ou pruné)

### Questions à répondre

1. Quels avantages offre l'utilisation de Flask pour exposer un modèle de Deep Learning?
2. Quels sont les défis liés au déploiement de modèles de Deep Learning dans des applications web?
3. Comment pourriez-vous améliorer les performances de l'application pour gérer plus d'utilisateurs simultanément?
4. Quelles mesures de sécurité devriez-vous implémenter avant de déployer cette application en production?


# Ressources complémentaires

- [Tutoriel TensorFlow sur les CNN](https://www.tensorflow.org/tutorials/images/cnn) - Guide officiel de TensorFlow sur l'implémentation des réseaux de neurones convolutifs
- [Visualisation de CNN (Distill.pub)](https://distill.pub/2017/feature-visualization/) - Article interactif sur la visualisation et l'interprétation des réseaux convolutifs
- [Documentation Flask](https://flask.palletsprojects.com/en/2.3.x/) - Documentation officielle du framework Flask pour le développement web


Retour à la Séance 2{ .md-button }
Continuer vers la Phase 2: RNN{ .md-button .md-button--primary }