"""
CONFIGURATION DU CHATBOT PÉDAGOGIQUE
Configuration centralisée pour le backend

⚠️ IMPORTANT: Remplacez VOTRE_CLE_API par votre vraie clé Mistral AI
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis .env
load_dotenv()

class Config:
    """Configuration principale de l'application"""
    
    # ================================
    # CONFIGURATION API MISTRAL AI
    # ================================
    
    # ⚠️ À REMPLACER PAR VOTRE VRAIE CLÉ API
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "VOTRE_CLE_API")
    
    # URL de base de l'API Mistral
    MISTRAL_BASE_URL = "https://api.mistral.ai/v1"
    
    # Modèle par défaut à utiliser
    DEFAULT_MODEL = "mistral-small"
    
    # Paramètres par défaut pour les requêtes
    DEFAULT_TEMPERATURE = 0.5
    DEFAULT_MAX_TOKENS = 500
    
    # ================================
    # CONFIGURATION APPLICATION
    # ================================
    
    # Mode debug (True pour développement, False pour production)
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # Port du serveur Flask
    PORT = int(os.getenv("PORT", 5000))
    
    # Host du serveur
    HOST = os.getenv("HOST", "0.0.0.0")
    
    # ================================
    # CONFIGURATION BASE DE CONNAISSANCES
    # ================================
    
    # Chemin vers le fichier de base de connaissances
    KNOWLEDGE_BASE_PATH = os.getenv("KNOWLEDGE_BASE_PATH", "data/knowledge_base.json")
    
    # Chemin vers les templates de prompts
    PROMPTS_TEMPLATES_PATH = os.getenv("PROMPTS_TEMPLATES_PATH", "data/prompts_templates.json")
    
    # Nombre maximum de résultats pour la recherche de concepts
    MAX_SEARCH_RESULTS = 5
    
    # ================================
    # CONFIGURATION PERFORMANCE
    # ================================
    
    # Taille maximum du cache des réponses
    CACHE_MAX_SIZE = 100
    
    # Délai minimum entre les requêtes API (en secondes)
    MIN_REQUEST_INTERVAL = 0.1
    
    # Timeout pour les requêtes API (en secondes)
    API_TIMEOUT = 30
    
    # Nombre maximum de tentatives en cas d'erreur
    MAX_RETRIES = 3
    
    # ================================
    # CONFIGURATION LOGGING
    # ================================
    
    # Niveau de logging (DEBUG, INFO, WARNING, ERROR)
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Fichier de log
    LOG_FILE = "chatbot.log"
    
    # Format des logs
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # ================================
    # CONFIGURATION SÉCURITÉ
    # ================================
    
    # Clé secrète pour Flask (générez une clé aléatoire en production)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    
    # CORS origins autorisées
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
    
    # ================================
    # CONFIGURATION QUIZ
    # ================================
    
    # Nombre maximum de questions par quiz
    MAX_QUIZ_QUESTIONS = 10
    
    # Nombre par défaut de questions
    DEFAULT_QUIZ_QUESTIONS = 5
    
    # Score minimum pour réussir un quiz (en pourcentage)
    QUIZ_PASSING_SCORE = 70
    
    # ================================
    # CONFIGURATION CONVERSATION
    # ================================
    
    # Taille maximum de l'historique de conversation
    MAX_CONVERSATION_HISTORY = 20
    
    # Nombre de messages de contexte à envoyer à l'API
    CONTEXT_MESSAGES_COUNT = 5
    
    # ================================
    # CONFIGURATION DÉVELOPPEMENT
    # ================================
    
    # Mode de développement avec données de test
    USE_TEST_DATA = os.getenv("USE_TEST_DATA", "False").lower() == "true"
    
    # Simulation des erreurs pour tests
    SIMULATE_API_ERRORS = os.getenv("SIMULATE_API_ERRORS", "False").lower() == "true"
    
    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        """
        Valide la configuration et retourne un rapport
        
        Returns:
            Dictionnaire avec le statut de validation
        """
        report = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        # Vérification de la clé API
        if cls.MISTRAL_API_KEY == "VOTRE_CLE_API" or not cls.MISTRAL_API_KEY:
            report["errors"].append("Clé API Mistral non configurée")
            report["valid"] = False
        
        # Vérification des fichiers
        if not os.path.exists(cls.KNOWLEDGE_BASE_PATH):
            report["warnings"].append(f"Fichier base de connaissances manquant: {cls.KNOWLEDGE_BASE_PATH}")
        
        if not os.path.exists(cls.PROMPTS_TEMPLATES_PATH):
            report["warnings"].append(f"Fichier templates manquant: {cls.PROMPTS_TEMPLATES_PATH}")
        
        # Vérification des valeurs numériques
        if cls.MAX_TOKENS <= 0:
            report["errors"].append("MAX_TOKENS doit être positif")
            report["valid"] = False
        
        if cls.TEMPERATURE < 0 or cls.TEMPERATURE > 1:
            report["warnings"].append("TEMPERATURE devrait être entre 0 et 1")
        
        return report
    
    @classmethod
    def get_mistral_config(cls) -> Dict[str, Any]:
        """
        Retourne la configuration pour le client Mistral
        
        Returns:
            Configuration Mistral
        """
        return {
            "api_key": cls.MISTRAL_API_KEY,
            "base_url": cls.MISTRAL_BASE_URL,
            "default_model": cls.DEFAULT_MODEL,
            "default_temperature": cls.DEFAULT_TEMPERATURE,
            "default_max_tokens": cls.DEFAULT_MAX_TOKENS,
            "timeout": cls.API_TIMEOUT,
            "max_retries": cls.MAX_RETRIES
        }
    
    @classmethod
    def get_flask_config(cls) -> Dict[str, Any]:
        """
        Retourne la configuration pour Flask
        
        Returns:
            Configuration Flask
        """
        return {
            "DEBUG": cls.DEBUG,
            "SECRET_KEY": cls.SECRET_KEY,
            "HOST": cls.HOST,
            "PORT": cls.PORT
        }
    
    @classmethod
    def print_config_summary(cls):
        """Affiche un résumé de la configuration"""
        print("🔧 Configuration du Chatbot Pédagogique")
        print("=" * 50)
        print(f"Mode Debug: {cls.DEBUG}")
        print(f"Port: {cls.PORT}")
        print(f"Modèle Mistral: {cls.DEFAULT_MODEL}")
        print(f"API Key configurée: {'✅' if cls.MISTRAL_API_KEY != 'VOTRE_CLE_API' else '❌'}")
        print(f"Base de connaissances: {cls.KNOWLEDGE_BASE_PATH}")
        print(f"Templates prompts: {cls.PROMPTS_TEMPLATES_PATH}")
        print("=" * 50)


