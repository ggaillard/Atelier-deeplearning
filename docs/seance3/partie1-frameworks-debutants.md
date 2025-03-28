# Phase 1 : Frameworks pour débutants (1h30)

## Introduction aux frameworks dans un contexte professionnel (15 min)

**Objectif**: Comprendre l'utilité des frameworks de Deep Learning pour un développeur en entreprise et identifier ceux qui sont réellement utilisés sur le terrain.

### Les frameworks en entreprise

Avant de plonger dans le code, prenons un moment pour comprendre pourquoi les frameworks de Deep Learning sont si importants en contexte professionnel:

- **Productivité**: Ils permettent de développer des applications d'IA sans repartir de zéro
- **Maintenabilité**: Code plus standard, plus facile à comprendre par d'autres développeurs
- **Performances**: Optimisations intégrées qui seraient complexes à développer soi-même
- **Déploiement**: Outils intégrés pour mettre en production les modèles

Dans le monde professionnel actuel, plusieurs frameworks de Deep Learning sont couramment utilisés:

| Framework | Principaux cas d'usage |
|-----------|------------------------|
| TensorFlow/Keras | Applications web/mobile, systèmes en production |
| PyTorch | Recherche, prototypage, startups |
| Hugging Face | NLP, chatbots, traitement de texte |
| Scikit-learn | Prétraitement, ML classique, pipeline de données |

> "Pour un stage, la capacité à utiliser efficacement des frameworks existants est recherchée davantage que l'expertise théorique approfondie en Deep Learning." 
> 

### TensorFlow/Keras: la solution pragmatique

Pour cette séance, nous allons nous concentrer sur TensorFlow/Keras pour plusieurs raisons:

1. **Interface simple**: Keras offre une API haut niveau, parfaite pour débuter
2. **Déploiement facile**: Solutions intégrées pour mettre en production (TF Serving, TFLite)
3. **Documentation riche**: Ressources abondantes en français
4. **Modèles pré-entraînés**: Large bibliothèque de modèles prêts à l'emploi
5. **Demande professionnelle**: Le plus mentionné dans les offres de stage

### Démonstration: Applications réelles en entreprise

Voici quelques exemples concrets développés par des entreprises locales employant des anciens étudiants:

- **PME de logistique**: Application de reconnaissance de documents (bons de livraison, factures) permettant d'automatiser la saisie → Économie de 15h/semaine
- **Agence web**: Système de détection de contenu inapproprié dans les commentaires de sites e-commerce
- **Cabinet médical**: Application de classification d'images pour le tri préliminaire de photos de lésions cutanées

## Atelier: Prise en main de TensorFlow/Keras (40 min)

**Objectif**: Découvrir par la pratique l'utilisation de TensorFlow/Keras pour créer rapidement un modèle fonctionnel.

### Installation et configuration (5 min)

Bonne nouvelle: nous allons utiliser Google Colab, donc aucune installation nécessaire!

