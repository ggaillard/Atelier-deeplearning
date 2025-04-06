# Proposition de restructuration du document "Frameworks pour débutants"

Pour améliorer la clarté et la progression du document "partie1-frameworks-debutants.md", je propose une restructuration avec une progression plus explicite et les fichiers/ressources manquants. Voici ma proposition:

## FRAMEWORKS POUR DÉBUTANTS (1h30)

### APERÇU DE LA SESSION
```
🎯 OBJECTIFS
- Comprendre l'utilité des frameworks de Deep Learning en entreprise
- Maîtriser les bases de TensorFlow/Keras
- Créer et déployer un modèle via une API

📋 PLAN DE LA SESSION
1. Introduction aux frameworks en contexte professionnel (15 min)
2. Atelier pratique: Développer un modèle avec TensorFlow/Keras (40 min)
3. Mini-projet: Création d'une API de reconnaissance d'images (35 min)
```

### 1. INTRODUCTION AUX FRAMEWORKS (15 min)

#### 1.1 Pourquoi utiliser des frameworks en entreprise?
- **Productivité**: Développement plus rapide
- **Maintenabilité**: Code standardisé
- **Performances**: Optimisations intégrées 
- **Déploiement**: Outils pour la mise en production

#### 1.2 Comparatif des frameworks courants
| Framework | Cas d'usage | Avantages | Inconvénients |
|-----------|-------------|-----------|---------------|
| TensorFlow/Keras | Applications web/mobile, production | Déploiement facile, bonne documentation | Peut être lourd pour le prototypage |
| PyTorch | Recherche, prototypage | Flexibilité, débogage facile | Déploiement plus complexe |
| Hugging Face | NLP, chatbots | Modèles pré-entraînés pour le texte | Spécialisé en NLP principalement |
| Scikit-learn | Prétraitement, ML classique | Simple, intégration facile | Limité pour le Deep Learning |

#### 1.3 Exemples réels d'entreprises
- Cas d'étude 1: Système de tri automatique de documents (PME de logistique)
- Cas d'étude 2: Modération de contenu pour site e-commerce (Agence web)
- Cas d'étude 3: Assistance diagnostic médical (Cabinet médical)

### 2. ATELIER PRATIQUE: TENSORFLOW/KERAS (40 min)

#### 2.1 Configuration de l'environnement (5 min)
**Option A: Google Colab (recommandée)**
1. Accédez au notebook via ce lien: [TensorFlow/Keras pour débutants](https://colab.research.google.com/drive/1hW-KJJoZ7RJqFfWD6PoiUVl_gj8bSW04)
2. Créez une copie dans votre Drive: `Fichier > Enregistrer une copie dans Drive`

**Option B: Configuration locale**
```bash
# Installation de TensorFlow
pip install tensorflow matplotlib numpy pandas

# Vérification
import tensorflow as tf
print(tf.__version__)
```

#### 2.2 Structure d'un projet TensorFlow/Keras (10 min)
Les étapes essentielles d'un projet sont toujours les mêmes:

```python
# 1. Importation des bibliothèques
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 2. Chargement et préparation des données
(train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
train_images = train_images / 255.0  # Normalisation
test_images = test_images / 255.0

# 3. Création du modèle
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# 4. Compilation du modèle
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Entraînement
model.fit(train_images, train_labels, epochs=5, validation_split=0.2)

# 6. Évaluation
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Précision sur données de test: {test_acc:.2f}")

# 7. Prédiction et utilisation
predictions = model.predict(test_images[:5])
```

#### 2.3 Exercice guidé: Fashion MNIST (25 min)

**Objectif**: Créer un modèle de classification d'images de vêtements

**Étapes**:
1. Explorez le jeu de données Fashion MNIST
2. Construisez et entraînez un modèle simple
3. Améliorez le modèle en modifiant l'architecture
4. Visualisez les résultats

**Fichier à utiliser**: [fashion_mnist_classification.ipynb](https://colab.research.google.com/drive/1a9CJp_rGFxpX3EnfhN9YJGeyK3zO2tWn)

**Points de contrôle**:
- ✓ Le modèle initial atteint >80% de précision
- ✓ Les prédictions sur les exemples de test sont majoritairement correctes
- ✓ Vous comprenez l'impact de vos modifications sur les performances

### 3. MINI-PROJET: API DE RECONNAISSANCE D'IMAGES (35 min)

#### 3.1 Concepts clés des APIs (5 min)
- **API REST**: Interface permettant à différentes applications de communiquer
- **Avantages en entreprise**:
  - Séparation frontend/backend
  - Réutilisation du modèle par plusieurs applications
  - Mise à jour du modèle sans toucher aux applications clientes

#### 3.2 Structure d'une API Flask/FastAPI (10 min)

```python
# Exemple avec Flask
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
    if 'image' not in request.files:
        return jsonify({'error': 'Pas d\'image fournie'}), 400
    
    file = request.files['image']
    image = Image.open(file.stream).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28)
    
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    
    return jsonify({
        'class': class_names[predicted_class],
        'confidence': float(predictions[0][predicted_class])
    })

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3.3 Travail pratique: Développement d'une API (20 min)

**Objectif**: Développer une API qui expose votre modèle de classification Fashion MNIST

**Étapes**:
1. Sauvegarder le modèle entraîné précédemment
2. Implémenter l'API avec Flask ou FastAPI
3. Tester l'API avec des requêtes d'images
4. Ajouter des fonctionnalités supplémentaires

**Fichier à utiliser**: [fashion_mnist_api.ipynb](https://colab.research.google.com/drive/1b2XkdH2NJ_R8n_5_pyIHh7b9HNTlbIXf)

**Points de contrôle**:
- ✓ L'API répond correctement aux requêtes d'images
- ✓ Le prétraitement des images fonctionne bien
- ✓ Les réponses incluent la classe prédite et le niveau de confiance

### FICHIERS À AJOUTER AU PROJET

#### 1. Notebook: TensorFlow/Keras pour débutants (tensorflow_keras_debutants.ipynb)

```python
# TensorFlow/Keras pour débutants
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("Version de TensorFlow:", tf.__version__)

# 1. Chargement des données Fashion MNIST
print("Chargement du jeu de données Fashion MNIST...")
(train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()

# Noms des classes
class_names = ['T-shirt/Top', 'Pantalon', 'Pull', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Basket', 'Sac', 'Bottine']

# 2. Exploration des données
print(f"Forme des données d'entraînement: {train_images.shape}")
print(f"Nombre d'échantillons d'entraînement: {len(train_labels)}")
print(f"Forme des données de test: {test_images.shape}")

# Affichage de quelques exemples
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap='gray')
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# 3. Prétraitement des données
# Normalisation des valeurs de pixels entre 0 et 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# 4. Création d'un modèle simple
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Conversion 28x28 -> 784
    keras.layers.Dense(128, activation='relu'),   # Couche cachée avec 128 neurones
    keras.layers.Dense(10, activation='softmax')  # Couche de sortie avec 10 neurones (10 classes)
])

# Affichage du résumé du modèle
model.summary()

# 5. Compilation du modèle
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 6. Entraînement du modèle
print("Entraînement du modèle...")
history = model.fit(
    train_images, 
    train_labels, 
    epochs=5,
    validation_split=0.2
)

# 7. Visualisation de l'apprentissage
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 8. Évaluation du modèle
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"\nPrécision sur les données de test: {test_acc*100:.2f}%")

