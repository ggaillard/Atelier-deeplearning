# CNN pour la classification d'images - MNIST

Ce document contient le code et les explications pour le notebook de classification d'images MNIST avec un CNN. Vous pouvez copier-coller chaque section dans une cellule Google Colab.

## Cellule 1 (Markdown) - Introduction

```markdown
# CNN pour la classification d'images - MNIST

## BTS SIO SLAM - Séance 2: Types de réseaux de neurones

Ce notebook vous guidera à travers l'implémentation et l'utilisation d'un réseau de neurones convolutif (CNN) pour la classification d'images, en utilisant le célèbre dataset MNIST des chiffres manuscrits.

### Objectifs d'apprentissage:
- Comprendre l'architecture d'un réseau convolutif (CNN)
- Implémenter un CNN avec TensorFlow/Keras
- Visualiser les filtres et feature maps
- Analyser les performances du modèle

### Prérequis:
- Connaissances de base en Python
- Avoir suivi la séance 1 d'introduction au Deep Learning
```

## Cellule 2 (Markdown) - Configuration

```markdown
## 1. Configuration de l'environnement

Commençons par importer les bibliothèques nécessaires.
```

## Cellule 3 (Code) - Imports

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
import time
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Configuration pour reproductibilité
np.random.seed(42)
tf.random.set_seed(42)

# Vérifier la version de TensorFlow
print(f"TensorFlow version: {tf.__version__}")
```

## Cellule 4 (Markdown) - Chargement des données

```markdown
## 2. Chargement et préparation du dataset MNIST

Le dataset MNIST contient 70,000 images de chiffres manuscrits de taille 28x28 pixels.
```

## Cellule 5 (Code) - Chargement MNIST

```python
print("Chargement des données MNIST...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Afficher les dimensions des données
print(f"Dimensions de X_train: {X_train.shape}")
print(f"Dimensions de y_train: {y_train.shape}")
print(f"Dimensions de X_test: {X_test.shape}")
print(f"Dimensions de y_test: {y_test.shape}")
print(f"Nombre de classes: {len(np.unique(y_train))}")
```

## Cellule 6 (Markdown) - Préparation des données

```markdown
### Préparation des données pour le CNN

Pour utiliser nos images avec un CNN, nous devons :
1. Ajouter une dimension pour le canal (les images sont en niveaux de gris, donc 1 seul canal)
2. Normaliser les valeurs de pixels entre 0 et 1
3. Convertir les étiquettes en format one-hot encoding
```

## Cellule 7 (Code) - Prétraitement

```python
# Redimensionnement et normalisation
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0

# Conversion des étiquettes en catégories one-hot
y_train_onehot = to_categorical(y_train, 10)
y_test_onehot = to_categorical(y_test, 10)

print(f"Nouvelle forme de X_train: {X_train.shape}")
print(f"Nouvelle forme de y_train_onehot: {y_train_onehot.shape}")
```

## Cellule 8 (Markdown) - Visualisation

```markdown
### Visualisation de quelques exemples

Regardons à quoi ressemblent nos données.
```

## Cellule 9 (Code) - Affichage des exemples

```python
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap='gray')
    plt.title(f"Chiffre: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
```

## Cellule 10 (Markdown) - Création du modèle

```markdown
## 3. Création d'un modèle CNN

Un CNN est un type de réseau de neurones spécialisé pour traiter des données ayant une structure en grille, comme les images. Les principales couches sont :

1. **Couches de convolution (Conv2D)** : Détectent des caractéristiques locales (lignes, formes...)
2. **Couches de pooling (MaxPooling2D)** : Réduisent la dimension des données
3. **Couches denses (Dense)** : Effectuent la classification finale

Nous allons créer un CNN simple avec 2 couches de convolution pour classifier les chiffres MNIST.
```

## Cellule 11 (Code) - Définition du modèle

```python
# Créer un modèle CNN
model = Sequential([
    # Première couche de convolution
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    
    # Deuxième couche de convolution
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    
    # Aplatissement pour passer aux couches denses
    Flatten(name='flatten'),
    
    # Couches denses (fully connected)
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout1'),  # Évite le surapprentissage
    Dense(10, activation='softmax', name='output')  # 10 classes (chiffres 0-9)
])

# Compiler le modèle
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Afficher le résumé de l'architecture
model.summary()
```

## Cellule 12 (Markdown) - Entraînement

```markdown
## 4. Entraînement du modèle

Entraînons maintenant notre CNN sur les données MNIST.
```

## Cellule 13 (Code) - Entraînement du modèle

```python
# Entraînement du modèle
start_time = time.time()

history = model.fit(
    X_train, 
    y_train_onehot, 
    batch_size=128, 
    epochs=5,  # Nombre réduit d'époques pour la démonstration
    validation_split=0.2,  # 20% des données d'entraînement pour la validation
    verbose=1
)

training_time = time.time() - start_time
print(f"\nTemps d'entraînement: {training_time:.2f} secondes")
```

## Cellule 14 (Markdown) - Visualisation de l'entraînement

```markdown
### Visualisation de l'évolution de l'entraînement
```

## Cellule 15 (Code) - Graphiques d'entraînement

```python
plt.figure(figsize=(12, 4))

# Graphique de précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Entraînement')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Évolution de la précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Graphique de perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Entraînement')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Évolution de la perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
```

## Cellule 16 (Markdown) - Évaluation

```markdown
## 5. Évaluation du modèle

Évaluons notre modèle sur l'ensemble de test.
```

## Cellule 17 (Code) - Évaluation et matrice de confusion

```python
# Évaluation sur l'ensemble de test
test_loss, test_acc = model.evaluate(X_test, y_test_onehot, verbose=1)
print(f"Précision sur l'ensemble de test: {test_acc*100:.2f}%")

# Prédictions
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Matrice de confusion
conf_mat = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédit')
plt.ylabel('Réel')
plt.title('Matrice de confusion')
plt.show()
```

## Cellule 18 (Markdown) - Visualisation des erreurs

```markdown
### Visualisation des exemples mal classifiés

Explorons quelques exemples que notre modèle a mal classifiés.
```

## Cellule 19 (Code) - Affichage des erreurs

```python
# Identifier les erreurs
misclassified_indices = np.where(y_pred_classes != y_test)[0]
misclassified_count = len(misclassified_indices)
print(f"Nombre total d'erreurs: {misclassified_count} sur {len(y_test)} images de test")

# Afficher quelques exemples mal classifiés
num_examples = min(10, misclassified_count)
plt.figure(figsize=(15, 6))

for i, idx in enumerate(misclassified_indices[:num_examples]):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f"Réel: {y_test[idx]}\nPrédit: {y_pred_classes[idx]}")
    plt.axis('off')
    
