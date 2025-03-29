"""
Prototype de chatbot pédagogique sur le Deep Learning utilisant l'API Mistral AI
Pour les étudiants BTS SIO 

Ce script crée un chatbot simple avec interface web via Flask
qui répond aux questions sur le Deep Learning.
"""

import os
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import uuid
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import json
import time
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'application

app = FastAPI(
    title="Chatbot Deep Learning",
    description="Un chatbot pédagogique sur le Deep Learning utilisant l'API Mistral AI",
    version="1.0.0"
)

# Ajout du middleware pour les sessions
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "deep_learning_chatbot_secret"))

# Ajout du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration des templates
templates = Jinja2Templates(directory="templates")

# Configuration de l'API Mistral
mistral_api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=mistral_api_key)
model = "mistral-tiny"  # Modèle économique et rapide, suffisant pour notre prototype

# Chargement de la base de connaissances simplifiée
def load_knowledge_base():
    try:
        with open('knowledge_base.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        # Base de connaissances minimale si le fichier n'existe pas
        return {
            "concepts": [
                {
                    "name": "réseau de neurones",
                    "definition": "Un modèle informatique inspiré du cerveau humain, composé de neurones artificiels connectés qui traitent l'information."
                },
                {
                    "name": "deep learning",
                    "definition": "Sous-domaine du machine learning utilisant des réseaux de neurones profonds (avec plusieurs couches) pour apprendre à partir de données."
                },
                {
                    "name": "CNN",
                    "definition": "Réseau de neurones convolutif, particulièrement efficace pour traiter des images grâce à des opérations de convolution."
                }
            ]
        }

knowledge_base = load_knowledge_base()

# Dictionnaire pour stocker les conversations (dans un vrai projet, utilisez une base de données)
conversations = {}

# Cache simple pour les réponses fréquentes
response_cache = {}

def create_system_prompt():
    """Crée un prompt système avec instructions et base de connaissances intégrée"""
    
    # Extraction des définitions pour les inclure dans le prompt
    definitions = ""
    for concept in knowledge_base["concepts"]:
        definitions += f"- {concept['name']}: {concept['definition']}\n"
    
    # Construction du prompt système complet
    system_prompt = f"""
    Tu es un assistant pédagogique spécialisé dans le Deep Learning pour des étudiants de BTS SIO SLAM.
    Ton rôle est d'expliquer les concepts complexes de manière simple et accessible.
    
    Directives:
    1. Utilise un langage clair et simple, évite le jargon technique quand c'est possible
    2. Propose des exemples concrets liés au développement logiciel
    3. N'utilise pas de formules mathématiques complexes
    4. Adapte tes explications pour des étudiants de niveau BTS
    5. Si tu ne connais pas la réponse, dis-le honnêtement
    
    Base de connaissances à utiliser en priorité:
    {definitions}
    
    Format de réponse recommandé:
    - Commencer par une définition simple et accessible
    - Expliquer le concept en termes simples
    - Donner un exemple concret d'application
    - Si pertinent, mentionner les frameworks utilisés (TensorFlow, Keras, etc.)
    """
    
    return system_prompt

# Routes de l'application
@app.route('/')
def home():
    """Page d'accueil avec l'interface du chatbot"""
    
    # Création d'un ID de session si inexistant
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint API pour les interactions avec le chatbot"""
    
    # Récupération des données de la requête
    data = request.json
    user_message = data.get('message', '')
    session_id = session.get('session_id', str(uuid.uuid4()))
    
    # Vérification des paramètres
    if not user_message:
        return jsonify({"error": "Le message ne peut pas être vide"}), 400
    
    # Vérification de la présence dans le cache
    cache_key = f"{session_id}:{user_message.lower().strip()}"
    if cache_key in response_cache:
        return jsonify({
            "reply": response_cache[cache_key],
            "source": "cache"
        })
    
    # Initialisation ou récupération de l'historique de conversation
    if session_id not in conversations:
        conversations[session_id] = [
            ChatMessage(role="system", content=create_system_prompt())
        ]
    
    # Ajout du message utilisateur à l'historique
    conversation_history = conversations[session_id]
    conversation_history.append(ChatMessage(role="user", content=user_message))
    
    # Limitation de la taille de l'historique pour économiser les tokens
    if len(conversation_history) > 10:  # Garder uniquement les 10 derniers messages
        # Toujours conserver le message système initial
        conversation_history = [conversation_history[0]] + conversation_history[-9:]
    
    try:
        # Appel à l'API Mistral
        start_time = time.time()
        response = client.chat(
            model=model,
            messages=conversation_history,
            temperature=0.7,  # Un peu de créativité mais pas trop
            max_tokens=800    # Limiter la longueur des réponses
        )
        api_time = time.time() - start_time
        
        # Extraction de la réponse
        ai_message = response.choices[0].message.content
        
        # Ajout de la réponse à l'historique
        conversation_history.append(ChatMessage(role="assistant", content=ai_message))
        
        # Mise en cache de la réponse
        response_cache[cache_key] = ai_message
        
        # Si le cache devient trop grand, supprimer les entrées les plus anciennes
        if len(response_cache) > 100:
            keys = list(response_cache.keys())
            for old_key in keys[:10]:  # Supprimer les 10 plus anciennes entrées
                response_cache.pop(old_key, None)
        
        # Mise à jour de l'historique dans le dictionnaire
        conversations[session_id] = conversation_history
        
        return jsonify({
            "reply": ai_message,
            "api_time": f"{api_time:.2f}s"
        })
    
    except Exception as e:
        # Gestion des erreurs d'API
        error_message = str(e)
        print(f"Erreur API Mistral: {error_message}")
        
        # Message d'erreur adapté à l'utilisateur
        user_friendly_message = "Désolé, je rencontre un problème technique. Veuillez réessayer dans quelques instants."
        
        return jsonify({
            "error": error_message,
            "reply": user_friendly_message
        }), 500

@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Réinitialise la conversation avec le chatbot"""
    
    session_id = session.get('session_id')
    if session_id and session_id in conversations:
        # Garde uniquement le message système initial
        system_message = conversations[session_id][0]
        conversations[session_id] = [system_message]
    
    return jsonify({"status": "success", "message": "Conversation réinitialisée"})

@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Renvoie la liste des sujets disponibles dans la base de connaissances"""
    
    topics = [concept['name'] for concept in knowledge_base['concepts']]
    return jsonify({"topics": topics})

# Configuration des templates et des fichiers statiques
@app.route('/templates/<path:path>')
def send_template(path):
    return render_template(path)

if __name__ == '__main__':
    # Création du dossier templates s'il n'existe pas
    os.makedirs('templates', exist_ok=True)
    
    # Création d'un template HTML minimal s'il n'existe pas
    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatBot Deep Learning</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        #chat-container {
            height: 500px;
            border: 1px solid #ddd;
            padding: 15px;
            overflow-y: auto;
            margin-bottom: 15px;
            border-radius: 8px;
            background-color: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .message {
            margin-bottom: 15px;
            padding: 10px 15px;
            border-radius: 18px;
            max-width: 80%;
            line-height: 1.4;
        }
        .user-message {
            background-color: #3498db;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 0;
            text-align: right;
        }
        .bot-message {
            background-color: #f1f1f1;
            margin-right: auto;
            border-bottom-left-radius: 0;
            color: #333;
        }
        #message-form {
            display: flex;
            margin-bottom: 15px;
        }
        #user-input {
            flex: 1;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px 0 0 4px;
            font-size: 16px;
        }
        #send-button {
            padding: 12px 20px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 0 4px 4px 0;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        #send-button:hover {
            background-color: #2980b9;
        }
        #loading {
            display: none;
            text-align: center;
            margin: 10px 0;
            color: #666;
        }
        .loader {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(0,0,0,.1);
            border-radius: 50%;
            border-top-color: #3498db;
            animation: spin 1s ease-in-out infinite;
            margin-right: 10px;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        .controls {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        #reset-button {
            padding: 8px 15px;
            background-color: #e74c3c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        #reset-button:hover {
            background-color: #c0392b;
        }
        #topics-dropdown {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .code-block {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 4px;
            font-family: monospace;
            overflow-x: auto;
            margin: 10px 0;
        }
        .api-time {
            font-size: 12px;
            color: #999;
            text-align: right;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>Assistant Deep Learning BTS SIO</h1>
    
    <div class="controls">
        <select id="topics-dropdown">
            <option value="">Sélectionnez un sujet...</option>
            <!-- Topics will be loaded dynamically -->
        </select>
        <button id="reset-button">Nouvelle conversation</button>
    </div>
    
    <div id="chat-container"></div>
    
    <div id="loading">
        <div class="loader"></div>
        <span>L'assistant réfléchit...</span>
    </div>
    
    <form id="message-form">
        <input type="text" id="user-input" placeholder="Posez votre question sur le Deep Learning..." required>
        <button type="submit" id="send-button">Envoyer</button>
    </form>
    
    <script>
        // DOM Elements
        const chatContainer = document.getElementById('chat-container');
        const messageForm = document.getElementById('message-form');
        const userInput = document.getElementById('user-input');
        const loading = document.getElementById('loading');
        const resetButton = document.getElementById('reset-button');
        const topicsDropdown = document.getElementById('topics-dropdown');
        
        // Add welcome message
        addBotMessage("👋 Bonjour ! Je suis votre assistant spécialisé en Deep Learning pour BTS SIO SLAM. Comment puis-je vous aider aujourd'hui ?");
        
        // Load topics
        fetch('/api/topics')
            .then(response => response.json())
            .then(data => {
                data.topics.forEach(topic => {
                    const option = document.createElement('option');
                    option.value = topic;
                    option.textContent = topic;
                    topicsDropdown.appendChild(option);
                });
            });
        
        // Topic selection
        topicsDropdown.addEventListener('change', function() {
            const selectedTopic = this.value;
            if (selectedTopic) {
                userInput.value = `Qu'est-ce que ${selectedTopic} ?`;
                messageForm.dispatchEvent(new Event('submit'));
            }
        });
        
        // Send message
        messageForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const message = userInput.value.trim();
            if (!message) return;
            
            // Display user message
            addUserMessage(message);
            userInput.value = '';
            
            // Show loading indicator
            loading.style.display = 'flex';
            
            try {
                // Send request to server
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        message: message
                    })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    // Display bot response
                    addBotMessage(data.reply, data.api_time);
                } else {
                    // Display error
                    addBotMessage("Désolé, une erreur s'est produite. Veuillez réessayer.");
                    console.error('Error:', data.error);
                }
            } catch (error) {
                addBotMessage("Désolé, je n'ai pas pu communiquer avec le serveur. Veuillez vérifier votre connexion.");
                console.error('Error:', error);
            } finally {
                // Hide loading indicator
                loading.style.display = 'none';
            }
        });
        
        // Reset conversation
        resetButton.addEventListener('click', async function() {
            try {
                await fetch('/api/reset', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                
                // Clear chat container
                chatContainer.innerHTML = '';
                
                // Add welcome message
                addBotMessage("👋 Conversation réinitialisée ! Comment puis-je vous aider ?");
            } catch (error) {
                console.error('Error resetting conversation:', error);
            }
        });
        
        // Helper functions
        function addUserMessage(text) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message user-message';
            messageDiv.textContent = text;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function addBotMessage(text, apiTime = null) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot-message';
            
            // Process markdown-like formatting
            text = formatMessage(text);
            
            messageDiv.innerHTML = text;
            
            // Add API time if available
            if (apiTime) {
                const timeDiv = document.createElement('div');
                timeDiv.className = 'api-time';
                timeDiv.textContent = `Temps de réponse: ${apiTime}`;
                messageDiv.appendChild(timeDiv);
            }
            
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
        
        function formatMessage(text) {
            // Code blocks
            text = text.replace(/```([\s\S]*?)```/g, '<div class="code-block">$1</div>');
            
            // Inline code
            text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
            
            // Bold
            text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            
            // Italic
            text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
            
            // Lists
            text = text.replace(/^\s*[-*]\s+(.*?)$/gm, '<li>$1</li>');
            text = text.replace(/<li>(.*?)<\/li>(\s*<li>)/g, '<li>$1</li><ul>$2');
            text = text.replace(/(<\/li>\s*)(?![<\s])/g, '$1</ul>');
            
            // Line breaks
            text = text.replace(/\n/g, '<br>');
            
            return text;
        }
    </script>
</body>
</html>""")
    
print("Template index.html créé avec succès!")

# Point d'entrée principal
if __name__ == "__main__":
    # Créer les templates
    create_templates()
    
    print("ChatBot démarré ! Accédez à http://127.0.0.1:8000 pour commencer.")
    print("Documentation API disponible à http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)