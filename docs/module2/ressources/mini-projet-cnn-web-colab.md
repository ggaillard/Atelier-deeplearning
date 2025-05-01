
### Mini-projet : Reconnaissance de chiffres manuscrits avec interface web dans Colab

#### Contexte professionnel

Vous êtes stagiaire dans une PME où les employés doivent régulièrement saisir manuellement des codes à partir de documents papier (bons de commande, formulaires clients, etc.). Votre responsable informatique souhaite explorer des solutions d'automatisation et vous demande de tester une application de reconnaissance de chiffres manuscrits.

### Étape 1: Configuration de l'environnement Colab (5 minutes)

Créez un nouveau notebook Google Colab et exécutez les cellules suivantes:

```python
# Installation des bibliothèques nécessaires
!pip install -q pyngrok
!pip install -q flask-ngrok

# Importation des bibliothèques
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import io
import base64
from flask import Flask, request, jsonify, render_template_string
from flask_ngrok import run_with_ngrok
import os
from google.colab import files
from pyngrok import ngrok

print("Configuration terminée!")
```

### Étape 2: Création et entraînement du modèle CNN (8 minutes)

```python
# Chargement du dataset MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Prétraitement des données
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Création du modèle CNN
model = Sequential([
    # Première couche de convolution
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Deuxième couche de convolution
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Aplatissement et couches denses
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Affichage de l'architecture
model.summary()

# Entraînement rapide pour la démonstration
print("Entraînement du modèle...")
model.fit(X_train[:10000], y_train[:10000], 
          batch_size=128,
          epochs=3,
          validation_split=0.1,
          verbose=1)

# Évaluation sur l'ensemble de test
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nPrécision sur le test: {test_acc*100:.2f}%")

# Sauvegarde du modèle
model.save('mnist_cnn_model.h5')
print("Modèle entraîné et sauvegardé!")
```

### Étape 3: Création de l'application web Flask (7 minutes)