# 9. Faire des prédictions
predictions = model.predict(test_images)

# Afficher les prédictions pour quelques images
plt.figure(figsize=(12, 12))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(test_images[i], cmap='gray')
    
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]
    
    color = 'blue' if predicted_label == true_label else 'red'
    
    plt.xlabel(f"Prédit: {class_names[predicted_label]}\nRéel: {class_names[true_label]}", color=color)
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()

# 10. Exercice: Améliorer le modèle
# TODO: Modifiez l'architecture du modèle pour améliorer les performances
# Suggestions:
# - Ajouter plus de couches Dense
# - Ajouter du Dropout pour réduire le surapprentissage
# - Essayer différentes fonctions d'activation
# - Modifier le nombre de neurones

# 11. Sauvegarde du modèle
model.save('fashion_mnist_model.h5')
print("Modèle sauvegardé avec succès dans 'fashion_mnist_model.h5'")
```

#### 2. Notebook: API de reconnaissance d'images (fashion_mnist_api.ipynb)

```python
# API de reconnaissance d'images avec Flask
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image
import io
import base64
from IPython.display import HTML, display
import json

# 1. Création ou chargement du modèle
# Option 1: Entraîner un nouveau modèle
def train_model():
    print("Entraînement d'un nouveau modèle...")
    
    # Chargement des données
    (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
    
    # Normalisation
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    
    # Création du modèle
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    # Compilation
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Entraînement
    model.fit(train_images, train_labels, epochs=5, validation_split=0.2)
    
    # Sauvegarde
    model.save('fashion_mnist_model.h5')
    print("Modèle sauvegardé dans 'fashion_mnist_model.h5'")
    
    return model, test_images, test_labels

# Option 2: Charger un modèle existant
def load_model():
    try:
        print("Chargement du modèle existant...")
        model = keras.models.load_model('fashion_mnist_model.h5')
        
        # Chargement des données de test
        (_, _), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        test_images = test_images / 255.0
        
        return model, test_images, test_labels
    except:
        print("Modèle existant non trouvé. Entraînement d'un nouveau modèle...")
        return train_model()

# Choix de l'option (décommentez celle que vous souhaitez utiliser)
# model, test_images, test_labels = train_model()
model, test_images, test_labels = load_model()

# Classes pour Fashion MNIST
class_names = ['T-shirt/Top', 'Pantalon', 'Pull', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Basket', 'Sac', 'Bottine']

# 2. Préparation des fonctions de l'API
def preprocess_image(image):
    """Prétraite une image pour la prédiction"""
    # Redimensionnement et conversion en niveaux de gris
    image = image.convert('L').resize((28, 28))
    
    # Conversion en array et normalisation
    image_array = np.array(image) / 255.0
    
    # Ajout de la dimension batch
    image_array = image_array.reshape(1, 28, 28)
    
    return image_array

def predict_image(image_array):
    """Prédit la classe d'une image"""
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class])
    
    return {
        'class': class_names[predicted_class],
        'class_id': int(predicted_class),
        'confidence': confidence * 100  # En pourcentage
    }

