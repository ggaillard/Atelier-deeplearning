Bien sûr, voici le fichier frameworks.md complet avec la partie sur le mini-projet simplifiée :

# Phase 1 : Frameworks de Deep Learning (1h30)

![Frameworks pour débutants](https://images.unsplash.com/photo-1545987796-200677ee1011?auto=format&fit=crop&q=80&w=1000&h=300)

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

## Atelier pratique : Prise en main de TensorFlow/Keras (30 min)

### Objectif

Développer une première application de reconnaissance d'images simple en utilisant TensorFlow/Keras et en suivant les bonnes pratiques de l'industrie.

### Instructions

1. **Configuration de l'environnement (5 min)**

   Ouvrez Google Colab et créez un nouveau notebook. Commencez par installer et importer les bibliothèques nécessaires:

   ```python
   # Vérification de la version de TensorFlow
   import tensorflow as tf
   print("TensorFlow version:", tf.__version__)
   
   # Importation des bibliothèques essentielles
   from tensorflow.keras import layers, models
   from tensorflow.keras.applications import MobileNetV2
   from tensorflow.keras.preprocessing import image
   import numpy as np
   import matplotlib.pyplot as plt
   ```

2. **Utilisation d'un modèle pré-entraîné (10 min)**

   Au lieu de créer un modèle à partir de zéro, nous allons utiliser un modèle pré-entraîné, comme le font la plupart des professionnels:

   ```python
   # Chargement d'un modèle pré-entraîné (sans les couches de classification)
   base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
   
   # Gel des couches pré-entraînées pour éviter leur modification
   base_model.trainable = False
   
   # Création de notre propre modèle en ajoutant des couches de classification
   model = models.Sequential([
       base_model,
       layers.GlobalAveragePooling2D(),
       layers.Dense(1024, activation='relu'),
       layers.Dense(1000, activation='softmax')  # 1000 classes ImageNet
   ])
   
   # Résumé du modèle pour comprendre son architecture
   model.summary()
   ```

3. **Préparation d'une image de test (5 min)**

   ```python
   # Téléchargement d'une image d'exemple
   !wget -q -O test_image.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Pug_600.jpg/280px-Pug_600.jpg
   
   # Fonction simple pour prétraiter une image
   def preprocess_image(img_path):
       # Chargement et redimensionnement
       img = image.load_img(img_path, target_size=(224, 224))
       
       # Conversion en tableau numpy
       img_array = image.img_to_array(img)
       
       # Ajout de la dimension de batch
       img_array = np.expand_dims(img_array, axis=0)
       
       # Prétraitement pour le modèle
       img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
       
       return img_array
   
   # Affichage de l'image
   plt.figure(figsize=(4, 4))
   plt.imshow(image.load_img('test_image.jpg'))
   plt.axis('off')
   plt.show()
   
   # Prétraitement
   processed_image = preprocess_image('test_image.jpg')
   ```

4. **Prédiction et interprétation des résultats (10 min)**

   Utilisez le modèle pour faire une prédiction et visualisez les résultats:

   ```python
   # Prédiction
   predictions = model.predict(processed_image)
   
   # Interprétation des résultats (top 5)
   from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
   
   # Décodage des prédictions (conversion des indices en labels)
   decoded_predictions = decode_predictions(predictions, top=5)[0]
   
   # Affichage des résultats
   plt.figure(figsize=(10, 3))
   labels = [pred[1] for pred in decoded_predictions]
   scores = [pred[2] for pred in decoded_predictions]
   
   plt.barh(labels, scores)
   plt.xlabel('Probabilité')
   plt.title('Top 5 des prédictions')
   plt.xlim(0, 1.0)
   plt.gca().invert_yaxis()  # Pour que le plus probable soit en haut
   plt.show()
   
   print("Prédictions:")
   for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
       print(f"{i+1}. {label} ({score:.2f})")
   ```

## Mini-projet : Développement d'une API de reconnaissance d'images (45 min)

### Objectif

Créer une API REST simple qui permette à d'autres applications d'utiliser votre modèle de reconnaissance d'images.

### Instructions

#### 1. Préparation de l'environnement pour l'API (5 min)

```python
# Installation de Flask pour l'API
!pip install flask flask-cors
```

#### 2. Création de l'application Flask (20 min)

Créez un fichier `app.py` avec le code suivant:

```python
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
from flask_cors import CORS
import base64
from io import BytesIO
from PIL import Image

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin

# Chargement du modèle pré-entraîné
print("Chargement du modèle...")
model = MobileNetV2(weights='imagenet')
print("Modèle chargé!")

# Fonction de prétraitement des images
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

# Endpoint principal pour les prédictions
@app.route('/predict', methods=['POST'])
def predict():
    # Vérification qu'une image a été envoyée
    if 'image' not in request.files:
        # Vérifier si l'image est envoyée en base64
        if request.json and 'image' in request.json:
            # Décodage de l'image base64
            image_data = base64.b64decode(request.json['image'].split(',')[1])
            img = Image.open(BytesIO(image_data))
        else:
            return jsonify({'error': 'Aucune image fournie'}), 400
    else:
        # Lecture de l'image depuis les fichiers
        file = request.files['image']
        img = Image.open(file.stream)
    
    # Prétraitement
    processed_img = preprocess_image(img)
    
    # Prédiction
    predictions = model.predict(processed_img)
    
    # Décodage des prédictions (top 5)
    decoded = decode_predictions(predictions, top=5)[0]
    
    # Formatage de la réponse
    results = []
    for _, label, score in decoded:
        results.append({
            'label': label,
            'probability': float(score)
        })
    
    return jsonify({
        'predictions': results
    })

if __name__ == '__main__':
    # Démarrer le serveur sur le port 5000
    app.run(host='0.0.0.0', port=5000)
```

#### 3. Interface utilisateur simple (15 min)

Créez un fichier `index.html` avec ce code:

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reconnaissance d'images</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .upload-section {
            margin: 20px 0;
            text-align: center;
        }
        #preview {
            max-width: 100%;
            max-height: 300px;
            margin: 20px auto;
            display: none;
            border-radius: 8px;
        }
        #results {
            margin-top: 20px;
            display: none;
        }
        .result-item {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        #loading {
            text-align: center;
            display: none;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Reconnaissance d'Images</h1>
        <p>Téléchargez une image pour voir ce que l'IA peut reconnaître.</p>
        
        <div class="upload-section">
            <input type="file" id="image-upload" accept="image/*">
            <button id="predict-button">Analyser l'image</button>
        </div>
        
        <img id="preview" src="#" alt="Aperçu de l'image">
        
        <div id="loading">
            Analyse en cours...
        </div>
        
        <div id="results">
            <h2>Résultats</h2>
            <div id="predictions-container"></div>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const imageUpload = document.getElementById('image-upload');
            const previewImage = document.getElementById('preview');
            const predictButton = document.getElementById('predict-button');
            const resultsDiv = document.getElementById('results');
            const loadingDiv = document.getElementById('loading');
            const predictionsContainer = document.getElementById('predictions-container');
            
            // Aperçu de l'image
            imageUpload.addEventListener('change', function() {
                if (this.files && this.files[0]) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        previewImage.src = e.target.result;
                        previewImage.style.display = 'block';
                        resultsDiv.style.display = 'none';
                    }
                    reader.readAsDataURL(this.files[0]);
                }
            });
            
            // Envoi de l'image pour analyse
            predictButton.addEventListener('click', function() {
                if (!imageUpload.files || !imageUpload.files[0]) {
                    alert('Veuillez sélectionner une image.');
                    return;
                }
                
                loadingDiv.style.display = 'block';
                resultsDiv.style.display = 'none';
                
                const formData = new FormData();
                formData.append('image', imageUpload.files[0]);
                
                fetch('http://localhost:5000/predict', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    loadingDiv.style.display = 'none';
                    predictionsContainer.innerHTML = '';
                    
                    if (data.error) {
                        predictionsContainer.innerHTML = `<p class="error">${data.error}</p>`;
                    } else {
                        data.predictions.forEach(pred => {
                            const resultItem = document.createElement('div');
                            resultItem.className = 'result-item';
                            
                            const label = document.createElement('div');
                            label.textContent = pred.label.replace('_', ' ');
                            
                            const probability = document.createElement('div');
                            probability.textContent = `${(pred.probability * 100).toFixed(2)}%`;
                            
                            resultItem.appendChild(label);
                            resultItem.appendChild(probability);
                            predictionsContainer.appendChild(resultItem);
                        });
                    }
                    
                    resultsDiv.style.display = 'block';
                })
                .catch(error => {
                    loadingDiv.style.display = 'none';
                    alert('Erreur lors de la communication avec l\'API: ' + error);
                });
            });
        });
    </script>
