# Comparaison entre Machine Learning classique et Deep Learning

## Introduction

Ce notebook interactif vous propose d'explorer par la pratique les différences fondamentales entre le Machine Learning classique et le Deep Learning. Vous manipulerez en parallèle deux approches différentes pour résoudre un même problème de classification d'images.

## Objectifs pédagogiques

À la fin de cette activité, vous serez capable de :
- Identifier les différences clés entre les deux approches
- Comprendre les forces et faiblesses de chaque méthode
- Analyser les performances dans différents contextes
- Expliquer pourquoi le Deep Learning excelle dans certaines tâches

## Partie 1 : Préparation et configuration

### 1.1 Importation des bibliothèques

Pour le notebook A (Machine Learning classique) :

```python
# Importation des bibliothèques nécessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import time
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.pipeline import Pipeline
```

Pour le notebook B (Deep Learning) :

```python
# Importation des bibliothèques nécessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import time
```

### 1.2 Chargement des données MNIST

Le jeu de données MNIST contient des images 28x28 pixels en niveaux de gris de chiffres manuscrits (0 à 9).

```python
# Chargement du jeu de données MNIST
from tensorflow.keras.datasets import mnist

# Chargement et séparation des données
(X_train_full, y_train_full), (X_test, y_test) = mnist.load_data()

# Utiliser un sous-ensemble pour accélérer les tests
sample_size = 10000
X_train = X_train_full[:sample_size]
y_train = y_train_full[:sample_size]

# Afficher les dimensions
print(f"Dimensions de X_train : {X_train.shape}")
print(f"Dimensions de y_train : {y_train.shape}")
print(f"Dimensions de X_test : {X_test.shape}")
print(f"Dimensions de y_test : {y_test.shape}")
```

### 1.3 Visualisation de quelques exemples

```python
# Afficher quelques exemples d'images
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.suptitle("Exemples de chiffres manuscrits", y=1.05)
plt.show()
```

## Partie 2 : Approche Machine Learning classique

### 2.1 Prétraitement des données pour le ML classique

Pour le ML classique, nous devons transformer les images 2D en vecteurs 1D et réduire la dimensionnalité pour accélérer l'entraînement.

```python
# Aplatir les images 28x28 en vecteurs 784
X_train_flat = X_train.reshape(X_train.shape[0], -1)
X_test_flat = X_test.reshape(X_test.shape[0], -1)

# Normaliser les valeurs de pixels entre 0 et 1
X_train_flat = X_train_flat / 255.0
X_test_flat = X_test_flat / 255.0

# Réduction de dimensionnalité avec PCA
n_components = 50  # Réduire de 784 à 50 dimensions
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train_flat)
X_test_pca = pca.transform(X_test_flat)

print(f"Forme originale : {X_train_flat.shape}")
print(f"Forme après PCA : {X_train_pca.shape}")
print(f"Variance expliquée : {sum(pca.explained_variance_ratio_)*100:.2f}%")
```

### 2.2 Création et entraînement du modèle Random Forest

```python
# Paramètres du modèle
n_estimators = 100  # Nombre d'arbres
max_depth = 15      # Profondeur maximale des arbres

# Création du modèle
rf_model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    random_state=42,
    n_jobs=-1  # Utiliser tous les cœurs disponibles
)

# Mesurer le temps d'entraînement
start_time = time.time()
print("Entraînement du modèle Random Forest...")
rf_model.fit(X_train_pca, y_train)
end_time = time.time()
training_time_rf = end_time - start_time

print(f"Temps d'entraînement : {training_time_rf:.2f} secondes")
```

### 2.3 Évaluation du modèle Random Forest

```python
# Prédictions sur l'ensemble de test
y_pred_rf = rf_model.predict(X_test_pca)

# Calcul des métriques
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
class_report_rf = classification_report(y_test, y_pred_rf)

print(f"Précision globale : {accuracy_rf*100:.2f}%")
print("\nMatrice de confusion :")
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_rf, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédictions')
plt.ylabel('Valeurs réelles')
plt.title('Matrice de confusion - Random Forest')
plt.show()

print("\nRapport de classification :")
print(class_report_rf)
```

### 2.4 Visualisation des erreurs du Random Forest

```python
# Identifier les erreurs
error_indices_rf = np.where(y_pred_rf != y_test)[0]
n_errors = min(10, len(error_indices_rf))

if n_errors > 0:
    plt.figure(figsize=(12, 4))
    for i in range(n_errors):
        plt.subplot(2, 5, i + 1)
        idx = error_indices_rf[i]
        img = X_test[idx]
        plt.imshow(img, cmap='gray')
        plt.title(f"Réel: {y_test[idx]}\nPrédit: {y_pred_rf[idx]}")
        plt.axis('off')
    plt.tight_layout()
    plt.suptitle("Erreurs de classification - Random Forest", y=1.05)
    plt.show()
```

## Partie 3 : Approche Deep Learning

### 3.1 Prétraitement des données pour le Deep Learning

