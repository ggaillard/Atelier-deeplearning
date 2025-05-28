/**
 * CHATBOT PÉDAGOGIQUE DEEP LEARNING
 * Application JavaScript principale
 * 
 * Fonctionnalités :
 * - Gestion de la conversation
 * - Intégration API backend
 * - Interface utilisateur interactive
 * - Gestion des thèmes
 * - Historique et progression
 */

class ChatbotApp {
    constructor() {
        // Configuration
        this.config = {
            apiBaseUrl: 'http://localhost:5000',
            maxRetries: 3,
            retryDelay: 1000,
            typingDelay: 1500,
            maxHistoryLength: 50
        };

        // État de l'application
        this.state = {
            isLoading: false,
            conversationHistory: [],
            currentLevel: 'beginner',
            currentTheme: 'default',
            conceptsExplored: new Set(),
            userProgress: {
                questionsAsked: 0,
                conceptsLearned: 0,
                quizzesCompleted: 0
            }
        };

        // Éléments DOM
        this.elements = {};
        
        // Initialisation
        this.init();
    }

    /**
     * Initialisation de l'application
     */
    init() {
        this.bindElements();
        this.attachEventListeners();
        this.loadUserPreferences();
        this.initializeChat();
        
        console.log('🤖 Chatbot pédagogique initialisé');
    }

    /**
     * Liaison des éléments DOM
     */
    bindElements() {
        this.elements = {
            // Chat
            chatMessages: document.getElementById('chat-messages'),
            chatForm: document.getElementById('chat-form'),
            userInput: document.getElementById('user-input'),
            sendBtn: document.getElementById('send-btn'),
            typingIndicator: document.getElementById('typing-indicator'),
            
            // Contrôles
            themeSelect: document.getElementById('theme-select'),
            levelSelect: document.getElementById('level-select'),
            clearBtn: document.getElementById('clear-btn'),
            quizBtn: document.getElementById('quiz-btn'),
            helpBtn: document.getElementById('help-btn'),
            
            // Sidebar
            conceptsHistory: document.getElementById('concepts-history'),
            progressFill: document.getElementById('progress-fill'),
            progressText: document.getElementById('progress-text'),
            
            // Status
            status: document.getElementById('status'),
            suggestions: document.getElementById('suggestions'),
            
            // Modals
            helpModal: document.getElementById('help-modal'),
            closeHelp: document.getElementById('close-help'),
            
            // Actions
            exportBtn: document.getElementById('export-btn'),
            shareBtn: document.getElementById('share-btn'),
            feedbackBtn: document.getElementById('feedback-btn')
        };
    }

    /**
     * Attachement des écouteurs d'événements
     */
    attachEventListeners() {
        // Chat form
        this.elements.chatForm.addEventListener('submit', (e) => this.handleSubmit(e));
        
        // Contrôles
        this.elements.themeSelect.addEventListener('change', (e) => this.changeTheme(e.target.value));
        this.elements.levelSelect.addEventListener('change', (e) => this.changeLevel(e.target.value));
        this.elements.clearBtn.addEventListener('click', () => this.clearConversation());
        this.elements.quizBtn.addEventListener('click', () => this.startQuiz());
        this.elements.helpBtn.addEventListener('click', () => this.showHelp());
        
        // Modal help
        this.elements.closeHelp.addEventListener('click', () => this.hideHelp());
        
        // Actions sidebar
        this.elements.exportBtn.addEventListener('click', () => this.exportConversation());
        this.elements.shareBtn.addEventListener('click', () => this.shareConversation());
        this.elements.feedbackBtn.addEventListener('click', () => this.showFeedback());
        
        // Auto-resize textarea
        this.elements.userInput.addEventListener('input', () => this.autoResizeTextarea());
        
        // Suggestions
        this.elements.suggestions.addEventListener('click', (e) => {
            if (e.target.classList.contains('suggestion')) {
                this.selectSuggestion(e.target.textContent);
            }
        });
        
        // Raccourcis clavier
        document.addEventListener('keydown', (e) => this.handleKeyboard(e));
        
        // Gestion des concepts explorés
        this.elements.conceptsHistory.addEventListener('click', (e) => {
            if (e.target.classList.contains('concept-tag')) {
                this.askAboutConcept(e.target.textContent);
            }
        });
    }