```python
# Définition du template HTML pour l'application web
html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reconnaissance de chiffres manuscrits</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f7fa;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .canvas-container {
            margin: 20px 0;
            position: relative;
        }
        #canvas {
            border: 2px solid #333;
            border-radius: 5px;
            background-color: #fff;
            cursor: crosshair;
        }
        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .clear-btn {
            background-color: #f44336;
        }
        .clear-btn:hover {
            background-color: #d32f2f;
        }
        .result-container {
            width: 100%;
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #result {
            font-size: 18px;
            margin-bottom: 15px;
        }
        .confidence-bar {
            width: 100%;
            max-width: 400px;
            height: 30px;
            background-color: #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
        }
        .confidence-level {
            height: 100%;
            background-color: #4CAF50;
            text-align: center;
            color: white;
            line-height: 30px;
        }
        #feature-maps {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            justify-content: center;
            margin-top: 20px;
        }
        .feature-map {
            border: 1px solid #ddd;
            background-color: #fff;
        }
        .viz-checkbox {
            margin: 10px 0;
        }
        .file-upload {
            margin: 15px 0;
        }
        .tab-container {
            width: 100%;
            margin-bottom: 20px;
        }
        .tabs {
            display: flex;
            margin-bottom: 10px;
        }
        .tab {
            padding: 10px 15px;
            background-color: #e0e0e0;
            border: 1px solid #ccc;
            border-radius: 5px 5px 0 0;
            cursor: pointer;
            margin-right: 5px;
        }
        .tab.active {
            background-color: #fff;
            border-bottom: 1px solid #fff;
        }
        .tab-content {
            display: none;
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 0 5px 5px 5px;
            background-color: #fff;
        }
        .tab-content.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Reconnaissance de chiffres manuscrits</h1>
        <p>Dessinez un chiffre (0-9) ci-dessous ou importez une image</p>
        
        <div class="tab-container">
            <div class="tabs">
                <div class="tab active" onclick="openTab(event, 'draw-tab')">Dessiner</div>
                <div class="tab" onclick="openTab(event, 'upload-tab')">Importer une image</div>
            </div>
            
            <div id="draw-tab" class="tab-content active">
                <div class="canvas-container">
                    <canvas id="canvas" width="280" height="280"></canvas>
                </div>
                
                <div class="controls">
                    <button id="predict-btn">Prédire</button>
                    <button id="clear-btn" class="clear-btn">Effacer</button>
                </div>
            </div>
            
            <div id="upload-tab" class="tab-content">
                <div class="file-upload">
                    <input type="file" id="image-upload" accept="image/*">
                </div>
                <div id="preview-container" style="display: none;">
                    <h3>Aperçu de l'image:</h3>
                    <img id="preview-image" style="max-width: 280px; max-height: 280px;">
                    <div class="controls" style="margin-top: 10px;">
                        <button id="predict-upload-btn">Prédire</button>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="viz-checkbox">
            <input type="checkbox" id="show-features" name="show-features">
            <label for="show-features">Visualiser les feature maps</label>
        </div>
        
        <div class="result-container" id="result-container" style="display: none;">
            <h2>Résultat:</h2>
            <div id="result">Prédiction en attente...</div>
            
            <div class="confidence-bar">
                <div class="confidence-level" id="confidence-level"></div>
            </div>
            
            <div id="feature-maps-container">
                <h3>Feature Maps:</h3>
                <div id="feature-maps"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Configuration du canvas pour le dessin
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        ctx.lineWidth = 15;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.strokeStyle = 'black';
        
        // Variables pour le dessin
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;
        
        // Remplir le fond en blanc
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Écouteurs d'événements pour le dessin
        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mousemove', draw);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mouseout', stopDrawing);
        
        // Écouteurs tactiles pour les appareils mobiles
        canvas.addEventListener('touchstart', handleTouchStart);
        canvas.addEventListener('touchmove', handleTouchMove);
        canvas.addEventListener('touchend', stopDrawing);
        
        function handleTouchStart(e) {
            e.preventDefault();
            const touch = e.touches[0];
            const rect = canvas.getBoundingClientRect();
            lastX = touch.clientX - rect.left;
            lastY = touch.clientY - rect.top;
            isDrawing = true;
        }
        
        function handleTouchMove(e) {
            e.preventDefault();
            if (!isDrawing) return;
            const touch = e.touches[0];
            const rect = canvas.getBoundingClientRect();
            const x = touch.clientX - rect.left;
            const y = touch.clientY - rect.top;
            
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(x, y);
            ctx.stroke();
            lastX = x;
            lastY = y;
        }
        
        function startDrawing(e) {
            isDrawing = true;
            const rect = canvas.getBoundingClientRect();
            [lastX, lastY] = [e.clientX - rect.left, e.clientY - rect.top];
        }
        
        function draw(e) {
            if (!isDrawing) return;
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(x, y);
            ctx.stroke();
            [lastX, lastY] = [x, y];
        }
        
        function stopDrawing() {
            isDrawing = false;
        }
        
        // Fonction pour effacer le canvas
        document.getElementById('clear-btn').addEventListener('click', clearCanvas);
        
        function clearCanvas() {
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            hideResult();
        }
        
        // Fonction pour prédire à partir du dessin
        document.getElementById('predict-btn').addEventListener('click', () => {
            predictDrawing();
        });
        
        function predictDrawing() {
            const imageData = canvas.toDataURL('image/png').split(',')[1];
            predict(imageData);
        }
        
        // Gestion de l'upload d'image
        document.getElementById('image-upload').addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('preview-image').src = e.target.result;
                    document.getElementById('preview-container').style.display = 'block';
                }
                reader.readAsDataURL(file);
            }
        });
        
        document.getElementById('predict-upload-btn').addEventListener('click', function() {
            const imageData = document.getElementById('preview-image').src.split(',')[1];
            predict(imageData);
        });
        
        // Fonction pour prédire
        function predict(imageData) {
            const showFeatures = document.getElementById('show-features').checked;
            
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    image: imageData,
                    show_features: showFeatures
                })
            })
            .then(response => response.json())
            .then(data => {
                displayResult(data);
            })
            .catch(error => {
                console.error('Erreur:', error);
                alert('Une erreur est survenue lors de la prédiction.');
            });
        }
        
        // Fonction pour afficher le résultat
        function displayResult(data) {
            document.getElementById('result-container').style.display = 'block';
            document.getElementById('result').textContent = `Prédit: ${data.prediction} (${data.confidence.toFixed(2)}%)`;
            
            const confidenceLevel = document.getElementById('confidence-level');
            confidenceLevel.style.width = `${data.confidence}%`;
            confidenceLevel.textContent = `${data.confidence.toFixed(2)}%`;
            
            // Affichage des feature maps si demandé
            const featureMapsContainer = document.getElementById('feature-maps-container');
            const featureMapsDiv = document.getElementById('feature-maps');
            
            if (data.feature_maps && data.feature_maps.length > 0) {
                featureMapsContainer.style.display = 'block';
                featureMapsDiv.innerHTML = '';
                
                data.feature_maps.forEach(mapData => {
                    const img = document.createElement('img');
                    img.src = 'data:image/png;base64,' + mapData;
                    img.className = 'feature-map';
                    img.width = 100;
                    img.height = 100;
                    featureMapsDiv.appendChild(img);
                });
            } else {
                featureMapsContainer.style.display = 'none';
            }
        }
        
        function hideResult() {
            document.getElementById('result-container').style.display = 'none';
        }
        
        // Fonction pour changer d'onglet
        function openTab(evt, tabName) {
            const tabContents = document.getElementsByClassName('tab-content');
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove('active');
            }
            
            const tabs = document.getElementsByClassName('tab');
            for (let i = 0; i < tabs.length; i++) {
                tabs[i].classList.remove('active');
            }
            
            document.getElementById(tabName).classList.add('active');
            evt.currentTarget.classList.add('active');
            
            hideResult();
        }
    </script>
</body>
</html>
"""

# Création de l'application Flask
app = Flask(__name__)
run_with_ngrok(app)  # Intégration avec ngrok pour l'accès public

# Chargement du modèle
model = load_model('mnist_cnn_model.h5')

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image_data = data['image']
    show_features = data.get('show_features', False)
    
    # Décodage de l'image
    image_bytes = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(image_bytes)).convert('L')
    
    # Redimensionnement et prétraitement
    img = img.resize((28, 28))
    img = ImageOps.invert(img)  # Inverser les couleurs si besoin
    
    # Conversion en array et normalisation
    img_array = np.array(img).astype('float32') / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    
    # Prédiction
    predictions = model.predict(img_array)[0]
    predicted_class = np.argmax(predictions)
    confidence = float(predictions[predicted_class] * 100)
    
    # Préparation de la réponse
    response = {
        'prediction': int(predicted_class),
        'confidence': confidence
    }
    
    # Génération des feature maps si demandé
    if show_features:
        feature_maps = []
        
        # Création d'un modèle pour extraire les feature maps de la première couche de convolution
        feature_model = tf.keras.Model(
            inputs=model.inputs,
            outputs=model.layers[0].output
        )
        
        # Obtention des feature maps
        feature_outputs = feature_model.predict(img_array)
        
        # Conversion des feature maps en images
        for i in range(min(8, feature_outputs.shape[3])):  # Limiter à 8 pour plus de clarté
            feature_map = feature_outputs[0, :, :, i]
            
            # Normalisation pour visualisation
            feature_map = (feature_map - feature_map.min()) / (feature_map.max() - feature_map.min() + 1e-9)
            
            # Conversion en image
            plt.figure(figsize=(1, 1))
            plt.imshow(feature_map, cmap='viridis')
            plt.axis('off')
            
            # Sauvegarde en buffer puis conversion en base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
            buf.seek(0)
            img_str = base64.b64encode(buf.read()).decode('utf-8')
            feature_maps.append(img_str)
            plt.close()
        
        response['feature_maps'] = feature_maps
    
    return jsonify(response)

# Configuration et lancement de l'application Flask
def run_app():
    app.run()

print("Configuration de l'application terminée!")
```