# 3. Création d'une API Flask simplifiée
# Note: Dans Colab, nous ne pouvons pas exécuter un vrai serveur Flask,
# mais nous pouvons simuler son comportement

def simulate_api_call(image):
    """Simule un appel à l'API Flask"""
    try:
        # Prétraitement
        image_array = preprocess_image(image)
        
        # Prédiction
        result = predict_image(image_array)
        
        return {
            'success': True,
            'prediction': result
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

# 4. Interface de test dans Colab
from google.colab import files
from IPython.display import display, clear_output

def test_with_upload():
    """Interface pour tester avec un upload d'image"""
    clear_output()
    print("Téléchargez une image de vêtement...")
    uploaded = files.upload()
    
    for filename in uploaded.keys():
        image = Image.open(io.BytesIO(uploaded[filename]))
        
        # Afficher l'image
        plt.figure(figsize=(4, 4))
        plt.imshow(image)
        plt.axis('off')
        plt.title("Image téléchargée")
        plt.show()
        
        # Simuler l'appel API
        result = simulate_api_call(image)
        
        if result['success']:
            pred = result['prediction']
            print(f"Classe prédite: {pred['class']}")
            print(f"Confiance: {pred['confidence']:.2f}%")
            
            # Graphique des probabilités
            predictions = model.predict(preprocess_image(image))[0]
            plt.figure(figsize=(10, 3))
            plt.bar(range(len(predictions)), predictions)
            plt.xticks(range(len(predictions)), class_names, rotation=45)
            plt.xlabel('Classe')
            plt.ylabel('Probabilité')
            plt.title('Probabilités par classe')
            plt.show()
        else:
            print(f"Erreur: {result['error']}")

# 5. Test avec des exemples de Fashion MNIST
def test_with_samples():
    """Test avec des exemples du jeu de données"""
    # Sélectionner quelques exemples
    sample_indices = np.random.choice(len(test_images), 3, replace=False)
    
    for idx in sample_indices:
        # Convertir l'array en image
        image = Image.fromarray((test_images[idx] * 255).astype(np.uint8))
        
        # Afficher l'image
        plt.figure(figsize=(4, 4))
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.title(f"Vrai classe: {class_names[test_labels[idx]]}")
        plt.show()
        
        # Simuler l'appel API
        result = simulate_api_call(image)
        
        if result['success']:
            pred = result['prediction']
            print(f"Classe prédite: {pred['class']}")
            print(f"Confiance: {pred['confidence']:.2f}%")
        else:
            print(f"Erreur: {result['error']}")
        
        print("-" * 50)

# 6. Implémentation complète de l'API Flask (code à exécuter localement)
flask_code = """
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Charger le modèle
model = tf.keras.models.load_model('fashion_mnist_model.h5')

# Classes
class_names = ['T-shirt/top', 'Pantalon', 'Pull', 'Robe', 'Manteau',
               'Sandale', 'Chemise', 'Basket', 'Sac', 'Bottine']

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'Pas d\\'image fournie'}), 400
    
    file = request.files['image']
    
    # Lire et prétraiter l'image
    image = Image.open(file.stream).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28)
    
    # Faire la prédiction
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class])
    
    return jsonify({
        'class': class_names[predicted_class],
        'class_id': int(predicted_class),
        'confidence': confidence * 100  # En pourcentage
    })

@app.route('/info', methods=['GET'])
def model_info():
    return jsonify({
        'name': 'Fashion MNIST Classifier',
        'classes': class_names,
        'version': '1.0'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
"""

print("Code Flask pour l'API (à utiliser localement):")
print("-" * 80)
print(flask_code)
print("-" * 80)

# Affichage du menu
print("\nOptions de test:")
print("1. Tester avec vos propres images")
print("2. Tester avec des exemples du jeu de données")

choice = input("Entrez votre choix (1 ou 2): ")
if choice == "1":
    test_with_upload()
elif choice == "2":
    test_with_samples()
else:
    print("Choix non valide")
```

### RESSOURCES SUPPLÉMENTAIRES

1. **Guide d'installation locale**
   - Instructions détaillées pour installer TensorFlow en local
   - Solutions aux problèmes courants
   - Configurations recommandées

2. **Cheat Sheet TensorFlow/Keras**
   - Résumé des fonctions et méthodes principales
   - Exemples d'utilisation communs
   - Bonnes pratiques

3. **Liste de vérification du projet API**
   - Points à vérifier avant de finaliser votre API
   - Conseils pour un déploiement réussi
   - Ressources pour aller plus loin

Cette structure révisée offre une progression plus claire, ajoute les fichiers manquants et fournit des points de contrôle pour que les étudiants puissent suivre leur progression. Les ressources supplémentaires aident également à résoudre les problèmes courants et à approfondir leurs connaissances.