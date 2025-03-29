# Guide simplifié d'utilisation de l'API Mistral AI

Ce guide vous explique comment intégrer l'API Mistral AI dans votre projet de chatbot pédagogique de manière simple et efficace.

## 1. Obtenir une clé API

### Créer un compte et obtenir une clé gratuite

1. Rendez-vous sur [https://console.mistral.ai/](https://console.mistral.ai/)
2. Inscrivez-vous avec votre adresse email
3. Connectez-vous à votre compte
4. Dans le tableau de bord, cliquez sur "API Keys"
5. Cliquez sur "Create API Key"
6. Donnez un nom à votre clé (ex: "Projet-Chatbot-BTS")
7. **IMPORTANT**: Copiez immédiatement la clé générée et conservez-la en lieu sûr. Elle ne sera plus affichée ensuite.

### Limites du compte gratuit
- Un nombre limité de requêtes par minute
- Utilisation des modèles de base (suffisant pour notre projet)
- Pas d'usage commercial

## 2. Installation des bibliothèques nécessaires

### Avec pip
```bash
pip install mistralai requests python-dotenv
```

### Dans Google Colab
```python
!pip install mistralai requests python-dotenv
```

## 3. Configuration de base

### Fichier .env pour stocker votre clé API (bonne pratique)
Créez un fichier nommé `.env` contenant:
```
MISTRAL_API_KEY=votre_clé_api_ici
```

### Configuration du client dans votre code Python
```python
import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialiser le client Mistral
client = MistralClient(api_key=api_key)

# Choisir le modèle
model = "mistral-tiny"  # Modèle de base, rapide et peu coûteux
```

## 4. Utilisation de base pour un chatbot

### Créer une fonction simple d'interaction
```python
def get_ai_response(user_message, conversation_history=None):
    """
    Obtient une réponse du modèle Mistral AI.
    
    Args:
        user_message (str): Message de l'utilisateur
        conversation_history (list, optional): Historique de la conversation
    
    Returns:
        str: Réponse du modèle
    """
    # Initialiser l'historique si nécessaire
    if conversation_history is None:
        conversation_history = []
    
    # Ajouter le message de l'utilisateur à l'historique
    conversation_history.append(ChatMessage(role="user", content=user_message))
    
    # Obtenir la réponse du modèle
    chat_response = client.chat(
        model=model,
        messages=conversation_history
    )
    
    # Extraire le texte de la réponse
    ai_response = chat_response.choices[0].message.content
    
    # Ajouter la réponse à l'historique
    conversation_history.append(ChatMessage(role="assistant", content=ai_response))
    
    return ai_response, conversation_history
```

### Exemple d'utilisation simple
```python
# Initialiser l'historique avec un message système pour définir le rôle du chatbot
conversation = [
    ChatMessage(
        role="system", 
        content="Tu es un assistant pédagogique spécialisé dans le Deep Learning. Tu donnes des explications claires, adaptées à des étudiants de BTS SIO. Tu utilises des exemples concrets et tu expliques les concepts techniques de manière simple."
    )
]

# Premier échange
user_input = "Peux-tu m'expliquer ce qu'est un réseau de neurones convolutif ?"
response, conversation = get_ai_response(user_input, conversation)
print("Assistant:", response)

# Deuxième échange (avec contexte de la conversation)
user_input = "Peux-tu me donner un exemple d'application concrète ?"
response, conversation = get_ai_response(user_input, conversation)
print("Assistant:", response)
```

## 5. Améliorations pour votre chatbot pédagogique

### Ajout d'une base de connaissances spécifique
Vous pouvez enrichir vos prompts système pour guider le modèle:

```python
def create_education_prompt(topic):
    """Crée un prompt spécifique pour un sujet de Deep Learning"""
    
    prompts = {
        "introduction": "Explique les concepts de base du Deep Learning comme si tu parlais à un étudiant de BTS SIO qui débute. Utilise des analogies simples et évite les formules mathématiques complexes.",
        
        "cnn": "Explique les réseaux de neurones convolutifs (CNN) de manière simple. Mentionne leur utilisation dans la vision par ordinateur, la structure en couches de convolution et pooling, et donne des exemples d'applications comme la reconnaissance d'images.",
        
        "rnn": "Explique les réseaux de neurones récurrents (RNN) simplement. Précise leur utilité pour les données séquentielles comme le texte, la notion de mémoire dans ces réseaux, et des exemples comme la génération de texte ou la traduction."
    }
    
    return prompts.get(topic, "Explique ce concept de Deep Learning de manière simple pour un étudiant de BTS SIO.")
```

### Gestion des paramètres du modèle
Vous pouvez ajuster les paramètres pour contrôler les réponses:

```python
def get_ai_response_with_params(user_message, conversation_history=None, temperature=0.7, max_tokens=1000):
    """Version améliorée avec paramètres ajustables"""
    
    # ... (même code que précédemment) ...
    
    # Obtenir la réponse avec paramètres personnalisés
    chat_response = client.chat(
        model=model,
        messages=conversation_history,
        temperature=temperature,  # Contrôle la créativité (0.1-1.0)
        max_tokens=max_tokens     # Limite la longueur de la réponse
    )
    
    # ... (suite identique) ...
```

### Format structuré pour les explications pédagogiques
Pour obtenir des réponses plus structurées, vous pouvez guider le format:

```python
def get_structured_explanation(topic):
    """Obtient une explication structurée sur un sujet de Deep Learning"""
    
    prompt = f"""
    Explique le concept de {topic} en Deep Learning avec la structure suivante:
    
    1. Définition simple (2-3 phrases)
    2. Fonctionnement de base (sans formules mathématiques)
    3. Cas d'usage concrets (2-3 exemples)
    4. Avantages et limites
    5. Analogie simple pour comprendre le concept
    
    Utilise un langage accessible pour des étudiants de niveau BTS.
    """
    
    response, _ = get_ai_response(prompt)
    return response
```

## 6. Gestion des erreurs et bonnes pratiques

### Gestion basique des erreurs
```python
def safe_ai_request(user_message, conversation_history=None):
    """Fonction avec gestion des erreurs de base"""
    try:
        return get_ai_response(user_message, conversation_history)
    except Exception as e:
        error_message = f"Erreur lors de la communication avec l'API: {str(e)}"
        print(error_message)
        # Réponse de secours
        return "Désolé, je rencontre des difficultés techniques actuellement. Pouvez-vous réessayer?", conversation_history
```

### Mise en cache des réponses fréquentes
```python
# Cache simple avec dictionnaire
response_cache = {}

def get_cached_response(question, conversation_history=None):
    """Utilise un cache pour les questions fréquentes"""
    # Simplifie la question pour la mise en cache
    simple_question = question.lower().strip()
    
    if simple_question in response_cache:
        print("Réponse trouvée dans le cache")
        return response_cache[simple_question], conversation_history
    
    # Si pas dans le cache, obtient la réponse de l'API
    response, updated_history = get_ai_response(question, conversation_history)
    
    # Stocke dans le cache
    response_cache[simple_question] = response
    
    return response, updated_history
```

## 7. Exemple complet d'intégration Flask

```python
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Configuration
load_dotenv()
app = Flask(__name__)
client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))
model = "mistral-tiny"

# Stockage des conversations (simple, pour démonstration)
conversations = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    # Récupère ou crée la conversation
    if session_id not in conversations:
        conversations[session_id] = [
            ChatMessage(
                role="system", 
                content="Tu es un assistant pédagogique expert en Deep Learning pour des étudiants de BTS SIO."
            )
        ]
    
    conversation = conversations[session_id]
    
    # Ajoute le message utilisateur
    conversation.append(ChatMessage(role="user", content=user_message))
    
    try:
        # Obtient la réponse
        response = client.chat(model=model, messages=conversation)
        ai_message = response.choices[0].message.content
        
        # Ajoute la réponse à l'historique
        conversation.append(ChatMessage(role="assistant", content=ai_message))
        
        return jsonify({
            'reply': ai_message,
            'session_id': session_id
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'reply': "Désolé, une erreur s'est produite."
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## 8. Ressources complémentaires

### Documentation officielle
- [Documentation Mistral AI](https://docs.mistral.ai/)
- [API Reference](https://docs.mistral.ai/api/)

### Templates et exemples
- [GitHub avec exemples d'intégration](https://github.com/mistralai/mistral-python)
- [Documentation de la bibliothèque Python](https://github.com/mistralai/client-python)

### Tutoriels recommandés
- [Tutoriel d'intégration Flask](https://blog.mistral.ai/tutorial-flask-mistral-ai/)
- [Améliorer la qualité des prompts](https://docs.mistral.ai/guides/prompt-engineering/)

## 9. Conseils pour votre projet BTS

1. **Commencez simple** : Assurez-vous que l'intégration de base fonctionne avant d'ajouter des fonctionnalités avancées
2. **Attention à votre clé API** : Ne la partagez pas et ne la publiez pas dans votre code source
3. **Testez vos prompts** : La qualité des réponses dépend beaucoup de la formulation de vos instructions
4. **Gérez le contexte** : Utilisez intelligemment l'historique des conversations pour des réponses cohérentes
5. **Prévoyez les erreurs** : Ajoutez une gestion robuste des erreurs d'API
6. **Optimisez les coûts** : Limitez la taille des historiques de conversation pour réduire les jetons utilisés
7. **Interface réactive** : Prévoyez des indicateurs de chargement pendant les appels API
8. **Testez avec des utilisateurs réels** : Recueillez des feedbacks sur la qualité des réponses

## 10. FAQ spécial BTS SIO 

### Q: Ai-je besoin d'une carte de crédit pour l'API Mistral AI ?
R: Non, vous pouvez créer un compte gratuit avec un quota limité suffisant pour le projet.

### Q: Comment stocker l'historique des conversations ?
R: Pour un projet simple, une structure de données en mémoire suffit. Pour un projet plus avancé, utilisez une base de données (SQLite est une option simple).

### Q: Est-ce que le modèle peut générer du code Python ?
R: Oui, Mistral AI peut générer du code Python basique pour des exemples d'utilisation de TensorFlow/Keras.

### Q: Comment limiter les coûts d'API si je veux déployer mon application ?
R: Limitez la longueur des contextes, mettez en cache les réponses fréquentes, et définissez des quotas d'utilisation par utilisateur.

### Q: Comment faire comprendre au modèle le contexte spécifique du Deep Learning ?
R: Utilisez des messages système précis et incluez des exemples de questions/réponses dans le prompt initial.

## 11. Exemple de template HTML/CSS/JS minimal

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Deep Learning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        #chat-container {
            height: 400px;
            border: 1px solid #ddd;
            padding: 15px;
            overflow-y: auto;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .message {
            margin-bottom: 10px;
            padding: 8px 15px;
            border-radius: 20px;
            max-width: 80%;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #e6f7ff;
            margin-left: auto;
            text-align: right;
            border-bottom-right-radius: 0;
        }
        .bot-message {
            background-color: #f1f1f1;
            margin-right: auto;
            border-bottom-left-radius: 0;
        }
        #message-form {
            display: flex;
        }
        #user-input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        #send-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            margin-left: 10px;
            cursor: pointer;
        }
        #loading {
            display: none;
            text-align: center;
            margin-top: 10px;
            color: #888;
        }
    </style>
</head>
<body>
    <h1>Assistant Deep Learning pour BTS SIO</h1>
    <div id="chat-container"></div>
    <div id="loading">L'assistant réfléchit...</div>
    <form id="message-form">
        <input type="text" id="user-input" placeholder="Posez votre question sur le Deep Learning..." required>
        <button type="submit" id="send-button">Envoyer</button>
    </form>

    <script>
        let sessionId = 'session_' + Date.now();
        const chatContainer = document.getElementById('chat-container');
        const messageForm = document.getElementById('message-form');
        const userInput = document.getElementById('user-input');
        const loading = document.getElementById('loading');

        // Ajouter un message d'accueil
        addBotMessage("Bonjour ! Je suis votre assistant Deep Learning. Comment puis-je vous aider aujourd'hui ?");

        messageForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const message = userInput.value.trim();
            if (!message) return;

            // Afficher le message de l'utilisateur
            addUserMessage(message);
            userInput.value = '';

            // Afficher l'indicateur de chargement
            loading.style.display = 'block';

            try {
                // Envoyer la requête au serveur
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        message: message,
                        session_id: sessionId
                    })
                });

                const data = await response.json();
                
                if (response.ok) {
                    // Afficher la réponse du bot
                    addBotMessage(data.reply);
                } else {
                    // Afficher l'erreur
                    addBotMessage("Désolé, une erreur s'est produite: " + data.error);
                }
            } catch (error) {
                addBotMessage("Désolé, je n'ai pas pu communiquer avec le serveur. Veuillez réessayer.");
                console.error('Error:', error);
            } finally {
                // Cacher l'indicateur de chargement
                loading.style.display = 'none';
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        });

        function addUserMessage(text) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message user-message';
            messageDiv.textContent = text;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function addBotMessage(text) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message bot-message';
            
            // Support for markdown-like formatting
            text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
            text = text.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
            text = text.replace(/`(.*?)`/g, '<code>$1</code>');
            
            // Convert line breaks
            text = text.replace(/\n/g, '<br>');
            
            messageDiv.innerHTML = text;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>
</body>
</html>
```

Ce guide vous a fourni toutes les bases nécessaires pour intégrer l'API Mistral AI dans votre projet de chatbot pédagogique. N'hésitez pas à adapter les exemples à vos besoins spécifiques et à expérimenter avec différentes approches pour améliorer votre application.