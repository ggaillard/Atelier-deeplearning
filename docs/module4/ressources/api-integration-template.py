"""
Template d'intégration API Mistral pour le chatbot pédagogique
Projet BTS SIO - Séance de 4h
"""

from flask import Flask, request, jsonify
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import json

# Configuration de l'application Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Pour gérer les accents correctement

# ==========================================
# CONFIGURATION DE L'API MISTRAL
# ==========================================

# TODO: Remplacez par votre clé API
MISTRAL_API_KEY = "votre_clé_api_ici"

# Initialisation du client Mistral
client = MistralClient(api_key=MISTRAL_API_KEY)

# Configuration du modèle
MODEL = "mistral-tiny"  # Options: mistral-tiny, mistral-small, mistral-medium

# ==========================================
# FONCTIONS DE BASE DE CONNAISSANCES
# ==========================================

def load_knowledge_base():
    """Charge la base de connaissances depuis le fichier JSON"""
    try:
        # TODO: Changez le chemin vers votre base de connaissances
        with open('knowledge/knowledge_base.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement de la base de connaissances: {e}")
        # Retourner une base vide en cas d'erreur
        return {"concepts": []}

def find_relevant_concepts(question, knowledge_base, max_concepts=2):
    """
    Recherche les concepts pertinents dans la base de connaissances
    en fonction de la question posée
    """
    # Version simple: recherche par mots-clés
    relevant_concepts = []
    
    # Extraction des mots-clés de la question
    keywords = question.lower().split()
    
    # Parcours des concepts
    for concept in knowledge_base.get("concepts", []):
        # Calcul d'un score simple de pertinence
        score = sum(1 for keyword in keywords if keyword in concept["title"].lower())
        
        if score > 0:
            relevant_concepts.append({
                "concept": concept,
                "score": score
            })
    
    # Tri par score de pertinence
    relevant_concepts.sort(key=lambda x: x["score"], reverse=True)
    
    # Retourne les concepts les plus pertinents
    return [item["concept"] for item in relevant_concepts[:max_concepts]]

# ==========================================
# FONCTIONS D'ENRICHISSEMENT DES PROMPTS
# ==========================================

def create_system_prompt(user_level="beginner"):
    """
    Crée le prompt système avec les instructions pour l'assistant
    """
    # TODO: Personnalisez ce prompt système selon votre option (SISR/SLAM)
    if os.getenv("CHATBOT_OPTION") == "sisr":
        # Prompt pour l'option SISR
        return f"""
        Vous êtes un assistant pédagogique spécialisé en réseau, système et Deep Learning.
        Votre objectif est d'aider les techniciens à diagnostiquer et résoudre des problèmes
        tout en leur expliquant les concepts de Deep Learning.
        
        Niveau de l'utilisateur: {user_level}
        
        Directives:
        1. Utilisez un langage clair et adapté au niveau technique de l'utilisateur
        2. Pour les questions de diagnostic, procédez par étapes systématiques
        3. Illustrez les concepts avec des exemples concrets du domaine réseau/système
        4. Soyez concis mais précis dans vos explications
        """
    else:
        # Prompt pour l'option SLAM
        return f"""
        Vous êtes un assistant pédagogique spécialisé en développement logiciel et Deep Learning.
        Votre objectif est d'aider les développeurs à comprendre des concepts de programmation
        tout en leur expliquant les concepts de Deep Learning.
        
        Niveau de l'utilisateur: {user_level}
        
        Directives:
        1. Utilisez un langage clair et adapté au niveau technique de l'utilisateur
        2. Incluez des exemples de code quand c'est pertinent
        3. Expliquez les concepts en faisant des parallèles avec le développement logiciel
        4. Soyez concis mais précis dans vos explications
        """

def enrich_prompt_with_knowledge(question, relevant_concepts, user_level="beginner"):
    """
    Enrichit la question utilisateur avec des informations de la base de connaissances
    """
    if not relevant_concepts:
        return question
    
    enriched_prompt = f"Question utilisateur: {question}\n\n"
    enriched_prompt += "Informations contextuelles pour vous aider à répondre:\n\n"
    
    for concept in relevant_concepts:
        # Ajouter le titre et la description générale
        enriched_prompt += f"Concept: {concept['title']}\n"
        if "description" in concept:
            enriched_prompt += f"Description: {concept['description']}\n"
        
        # Ajouter l'explication adaptée au niveau de l'utilisateur
        if "levels" in concept and user_level in concept["levels"]:
            enriched_prompt += f"Explication ({user_level}): {concept['levels'][user_level]}\n"
        
        # Ajouter un exemple pertinent
        if "examples" in concept and concept["examples"]:
            example = concept["examples"][0]
            if isinstance(example, dict) and "description" in example:
                enriched_prompt += f"Exemple: {example['description']}\n"
            elif isinstance(example, str):
                enriched_prompt += f"Exemple: {example}\n"
        
        enriched_prompt += "\n"
    
    enriched_prompt += f"Réponds maintenant à la question de l'utilisateur en te basant sur ces informations, adapté au niveau {user_level}."
    
    return enriched_prompt

# ==========================================
# ROUTES DE L'API
# ==========================================

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Point d'entrée principal pour les requêtes de chat
    Attend un JSON avec:
    - message: le message utilisateur
    - history: l'historique de conversation (optionnel)
    - user_level: le niveau de l'utilisateur (optionnel)
    """
    try:
        data = request.json
        
        if not data or 'message' not in data:
            return jsonify({"error": "Le message est requis"}), 400
        
        user_message = data['message']
        history = data.get('history', [])
        user_level = data.get('user_level', 'beginner')
        
        # Chargement de la base de connaissances
        knowledge_base = load_knowledge_base()
        
        # Recherche des concepts pertinents
        relevant_concepts = find_relevant_concepts(user_message, knowledge_base)
        
        # Construction des messages pour l'API
        messages = []
        
        # Ajout du prompt système
        system_prompt = create_system_prompt(user_level)
        messages.append(ChatMessage(role="system", content=system_prompt))
        
        # Ajout de l'historique
        for msg in history:
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            if role and content:
                messages.append(ChatMessage(role=role, content=content))
        
        # Ajout du message utilisateur enrichi
        enriched_prompt = enrich_prompt_with_knowledge(user_message, relevant_concepts, user_level)
        messages.append(ChatMessage(role="user", content=enriched_prompt))
        
        # Appel à l'API Mistral
        chat_response = client.chat(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extraction de la réponse
        response_content = chat_response.choices[0].message.content
        
        return jsonify({
            "response": response_content,
            "enriched": bool(relevant_concepts)  # Indique si la réponse a été enrichie
        })
        
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API: {e}")
        return jsonify({
            "error": "Une erreur est survenue lors du traitement de votre demande",
            "details": str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Route simple pour vérifier que l'API fonctionne
    """
    return jsonify({"status": "OK", "message": "API opérationnelle"})

# ==========================================
# ROUTE SPÉCIFIQUE SISR: DIAGNOSTIC
# ==========================================

@app.route('/api/diagnostic', methods=['POST'])
def diagnostic():
    """
    Route spécifique pour le diagnostic (option SISR)
    """
    # TODO: Implémentez la logique de diagnostic pour SISR
    if os.getenv("CHATBOT_OPTION") != "sisr":
        return jsonify({"error": "Cette fonctionnalité est disponible uniquement pour l'option SISR"}), 400
    
    try:
        data = request.json
        problem_type = data.get('problem_type')
        current_step = data.get('current_step', 'start')
        
        # Exemple simple d'arbre de décision pour WiFi
        if problem_type == "wifi":
            if current_step == "start":
                return jsonify({
                    "question": "Est-ce que le voyant WiFi est allumé sur votre appareil?",
                    "options": ["Oui", "Non", "Je ne sais pas"],
                    "next_step": "wifi_light"
                })
            elif current_step == "wifi_light":
                answer = data.get('answer')
                if answer == "Non":
                    return jsonify({
                        "solution": "Activez le WiFi en utilisant le bouton ou la combinaison de touches (souvent Fn+F2/F3).",
                        "finished": True
                    })
                else:
                    return jsonify({
                        "question": "Voyez-vous le nom de votre réseau WiFi dans la liste des réseaux disponibles?",
                        "options": ["Oui", "Non"],
                        "next_step": "wifi_network_visible"
                    })
        
        # Réponse par défaut
        return jsonify({
            "error": "Diagnostic non implémenté pour ce type de problème",
            "finished": True
        })
        
    except Exception as e:
        return jsonify({
            "error": "Erreur lors du diagnostic",
            "details": str(e)
        }), 500

# ==========================================
# ROUTE SPÉCIFIQUE SLAM: AUTHENTIFICATION
# ==========================================

@app.route('/api/auth/login', methods=['POST'])
def login():
    """
    Route spécifique pour l'authentification (option SLAM)
    """
    # TODO: Implémentez la logique d'authentification pour SLAM
    if os.getenv("CHATBOT_OPTION") != "slam":
        return jsonify({"error": "Cette fonctionnalité est disponible uniquement pour l'option SLAM"}), 400
    
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Authentification simplifiée pour la démonstration
        # En production, utilisez une base de données et hashage des mots de passe
        valid_users = {
            "etudiant": "bts2025",
            "admin": "admin2025"
        }
        
        if username in valid_users and valid_users[username] == password:
            return jsonify({
                "success": True,
                "username": username,
                "message": "Connexion réussie"
            })
        else:
            return jsonify({
                "success": False,
                "message": "Nom d'utilisateur ou mot de passe incorrect"
            }), 401
            
    except Exception as e:
        return jsonify({
            "error": "Erreur lors de l'authentification",
            "details": str(e)
        }), 500

# ==========================================
# LANCEMENT DE L'APPLICATION
# ==========================================

if __name__ == '__main__':
    # Détermination de l'option (SISR ou SLAM)
    option = input("Quelle option ? (sisr/slam): ").lower()
    if option not in ["sisr", "slam"]:
        print("Option non reconnue, utilisation de l'option par défaut: sisr")
        option = "sisr"
    
    # Configuration de l'environnement
    os.environ["CHATBOT_OPTION"] = option
    
    print(f"Démarrage du serveur en mode {option.upper()}...")
    
    # Lancement du serveur sur le port 5001 (pour éviter les conflits avec d'autres services)
    app.run(debug=True, port=5001)