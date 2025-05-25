from flask import Flask, render_template, request, jsonify
import json
import os
from dotenv import load_dotenv
import requests

# Configuration
load_dotenv()
app = Flask(__name__)

# Configuration API Mistral
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "votre_clé_ici")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# Chargement de la base de connaissances
def load_knowledge_base():
    """Charge la base de connaissances depuis le fichier JSON"""
    try:
        with open('knowledge/base_structure.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"concepts": []}

# Base de connaissances globale
KNOWLEDGE_BASE = load_knowledge_base()

def enrich_prompt(user_question, knowledge_base):
    """
    Enrichit le prompt avec des informations de la base de connaissances
    TODO: À compléter par les étudiants
    """
    # Recherche simple par mots-clés (à améliorer)
    relevant_info = ""
    question_lower = user_question.lower()
    
    for concept in knowledge_base.get("concepts", []):
        if any(keyword in question_lower for keyword in concept.get("keywords", [])):
            relevant_info += f"\nConcept: {concept.get('title', '')}\n"
            relevant_info += f"Définition: {concept.get('definition', '')}\n"
            if concept.get("examples"):
                relevant_info += f"Exemple: {concept['examples'][0]}\n"
    
    return relevant_info

def call_mistral_api(messages):
    """
    Appelle l'API Mistral AI
    TODO: Gestion d'erreurs à améliorer par les étudiants
    """
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistral-tiny",
        "messages": messages,
        "max_tokens": 300,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erreur API: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Point d'entrée principal du chatbot
    TODO: À compléter par les étudiants
    """
    data = request.json
    user_message = data.get('message', '')
    conversation_history = data.get('history', [])
    
    # Enrichissement du prompt
    context = enrich_prompt(user_message, KNOWLEDGE_BASE)
    
    # Construction du prompt système
    system_prompt = f"""Tu es un assistant pédagogique spécialisé en Deep Learning pour des étudiants de BTS SIO.

Contexte pertinent de notre base de connaissances:
{context}

Instructions:
- Réponds de manière claire et pédagogique
- Utilise des exemples concrets
- Adapte ton niveau à un étudiant de BTS
- Si tu ne sais pas, dis-le clairement
- Sois concis (maximum 200 mots)"""

    # Construction des messages
    messages = [{"role": "system", "content": system_prompt}]
    
    # Ajout de l'historique (limité pour éviter les tokens excessifs)
    for msg in conversation_history[-5:]:  # Garde seulement les 5 derniers échanges
        messages.append(msg)
    
    messages.append({"role": "user", "content": user_message})
    
    # Appel API
    response = call_mistral_api(messages)
    
    return jsonify({
        "response": response,
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)