    /**
     * Gestion de la soumission du formulaire
     */
    async handleSubmit(e) {
        e.preventDefault();
        
        const message = this.elements.userInput.value.trim();
        if (!message || this.state.isLoading) return;
        
        // Ajouter le message utilisateur
        this.addMessage(message, 'user');
        this.elements.userInput.value = '';
        this.autoResizeTextarea();
        
        // Envoyer à l'API
        await this.sendMessage(message);
    }

    /**
     * Envoi du message à l'API
     */
    async sendMessage(message) {
        this.setLoading(true);
        this.showTypingIndicator();
        
        try {
            const response = await this.callAPI('/api/chat', {
                message: message,
                level: this.state.currentLevel,
                history: this.state.conversationHistory.slice(-10) // Derniers 10 messages
            });
            
            if (response.success) {
                // Ajouter la réponse de l'assistant
                setTimeout(() => {
                    this.hideTypingIndicator();
                    this.addMessage(response.response, 'assistant', response.metadata);
                    this.updateProgress(response.concepts || []);
                    this.showSuggestions(response.suggestions || []);
                }, this.config.typingDelay);
            } else {
                throw new Error(response.error || 'Erreur inconnue');
            }
            
        } catch (error) {
            this.hideTypingIndicator();
            this.showError('Désolé, je ne peux pas répondre pour le moment. Réessayez dans quelques instants.');
            console.error('Erreur API:', error);
        } finally {
            this.setLoading(false);
        }
    }