```python
# Redimensionner et normaliser les données
X_train_dl = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255
X_test_dl = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255

# Conversion des labels en catégories one-hot
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

print(f"Forme de X_train_dl : {X_train_dl.shape}")
print(f"Forme de y_train_cat : {y_train_cat.shape}")
```

### 3.2 Création du modèle CNN

```python
# Création d'un modèle CNN simple
cnn_model = Sequential([
    # Première couche de convolution
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Deuxième couche de convolution
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Aplatissement et couches denses
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),  # Pour réduire le surapprentissage
    Dense(10, activation='softmax')  # 10 classes (chiffres 0-9)
])

# Compilation du modèle
cnn_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Afficher un résumé du modèle
cnn_model.summary()
```

### 3.3 Entraînement du modèle CNN

```python
# Mesurer le temps d'entraînement
start_time = time.time()
print("Entraînement du modèle CNN...")

# Entraînement
history = cnn_model.fit(
    X_train_dl, y_train_cat,
    batch_size=128,
    epochs=5,  # Nombre d'époques réduit pour la démonstration
    validation_split=0.1,
    verbose=1
)

end_time = time.time()
training_time_cnn = end_time - start_time

print(f"Temps d'entraînement : {training_time_cnn:.2f} secondes")
```

### 3.4 Évaluation du modèle CNN

```python
# Évaluation sur l'ensemble de test
test_loss, test_acc = cnn_model.evaluate(X_test_dl, y_test_cat, verbose=0)
print(f"Précision sur l'ensemble de test : {test_acc*100:.2f}%")

# Prédictions
y_pred_cnn = cnn_model.predict(X_test_dl)
y_pred_classes = np.argmax(y_pred_cnn, axis=1)

# Matrice de confusion
conf_matrix_cnn = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_cnn, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Prédictions')
plt.ylabel('Valeurs réelles')
plt.title('Matrice de confusion - CNN')
plt.show()

# Rapport de classification
print("\nRapport de classification :")
print(classification_report(y_test, y_pred_classes))
```

### 3.5 Visualisation des erreurs du CNN

```python
# Identifier les erreurs
error_indices_cnn = np.where(y_pred_classes != y_test)[0]
n_errors = min(10, len(error_indices_cnn))

if n_errors > 0:
    plt.figure(figsize=(12, 4))
    for i in range(n_errors):
        plt.subplot(2, 5, i + 1)
        idx = error_indices_cnn[i]
        img = X_test[idx]
        plt.imshow(img, cmap='gray')
        plt.title(f"Réel: {y_test[idx]}\nPrédit: {y_pred_classes[idx]}")
        plt.axis('off')
    plt.tight_layout()
    plt.suptitle("Erreurs de classification - CNN", y=1.05)
    plt.show()
```

### 3.6 Visualisation de l'apprentissage

```python
# Visualiser l'évolution de l'apprentissage
plt.figure(figsize=(12, 4))

# Évolution de la précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Entraînement')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Évolution de la précision')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()

# Évolution de la perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Entraînement')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Évolution de la perte')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()

plt.tight_layout()
plt.show()
```

## Partie 4 : Défi de généralisation

Dans cette partie, nous allons tester les deux modèles sur des données transformées pour évaluer leur capacité de généralisation.

### 4.1 Création de données modifiées

```python
# Fonction pour ajouter du bruit aux images
def add_noise(images, noise_level=0.2):
    noisy_images = images.copy()
    noise = np.random.normal(0, noise_level, images.shape)
    noisy_images = noisy_images + noise
    return np.clip(noisy_images, 0, 1)  # Limiter les valeurs entre 0 et 1

# Fonction pour appliquer une rotation aux images
def rotate_images(images, max_angle=15):
    from scipy.ndimage import rotate
    rotated_images = np.zeros_like(images)
    for i in range(len(images)):
        angle = np.random.uniform(-max_angle, max_angle)
        rotated = rotate(images[i], angle, reshape=False)
        rotated_images[i] = rotated
    return rotated_images

# Créer des versions modifiées du jeu de test
X_test_noisy = add_noise(X_test / 255.0)
X_test_rotated = rotate_images(X_test / 255.0)

# Visualiser quelques exemples
plt.figure(figsize=(12, 8))
for i in range(5):
    # Original
    plt.subplot(3, 5, i + 1)
    plt.imshow(X_test[i], cmap='gray')
    plt.title(f"Original: {y_test[i]}")
    plt.axis('off')
    
    # Avec bruit
    plt.subplot(3, 5, i + 6)
    plt.imshow(X_test_noisy[i], cmap='gray')
    plt.title("Avec bruit")
    plt.axis('off')
    
    # Avec rotation
    plt.subplot(3, 5, i + 11)
    plt.imshow(X_test_rotated[i], cmap='gray')
    plt.title("Avec rotation")
    plt.axis('off')

plt.tight_layout()
plt.suptitle("Exemples de chiffres modifiés", y=1.02)
plt.show()
```

### 4.2 Évaluation sur les données modifiées

