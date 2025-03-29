"""
Template d'API FastAPI pour exposer un modèle de Deep Learning
Version: 1.0
Pour:  Séance 3

Fonctionnalités incluses:
- Structure de base d'une API FastAPI
- Chargement d'un modèle TensorFlow
- Prétraitement des images
- Endpoint de prédiction
- Documentation automatique des endpoints (Swagger UI)
- Gestion des erreurs
- Rate limiting simple
- Système de cache basique
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, Request, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import time
import hashlib
import logging
from functools import wraps
from datetime import datetime, timedelta
import json
import uvicorn
from pydantic import BaseModel
from typing import List, Dict, Optional, Any

# Configuration de l'application
app = FastAPI(
    title="API de Deep Learning",
    description="API pour exposer un modèle de Deep Learning pour la classification d'images",
    version="1.0.0"
)

# Permettre CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("api-dl")

# Variables de configuration (à ajuster selon vos besoins)
MODEL_PATH = "mon_modele.h5"  # Chemin vers votre modèle sauvegardé
CLASS_NAMES = []  # Noms des classes que votre modèle peut prédire
MAX_REQUESTS_PER_MINUTE = 60  # Limite de requêtes par minute
CACHE_DURATION = 300  # Durée de cache en secondes (5 minutes)

# Système de limite de requêtes simple
request_counts = {}  # Format: {ip: {'count': n, 'last_reset': timestamp}}

# Système de cache simple
prediction_cache = {}  # Format: {image_hash: {'prediction': result, 'timestamp': time}}

# --- Chargement du modèle ---
def load_model():
    """Charge le modèle TensorFlow depuis le fichier sauvegardé"""
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        logger.info(f"Modèle chargé avec succès depuis {MODEL_PATH}")
        return model
    except Exception as e:
        logger.error(f"Erreur lors du chargement du modèle: {str(e)}")
        # Retourner None indique un échec de chargement
        return None

# Charger le modèle au démarrage de l'application
model = load_model()

# --- Modèles de données avec Pydantic ---
class PredictionResult(BaseModel):
    prediction: int
    confidence: float
    class_name: Optional[str] = None
    processing_time: float

class ErrorResponse(BaseModel):
    error: str
    details: Optional[str] = None

# --- Middleware de limiter de requêtes ---
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Obtenir l'adresse IP du client
    ip = request.client.host
    
    # Vérifier uniquement les routes API
    if request.url.path.startswith("/api/"):
        now = time.time()
        
        # Initialiser ou réinitialiser le compteur si nécessaire
        if ip not in request_counts or now - request_counts[ip]["last_reset"] > 60:
            request_counts[ip] = {"count": 0, "last_reset": now}
        
        # Vérifier la limite
        if request_counts[ip]["count"] >= MAX_REQUESTS_PER_MINUTE:
            return JSONResponse(
                status_code=429,
                content={"error": "Too many requests", "retry_after": "60 seconds"}
            )
        
        # Incrémenter le compteur
        request_counts[ip]["count"] += 1
    
    # Continuer le traitement de la requête
    response = await call_next(request)
    return response

# --- Fonctions de prétraitement ---
def get_image_hash(image_data):
    """
    Génère un hash unique pour une image donnée
    """
    return hashlib.md5(image_data).hexdigest()

def preprocess_image(image, target_size=(224, 224)):
    """
    Prétraite une image pour la prédiction
    
    Args:
        image (PIL.Image): Image à prétraiter
        target_size (tuple): Taille cible de l'image
        
    Returns:
        numpy.ndarray: Image prétraitée prête pour la prédiction
    """
    # Redimensionner
    image = image.resize(target_size)
    
    # Convertir en tableau numpy
    image_array = np.array(image)
    
    # Normaliser les valeurs de pixels entre 0 et 1
    image_array = image_array / 255.0
    
    # Ajouter la dimension de batch
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

# --- Routes API ---
@app.get("/")
async def root():
    """Page d'accueil de l'API"""
    return {"message": "Bienvenue sur l'API de Deep Learning. Accédez à /docs pour la documentation."}

@app.post("/api/predict", response_model=PredictionResult)
async def predict(file: UploadFile = File(...)):
    """
    Prédit la classe d'une image
    
    Args:
        file: Fichier image à classifier
        
    Returns:
        PredictionResult: Résultat de la prédiction
    """
    # Vérifier que le modèle est chargé
    if model is None:
        raise HTTPException(status_code=500, detail="Modèle non disponible")
    
    # Lire l'image
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la lecture de l'image: {str(e)}")
    
    # Vérifier si l'image est dans le cache
    image_hash = get_image_hash(image_data)
    current_time = time.time()
    
    if image_hash in prediction_cache:
        cache_entry = prediction_cache[image_hash]
        if current_time - cache_entry["timestamp"] < CACHE_DURATION:
            logger.info(f"Résultat trouvé dans le cache pour {file.filename}")
            return cache_entry["prediction"]
    
    # Prétraiter l'image
    try:
        processed_image = preprocess_image(image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors du prétraitement: {str(e)}")
    
    # Faire la prédiction
    try:
        start_time = time.time()
        predictions = model.predict(processed_image)
        end_time = time.time()
        
        processing_time = end_time - start_time
        
        # Extraire la classe prédite et la confiance
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])
        
        # Ajouter le nom de classe s'il est disponible
        class_name = CLASS_NAMES[predicted_class] if predicted_class < len(CLASS_NAMES) else None
        
        # Créer le résultat
        result = PredictionResult(
            prediction=int(predicted_class),
            confidence=float(confidence * 100),  # En pourcentage
            class_name=class_name,
            processing_time=processing_time
        )
        
        # Mettre en cache le résultat
        prediction_cache[image_hash] = {
            "prediction": result,
            "timestamp": current_time
        }
        
        # Nettoyer le cache si nécessaire
        if len(prediction_cache) > 100:  # Limiter la taille du cache
            oldest_keys = sorted(prediction_cache.keys(), 
                               key=lambda k: prediction_cache[k]["timestamp"])[:10]
            for key in oldest_keys:
                prediction_cache.pop(key, None)
        
        logger.info(f"Prédiction réussie pour {file.filename}: classe {predicted_class} avec {confidence*100:.2f}% de confiance")
        return result
        
    except Exception as e:
        logger.error(f"Erreur lors de la prédiction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction: {str(e)}")

@app.get("/api/health")
async def health_check():
    """
    Vérifie l'état de santé de l'API
    
    Returns:
        dict: Statut de l'API et du modèle
    """
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/info")
async def api_info():
    """
    Fournit des informations sur l'API et le modèle
    
    Returns:
        dict: Informations sur l'API et le modèle
    """
    model_info = {}
    
    if model is not None:
        # Extraire les informations du modèle
        model_info = {
            "input_shape": [dim if dim is not None else "variable" for dim in model.input_shape],
            "output_shape": [dim if dim is not None else "variable" for dim in model.output_shape],
            "layers_count": len(model.layers),
            "classes": len(CLASS_NAMES) if CLASS_NAMES else "unknown"
        }
    
    return {
        "api_version": "1.0.0",
        "model_loaded": model is not None,
        "model_info": model_info,
        "class_names": CLASS_NAMES,
        "max_requests_per_minute": MAX_REQUESTS_PER_MINUTE
    }

# Configuration des templates et des fichiers statiques (si nécessaire)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

if os.path.exists("templates"):
    templates = Jinja2Templates(directory="templates")
    
    @app.get("/ui", response_class=HTMLResponse)
    async def ui(request: Request):
        """Interface utilisateur simple"""
        return templates.TemplateResponse("index.html", {"request": request})

# --- Fonction principale ---
def main():
    """Point d'entrée principal pour l'exécution directe"""
    # Vérifier si les dossiers templates et static existent, sinon les créer
    os.makedirs("static", exist_ok=True)
    os.makedirs("templates", exist_ok=True)
    
    # Créer un fichier index.html minimal si nécessaire
    if not os.path.exists("templates/index.html"):
        with open("templates/index.html", "w") as f:
            f.write("""