    /**
     * Appel à l'API avec gestion des erreurs
     */
    async callAPI(endpoint, data, retries = 0) {
        try {
            const response = await fetch(`${this.config.apiBaseUrl}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            return await response.json();
            
        } catch (error) {
            if (retries < this.config.maxRetries) {
                console.log(`Tentative ${retries + 1}/${this.config.maxRetries}...`);
                await this.delay(this.config.retryDelay);
                return this.callAPI(endpoint, data, retries + 1);
            }
            throw error;
        }
    }

    /**
     * Ajout d'un message à la conversation
     */
    addMessage(content, type, metadata = {}) {
        const messageElement = this.createMessageElement(content, type, metadata);
        this.elements.chatMessages.appendChild(messageElement);
        this.scrollToBottom();
        
        // Ajouter à l'historique
        this.state.conversationHistory.push({
            content,
            type,
            timestamp: new Date().toISOString(),
            metadata
        });
        
        // Limiter la taille de l'historique
        if (this.state.conversationHistory.length > this.config.maxHistoryLength) {
            this.state.conversationHistory = this.state.conversationHistory.slice(-this.config.maxHistoryLength);
        }
        
        // Mettre à jour les statistiques
        if (type === 'user') {
            this.state.userProgress.questionsAsked++;
        }
        
        // Sauvegarder localement
        this.saveState();
    }

    /**
     * Création d'un élément message
     */
    createMessageElement(content, type, metadata = {}) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.textContent = type === 'user' ? '👤' : '🤖';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const textDiv = document.createElement('div');
        textDiv.className = 'message-text';
        
        // Traitement du contenu (markdown simple)
        textDiv.innerHTML = this.formatMessage(content);
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString();
        
        contentDiv.appendChild(textDiv);
        contentDiv.appendChild(timeDiv);
        
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        // Ajouter des actions si c'est un message assistant avec métadonnées
        if (type === 'assistant' && metadata.concepts) {
            this.addMessageActions(contentDiv, metadata);
        }
        
        return messageDiv;
    }

    /**
     * Formatage simple du message (markdown basique)
     */
    formatMessage(content) {
        return content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>')
            .replace(/`(.*?)`/g, '<code>$1</code>')
            .replace(/\n/g, '<br>');
    }

    /**
     * Ajout d'actions aux messages assistant
     */
    addMessageActions(contentDiv, metadata) {
        if (metadata.concepts && metadata.concepts.length > 0) {
            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'message-actions';
            
            metadata.concepts.forEach(concept => {
                const conceptBtn = document.createElement('button');
                conceptBtn.className = 'concept-btn';
                conceptBtn.textContent = `💡 ${concept}`;
                conceptBtn.onclick = () => this.exploreConceptDeeper(concept);
                actionsDiv.appendChild(conceptBtn);
            });
            
            contentDiv.appendChild(actionsDiv);
        }
    }

    /**
     * Indicateur de frappe
     */
    showTypingIndicator() {
        this.elements.typingIndicator.classList.add('active');
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        this.elements.typingIndicator.classList.remove('active');
    }

    /**
     * Gestion du loading
     */
    setLoading(loading) {
        this.state.isLoading = loading;
        this.elements.sendBtn.disabled = loading;
        this.elements.userInput.disabled = loading;
        
        if (loading) {
            this.elements.status.textContent = 'Génération de la réponse...';
            this.elements.sendBtn.classList.add('loading');
        } else {
            this.elements.status.textContent = 'Prêt à répondre à vos questions';
            this.elements.sendBtn.classList.remove('loading');
        }
    }

    /**
     * Affichage des erreurs
     */
    showError(message) {
        const errorDiv = this.createMessageElement(`❌ ${message}`, 'assistant');
        errorDiv.classList.add('error-message');
        this.elements.chatMessages.appendChild(errorDiv);
        this.scrollToBottom();
    }

    /**
     * Scroll automatique vers le bas
     */
    scrollToBottom() {
        this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
    }

    /**
     * Auto-resize du textarea
     */
    autoResizeTextarea() {
        const textarea = this.elements.userInput;
        textarea.style.height = 'auto';
        textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px';
    }

    /**
     * Changement de thème
     */
    changeTheme(theme) {
        this.state.currentTheme = theme;
        document.body.setAttribute('data-theme', theme);
        this.saveState();
        this.showToast(`Thème "${theme}" appliqué`, 'success');
    }

    /**
     * Changement de niveau
     */
    changeLevel(level) {
        this.state.currentLevel = level;
        this.saveState();
        this.showToast(`Niveau "${level}" sélectionné`, 'info');
        
        // Adaptation de l'interface selon le niveau
        this.adaptUIToLevel(level);
    }

    /**
     * Adaptation de l'UI selon le niveau
     */
    adaptUIToLevel(level) {
        const suggestions = {
            beginner: ['Qu\'est-ce que l\'IA ?', 'Comment ça marche ?', 'À quoi ça sert ?'],
            intermediate: ['Différence CNN vs RNN', 'Comment optimiser ?', 'Cas d\'usage pratiques'],
            advanced: ['Architectures Transformer', 'Fine-tuning', 'Optimisation hyperparamètres']
        };
        
        this.showSuggestions(suggestions[level] || []);
    }

    /**
     * Affichage des suggestions
     */
    showSuggestions(suggestions) {
        this.elements.suggestions.innerHTML = '';
        
        suggestions.slice(0, 3).forEach(suggestion => {
            const suggestionBtn = document.createElement('button');
            suggestionBtn.className = 'suggestion';
            suggestionBtn.textContent = suggestion;
            this.elements.suggestions.appendChild(suggestionBtn);
        });
    }

    /**
     * Sélection d'une suggestion
     */
    selectSuggestion(suggestion) {
        this.elements.userInput.value = suggestion;
        this.elements.userInput.focus();
        this.autoResizeTextarea();
    }

    /**
     * Mise à jour de la progression
     */
    updateProgress(concepts) {
        concepts.forEach(concept => {
            this.state.conceptsExplored.add(concept);
            this.addConceptToHistory(concept);
        });
        
        this.state.userProgress.conceptsLearned = this.state.conceptsExplored.size;
        
        // Calcul du pourcentage (basé sur 20 concepts principaux)
        const progressPercentage = Math.min((this.state.conceptsExplored.size / 20) * 100, 100);
        
        this.elements.progressFill.style.width = `${progressPercentage}%`;
        this.elements.progressText.textContent = `${Math.round(progressPercentage)}% complété`;
        
        this.saveState();
    }

    /**
     * Ajout d'un concept à l'historique
     */
    addConceptToHistory(concept) {
        if (document.querySelector(`[data-concept="${concept}"]`)) return; // Déjà présent
        
        const conceptTag = document.createElement('div');
        conceptTag.className = 'concept-tag';
        conceptTag.setAttribute('data-concept', concept);
        conceptTag.textContent = concept;
        
        this.elements.conceptsHistory.appendChild(conceptTag);
    }

    /**
     * Explorer un concept plus en profondeur
     */
    async exploreConceptDeeper(concept) {
        const question = `Peux-tu m'expliquer "${concept}" plus en détail avec des exemples ?`;
        this.elements.userInput.value = question;
        await this.handleSubmit(new Event('submit'));
    }

    /**
     * Poser une question sur un concept
     */
    async askAboutConcept(concept) {
        const question = `Parle-moi de ${concept}`;
        this.elements.userInput.value = question;
        await this.handleSubmit(new Event('submit'));
    }

    /**
     * Effacer la conversation
     */
    clearConversation() {
        if (confirm('Êtes-vous sûr de vouloir effacer la conversation ?')) {
            this.elements.chatMessages.innerHTML = '';
            this.state.conversationHistory = [];
            this.initializeChat();
            this.showToast('Conversation effacée', 'info');
        }
    }

    /**
     * Initialisation du chat avec message de bienvenue
     */
    initializeChat() {
        // Message de bienvenue déjà dans le HTML
        // On peut ajouter d'autres initialisations ici
        this.updateProgress([]);
    }

    /**
     * Lancement du quiz
     */
    startQuiz() {
        if (typeof Quiz !== 'undefined' && Quiz.start) {
            Quiz.start();
        } else {
            this.showToast('Module quiz non disponible', 'warning');
        }
    }

    /**
     * Affichage de l'aide
     */
    showHelp() {
        this.elements.helpModal.classList.add('active');
    }

    hideHelp() {
        this.elements.helpModal.classList.remove('active');
    }

    /**
     * Export de la conversation
     */
    exportConversation() {
        const data = {
            timestamp: new Date().toISOString(),
            level: this.state.currentLevel,
            theme: this.state.currentTheme,
            progress: this.state.userProgress,
            concepts: Array.from(this.state.conceptsExplored),
            conversation: this.state.conversationHistory
        };
        
        const blob = new Blob([JSON.stringify(data, null, 2)], {
            type: 'application/json'
        });
        
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `conversation-deeplearning-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        
        URL.revokeObjectURL(url);
        this.showToast('Conversation exportée', 'success');
    }

    /**
     * Partage de la conversation
     */
    shareConversation() {
        if (navigator.share) {
            navigator.share({
                title: 'Ma conversation Deep Learning',
                text: `J'ai exploré ${this.state.conceptsExplored.size} concepts de Deep Learning !`,
                url: window.location.href
            });
        } else {
            // Fallback : copier le lien
            navigator.clipboard.writeText(window.location.href);
            this.showToast('Lien copié dans le presse-papier', 'info');
        }
    }

    /**
     * Feedback utilisateur
     */
    showFeedback() {
        const rating = prompt('Comment évaluez-vous votre expérience ? (1-5)');
        if (rating && rating >= 1 && rating <= 5) {
            this.showToast(`Merci pour votre évaluation : ${rating}/5 ⭐`, 'success');
            // Ici on pourrait envoyer le feedback à l'API
        }
    }

    /**
     * Gestion des raccourcis clavier
     */
    handleKeyboard(e) {
        // Ctrl+Enter pour envoyer
        if (e.ctrlKey && e.key === 'Enter') {
            this.handleSubmit(new Event('submit'));
        }
        
        // Escape pour fermer les modals
        if (e.key === 'Escape') {
            this.hideHelp();
        }
        
        // Ctrl+L pour effacer
        if (e.ctrlKey && e.key === 'l') {
            e.preventDefault();
            this.clearConversation();
        }
    }

    /**
     * Affichage des toasts
     */
    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        
        const container = document.getElementById('toast-container');
        container.appendChild(toast);
        
        // Animation d'entrée
        setTimeout(() => toast.classList.add('show'), 100);
        
        // Suppression automatique
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => container.removeChild(toast), 300);
        }, 3000);
    }

    /**
     * Sauvegarde de l'état
     */
    saveState() {
        const stateToSave = {
            currentLevel: this.state.currentLevel,
            currentTheme: this.state.currentTheme,
            conceptsExplored: Array.from(this.state.conceptsExplored),
            userProgress: this.state.userProgress,
            conversationHistory: this.state.conversationHistory.slice(-20) // Garde les 20 derniers
        };
        
        localStorage.setItem('chatbotState', JSON.stringify(stateToSave));
    }

    /**
     * Chargement des préférences utilisateur
     */
    loadUserPreferences() {
        try {
            const saved = localStorage.getItem('chatbotState');
            if (saved) {
                const state = JSON.parse(saved);
                
                // Restaurer l'état
                this.state.currentLevel = state.currentLevel || 'beginner';
                this.state.currentTheme = state.currentTheme || 'default';
                this.state.conceptsExplored = new Set(state.conceptsExplored || []);
                this.state.userProgress = { ...this.state.userProgress, ...state.userProgress };
                
                // Appliquer les préférences à l'UI
                this.elements.levelSelect.value = this.state.currentLevel;
                this.elements.themeSelect.value = this.state.currentTheme;
                this.changeTheme(this.state.currentTheme);
                this.adaptUIToLevel(this.state.currentLevel);
                
                // Restaurer les concepts explorés
                state.conceptsExplored?.forEach(concept => {
                    this.addConceptToHistory(concept);
                });
                
                this.updateProgress([]);
            }
        } catch (error) {
            console.warn('Erreur lors du chargement des préférences:', error);
        }
    }

    /**
     * Utilitaire : délai
     */
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    /**
     * Vérification de la santé de l'API
     */
    async checkAPIHealth() {
        try {
            const response = await fetch(`${this.config.apiBaseUrl}/health`);
            return response.ok;
        } catch {
            return false;
        }
    }
}