1. Ouvrez le notebook "TensorFlow/Keras pour débutants" dans Google Colab
2. Le lien est disponible ici: [tensorflow-keras-debutants.ipynb](https://colab.research.google.com/drive/...)
3. Tout est préconfiguré, il suffit d'exécuter les cellules

Si vous souhaitez installer localement plus tard:
```bash
# Avec pip
pip install tensorflow

# Vérification
import tensorflow as tf
print(tf.__version__)
```

### Structure d'un projet TensorFlow/Keras (10 min)

Explorons ensemble la structure typique d'un projet avec TensorFlow/Keras:

1. **Importation des bibliothèques**
   ```python
   import tensorflow as tf
   from tensorflow.keras import layers, models
   import numpy as np
   import matplotlib.pyplot as plt
   ```

2. **Préparation des données**
   ```python
   # Chargement de données (ex: MNIST - chiffres manuscrits)
   (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
   
   # Normalisation (ramener les valeurs entre 0 et 1)
   train_images = train_images / 255.0
   test_images = test_images / 255.0
   ```

3. **Création du modèle**
   ```python
   model = models.Sequential([
       layers.Flatten(input_shape=(28, 28)),      # Aplatit l'image 28x28 en un vecteur
       layers.Dense(128, activation='relu'),      # Couche cachée avec 128 neurones
       layers.Dense(10, activation='softmax')     # Couche de sortie (10 chiffres)
   ])
   ```

4. **Compilation du modèle**
   ```python
   model.compile(
       optimizer='adam',                           # Algorithme d'optimisation
       loss='sparse_categorical_crossentropy',     # Fonction de perte
       metrics=['accuracy']                        # Métrique à suivre
   )
   ```

5. **Entraînement**
   ```python
   model.fit(
       train_images, 
       train_labels, 
       epochs=5,                  # Nombre de passages sur les données
       batch_size=32,             # Taille des lots
       validation_split=0.2       # 20% des données pour la validation
   )
   ```

6. **Évaluation**
   ```python
   test_loss, test_acc = model.evaluate(test_images, test_labels)
   print(f'Précision sur données de test: {test_acc:.2f}')
   ```

7. **Prédiction et utilisation**
   ```python
   predictions = model.predict(test_images[:5])
   print("Prédictions:", np.argmax(predictions, axis=1))
   print("Valeurs réelles:", test_labels[:5])
   ```

8. **Sauvegarde du modèle**
   ```python
   model.save('mon_modele.h5')  # Format HDF5
   # ou
   model.save('dossier_modele')  # Format SavedModel (pour TF Serving)
   ```

### Exercice guidé: Créer votre premier modèle (25 min)

Suivez les instructions dans le notebook Colab pour:

1. **Explorer le jeu de données Fashion MNIST**
   - 10 catégories de vêtements (t-shirts, pantalons, etc.)
   - Images 28x28 en niveaux de gris
   - Parfait pour commencer avec la classification d'images

2. **Construire un modèle simple**
   - Modèle séquentiel avec 2-3 couches
   - Visualiser l'architecture avec `model.summary()`

3. **Entraîner et évaluer le modèle**
   - Observer les courbes d'apprentissage (accuracy, loss)
   - Comprendre le phénomène de surapprentissage

4. **Faire des prédictions**
   - Tester le modèle sur de nouvelles images
   - Visualiser les résultats avec des graphiques

5. **Modifier le modèle pour l'améliorer**
   - Ajouter/supprimer des couches
   - Changer le nombre de neurones
   - Observer l'impact sur les performances

## Mini-projet: Créer une API de reconnaissance d'images (35 min)

**Objectif**: Transformer votre modèle en un service web utilisable dans un projet réel.

### Qu'est-ce qu'une API et pourquoi c'est important (5 min)

- Une **API** (Application Programming Interface) permet à différents logiciels de communiquer entre eux
- Dans le monde professionnel, les modèles ML sont rarement utilisés directement - ils sont exposés via des API
- Avantages:
  - Séparation du frontend et du backend
  - Réutilisation du modèle par plusieurs applications
  - Mise à jour du modèle sans toucher aux applications clientes
  - Scalabilité indépendante

### Structure d'une API Flask pour l'IA (10 min)

Voici la structure de base d'une API Flask qui expose un modèle TensorFlow:

```python
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Charger le modèle pré-entraîné
model = tf.keras.models.load_model('mon_modele.h5')

# Classes pour Fashion MNIST
class_names = ['T-shirt/top', 'Pantalon', 'Pull', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Basket', 'Sac', 'Bottine']

@app.route('/predict', methods=['POST'])
def predict():
    # Vérifier si la requête contient un fichier
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image trouvée'}), 400
    
    # Récupérer l'image
    file = request.files['image']
    img_bytes = file.read()
    
    try:
        # Prétraitement de l'image
        image = Image.open(io.BytesIO(img_bytes)).convert('L')  # Convertir en niveaux de gris
        image = image.resize((28, 28))  # Redimensionner à 28x28
        image_array = np.array(image) / 255.0  # Normaliser
        image_array = image_array.reshape(1, 28, 28)  # Ajouter dimension batch
        
        # Faire la prédiction
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])
        
        # Préparer la réponse
        result = {
            'class': class_names[predicted_class],
            'class_id': int(predicted_class),
            'confidence': confidence
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Travail pratique: Développer votre API (20 min)

Suivez les instructions dans le notebook "API de reconnaissance d'images":

1. **Entraîner ou charger un modèle pré-entraîné**
   - Utilisez soit le modèle que vous venez de créer
   - Soit chargez un modèle pré-entraîné (plus rapide)

2. **Créer l'API Flask**
   - Compléter les sections manquantes dans le template fourni
   - Ajouter la logique de prétraitement des images
   - Implémenter la fonction de prédiction

3. **Tester l'API**
   - Utiliser l'outil de test intégré dans Colab
   - Envoyer des images et vérifier les réponses

4. **Ajouter des fonctionnalités (si le temps le permet)**
   - Endpoint `/info` pour obtenir des informations sur le modèle
   - Gestion de plusieurs formats d'image
   - Limitation du nombre de requêtes

## Conclusion et transition (5 min)

### Ce que nous avons appris

- Les frameworks de Deep Learning les plus utilisés en entreprise
- Comment créer rapidement un modèle avec TensorFlow/Keras
- Comment exposer un modèle via une API REST
- Les bonnes pratiques pour un projet d'IA en production

### Pourquoi c'est important pour votre stage

Ces compétences sont directement applicables dans un contexte professionnel:
- Vous pouvez désormais créer une application IA simple mais complète
- Vous avez une API fonctionnelle à montrer lors d'entretiens
- Vous comprenez le workflow complet d'un projet d'IA

### Pour aller plus loin

- Explorer les modèles pré-entraînés plus avancés (MobileNet, ResNet, etc.)
- Apprendre à déployer une API sur un service cloud (Heroku, Google Cloud)
- S'initier au transfert learning pour adapter des modèles à vos données

### Prochaine étape

Dans la prochaine phase, nous allons voir comment améliorer les performances de votre modèle sans avoir besoin de connaissances mathématiques avancées.

[Passer à la Phase 2](partie2-amelioration.md){ .md-button .md-button--primary }