plt.tight_layout()
plt.show()
```

## Cellule 20 (Markdown) - Réflexion sur les erreurs

```markdown
### 🧠 Réflexion sur les erreurs

**Question**: En observant les exemples mal classifiés, quelles pourraient être les raisons de ces erreurs? Notez vos observations et hypothèses ci-dessous.

**Points à considérer:**
- Certains chiffres sont-ils plus souvent confondus que d'autres?
- Quelles caractéristiques visuelles communes peuvent expliquer les erreurs?
```

## Cellule 21 (Markdown) - Zone de réponse

```markdown
*Écrivez vos observations ici...*
```

## Cellule 22 (Markdown) - Visualisation des filtres

```markdown
## 6. Visualisation des filtres et feature maps

Une des grandes forces des CNNs est leur interprétabilité visuelle. Explorons ce que le réseau "voit" réellement.
```

## Cellule 23 (Code) - Visualisation des filtres

```python
# Fonction pour visualiser les filtres de convolution
def visualize_filters(model, layer_name, num_filters=8):
    """Visualise les filtres d'une couche de convolution"""
    
    # Récupérer les poids du filtre de la couche spécifiée
    filters, biases = model.get_layer(layer_name).get_weights()
    
    # Normaliser les filtres pour une meilleure visualisation
    f_min, f_max = filters.min(), filters.max()
    filters = (filters - f_min) / (f_max - f_min)
    
    # Afficher les premiers filtres
    plt.figure(figsize=(12, 4))
    for i in range(num_filters):
        plt.subplot(2, 4, i+1)
        # Pour la première couche de convolution, les filtres sont 3D (hauteur, largeur, canaux)
        # Nous affichons le filtre pour le premier canal (0)
        plt.imshow(filters[:, :, 0, i], cmap='viridis')
        plt.title(f'Filtre {i+1}')
        plt.axis('off')
    plt.suptitle(f'Filtres de la couche {layer_name}')
    plt.tight_layout()
    plt.show()

# Visualiser les filtres de la première couche de convolution
visualize_filters(model, 'conv1')
```

## Cellule 24 (Markdown) - Feature maps

```markdown
### Visualisation des feature maps (cartes d'activation)
```

## Cellule 25 (Code) - Visualisation des feature maps

```python
def visualize_feature_maps(model, image, layer_name, num_features=8):
    """Visualise les feature maps (activations) d'une couche pour une image donnée"""
    
    # Créer un modèle qui renvoie les activations de la couche spécifiée
    layer_model = tf.keras.Model(inputs=model.input, outputs=model.get_layer(layer_name).output)
    
    # Obtenir les activations pour une image
    feature_maps = layer_model.predict(image.reshape(1, 28, 28, 1))
    
    # Afficher les premières cartes d'activation
    plt.figure(figsize=(12, 4))
    for i in range(min(num_features, feature_maps.shape[3])):
        plt.subplot(2, 4, i+1)
        plt.imshow(feature_maps[0, :, :, i], cmap='viridis')
        plt.title(f'Feature {i+1}')
        plt.axis('off')
    plt.suptitle(f'Feature Maps de la couche {layer_name}')
    plt.tight_layout()
    plt.show()

