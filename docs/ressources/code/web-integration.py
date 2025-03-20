# Intégration d'un modèle CNN dans une application web
# BTS SIO SLAM - Séance 2: Types de réseaux et applications

from flask import Flask, request, jsonify, render_template, send_from_directory
import tensorflow as tf
import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import time

# Créer l'application Flask
app = Flask(__name__)

# Configuration
MODEL_PATH = 'cnn_mnist_model.h5'  # Chemin vers le modèle entraîné
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Charger le modèle CNN
print("Chargement du modèle...")
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Modèle chargé avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du modèle: {e}")
    print("Un modèle par défaut sera utilisé")
    # Si le modèle n'est pas trouvé, créer un modèle simple pour démonstration
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fonction de prétraitement des images
def preprocess_image(image_data):
    """
    Prétraite l'image pour qu'elle corresponde au format attendu par le modèle
    """
    # Convertir l'image en niveaux de gris
    image = ImageOps.grayscale(image_data)
    
    # Redimensionner à 28x28 pixels
    image = image.resize((28, 28))
    
    # Normaliser les pixels entre 0 et 1
    image_array = np.array(image) / 255.0
    
    # Ajouter les dimensions de batch et de canal
    image_array = image_array.reshape(1, 28, 28, 1)
    
    return image_array

# Fonction pour générer la visualisation des prédictions
def generate_prediction_visualization(image_array, prediction):
    """
    Génère une visualisation des probabilités de prédiction pour chaque chiffre
    """
    plt.figure(figsize=(10, 4))
    
    # Afficher l'image originale
    plt.subplot(1, 2, 1)
    plt.imshow(image_array.reshape(28, 28), cmap='gray')
    plt.title('Image d\'entrée')
    plt.axis('off')
    
    # Afficher les probabilités
    plt.subplot(1, 2, 2)
    classes = range(10)
    plt.bar(classes, prediction[0])
    plt.xticks(classes)
    plt.xlabel('Chiffre')
    plt.ylabel('Probabilité')
    plt.title('Prédiction du modèle')
    
    # Sauvegarder l'image en mémoire
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # Convertir en base64 pour l'affichage HTML
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