### Étape 4: Lancement de l'application web (2 minutes)

```python
# Configurer et lancer ngrok avec Colab
# Définir un token ngrok (optionnel mais recommandé pour éviter les limitations)
# Vous pouvez créer un compte gratuit sur ngrok.com pour obtenir un token
ngrok_token = input("Entrez votre token ngrok (optionnel, appuyez sur Entrée pour ignorer): ")
if ngrok_token:
    !ngrok authtoken {ngrok_token}

# Lancer l'application Flask avec ngrok
print("Lancement de l'application web...")
print("Cela peut prendre quelques secondes...")
app.run()
```

### Étape 5: Tests pratiques (15 minutes)

Une fois l'application lancée, vous obtiendrez un lien ngrok (https://xxxx.ngrok.io) que vous pourrez ouvrir dans un nouvel onglet de votre navigateur.

1. **Test avec dessins à la souris**
   - Dans l'interface web, dessinez clairement un chiffre (de 0 à 9) dans la zone prévue
   - Cliquez sur le bouton "Prédire"
   - Notez la prédiction et le niveau de confiance
   - Répétez ce processus avec 5 chiffres différents
   - Remplissez le tableau des résultats dans la section d'évaluation

2. **Test avec image importée**
   - Préparez une image de chiffre manuscrit (vous pouvez l'écrire sur papier et prendre une photo)
   - Cliquez sur l'onglet "Importer une image"
   - Sélectionnez votre image
   - Cliquez sur "Prédire" et notez les résultats

3. **Test avec feature maps**
   - Cochez la case "Visualiser les feature maps"
   - Dessinez un nouveau chiffre et cliquez sur "Prédire"
   - Observez les feature maps qui s'affichent

### Étape 6: Évaluation et documentation (10 minutes)

À l'aide de cette cellule, créez un tableau pour consigner vos résultats:

```python
# Création d'un tableau pour documenter les résultats
from IPython.display import Markdown, display
import pandas as pd

# Afficher un tableau pour les résultats
data = {
    'Chiffre dessiné': [],
    'Prédiction': [],
    'Confiance (%)': [],
    'Correct (Oui/Non)': []
}

# Ajouter les résultats observés pendant vos tests (exemple)
# Remplacez par vos propres données
data['Chiffre dessiné'] = [5, 7, 3, 9, 0]  # Exemple, remplacez par vos tests
data['Prédiction'] = [5, 7, 8, 9, 0]       # Exemple, remplacez par vos résultats
data['Confiance (%)'] = [98.2, 96.5, 74.3, 88.1, 99.0]  # Exemple
data['Correct (Oui/Non)'] = ['Oui', 'Oui', 'Non', 'Oui', 'Oui']  # Exemple

# Création et affichage du tableau
results_df = pd.DataFrame(data)
display(results_df)

# Calcul et affichage des statistiques
correct_count = results_df['Correct (Oui/Non)'].value_counts().get('Oui', 0)
total_count = len(results_df)
accuracy = (correct_count / total_count) * 100 if total_count > 0 else 0

display(Markdown(f"""
### Résumé des tests
- **Nombre total de tests:** {total_count}
- **Prédictions correctes:** {correct_count}
- **Taux de réussite:** {accuracy:.2f}%
- **Confiance moyenne:** {results_df['Confiance (%)'].mean():.2f}%
"""))

# Les chiffres les mieux reconnus et les plus difficiles
display(Markdown("""
### Observations
- **Chiffres les mieux reconnus:** [À compléter]
- **Chiffres les plus difficiles:** [À compléter]
- **Niveau de confiance moyen:** [À compléter]
"""))

# Analyse critique
display(Markdown("""
### Points forts et limitations

**Points forts:**
1. [À compléter]
2. [À compléter]
3. [À compléter]

**Limitations:**
1. [À compléter]
2. [À compléter]
3. [À compléter]
"""))

# Propositions d'amélioration
display(Markdown("""
### Propositions d'amélioration
1. [À compléter]
2. [À compléter]
3. [À compléter]
"""))
```

## Livrable à rendre

À la fin de la session, créez une copie de votre notebook Colab et partagez-le avec votre formateur. Assurez-vous d'avoir rempli toutes les sections d'évaluation avec vos observations.

1. Dans Google Colab, cliquez sur "Fichier" > "Enregistrer une copie dans Drive"
2. Une fois sauvegardé dans Google Drive, cliquez sur "Partager" en haut à droite
3. Ajoutez l'adresse email de votre formateur et définissez les permissions sur "Lecteur"
4. Cliquez sur "Envoyer"

## Pour aller plus loin (si vous terminez en avance)

Si vous avez terminé avant la fin du temps imparti, explorez ces pistes :
- Comment utiliser d'autres architectures CNN (VGG16, MobileNet) via TensorFlow Hub
- Comment améliorer la robustesse du modèle avec l'augmentation de données
- Comment optimiser le modèle pour des performances plus rapides
```