# Choisir une image de test
sample_idx = 12  # Vous pouvez essayer avec différents indices
sample_image = X_test[sample_idx]

# Afficher l'image originale
plt.figure(figsize=(3, 3))
plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Chiffre: {y_test[sample_idx]}")
plt.axis('off')
plt.show()

# Visualiser les feature maps pour chaque couche de convolution
print("Feature maps de la première couche de convolution:")
visualize_feature_maps(model, sample_image, 'conv1')

print("Feature maps de la deuxième couche de convolution:")
visualize_feature_maps(model, sample_image, 'conv2')
```

## Cellule 26 (Markdown) - Interprétation

```markdown
### 💡 Interprétation des feature maps

Les feature maps nous montrent ce que "voit" chaque filtre de convolution :

- **Première couche** : Détecte principalement des caractéristiques de base comme les bords et les contours
- **Deuxième couche** : Combine ces caractéristiques de base pour détecter des formes plus complexes

Cette hiérarchie de représentations est ce qui rend les CNNs si puissants pour la vision par ordinateur.
```

## Cellule 27 (Markdown) - Test de robustesse

```markdown
## 7. Test avec des images bruitées

Testons la robustesse de notre modèle face à des perturbations.
```

## Cellule 28 (Code) - Test avec bruit

```python
# Fonction pour ajouter du bruit aux images
def add_noise(images, noise_level=0.2):
    """Ajoute du bruit gaussien aux images"""
    noisy_images = images.copy()
    noise = np.random.normal(0, noise_level, images.shape)
    noisy_images = noisy_images + noise
    # Assurer que les valeurs restent entre 0 et 1
    return np.clip(noisy_images, 0, 1)

# Créer des versions bruitées de quelques images de test
num_test_images = 5
test_samples = X_test[:num_test_images]
noisy_samples = add_noise(test_samples, noise_level=0.3)

# Visualiser les images originales et bruitées
plt.figure(figsize=(12, 4))
for i in range(num_test_images):
    # Image originale
    plt.subplot(2, num_test_images, i+1)
    plt.imshow(test_samples[i].reshape(28, 28), cmap='gray')
    plt.title(f"Original: {y_test[i]}")
    plt.axis('off')
    
    # Image bruitée
    plt.subplot(2, num_test_images, i+num_test_images+1)
    plt.imshow(noisy_samples[i].reshape(28, 28), cmap='gray')
    plt.axis('off')
    
plt.tight_layout()
plt.show()

# Prédire sur les images bruitées
noisy_predictions = model.predict(noisy_samples)
noisy_pred_classes = np.argmax(noisy_predictions, axis=1)

# Afficher les résultats
print("Résultats des prédictions sur les images bruitées:")
for i in range(num_test_images):
    status = "✓" if noisy_pred_classes[i] == y_test[i] else "✗"
    print(f"Image {i+1} - Réel: {y_test[i]}, Prédit: {noisy_pred_classes[i]} {status}")

# Calculer la précision sur les images bruitées
accuracy_on_noisy = np.mean(noisy_pred_classes == y_test[:num_test_images]) * 100
print(f"\nPrécision sur les images bruitées: {accuracy_on_noisy:.1f}%")
```

## Cellule 29 (Markdown) - Exercice d'amélioration

```markdown
## 8. Exercice : Amélioration du modèle

À vous de jouer ! Essayez de modifier l'architecture du modèle pour améliorer ses performances. Voici quelques suggestions :

1. Ajouter plus de couches de convolution
2. Modifier le nombre de filtres
3. Changer la taille des filtres
4. Ajuster les paramètres d'entraînement (epochs, batch_size)

Copiez le code de création du modèle ci-dessous et modifiez-le :
```

## Cellule 30 (Code) - Modèle amélioré

```python
# VOTRE CODE ICI
# Créez votre propre modèle amélioré

improved_model = Sequential([
    # Modifiez l'architecture ici
    
])

# Compiler le modèle
improved_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Afficher le résumé
improved_model.summary()
```

## Cellule 31 (Code) - Entraînement du modèle amélioré

```python
# Entraînez votre modèle amélioré
# history = improved_model.fit(...)
```

## Cellule 32 (Markdown) - Conclusion

```markdown
## 9. Conclusion

Dans ce notebook, vous avez :
- Créé et entraîné un réseau de neurones convolutif (CNN) pour la classification d'images
- Visualisé les filtres et les feature maps pour comprendre ce que "voit" le réseau
- Évalué les performances du modèle et sa robustesse face au bruit

Les CNN sont la base de nombreuses applications modernes de vision par ordinateur comme la reconnaissance faciale, la détection d'objets, et bien d'autres.
```