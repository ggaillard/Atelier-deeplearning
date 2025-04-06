# Phase 2 : Atelier pratique TensorFlow/Keras (40 min)

![Atelier TensorFlow/Keras](https://images.unsplash.com/photo-1526649661456-89c7ed4d00b8?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectif

Découvrir par la pratique l'utilisation de TensorFlow/Keras pour créer rapidement un modèle fonctionnel.

## Installation et configuration (5 min)

Bonne nouvelle: nous allons utiliser Google Colab, donc aucune installation nécessaire!

1. Ouvrez le notebook "TensorFlow/Keras pour débutants" dans Google Colab
2. Le lien est disponible ici: [tensorflow-keras-debutants.ipynb](ressources/tensorflow-keras-debutants.ipynb)
3. Tout est préconfiguré, il suffit d'exécuter les cellules

Si vous souhaitez installer localement plus tard:
```bash
# Avec pip
pip install tensorflow

# Vérification
import tensorflow as tf
print(tf.__version__)
```

## Structure d'un projet TensorFlow/Keras (10 min)

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

## Exercice guidé: Créer votre premier modèle (25 min)

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

## Conclusion

Cet atelier vous a permis de prendre en main TensorFlow/Keras et de créer votre premier modèle de Deep Learning. Dans la prochaine phase, nous allons voir comment transformer ce modèle en une API utilisable dans un projet réel.

[Passer à la Phase 3](partie3-api-reconnaissance.md){ .md-button .md-button--primary }