```python
# Préparation pour Random Forest
X_test_noisy_flat = X_test_noisy.reshape(X_test.shape[0], -1)
X_test_rotated_flat = X_test_rotated.reshape(X_test.shape[0], -1)
X_test_noisy_pca = pca.transform(X_test_noisy_flat)
X_test_rotated_pca = pca.transform(X_test_rotated_flat)

# Préparation pour CNN
X_test_noisy_dl = X_test_noisy.reshape(X_test.shape[0], 28, 28, 1)
X_test_rotated_dl = X_test_rotated.reshape(X_test.shape[0], 28, 28, 1)

# Évaluation de Random Forest
y_pred_rf_noisy = rf_model.predict(X_test_noisy_pca)
y_pred_rf_rotated = rf_model.predict(X_test_rotated_pca)
accuracy_rf_noisy = accuracy_score(y_test, y_pred_rf_noisy)
accuracy_rf_rotated = accuracy_score(y_test, y_pred_rf_rotated)

# Évaluation de CNN
y_pred_cnn_noisy = cnn_model.predict(X_test_noisy_dl)
y_pred_cnn_rotated = cnn_model.predict(X_test_rotated_dl)
y_pred_cnn_noisy_classes = np.argmax(y_pred_cnn_noisy, axis=1)
y_pred_cnn_rotated_classes = np.argmax(y_pred_cnn_rotated, axis=1)
accuracy_cnn_noisy = accuracy_score(y_test, y_pred_cnn_noisy_classes)
accuracy_cnn_rotated = accuracy_score(y_test, y_pred_cnn_rotated_classes)

# Affichage des résultats
print("Performances sur les données originales :")
print(f"Random Forest : {accuracy_rf*100:.2f}%")
print(f"CNN : {test_acc*100:.2f}%")
print("\nPerformances sur les données avec bruit :")
print(f"Random Forest : {accuracy_rf_noisy*100:.2f}%")
print(f"CNN : {accuracy_cnn_noisy*100:.2f}%")
print("\nPerformances sur les données avec rotation :")
print(f"Random Forest : {accuracy_rf_rotated*100:.2f}%")
print(f"CNN : {accuracy_cnn_rotated*100:.2f}%")
```

### 4.3 Visualisation comparative des performances

```python
# Créer un dataframe pour les comparaisons
import pandas as pd

data = {
    'Type de données': ['Originales', 'Avec bruit', 'Avec rotation'],
    'Random Forest': [accuracy_rf*100, accuracy_rf_noisy*100, accuracy_rf_rotated*100],
    'CNN': [test_acc*100, accuracy_cnn_noisy*100, accuracy_cnn_rotated*100]
}

df = pd.DataFrame(data)

# Visualisation en barres groupées
plt.figure(figsize=(10, 6))
x = np.arange(len(df['Type de données']))
width = 0.35

plt.bar(x - width/2, df['Random Forest'], width, label='Random Forest')
plt.bar(x + width/2, df['CNN'], width, label='CNN')

plt.xlabel('Type de données')
plt.ylabel('Précision (%)')
plt.title('Comparaison des performances ML vs DL')
plt.xticks(x, df['Type de données'])
plt.legend()

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

## Partie 5 : Analyse comparative

### 5.1 Tableau comparatif des approches

Complétez le tableau ci-dessous en vous basant sur vos observations :

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (CNN) |
|----------------|----------------------------------|---------------------|
| Préparation des données | | |
| Complexité du modèle | | |
| Temps d'entraînement | | |
| Précision sur données originales | | |
| Précision sur données bruitées | | |
| Précision sur données avec rotation | | |
| Interprétabilité | | |
| Ressources nécessaires | | |

### 5.2 Questions de réflexion

1. Quelles sont les principales différences que vous avez observées entre les deux approches ?
2. Pourquoi le Deep Learning performe-t-il différemment du Machine Learning classique sur des données transformées ?
3. Dans quels contextes recommanderiez-vous d'utiliser :
   - Le Machine Learning classique ?
   - Le Deep Learning ?
4. Quels compromis devez-vous considérer lors du choix entre ces deux approches ?
5. Comment pourriez-vous améliorer chacun des modèles pour obtenir de meilleures performances ?

## Conclusion

Cette exploration comparative vous a permis de découvrir et d'expérimenter les différences fondamentales entre le Machine Learning classique et le Deep Learning. Vous avez pu observer comment chaque approche traite les données, comment elles apprennent et généralisent, ainsi que leurs forces et faiblesses respectives.

Points clés à retenir :
- Le Deep Learning excelle dans l'apprentissage automatique des caractéristiques pertinentes
- Le Machine Learning classique nécessite souvent une extraction manuelle des caractéristiques
- La capacité de généralisation diffère significativement entre les deux approches
- Chaque méthode a ses propres avantages en termes de temps d'apprentissage, précision et facilité d'utilisation

Dans les prochaines séances, nous approfondirons ces concepts et explorerons plus en détail les architectures spécifiques de réseaux de neurones.