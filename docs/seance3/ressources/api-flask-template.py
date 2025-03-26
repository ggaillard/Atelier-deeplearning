"""
Template d'API Flask pour exposer un modèle de Deep Learning
Version: 1.0
Pour:  Séance 3

Fonctionnalités incluses:
- Structure de base d'une API Flask
- Chargement d'un modèle TensorFlow
- Prétraitement des images
- Endpoint de prédiction
- Documentation automatique des endpoints
- Gestion des erreurs
- Rate limiting simple
- Système de cache basique
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
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

# Configuration de l'application
app = Flask(__name__)
CORS(app)  # Permettre les requêtes cross-origin

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

# --- Décorateurs et utilitaires ---
def rate_limit(f):
    """
    Décorateur pour limiter le nombre de requêtes par IP
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.remote_addr
        
        # Initialiser ou réinitialiser le compteur si nécessaire
        now = time.time()
        if ip not in request_counts or now - request_counts[ip]['last_reset'] > 60:
            request_counts[ip] = {'count': 0, 'last_reset': now}
        
        # Vérifier la limite
        if request_counts[ip]['count'] >= MAX_REQUESTS_PER_MINUTE:
            return jsonify({'error': 'Trop de requêtes, veuillez réessayer plus tard'}), 429
        
        # Incrémenter le compteur
        request_counts[ip]['count'] += 1
        
        # Exécuter la fonction
        return f(*args, **kwargs)
    return decorated_function

def get_image_hash(image_data):
    """
    Génère un hash unique pour une image donnée
    """
    return hashlib.md5(image_data).hexdigest()

# --- Fonctions de prétraitement ---
def preprocess_image(image, target_size=(224, 224