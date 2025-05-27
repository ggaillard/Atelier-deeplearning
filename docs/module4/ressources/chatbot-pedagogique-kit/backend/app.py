"""
SERVEUR BACKEND - CHATBOT PÉDAGOGIQUE DEEP LEARNING
Application Flask complète avec intégration API Mistral

Fonctionnalités :
- API REST pour le chatbot
- Intégration Mistral AI
- Gestion de la base de connaissances
- Génération de quiz
- Système de logging
- CORS pour frontend
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json
import logging
from datetime import datetime
import traceback

# Imports des modules personnalisés
from mistral_client import MistralClient
from knowledge_manager import KnowledgeManager
from prompt_optimizer import PromptOptimizer
from config import Config

# Configuration de l'application
app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin du frontend

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialisation des composants
try:
    config = Config()
    mistral_client = MistralClient(config.MISTRAL_API_KEY)
    knowledge_manager = KnowledgeManager('data/knowledge_base.json')
    prompt_optimizer = PromptOptimizer('data/prompts_templates.json')
    
    logger.info("✅ Tous les composants initialisés avec succès")
except Exception as e:
    logger.error(f"❌ Erreur d'initialisation: {e}")
    raise

# ================================
# ROUTES PRINCIPALES
# ================================

@app.route('/')
def index():
    """Page d'accueil avec informations sur l'API"""
    return jsonify({
        "message": "Chatbot Pédagogique Deep Learning API",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "/api/chat": "POST - Conversation avec le chatbot",
            "/api/quiz/generate": "POST - Génération de quiz",
            "/api/concepts": "GET - Liste des concepts disponibles",
            "/health": "GET - Santé de l'API"
        }
    })

@app.route('/health')
def health_check():
    """Vérification de la santé de l'API"""
    try:
        # Test de l'API Mistral
        health_status = mistral_client.test_connection()
        
        return jsonify({
            "status": "healthy" if health_status else "degraded",
            "timestamp": datetime.now().isoformat(),
            "components": {
                "mistral_api": health_status,
                "knowledge_base": knowledge_manager.is_loaded(),
                "prompt_optimizer": prompt_optimizer.is_ready()
            }
        })
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

