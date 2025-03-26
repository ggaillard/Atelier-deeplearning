# Guide d'utilisation des modèles pré-entraînés TensorFlow

## Introduction aux modèles pré-entraînés

Les modèles pré-entraînés sont un des moyens les plus efficaces d'obtenir rapidement d'excellentes performances en Deep Learning sans avoir besoin de grandes quantités de données ni de ressources de calcul importantes. Cette approche est particulièrement pertinente pour les projets  où le temps et les ressources sont souvent limités.

### Qu'est-ce qu'un modèle pré-entraîné ?

Un modèle pré-entraîné est un réseau de neurones qui a déjà été entraîné sur un grand jeu de données (souvent des millions d'images ou de textes). Ces modèles ont appris des représentations génériques qui peuvent être réutilisées pour d'autres tâches similaires.

### Avantages pour vos projets

- **Gain de temps** : Évitez des jours ou semaines d'entraînement
- **Économie de ressources** : Pas besoin de GPU puissant
- **Meilleures performances** : Bénéficiez de modèles entraînés sur des datasets massifs
- **Moins de données requises** : Parfait quand vous disposez de peu d'exemples

## Modèles pré-entraînés disponibles dans TensorFlow/Keras

TensorFlow propose une large collection de modèles pré-entraînés via Keras et TensorFlow Hub. Voici les principaux modèles disponibles classés par domaine d'application :

### Vision par ordinateur

| Modèle | Taille | Précision | Rapidité | Cas d'usage |
|--------|--------|-----------|----------|-------------|
| MobileNetV2 | 14 MB | Moyenne | Très rapide | Applications mobiles, détection en temps réel |
| ResNet50 | 98 MB | Élevée | Moyenne | Classification d'images générale |
| EfficientNetB0 | 29 MB | Élevée | Rapide | Bon compromis taille/performance |
| EfficientNetB7 | 256 MB | Très élevée | Lent | Précision maximale requise |
| VGG16 | 528 MB | Moyenne | Lent | Extraction de caractéristiques |
| InceptionV3 | 92 MB | Élevée | Moyenne | Classification avec précision |

### Traitement du langage naturel

| Modèle | Taille | Précision | Rapidité | Cas d'usage |
|--------|--------|-----------|----------|-------------|
| BERT Small | 55 MB | Moyenne | Rapide | Classification de texte simple |
| BERT Base | 110 MB | Élevée | Moyenne | Analyse de sentiment, classification |
| DistilBERT | 66 MB | Bonne | Rapide | Version légère de BERT |
| Universal Sentence Encoder | 68 MB | Moyenne | Rapide | Comparaison de textes, recherche |

## Comment utiliser un modèle pré-entraîné

### 1. Chargement d'un modèle pré-entraîné

```python
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2, ResNet50

# Option 1: Modèle pour la classification
model = MobileNetV2(weights='imagenet', include_top=True)

# Option 2: Modèle pour l'extraction de caractéristiques (sans les couches de classification)
feature_extractor = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
```

#### Paramètres importants

- `weights='imagenet'` : Charge les poids pré-entraînés sur ImageNet
- `include_top=True/False` : Inclut ou non les couches de classification finale
- `input_shape` : Dimensions requises des images d'entrée

### 2. Utilisation directe (prédiction)

```python
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Charger et prétraiter l'image
img_path = 'mon_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)  # Prétraitement spécifique au modèle

# Prédiction
preds = model.predict(x)
results = decode_predictions(preds, top=3)[0]
print("Prédictions:")
for result in results:
    print(f"{result[1]}: {result[2]*100:.2f}%")
```

### 3. Transfer Learning (réutilisation pour votre propre tâche)

Le transfer learning est une technique qui vous permet d'adapter un modèle pré-entraîné à votre propre jeu de données. C'est extrêmement utile quand vous avez peu de données.

```python
# Créer un modèle de base (sans les couches de classification)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Geler les poids du modèle de base
base_model.trainable = False

# Ajouter vos propres couches de classification
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')  # nombre de classes dans votre problème
])

# Compiler le modèle
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Entraîner uniquement les nouvelles couches
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=10,
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)
```

### 4. Fine-tuning (ajustement fin)

Le fine-tuning est une étape supplémentaire après le transfer learning, où vous "dégeler" certaines couches du modèle pré-entraîné pour les ajuster à vos données.

```python
# Après l'entraînement initial, dégeler une partie du modèle de base
base_model.trainable = True

# Geler les premières couches et n'entraîner que les couches plus profondes
for layer in base_model.layers[:100]:
    layer.trainable = False
for layer in base_model.layers[100:]:
    layer.trainable = True

# Recompiler avec un taux d'apprentissage plus faible
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),  # Taux plus faible
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Fine-tuning
history_fine = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=5,
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)
```

## Exemples pratiques

### Exemple 1: Classification d'images personnalisée

Voici un exemple complet pour créer un classificateur d'images personnalisé à partir de MobileNetV2 :

```python
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Paramètres
IMAGE_SIZE = (224, 224)