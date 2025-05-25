# RNN/LSTM pour l'analyse de sentiment - Notebook complet

Ce notebook vous guide dans la création d'un modèle LSTM pour analyser le sentiment de textes (positif/négatif).

## Cellule 1 (Markdown) - Introduction

```markdown
# 🧠 RNN/LSTM pour l'analyse de sentiment

## Découverte des réseaux récurrents avec un cas concret

Dans ce notebook, vous allez :
- ✅ Comprendre comment les RNN traitent les séquences de texte
- ✅ Créer un modèle LSTM pour analyser le sentiment
- ✅ Visualiser les embeddings de mots
- ✅ Tester le modèle sur vos propres phrases

**Durée estimée** : 50 minutes

**Cas d'usage** : Analyser automatiquement les avis clients, commentaires, etc.
```

## Cellule 2 (Code) - Configuration et imports

```python
# Imports nécessaires
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing import sequence
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import pandas as pd

# Configuration
print(f"TensorFlow version: {tf.__version__}")
print("GPU disponible:", "Oui" if tf.config.list_physical_devices('GPU') else "Non")

# Paramètres du modèle
MAX_FEATURES = 5000  # Nombre de mots dans le vocabulaire
MAX_LEN = 200       # Longueur maximale des séquences
EMBEDDING_SIZE = 128 # Taille des embeddings

print("\n✅ Configuration terminée !")
```

## Cellule 3 (Code) - Chargement et exploration des données

```python
# Chargement du dataset IMDB (avis de films)
print("📥 Chargement du dataset IMDB...")
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=MAX_FEATURES)

print(f"📊 Données d'entraînement : {len(X_train)} avis")
print(f"📊 Données de test : {len(X_test)} avis")
print(f"📊 Vocabulaire : {MAX_FEATURES} mots les plus fréquents")

# Récupération du dictionnaire de mots
word_index = imdb.get_word_index()
reverse_word_index = {v: k for k, v in word_index.items()}
reverse_word_index[0] = '<PAD>'
reverse_word_index[1] = '<START>'
reverse_word_index[2] = '<UNKNOWN>'

def decode_review(encoded_review):
    """Convertit une séquence d'indices en texte lisible"""
    return ' '.join([reverse_word_index.get(i, '<UNKNOWN>') for i in encoded_review])

# Affichage de quelques exemples
print("\n📝 Exemples d'avis (avant preprocessing) :")
for i in range(3):
    sentiment = "😊 POSITIF" if y_train[i] == 1 else "😞 NÉGATIF"
    print(f"\n{sentiment} - Longueur: {len(X_train[i])} mots")
    decoded = decode_review(X_train[i])
    # Afficher seulement les premiers mots pour la lisibilité
    print(f"Texte: {decoded[:200]}...")

# Distribution des longueurs
lengths = [len(x) for x in X_train]
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(lengths, bins=50, alpha=0.7)
plt.title('Distribution des longueurs d\'avis')
plt.xlabel('Nombre de mots')
plt.ylabel('Fréquence')
plt.axvline(MAX_LEN, color='red', linestyle='--', label=f'Limite fixée: {MAX_LEN}')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(y_train, bins=2, alpha=0.7, color=['red', 'green'])
plt.title('Distribution des sentiments')
plt.xlabel('Sentiment (0=Négatif, 1=Positif)')
plt.ylabel('Nombre d\'avis')
plt.xticks([0, 1], ['Négatif', 'Positif'])

plt.tight_layout()
plt.show()

print(f"\n📊 Statistiques des longueurs :")
print(f"   - Longueur moyenne : {np.mean(lengths):.1f} mots")
print(f"   - Longueur médiane : {np.median(lengths):.1f} mots")
print(f"   - Avis > {MAX_LEN} mots : {np.sum(np.array(lengths) > MAX_LEN)}")
```

## Cellule 4 (Code) - Préparation des données