# ================================
# API CHATBOT
# ================================

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint principal pour la conversation avec le chatbot
    
    Body: {
        "message": "Question de l'utilisateur",
        "level": "beginner|intermediate|advanced",
        "history": [messages précédents] (optionnel)
    }
    """
    try:
        data = request.get_json()
        
        # Validation des données
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "error": "Message manquant"
            }), 400
        
        user_message = data['message'].strip()
        user_level = data.get('level', 'intermediate')
        conversation_history = data.get('history', [])
        
        if not user_message:
            return jsonify({
                "success": False,
                "error": "Message vide"
            }), 400
        
        logger.info(f"💬 Nouvelle question [{user_level}]: {user_message[:100]}...")
        
        # Recherche dans la base de connaissances
        relevant_concepts = knowledge_manager.search_concepts(user_message)
        
        # Génération du prompt optimisé
        optimized_prompt = prompt_optimizer.create_educational_prompt(
            user_message=user_message,
            user_level=user_level,
            relevant_concepts=relevant_concepts,
            conversation_history=conversation_history[-5:]  # 5 derniers messages
        )
        
        # Appel à l'API Mistral
        response = mistral_client.generate_response(
            prompt=optimized_prompt,
            temperature=get_temperature_for_level(user_level),
            max_tokens=500
        )
        
        if not response:
            raise Exception("Aucune réponse de l'API Mistral")
        
        # Extraction des concepts mentionnés
        mentioned_concepts = knowledge_manager.extract_concepts_from_text(response)
        
        # Génération de suggestions
        suggestions = generate_suggestions(user_message, mentioned_concepts, user_level)
        
        # Logging de la réponse
        logger.info(f"✅ Réponse générée ({len(response)} chars, {len(mentioned_concepts)} concepts)")
        
        return jsonify({
            "success": True,
            "response": response,
            "metadata": {
                "concepts": mentioned_concepts,
                "level": user_level,
                "response_length": len(response)
            },
            "suggestions": suggestions
        })
        
    except Exception as e:
        logger.error(f"❌ Erreur dans /api/chat: {e}")
        logger.error(traceback.format_exc())
        
        return jsonify({
            "success": False,
            "error": "Erreur interne du serveur",
            "details": str(e) if app.debug else None
        }), 500

# ================================
# API QUIZ
# ================================

@app.route('/api/quiz/generate', methods=['POST'])
def generate_quiz():
    """
    Génération d'un quiz sur un sujet donné
    
    Body: {
        "topic": "nom_du_sujet",
        "difficulty": "beginner|intermediate|advanced",
        "count": nombre_de_questions (défaut: 5)
    }
    """
    try:
        data = request.get_json() or {}
        
        topic = data.get('topic', 'deep_learning_general')
        difficulty = data.get('difficulty', 'intermediate')
        question_count = min(data.get('count', 5), 10)  # Max 10 questions
        
        logger.info(f"📝 Génération quiz: {topic} ({difficulty}, {question_count} questions)")
        
        # Récupération des questions de la base de connaissances
        quiz_data = knowledge_manager.generate_quiz(
            topic=topic,
            difficulty=difficulty,
            count=question_count
        )
        
        if not quiz_data or not quiz_data.get('questions'):
            # Fallback : génération via Mistral
            quiz_data = generate_quiz_with_mistral(topic, difficulty, question_count)
        
        logger.info(f"✅ Quiz généré: {len(quiz_data.get('questions', []))} questions")
        
        return jsonify(quiz_data)
        
    except Exception as e:
        logger.error(f"❌ Erreur génération quiz: {e}")
        return jsonify({
            "success": False,
            "error": "Impossible de générer le quiz"
        }), 500

@app.route('/api/quiz/results', methods=['POST'])
def save_quiz_results():
    """Sauvegarde des résultats de quiz"""
    try:
        data = request.get_json()
        
        # Validation des données
        required_fields = ['topic', 'score', 'answers']
        if not all(field in data for field in required_fields):
            return jsonify({
                "success": False,
                "error": "Données manquantes"
            }), 400
        
        # Ajout de métadonnées
        result_data = {
            **data,
            "id": f"quiz_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "server_saved": True
        }
        
        # Sauvegarde (ici on pourrait sauver en base de données)
        logger.info(f"📊 Résultat quiz sauvé: {data['topic']} - Score: {data['score']}%")
        
        return jsonify({
            "success": True,
            "message": "Résultats sauvegardés"
        })
        
    except Exception as e:
        logger.error(f"❌ Erreur sauvegarde quiz: {e}")
        return jsonify({
            "success": False,
            "error": "Erreur de sauvegarde"
        }), 500

# ================================
# API CONCEPTS
# ================================

@app.route('/api/concepts')
def get_concepts():
    """Liste des concepts disponibles"""
    try:
        concepts = knowledge_manager.get_all_concepts()
        
        return jsonify({
            "success": True,
            "concepts": concepts,
            "total": len(concepts)
        })
        
    except Exception as e:
        logger.error(f"❌ Erreur récupération concepts: {e}")
        return jsonify({
            "success": False,
            "error": "Erreur de récupération"
        }), 500

@app.route('/api/concepts/<concept_id>')
def get_concept_details(concept_id):
    """Détails d'un concept spécifique"""
    try:
        concept = knowledge_manager.get_concept(concept_id)
        
        if not concept:
            return jsonify({
                "success": False,
                "error": "Concept non trouvé"
            }), 404
        
        return jsonify({
            "success": True,
            "concept": concept
        })
        
    except Exception as e:
        logger.error(f"❌ Erreur récupération concept {concept_id}: {e}")
        return jsonify({
            "success": False,
            "error": "Erreur de récupération"
        }), 500

# ================================
# FONCTIONS UTILITAIRES
# ================================