# Routes Flask
@app.route('/')
def home():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint pour prédire le chiffre à partir d'une image"""
    # Vérifier si une image a été envoyée
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image fournie'}), 400
    
    file = request.files['image']
    
    # Vérifier si le fichier est vide
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide'}), 400
    
    try:
        # Ouvrir et prétraiter l'image
        image = Image.open(file)
        processed_image = preprocess_image(image)
        
        # Mesurer le temps d'inférence
        start_time = time.time()
        prediction = model.predict(processed_image)
        inference_time = time.time() - start_time
        
        # Déterminer le chiffre avec la plus haute probabilité
        predicted_digit = np.argmax(prediction[0])
        confidence = float(prediction[0][predicted_digit] * 100)
        
        # Générer la visualisation
        viz_base64 = generate_prediction_visualization(processed_image, prediction)
        
        # Préparation de la réponse
        result = {
            'predicted_digit': int(predicted_digit),
            'confidence': confidence,
            'inference_time_ms': inference_time * 1000,
            'visualization': viz_base64,
            'probabilities': prediction[0].tolist()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Servir les fichiers téléchargés"""
    return send_from_directory(UPLOAD_FOLDER, filename)

# Création des templates
def create_templates():
    """Crée les templates nécessaires pour l'application"""
    os.makedirs('templates', exist_ok=True)
    
    # Index.html
    with open('templates/index.html', 'w') as f:
        f.write("""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reconnaissance de chiffres - CNN MNIST</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f7fa;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .container {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .upload-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
            margin: 20px 0;
            padding: 20px;
            border: 2px dashed #bdc3c7;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        #drop-area {
            width: 100%;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
        #file-input {
            display: none;
        }
        .button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #2980b9;
        }
        .results-container {
            margin-top: 20px;
            display: none;
        }
        .loading {
            text-align: center;
            margin: 20px 0;
            display: none;
        }
        .prediction-result {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin: 20px 0;
        }
        .info-box {
            background-color: #e8f4fc;
            border-left: 4px solid #3498db;
            padding: 10px 15px;
            margin: 15px 0;
            border-radius: 4px;
        }
        .visualization {
            max-width: 100%;
            height: auto;
            margin: 20px 0;
        }
        @media (max-width: 600px) {
            .upload-container {
                padding: 10px;
            }
            #drop-area {
                height: 150px;
            }
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Reconnaissance de chiffres avec un CNN</h1>
        <p>Cette application utilise un réseau de neurones convolutif (CNN) entraîné sur le dataset MNIST pour reconnaître des chiffres manuscrits.</p>
        
        <div class="info-box">
            <p><strong>Comment utiliser :</strong> Uploadez une image d'un chiffre manuscrit (préférablement sur fond blanc). Le modèle analysera l'image et prédira le chiffre.</p>
        </div>
        
        <div class="upload-container">
            <div id="drop-area">
                <p>Glissez-déposez une image ici</p>
                <p>ou</p>
                <label for="file-input" class="button">Choisir une image</label>
                <input type="file" id="file-input" accept="image/*">
            </div>
            <div id="preview-container" style="display: none;">
                <img id="preview-image" style="max-width: 200px; max-height: 200px;">
                <button id="predict-button" class="button">Analyser l'image</button>
            </div>
        </div>
        
        <div id="loading" class="loading">
            <p>Analyse de l'image en cours...</p>
        </div>
        
        <div id="results" class="results-container">
            <div class="prediction-result">
                Chiffre prédit : <span id="predicted-digit">-</span>
                <span id="confidence"></span>
            </div>
            
            <div id="visualization-container">
                <img id="visualization" class="visualization">
            </div>
            
            <div class="info-box">
                <h3>Informations techniques</h3>
                <table>
                    <tr>
                        <th>Métrique</th>
                        <th>Valeur</th>
                    </tr>
                    <tr>
                        <td>Temps d'inférence</td>
                        <td id="inference-time">-</td>
                    </tr>
                    <tr>
                        <td>Confiance</td>
                        <td id="confidence-value">-</td>
                    </tr>
                    <tr>
                        <td>Modèle</td>
                        <td>CNN (TensorFlow/Keras)</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    
    <div class="container">
        <h2>À propos de cette application</h2>
        <p>Cette application démontre l'intégration d'un modèle de Deep Learning (CNN) dans une application web. Les réseaux de neurones convolutifs sont particulièrement efficaces pour les tâches de vision par ordinateur comme la reconnaissance d'images.</p>
        
        <h3>Comment fonctionne un CNN?</h3>
        <p>Un CNN (Convolutional Neural Network) utilise des couches de convolution pour détecter automatiquement des caractéristiques (features) dans les images :</p>
        <ul>
            <li><strong>Couches de convolution</strong> : détectent des motifs locaux comme des bords, des textures</li>
            <li><strong>Pooling</strong> : réduit la dimensionnalité et rend le modèle plus robuste aux variations</li>
            <li><strong>Couches denses</strong> : effectuent la classification finale</li>
        </ul>
        
        <h3>Technologies utilisées</h3>
        <ul>
            <li><strong>Backend</strong> : Flask (Python), TensorFlow/Keras</li>
            <li><strong>Frontend</strong> : HTML, CSS, JavaScript</li>
            <li><strong>Dataset</strong> : MNIST (chiffres manuscrits)</li>
        </ul>
    </div>
    
    <script>
        // Éléments DOM
        const dropArea = document.getElementById('drop-area');
        const fileInput = document.getElementById('file-input');
        const previewContainer = document.getElementById('preview-container');
        const previewImage = document.getElementById('preview-image');
        const predictButton = document.getElementById('predict-button');
        const loadingIndicator = document.getElementById('loading');
        const resultsContainer = document.getElementById('results');
        const predictedDigit = document.getElementById('predicted-digit');
        const confidenceSpan = document.getElementById('confidence');
        const confidenceValue = document.getElementById('confidence-value');
        const inferenceTime = document.getElementById('inference-time');
        const visualization = document.getElementById('visualization');
        
        // Prevent default drag behaviors
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        // Highlight drop area when item is dragged over it
        ['dragenter', 'dragover'].forEach(eventName => {
            dropArea.addEventListener(eventName, highlight, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, unhighlight, false);
        });
        
        function highlight() {
            dropArea.style.backgroundColor = '#e8f4fc';
            dropArea.style.borderColor = '#3498db';
        }
        
        function unhighlight() {
            dropArea.style.backgroundColor = '#f9f9f9';
            dropArea.style.borderColor = '#bdc3c7';
        }
        
        // Handle dropped files
        dropArea.addEventListener('drop', handleDrop, false);
        
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            handleFiles(files);
        }
        
        // Handle file input change
        fileInput.addEventListener('change', function() {
            handleFiles(this.files);
        });
        
        function handleFiles(files) {
            if (files.length > 0) {
                const file = files[0];
                
                // Check if the file is an image
                if (!file.type.match('image.*')) {
                    alert('Veuillez sélectionner une image');
                    return;
                }
                
                // Preview the image
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                    previewContainer.style.display = 'block';
                    
                    // Hide previous results if any
                    resultsContainer.style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        }
        
        // Handle prediction button click
        predictButton.addEventListener('click', function() {
            // Show loading indicator
            loadingIndicator.style.display = 'block';
            
            // Create form data
            const formData = new FormData();
            formData.append('image', fileInput.files[0]);
            
            // Send request to the server
            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Hide loading indicator
                loadingIndicator.style.display = 'none';
                
                // Show results
                resultsContainer.style.display = 'block';
                
                if (data.error) {
                    predictedDigit.textContent = 'Erreur';
                    confidenceSpan.textContent = '';
                    alert('Erreur: ' + data.error);
                } else {
                    // Display prediction results
                    predictedDigit.textContent = data.predicted_digit;
                    confidenceSpan.textContent = ` (${data.confidence.toFixed(2)}% de confiance)`;
                    confidenceValue.textContent = `${data.confidence.toFixed(2)}%`;
                    inferenceTime.textContent = `${data.inference_time_ms.toFixed(2)} ms`;
                    
                    // Display visualization
                    visualization.src = 'data:image/png;base64,' + data.visualization;
                }
            })
            .catch(error => {
                loadingIndicator.style.display = 'none';
                alert('Erreur lors de la communication avec le serveur: ' + error);
            });
        });
    </script>
</body>
</html>
        """)
    
    print("Template index.html créé avec succès!")

# Fonction principale
def main():
    # Créer les templates
    create_templates()
    
    # Démarrer l'application Flask
    print("\nDémarrage de l'application web de reconnaissance de chiffres...")
    print("URL: http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == "__main__":
    main()
    