```python
# Padding des séquences (toutes à la même longueur)
print("🔧 Préparation des données...")
print(f"   - Troncature/padding à {MAX_LEN} mots")

X_train = sequence.pad_sequences(X_train, maxlen=MAX_LEN, padding='post')
X_test = sequence.pad_sequences(X_test, maxlen=MAX_LEN, padding='post')

print(f"   - Forme finale X_train : {X_train.shape}")
print(f"   - Forme finale X_test : {X_test.shape}")

# Visualisation de l'effet du padding
exemple_idx = 0
print(f"\n📝 Exemple de preprocessing :")
print(f"   - Avis original : {len([x for x in X_train[exemple_idx] if x != 0])} mots utiles")
print(f"   - Après padding : {X_train.shape[1]} positions")
print(f"   - Premières valeurs : {X_train[exemple_idx][:20]}")
print(f"   - (0 = padding, autres = indices de mots)")

# Conversion en format approprié pour TensorFlow
X_train = X_train.astype('int32')
X_test = X_test.astype('int32')
y_train = y_train.astype('int32') 
y_test = y_test.astype('int32')

print("\n✅ Données préparées pour l'entraînement !")
```

## Cellule 5 (Code) - Construction du modèle LSTM

```python
# Construction du modèle LSTM
print("🏗️ Construction du modèle LSTM...")

model = Sequential([
    # Couche d'embedding : convertit les indices en vecteurs denses
    Embedding(
        input_dim=MAX_FEATURES,    # Taille du vocabulaire
        output_dim=EMBEDDING_SIZE, # Dimension des embeddings
        input_length=MAX_LEN,      # Longueur des séquences
        name='embedding'
    ),
    
    # Couche LSTM : traite les séquences
    LSTM(
        units=64,           # Nombre d'unités LSTM
        dropout=0.2,        # Dropout sur les entrées
        recurrent_dropout=0.2,  # Dropout sur les connexions récurrentes
        name='lstm'
    ),
    
    # Couche de régularisation
    Dropout(0.5, name='dropout'),
    
    # Couche de sortie : classification binaire
    Dense(1, activation='sigmoid', name='output')
])

# Compilation du modèle
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Affichage de l'architecture
print("\n📋 Architecture du modèle :")
model.summary()

print(f"\n🔢 Détails des couches :")
print(f"   - Embedding : {MAX_FEATURES} mots → {EMBEDDING_SIZE} dimensions")
print(f"   - LSTM : 64 unités avec mémoire séquentielle")
print(f"   - Dense : 1 neurone pour classification binaire (0-1)")
print(f"   - Total paramètres : {model.count_params():,}")
```

## Cellule 6 (Code) - Entraînement du modèle

```python
# Entraînement du modèle
print("🚀 Début de l'entraînement...")
print("⏱️ Les LSTM sont plus lents que les CNN, patience !")

# Entraînement avec validation
history = model.fit(
    X_train, y_train,
    batch_size=128,
    epochs=3,  # Peu d'époques pour la démonstration
    validation_split=0.2,
    verbose=1
)

# Évaluation finale
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n📊 Résultats finaux :")
print(f"   - Précision sur test : {test_accuracy*100:.2f}%")
print(f"   - Perte sur test : {test_loss:.4f}")

# Visualisation des courbes d'apprentissage
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], 'b-', label='Entraînement', linewidth=2)
plt.plot(history.history['val_accuracy'], 'r-', label='Validation', linewidth=2)
plt.title('Évolution de la précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], 'b-', label='Entraînement', linewidth=2)
plt.plot(history.history['val_loss'], 'r-', label='Validation', linewidth=2)
plt.title('Évolution de la perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n✅ Entraînement terminé !")
```

## Cellule 7 (Code) - Test et prédictions

```python
# Test du modèle sur quelques exemples
print("🔍 Test du modèle sur des exemples...")

# Sélection d'exemples
indices = np.random.choice(len(X_test), 8, replace=False)
test_examples = X_test[indices]
true_labels = y_test[indices]

# Prédictions
predictions = model.predict(test_examples, verbose=0)
predicted_probs = predictions.flatten()
predicted_labels = (predicted_probs > 0.5).astype(int)

# Affichage des résultats
print("\n📝 Exemples de prédictions :")
for i in range(8):
    true_sentiment = "😊 POSITIF" if true_labels[i] == 1 else "😞 NÉGATIF"
    pred_sentiment = "😊 POSITIF" if predicte