# ==============================
# CONFIGURATION SPÉCIFIQUE ÉTUDIANTS
# ==============================

class StudentConfig:
    """Configuration spécifique aux étudiants pour personnalisation"""
    
    # ================================
    # À PERSONNALISER PAR L'ÉTUDIANT
    # ================================
    
    # Nom du projet (affiché dans les logs et l'interface)
    PROJECT_NAME = "Chatbot Deep Learning - [VOTRE NOM]"
    
    # Thème par défaut de l'interface
    DEFAULT_THEME = "default"  # Options: default, dark, education, tech
    
    # Niveau par défaut pour les nouveaux utilisateurs
    DEFAULT_USER_LEVEL = "beginner"  # Options: beginner, intermediate, advanced
    
    # Fonctionnalités activées (pour personnalisation graduelle)
    FEATURES = {
        "quiz": True,           # Système de quiz
        "progress": True,       # Suivi de progression
        "themes": True,         # Sélection de thèmes
        "export": True,         # Export de conversation
        "suggestions": True,    # Suggestions automatiques
        "analytics": False      # Analytiques avancées (optionnel)
    }
    
    # Configuration du quiz (Choix B)
    QUIZ_CONFIG = {
        "enabled": True,
        "default_count": 5,
        "show_explanations": True,
        "save_results": True,
        "adaptive_difficulty": False  # Difficulté adaptative (avancé)
    }
    
    # Configuration des thèmes (Choix A)
    THEME_CONFIG = {
        "enabled": True,
        "available_themes": ["default", "dark", "education", "tech"],
        "custom_theme_support": True,
        "remember_preference": True
    }
    
    # Configuration de l'optimisation IA (Choix C)
    AI_OPTIMIZATION = {
        "enabled": False,       # À activer pour le Choix C
        "dynamic_prompts": True,
        "context_analysis": True,
        "intent_detection": True,
        "adaptive_responses": True
    }