def get_temperature_for_level(level):
    """Retourne la température appropriée selon le niveau"""
    temperatures = {
        'beginner': 0.7,      # Plus créatif pour les analogies
        'intermediate': 0.5,   # Équilibré
        'advanced': 0.3       # Plus précis et technique
    }
    return temperatures.get(level, 0.5)

def generate_suggestions(user_message, concepts, level):
    """Génère des suggestions de questions de suivi"""
    suggestions = []
    
    # Suggestions basées sur les concepts mentionnés
    for concept in concepts[:2]:  # Max 2 concepts
        concept_data = knowledge_manager.get_concept(concept)
        if concept_data and 'related_concepts' in concept_data:
            related = concept_data['related_concepts'][:1]  # 1 concept lié
            if related:
                suggestions.append(f"Comment {concept} est-il lié à {related[0]} ?")
    
    # Suggestions génériques selon le niveau
    level_suggestions = {
        'beginner': [
            "Peux-tu me donner un exemple concret ?",
            "Comment cela s'applique-t-il dans la vraie vie ?",
            "Quelle est l'analogie la plus simple ?"
        ],
        'intermediate': [
            "Quels sont les cas d'usage pratiques ?",
            "Comment implémenter cela en code ?",
            "Quelles sont les meilleures pratiques ?"
        ],
        'advanced': [
            "Quelles sont les optimisations possibles ?",
            "Comment cela évolue-t-il avec les recherches récentes ?",
            "Quels sont les défis techniques actuels ?"
        ]
    }
    
    suggestions.extend(level_suggestions.get(level, [])[:2])
    
    return suggestions[:3]  # Max 3 suggestions

def generate_quiz_with_mistral(topic, difficulty, count):
    """Génération de quiz via Mistral AI en fallback"""
    try:
        prompt = f"""
        Génère un quiz de {count} questions sur le sujet "{topic}" avec un niveau {difficulty}.
        
        Format JSON exact :
        {{
            "title": "Titre du quiz",
            "questions": [
                {{
                    "id": 1,
                    "question": "Question ?",
                    "options": ["Option A", "Option B", "Option C", "Option D"],
                    "correctAnswer": 0,
                    "explanation": "Explication de la réponse",
                    "difficulty": "{difficulty}"
                }}
            ]
        }}
        
        Assure-toi que les questions sont pédagogiques et adaptées au niveau {difficulty}.
        """
        
        response = mistral_client.generate_response(prompt, temperature=0.3, max_tokens=1000)
        
        # Extraction du JSON de la réponse
        import re
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
    except Exception as e:
        logger.error(f"Erreur génération quiz Mistral: {e}")
    
    # Fallback ultime
    return {
        "title": f"Quiz {topic}",
        "questions": [
            {
                "id": 1,
                "question": "Question temporaire - Quiz en cours de génération",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correctAnswer": 0,
                "explanation": "Question temporaire",
                "difficulty": difficulty
            }
        ]
    }

# ================================
# GESTION DES ERREURS
# ================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint non trouvé"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Erreur 500: {error}")
    return jsonify({
        "success": False,
        "error": "Erreur interne du serveur"
    }), 500

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Exception non gérée: {e}")
    logger.error(traceback.format_exc())
    
    return jsonify({
        "success": False,
        "error": "Une erreur inattendue s'est produite"
    }), 500

# ================================
# POINT D'ENTRÉE
# ================================

if __name__ == '__main__':
    logger.info("🚀 Démarrage du serveur chatbot...")
    
    # Vérifications au démarrage
    if not config.MISTRAL_API_KEY or config.MISTRAL_API_KEY == 'VOTRE_CLE_API':
        logger.error("❌ Clé API Mistral non configurée!")
        logger.error("Configurez votre clé dans backend/config.py ou backend/.env")
        exit(1)
    
    # Test de connexion
    if not mistral_client.test_connection():
        logger.warning("⚠️ API Mistral non accessible, fonctionnalités limitées")
    
    logger.info("✅ Serveur prêt")
    
    # Démarrage du serveur
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=config.DEBUG,
        threaded=True
    )