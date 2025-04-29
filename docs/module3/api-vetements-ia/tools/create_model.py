"""
Script pour créer un modèle de classification de vêtements basé sur MobileNetV2
Ce script peut être utilisé pour recréer le modèle mobilenet_clothing_model.h5
"""

import os
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import time

print("=== Création du modèle de classification de vêtements ===")
print(f"TensorFlow version: {tf.__version__}")

# Vérifier si GPU est disponible
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPU disponible: {gpus}")
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(f"Erreur de configuration GPU: {e}")
else:
    print("Aucun GPU détecté, utilisation du CPU (l'entraînement sera plus lent)")

# Téléchargement automatique du jeu de données Fashion MNIST
print("\n1. Téléchargement du jeu de données Fashion MNIST...")
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Noms des classes pour Fashion MNIST
class_names = ['T-shirt/top', 'Pantalon', 'Pull-over', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Sneaker', 'Sac', 'Bottine']

print(f"Nombre d'exemples d'entraînement: {len(train_images)}")
print(f"Nombre d'exemples de test: {len(test_images)}")
print(f"Classes: {class_names}")

# Préparation des données
print("\n2. Préparation des données...")
start_time = time.time()

# Redimensionnement pour MobileNetV2 (qui attend des images 224x224x3)
print("   Redimensionnement des images à 224x224...")
train_images_resized = tf.image.resize(
    tf.expand_dims(train_images, -1), 
    [224, 224]
)
train_images_rgb = tf.repeat(train_images_resized, 3, axis=-1)  # Conversion en RGB
train_images_normalized = train_images_rgb / 255.0  # Normalisation

test_images_resized = tf.image.resize(
    tf.expand_dims(test_images, -1), 
    [224, 224]
)
test_images_rgb = tf.repeat(test_images_resized, 3, axis=-1)
test_images_normalized = test_images_rgb / 255.0

print(f"   Forme des données d'entraînement: {train_images_normalized.shape}")
print(f"   Forme des données de test: {test_images_normalized.shape}")
print(f"   Préparation terminée en {time.time() - start_time:.2f} secondes")

# Création du modèle par transfer learning
print("\n3. Création du modèle avec transfer learning...")
start_time = time.time()

print("   Téléchargement de MobileNetV2 pré-entraîné...")
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,  # Sans les couches de classification finales
    weights='imagenet'  # Pré-entraîné sur ImageNet
)

# Gel des couches du modèle de base
print("   Gel des couches du modèle de base...")
base_model.trainable = False

# Ajout de couches personnalisées
print("   Ajout des couches de classification personnalisées...")
x = base_model.output
x = GlobalAveragePooling2D()(x)  # Pooling global pour réduire la dimensionnalité
x = Dense(128, activation='relu')(x)  # Couche dense intermédiaire
predictions = Dense(10, activation='softmax')(x)  # 10 classes pour Fashion MNIST

# Construction du modèle final
model = Model(inputs=base_model.input, outputs=predictions)

# Afficher un résumé du modèle
model.summary()

print(f"   Création du modèle terminée en {time.time() - start_time:.2f} secondes")

# Compilation
print("\n4. Compilation du modèle...")
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Entraînement
print("\n5. Entraînement du modèle...")
print("   Note: Cette étape peut prendre plusieurs minutes")
start_time = time.time()

# Pour accélérer la démonstration, on utilise un sous-ensemble des données
SUBSET_SIZE = 10000  # Utiliser seulement 10 000 exemples pour l'entraînement rapide
train_subset = train_images_normalized[:SUBSET_SIZE]
labels_subset = train_labels[:SUBSET_SIZE]

# Entraînement sur 3 époques seulement pour la démonstration
history = model.fit(
    train_subset, labels_subset,
    epochs=3,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

print(f"   Entraînement terminé en {time.time() - start_time:.2f} secondes")

# Évaluation
print("\n6. Évaluation du modèle...")
test_loss, test_acc = model.evaluate(test_images_normalized, test_labels, verbose=0)
print(f"   Précision sur les données de test: {test_acc*100:.2f}%")

# Sauvegarde du modèle
output_dir = "../models/pretrained_model"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

model_path = os.path.join(output_dir, "mobilenet_clothing_model.h5")
print(f"\n7. Sauvegarde du modèle dans {model_path}")
model.save(model_path)
print(f"   Taille du fichier: {os.path.getsize(model_path) / (1024*1024):.2f} Mo")

print("\nProcessus terminé avec succès!")
print("Vous pouvez maintenant utiliser ce modèle dans l'application de classification de vêtements.")