# ==============================
# UTILITAIRES DE CONFIGURATION
# ==============================

def create_env_file():
    """Crée un fichier .env exemple"""
    env_content = """# Configuration du Chatbot Pédagogique Deep Learning
# Copiez ce fichier en .env et remplacez les valeurs

# ⚠️ OBLIGATOIRE: Votre clé API Mistral AI
MISTRAL_API_KEY=VOTRE_CLE_API_ICI

# Configuration optionnelle
DEBUG=True
PORT=5000
HOST=0.0.0.0

# Chemins personnalisés (optionnel)
KNOWLEDGE_BASE_PATH=data/knowledge_base.json
PROMPTS_TEMPLATES_PATH=data/prompts_templates.json

# Logging
LOG_LEVEL=INFO

# Sécurité (changez en production)
SECRET_KEY=dev-secret-key-change-in-production

# CORS (pour développement local)
CORS_ORIGINS=*

# Mode test
USE_TEST_DATA=False
SIMULATE_API_ERRORS=False
"""
    
    try:
        with open(".env.example", "w", encoding="utf-8") as f:
            f.write(env_content)
        print("✅ Fichier .env.example créé")
        print("   Copiez-le en .env et configurez votre clé API")
    except Exception as e:
        print(f"❌ Erreur création .env.example: {e}")

def setup_directories():
    """Crée les répertoires nécessaires"""
    directories = [
        "data",
        "logs", 
        "tests",
        "docs"
    ]
    
    for dir_name in directories:
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"📁 Répertoire créé/vérifié: {dir_name}")
        except Exception as e:
            print(f"❌ Erreur création répertoire {dir_name}: {e}")

def check_dependencies():
    """Vérifie que les dépendances sont installées"""
    required_packages = [
        "flask",
        "flask-cors", 
        "requests",
        "python-dotenv"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Packages manquants:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n💡 Installez avec: pip install " + " ".join(missing_packages))
        return False
    else:
        print("✅ Toutes les dépendances sont installées")
        return True


# ==============================
# SCRIPT DE VÉRIFICATION
# ==============================

if __name__ == "__main__":
    print("🔧 Vérification de la configuration...")
    
    # Validation de la configuration
    validation = Config.validate_config()
    
    if validation["valid"]:
        print("✅ Configuration valide")
    else:
        print("❌ Configuration invalide:")
        for error in validation["errors"]:
            print(f"   - {error}")
    
    if validation["warnings"]:
        print("⚠️ Avertissements:")
        for warning in validation["warnings"]:
            print(f"   - {warning}")
    
    # Affichage du résumé
    Config.print_config_summary()
    
    # Vérification des dépendances
    print("\n📦 Vérification des dépendances...")
    check_dependencies()
    
    # Création des fichiers/répertoires si nécessaire
    print("\n📁 Configuration de l'environnement...")
    setup_directories()
    
    if not os.path.exists(".env"):
        print("\n📝 Création du fichier .env exemple...")
        create_env_file()
    
    print("\n🎯 Configuration terminée !")
    
    if Config.MISTRAL_API_KEY == "VOTRE_CLE_API":
        print("\n⚠️  N'OUBLIEZ PAS:")
        print("   1. Créer votre compte sur https://console.mistral.ai/")
        print("   2. Générer une clé API")
        print("   3. Remplacer VOTRE_CLE_API dans ce fichier")
        print("   4. OU créer un fichier .env avec MISTRAL_API_KEY=votre_clé")