Challenge d'expérimentation guidée sur un modèle MNIST


Suivez les instructions dans le notebook pour :

- Charger le dataset MNIST (chiffres manuscrits)
- Construire un réseau de neurones simple
- Entraîner le modèle et observer son apprentissage
- Tester le modèle sur de nouvelles images

Complétez la fiche d'observations au fur et à mesure.

### Instructions étape par étape

#### Exploration des données (5 min)

- Exécutez les cellules d'importation et de chargement des données
- Observez quelques exemples d'images de chiffres manuscrits
- Notez la taille du dataset et le format des images

#### Construction du modèle (10 min)

- Identifiez la cellule qui définit l'architecture du réseau
- Observez la structure : couche d'entrée, couche cachée, couche de sortie
- Notez les dimensions et les fonctions d'activation

#### Entraînement du modèle (10 min)

- Lancez l'entraînement en exécutant la cellule correspondante
- Observez l'évolution de la précision et de la perte (loss)
- Notez le temps d'entraînement

#### Test du modèle (5 min)

- Testez le modèle sur les données de validation
- Observez la matrice de confusion (quelles classes sont confondues)
- Si disponible, utilisez l'interface de dessin pour tester vos propres chiffres

## Challenge d'expérimentation (15 min)

À vous de jouer ! Modifiez le modèle et observez les effets sur ses performances.

### Expérience 1 : Variation du nombre d'époques

- Modifiez la variable `epochs` à 5, 10 puis 20
- Observez l'impact sur la précision et le temps d'entraînement
- Question : Y a-t-il un nombre optimal d'époques ?

### Expérience 2 : Modification de l'architecture

- Changez le nombre de neurones dans la couche cachée (32, 64, 128, 256)
- Ajoutez une seconde couche cachée (un exemple est fourni en commentaire)
- Question : Une architecture plus complexe donne-t-elle toujours de meilleurs résultats ?

### Expérience 3 : Changement de la fonction d'activation

- Testez différentes fonctions d'activation ('relu', 'sigmoid', 'tanh')
- Observez l'impact sur la vitesse d'apprentissage et la précision finale
- Question : Quelle fonction d'activation semble la plus adaptée pour ce problème ?

## Conclusion et transition (5 min)

- Sauvegardez votre notebook avec vos expérimentations
- Complétez entièrement votre fiche d'observations
- Préparez-vous à partager vos découvertes

Ce que nous venons d'observer :

- Les réseaux de neurones apprennent à partir d'exemples
- Leurs performances dépendent de nombreux paramètres ajustables
- Le processus d'entraînement améliore progressivement la précision

Dans la prochaine phase, nous allons comparer cette approche avec le Machine Learning classique et comprendre plus en détail le fonctionnement des réseaux de neurones.

[Continuer vers la Phase 2 : Découverte des concepts](partie2-decouverte-concepts.md){ .md-button .md-button--primary }

## Annexe : Contenu du notebook "Hello World du Deep Learning"

Le notebook que vous allez explorer contient les sections suivantes :

### 1. Importation des bibliothèques

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
```

### 2. Chargement et préparation des données

Nous utilisons le dataset MNIST, qui contient 70 000 images de chiffres manuscrits en niveaux de gris (28x28 pixels).

```python
# Chargement des données
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Affichage des dimensions
print(f"Données d'entraînement: {x_train.shape} images, labels: {y_train.shape}")
print(f"Données de test: {x_test.shape} images, labels: {y_test.shape}")
```

Visualisation des exemples d'images :

```python
# Afficher 5 exemples d'images
plt.figure(figsize=(10, 2))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
```

Préparation des données pour l'entraînement :

```python
# Normalisation des pixels (de 0-255 à 0-1)
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Reshape des images en vecteurs (28x28 -> 784)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# One-hot encoding des labels (transformer les chiffres en vecteurs)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print("Forme des données après préparation:")
print(f"x_train: {x_train.shape}")
print(f"y_train: {y_train.shape}")
```

### 3. Construction du modèle

Nous allons créer un réseau de neurones simple avec :
- Une couche d'entrée (784 neurones pour les 784 pixels)
- Une couche cachée (64 neurones)
- Une couche de sortie (10 neurones pour les 10 chiffres)

```python
# Construction du modèle
model = keras.Sequential([
    # Couche d'entrée -> couche cachée
    layers.Dense(64, activation="relu", input_shape=(784,)),
    
    # Couche cachée -> couche de sortie
    layers.Dense(10, activation="softmax")
])

# Résumé du modèle
model.summary()
```

Compilation du modèle avec les paramètres d'entraînement :

```python
# Compilation du modèle
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

### 4. Entraînement du modèle

```python
# Définition des paramètres d'entraînement
batch_size = 128
epochs = 5

# Entraînement du modèle
history = model.fit(
    x_train, y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.1,
    verbose=1
)
```

Visualisation de l'évolution de l'entraînement :

```python
# Visualisation de l'évolution de l'entraînement
plt.figure(figsize=(12, 4))

# Évolution de la précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Entraînement')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()

# Évolution de la perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Entraînement')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Perte (Loss)')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()

plt.tight_layout()
plt.show()
```

### 5. Évaluation du modèle

```python
# Évaluation sur les données de test
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Précision sur les données de test: {test_acc:.4f}")
```

Examen détaillé des prédictions :

```python
# Faire des prédictions
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# Matrice de confusion
plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_true_classes, y_pred_classes)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédiction')
plt.ylabel('Réalité')
plt.title('Matrice de confusion')
plt.show()

# Rapport de classification
print("Rapport de classification :")
print(classification_report(y_true_classes, y_pred_classes))
```

### 6. Visualisation des prédictions

```python
# Sélectionner quelques exemples aléatoires
num_examples = 5
example_indices = np.random.choice(len(x_test), num_examples, replace=False)

plt.figure(figsize=(15, 3))
for i, idx in enumerate(example_indices):
    # Afficher l'image
    plt.subplot(1, num_examples, i+1)
    img = x_test[idx].reshape(28, 28)
    plt.imshow(img, cmap='gray')
    
    # Prédiction
    pred = y_pred[idx]
    pred_class = np.argmax(pred)
    true_class = y_true_classes[idx]
    
    # Titre avec prédiction et confiance
    title = f"Prédit: {pred_class}\n"
    title += f"Réel: {true_class}\n"
    title += f"Confiance: {pred[pred_class]:.2f}"
    plt.title(title, color=("green" if pred_class == true_class else "red"))
    plt.axis('off')

plt.tight_layout()
plt.show()
```

### 7. Expérimentations

```python
# Modifier le nombre d'époques
# epochs = 10  # Essayez avec 5, 10, 20 époques

# Modifier l'architecture du réseau
"""
model = keras.Sequential([
    # Couche d'entrée -> première couche cachée
    layers.Dense(128, activation="relu", input_shape=(784,)),
    
    # Deuxième couche cachée (ajout d'une couche)
    layers.Dense(64, activation="relu"),
    
    # Couche cachée -> couche de sortie
    layers.Dense(10, activation="softmax")
])
"""

# Changer la fonction d'activation
"""
model = keras.Sequential([
    # Essayez avec 'relu', 'sigmoid', 'tanh'
    layers.Dense(64, activation="tanh", input_shape=(784,)),
    layers.Dense(10, activation="softmax")
])
"""
```

### 8. Interface de dessin interactive

Le notebook inclut une interface de dessin permettant de tester le modèle avec vos propres dessins de chiffres (disponible dans Google Colab).