<!DOCTYPE html>
<html>
<head>
    <title>Interface de l'API Deep Learning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .container {
            background-color: #f9f9f9;
            border-radius: 5px;
            padding: 20px;
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            display: none;
        }
        .preview {
            max-width: 300px;
            max-height: 300px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Interface de l'API Deep Learning</h1>
    <div class="container">
        <h2>Classification d'image</h2>
        <div class="form-group">
            <label for="image">Sélectionnez une image :</label>
            <input type="file" id="image" accept="image/*">
        </div>
        <button class="btn" id="predict">Prédire</button>
        
        <div class="result" id="result">
            <h3>Résultat :</h3>
            <img id="preview" class="preview">
            <p><strong>Classe prédite :</strong> <span id="prediction"></span></p>
            <p><strong>Confiance :</strong> <span id="confidence"></span>%</p>
            <p><strong>Temps de traitement :</strong> <span id="time"></span> ms</p>
        </div>
    </div>

    <script>
        document.getElementById('predict').addEventListener('click', async () => {
            const fileInput = document.getElementById('image');
            const resultDiv = document.getElementById('result');
            const predictionSpan = document.getElementById('prediction');
            const confidenceSpan = document.getElementById('confidence');
            const timeSpan = document.getElementById('time');
            const preview = document.getElementById('preview');
            
            if (!fileInput.files || fileInput.files.length === 0) {
                alert('Veuillez sélectionner une image');
                return;
            }
            
            const file = fileInput.files[0];
            const formData = new FormData();
            formData.append('file', file);
            
            // Afficher l'aperçu
            preview.src = URL.createObjectURL(file);
            
            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Erreur lors de la prédiction');
                }
                
                const result = await response.json();
                
                predictionSpan.textContent = result.class_name || result.prediction;
                confidenceSpan.textContent = result.confidence.toFixed(2);
                timeSpan.textContent = (result.processing_time * 1000).toFixed(2);
                resultDiv.style.display = 'block';
                
            } catch (error) {
                alert('Erreur: ' + error.message);
            }
        });
    </script>
</body>
</html>
            """)
    
    # Démarrer le serveur
    print(f"Démarrage du serveur sur http://localhost:8000")
    print("Documentation API disponible sur http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()