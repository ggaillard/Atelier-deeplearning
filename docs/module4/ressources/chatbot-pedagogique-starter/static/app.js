// Variables globales
let conversationHistory = [];
let isProcessing = false;

// Éléments DOM
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const sendText = document.getElementById('send-text');
const loading = document.getElementById('loading');

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !isProcessing) {
            sendMessage();
        }
    });
    
    userInput.focus();
});

// Fonction principale d'envoi de message
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message || isProcessing) return;
    
    // Affichage du message utilisateur
    addMessage(message, 'user');
    userInput.value = '';
    
    // État de chargement
    setLoading(true);
    
    try {
        // Appel API
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                history: conversationHistory
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            // Ajout de la réponse du bot
            addMessage(data.response, 'bot');
            
            // Mise à jour de l'historique
            conversationHistory.push(
                { role: 'user', content: message },
                { role: 'assistant', content: data.response }
            );
            
            // Limitation de l'historique
            if (conversationHistory.length > 10) {
                conversationHistory = conversationHistory.slice(-10);
            }
        } else {
            addMessage('Désolé, une erreur est survenue. Pouvez-vous reformuler ?', 'bot');
        }
    } catch (error) {
        console.error('Erreur:', error);
        addMessage('Erreur de connexion. Vérifiez votre connexion internet.', 'bot');
    } finally {
        setLoading(false);
    }
}

// Ajout d'un message à l'interface
function addMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    const avatar = sender === 'user' ? '👤' : '🤖';
    
    messageDiv.innerHTML = `
        <div class="avatar">${avatar}</div>
        <div class="content">
            <p>${content}</p>
        </div>
    `;
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Gestion de l'état de chargement
function setLoading(loading) {
    isProcessing = loading;
    sendBtn.disabled = loading;
    
    if (loading) {
        sendText.style.display = 'none';
        document.getElementById('loading').style.display = 'inline';
    } else {
        sendText.style.display = 'inline';
        document.getElementById('loading').style.display = 'none';
    }
}

// Fonction pour les suggestions
function askQuestion(question) {
    userInput.value = question;
    sendMessage();
}

// Fonction de réinitialisation (bonus)
function resetChat() {
    conversationHistory = [];
    chatMessages.innerHTML = `
        <div class="message bot">
            <div class="avatar">🤖</div>
            <div class="content">
                <p>Bonjour ! Je suis votre assistant pour le Deep Learning. 
                Posez-moi vos questions sur les réseaux de neurones, CNN, RNN, etc.</p>
            </div>
        </div>
    `;
}