// CSS pour les éléments ajoutés dynamiquement
const additionalCSS = `
.concept-btn {
    background: var(--accent-color);
    color: white;
    border: none;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.8rem;
    margin: 2px;
    cursor: pointer;
    transition: var(--transition-fast);
}

.concept-btn:hover {
    transform: scale(1.05);
    box-shadow: var(--shadow-sm);
}

.message-actions {
    margin-top: 8px;
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
}

.error-message .message-content {
    background: rgba(239, 68, 68, 0.1);
    border-left: 4px solid var(--danger-color);
}

.loading {
    opacity: 0.6;
    pointer-events: none;
}

@media (max-width: 768px) {
    .concept-btn {
        font-size: 0.75rem;
        padding: 3px 6px;
    }
}
`;

// Ajouter le CSS
const style = document.createElement('style');
style.textContent = additionalCSS;
document.head.appendChild(style);

// Initialisation de l'application
let chatbotApp;

document.addEventListener('DOMContentLoaded', () => {
    chatbotApp = new ChatbotApp();
    
    // Vérification de la santé de l'API au démarrage
    chatbotApp.checkAPIHealth().then(healthy => {
        if (!healthy) {
            console.warn('⚠️ API non disponible. Vérifiez que le serveur backend est démarré.');
            chatbotApp.showToast('Serveur non disponible. Vérifiez le backend.', 'warning');
        }
    });
});

// Export pour usage externe
window.ChatbotApp = ChatbotApp;