</body>
</html>
```

#### 4. Lancement et test de l'API (5 min)

```python
# Lancer le serveur Flask
!python app.py
```

Dans votre navigateur, ouvrez le fichier `index.html` pour accéder à l'interface utilisateur.

### Comment tester votre API

1. **Via l'interface web**:
   - Téléchargez une image en cliquant sur le bouton de sélection de fichier
   - Cliquez sur "Analyser l'image"
   - Observez les résultats qui s'affichent

2. **Via des requêtes HTTP directes**:
   ```python
   import requests

   # Avec un fichier
   with open('test_image.jpg', 'rb') as img:
       response = requests.post('http://localhost:5000/predict', 
                               files={'image': img})
   
   # Afficher les résultats
   print(response.json())
   ```

## Bonnes pratiques pour les projets professionnels (15 min)

Pour conclure cette phase, passons en revue les bonnes pratiques essentielles pour développer des applications de Deep Learning en contexte professionnel:

### 1. Structure du code

- **Modularité**: Séparez clairement les différentes fonctionnalités (prétraitement, modèle, API)
- **Documentation**: Commentez votre code et créez une documentation utilisateur
- **Gestion d'erreurs**: Prévoyez des cas d'erreur et des messages adaptés
- **Logging**: Ajoutez des logs pour faciliter le débogage

### 2. Performances

- **Batch processing**: Traitez les données par lots plutôt qu'individuellement
- **Mise en cache**: Évitez de recharger le modèle à chaque requête
- **Précalcul**: Précalculez ce qui peut l'être pour accélérer les inférences
- **Optimisation matérielle**: Utilisez GPU/TPU quand disponible, CPU optimisé sinon

### 3. Sécurité

- **Validation des entrées**: Vérifiez toujours les données entrantes
- **Limitation de taille**: Fixez une taille maximale pour les fichiers
- **Rate limiting**: Limitez le nombre de requêtes par utilisateur
- **Sanitization**: Nettoyez les chemins de fichiers et autres entrées sensibles

### 4. Déploiement

- **Conteneurisation**: Utilisez Docker pour faciliter le déploiement
- **CI/CD**: Automatisez les tests et le déploiement
- **Monitoring**: Surveillez les performances et erreurs
- **Versioning**: Versionnez vos modèles et API

## Conclusion et transition

Cette phase vous a permis de découvrir comment utiliser efficacement TensorFlow/Keras dans un contexte professionnel, en développant une API simple mais fonctionnelle de reconnaissance d'images. Dans la prochaine partie, nous allons nous concentrer sur l'amélioration des performances de nos modèles pour les rendre plus adaptés à des environnements de production.

[Retour au Module 3](index.md){ .md-button }
[Continuer vers l'amélioration des performances](integration.md){ .md-button .md-button--primary }