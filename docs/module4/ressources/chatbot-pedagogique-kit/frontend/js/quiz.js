/**
 * MODULE QUIZ - CHOIX B PERSONNALISATION
 * Système de quiz interactif pour le chatbot pédagogique
 * 
 * Fonctionnalités :
 * - Génération de quiz adaptatifs
 * - Interface interactive de questions/réponses
 * - Système de scoring et feedback
 * - Progression et statistiques
 * - Sauvegarde des résultats
 */

class QuizManager {
    constructor() {
        this.config = {
            apiBaseUrl: 'http://localhost:5000',
            defaultQuestionCount: 5,
            timePerQuestion: 30, // secondes
            passingScore: 70, // pourcentage
            maxRetries: 2
        };

        this.state = {
            currentQuiz: null,
            currentQuestionIndex: 0,
            userAnswers: [],
            score: 0,
            timeRemaining: 0,
            isActive: false,
            startTime: null,
            selectedTopic: null,
            difficulty: 'intermediate'
        };

        this.elements = {};
        this.timer = null;
        
        this.init();
    }

    /**
     * Initialisation du module quiz
     */
    init() {
        this.bindElements();
        this.attachEventListeners();
        this.loadQuizData();
        
        console.log('📝 Module Quiz initialisé');
    }

    /**
     * Liaison des éléments DOM
     */
    bindElements() {
        this.elements = {
            // Overlay et container principal
            overlay: document.getElementById('quiz-overlay'),
            container: document.querySelector('.quiz-container'),
            
            // Header
            topic: document.getElementById('quiz-topic'),
            closeBtn: document.getElementById('close-quiz'),
            
            // Contenu du quiz
            content: document.querySelector('.quiz-content'),
            questionContainer: document.getElementById('question-container'),
            
            // Navigation
            prevBtn: document.getElementById('prev-question'),
            nextBtn: document.getElementById('next-question'),
            submitBtn: document.getElementById('submit-quiz'),
            
            // Progression
            progressFill: document.getElementById('quiz-progress-fill'),
            progressText: document.getElementById('quiz-progress-text'),
            
            // Résultats
            results: document.getElementById('quiz-results'),
            scorePercentage: document.getElementById('score-percentage'),
            scoreMessage: document.getElementById('score-message'),
            detailedResults: document.getElementById('detailed-results'),
            retryBtn: document.getElementById('retry-quiz'),
            closeResultsBtn: document.getElementById('close-results')
        };
    }

    /**
     * Attachement des écouteurs d'événements
     */
    attachEventListeners() {
        // Fermeture du quiz
        this.elements.closeBtn.addEventListener('click', () => this.close());
        this.elements.overlay.addEventListener('click', (e) => {
            if (e.target === this.elements.overlay) this.close();
        });
        
        // Navigation
        this.elements.prevBtn.addEventListener('click', () => this.previousQuestion());
        this.elements.nextBtn.addEventListener('click', () => this.nextQuestion());
        this.elements.submitBtn.addEventListener('click', () => this.submitQuiz());
        
        // Résultats
        this.elements.retryBtn.addEventListener('click', () => this.retryQuiz());
        this.elements.closeResultsBtn.addEventListener('click', () => this.close());
        
        // Raccourcis clavier
        document.addEventListener('keydown', (e) => {
            if (this.state.isActive) {
                this.handleKeyboard(e);
            }
        });
    }

    /**
     * Démarrage d'un quiz
     */
    async start(topic = null, difficulty = 'intermediate') {
        try {
            this.state.selectedTopic = topic;
            this.state.difficulty = difficulty;
            
            // Récupérer les questions
            const quizData = await this.generateQuiz(topic, difficulty);
            
            if (!quizData || !quizData.questions || quizData.questions.length === 0) {
                throw new Error('Aucune question disponible pour ce sujet');
            }
            
            // Initialiser le quiz
            this.state.currentQuiz = quizData;
            this.state.currentQuestionIndex = 0;
            this.state.userAnswers = new Array(quizData.questions.length).fill(null);
            this.state.score = 0;
            this.state.isActive = true;
            this.state.startTime = new Date();
            
            // Afficher l'interface
            this.showQuizUI();
            this.displayQuestion();
            this.updateNavigation();
            this.updateProgress();
            
        } catch (error) {
            console.error('Erreur lors du démarrage du quiz:', error);
            this.showError('Impossible de charger le quiz. Réessayez plus tard.');
        }
    }

    /**
     * Génération du quiz via l'API
     */
    async generateQuiz(topic, difficulty) {
        const response = await fetch(`${this.config.apiBaseUrl}/api/quiz/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                topic: topic || 'deep_learning_general',
                difficulty: difficulty,
                count: this.config.defaultQuestionCount
            })
        });
        
        if (!response.ok) {
            throw new Error(`Erreur API: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Chargement des données de quiz (fallback local)
     */
    async loadQuizData() {
        // Données de quiz par défaut si l'API n'est pas disponible
        this.fallbackQuizzes = {
            deep_learning_general: {
                title: "Concepts généraux du Deep Learning",
                questions: [
                    {
                        id: 1,
                        question: "Qu'est-ce qui caractérise principalement le Deep Learning par rapport au Machine Learning classique ?",
                        options: [
                            "Il utilise toujours plus de données",
                            "Il extrait automatiquement les caractéristiques pertinentes",
                            "Il est plus rapide à entraîner",
                            "Il ne nécessite pas de GPU"
                        ],
                        correctAnswer: 1,
                        explanation: "Le Deep Learning se distingue par sa capacité à extraire automatiquement des caractéristiques hiérarchiques à partir des données brutes, éliminant le besoin d'extraction manuelle des features.",
                        difficulty: "beginner"
                    },
                    {
                        id: 2,
                        question: "Quel est le rôle principal de la fonction d'activation dans un neurone artificiel ?",
                        options: [
                            "Augmenter la vitesse de calcul",
                            "Introduire de la non-linéarité",
                            "Réduire la taille du modèle",
                            "Éviter le surapprentissage"
                        ],
                        correctAnswer: 1,
                        explanation: "La fonction d'activation introduit de la non-linéarité dans le réseau, permettant d'apprendre des relations complexes entre les données.",
                        difficulty: "intermediate"
                    },
                    {
                        id: 3,
                        question: "Quelle technique est utilisée pour mettre à jour les poids dans un réseau de neurones ?",
                        options: [
                            "Descente de gradient",
                            "Montée de gradient",
                            "Recherche aléatoire",
                            "Algorithme génétique"
                        ],
                        correctAnswer: 0,
                        explanation: "La descente de gradient est l'algorithme d'optimisation standard pour ajuster les poids afin de minimiser la fonction de coût.",
                        difficulty: "intermediate"
                    },
                    {
                        id: 4,
                        question: "Qu'est-ce que le surapprentissage (overfitting) ?",
                        options: [
                            "Quand le modèle apprend trop lentement",
                            "Quand le modèle mémorise les données d'entraînement sans généraliser",
                            "Quand le modèle a trop de paramètres",
                            "Quand l'entraînement prend trop de temps"
                        ],
                        correctAnswer: 1,
                        explanation: "Le surapprentissage se produit quand le modèle mémorise les données d'entraînement au lieu d'apprendre des patterns généralisables.",
                        difficulty: "intermediate"
                    },
                    {
                        id: 5,
                        question: "Quelle architecture est la plus adaptée pour traiter des images ?",
                        options: [
                            "RNN (Réseaux Récurrents)",
                            "CNN (Réseaux Convolutifs)",
                            "LSTM",
                            "Perceptron simple"
                        ],
                        correctAnswer: 1,
                        explanation: "Les CNN sont spécialement conçus pour traiter les données spatiales comme les images, grâce aux opérations de convolution et pooling.",
                        difficulty: "beginner"
                    }
                ]
            }
        };
    }

    /**
     * Affichage de l'interface quiz
     */
    showQuizUI() {
        // Masquer les résultats et afficher le contenu
        this.elements.results.style.display = 'none';
        this.elements.content.style.display = 'block';
        
        // Mettre à jour le titre
        this.elements.topic.textContent = this.state.currentQuiz.title || 'Quiz Deep Learning';
        
        // Afficher l'overlay
        this.elements.overlay.classList.add('active');
        
        // Focus sur le container pour l'accessibilité
        this.elements.container.focus();
    }

    /**
     * Affichage d'une question
     */
    displayQuestion() {
        const question = this.state.currentQuiz.questions[this.state.currentQuestionIndex];
        if (!question) return;
        
        const questionHTML = `
            <div class="question-wrapper">
                <div class="question-number">
                    Question ${this.state.currentQuestionIndex + 1} sur ${this.state.currentQuiz.questions.length}
                </div>
                <div class="question" id="current-question">
                    ${question.question}
                </div>
                <div class="options" id="question-options">
                    ${question.options.map((option, index) => `
                        <div class="option" data-index="${index}" onclick="Quiz.selectOption(${index})">
                            <span class="option-letter">${String.fromCharCode(65 + index)}</span>
                            <span class="option-text">${option}</span>
                        </div>
                    `).join('')}
                </div>
                <div class="question-feedback" id="question-feedback" style="display: none;">
                    <!-- Feedback sera ajouté après sélection -->
                </div>
            </div>
        `;
        
        this.elements.questionContainer.innerHTML = questionHTML;
        
        // Restaurer la réponse précédente si elle existe
        const previousAnswer = this.state.userAnswers[this.state.currentQuestionIndex];
        if (previousAnswer !== null) {
            this.selectOption(previousAnswer, false);
        }
    }

    /**
     * Sélection d'une option
     */
    selectOption(optionIndex, animate = true) {
        // Désélectionner toutes les options
        document.querySelectorAll('.option').forEach(opt => {
            opt.classList.remove('selected');
        });
        
        // Sélectionner l'option choisie
        const selectedOption = document.querySelector(`[data-index="${optionIndex}"]`);
        if (selectedOption) {
            selectedOption.classList.add('selected');
            
            if (animate) {
                selectedOption.style.transform = 'scale(0.98)';
                setTimeout(() => {
                    selectedOption.style.transform = 'scale(1)';
                }, 150);
            }
        }
        
        // Sauvegarder la réponse
        this.state.userAnswers[this.state.currentQuestionIndex] = optionIndex;
        
        // Mettre à jour la navigation
        this.updateNavigation();
    }

    /**
     * Question suivante
     */
    nextQuestion() {
        if (this.state.currentQuestionIndex < this.state.currentQuiz.questions.length - 1) {
            this.state.currentQuestionIndex++;
            this.displayQuestion();
            this.updateNavigation();
            this.updateProgress();
            this.scrollToTop();
        }
    }

    /**
     * Question précédente
     */
    previousQuestion() {
        if (this.state.currentQuestionIndex > 0) {
            this.state.currentQuestionIndex--;
            this.displayQuestion();
            this.updateNavigation();
            this.updateProgress();
            this.scrollToTop();
        }
    }

    /**
     * Mise à jour de la navigation
     */
    updateNavigation() {
        const isFirst = this.state.currentQuestionIndex === 0;
        const isLast = this.state.currentQuestionIndex === this.state.currentQuiz.questions.length - 1;
        const hasAnswer = this.state.userAnswers[this.state.currentQuestionIndex] !== null;
        
        // Bouton précédent
        this.elements.prevBtn.disabled = isFirst;
        
        // Bouton suivant
        this.elements.nextBtn.disabled = isLast;
        this.elements.nextBtn.style.display = isLast ? 'none' : 'block';
        
        // Bouton soumettre
        this.elements.submitBtn.style.display = isLast ? 'block' : 'none';
        this.elements.submitBtn.disabled = !this.allQuestionsAnswered();
    }

    /**
     * Mise à jour de la progression
     */
    updateProgress() {
        const progress = ((this.state.currentQuestionIndex + 1) / this.state.currentQuiz.questions.length) * 100;
        const answered = this.state.userAnswers.filter(answer => answer !== null).length;
        
        this.elements.progressFill.style.width = `${progress}%`;
        this.elements.progressText.textContent = 
            `Question ${this.state.currentQuestionIndex + 1} sur ${this.state.currentQuiz.questions.length} (${answered} répondues)`;
    }

    /**
     * Vérification si toutes les questions ont une réponse
     */
    allQuestionsAnswered() {
        return this.state.userAnswers.every(answer => answer !== null);
    }

    /**
     * Soumission du quiz
     */
    async submitQuiz() {
        if (!this.allQuestionsAnswered()) {
            if (!confirm('Vous n\'avez pas répondu à toutes les questions. Voulez-vous quand même soumettre ?')) {
                return;
            }
        }
        
        // Calcul du score
        this.calculateScore();
        
        // Sauvegarde des résultats
        await this.saveResults();
        
        // Affichage des résultats
        this.showResults();
        
        // Notification à l'app principale
        if (window.chatbotApp) {
            window.chatbotApp.state.userProgress.quizzesCompleted++;
            window.chatbotApp.saveState();
        }
    }

    /**
     * Calcul du score
     */
    calculateScore() {
        let correctAnswers = 0;
        const totalQuestions = this.state.currentQuiz.questions.length;
        
        this.state.currentQuiz.questions.forEach((question, index) => {
            const userAnswer = this.state.userAnswers[index];
            if (userAnswer === question.correctAnswer) {
                correctAnswers++;
            }
        });
        
        this.state.score = Math.round((correctAnswers / totalQuestions) * 100);
        return {
            score: this.state.score,
            correct: correctAnswers,
            total: totalQuestions
        };
    }

    /**
     * Sauvegarde des résultats
     */
    async saveResults() {
        const results = {
            topic: this.state.selectedTopic,
            difficulty: this.state.difficulty,
            score: this.state.score,
            answers: this.state.userAnswers,
            timestamp: new Date().toISOString(),
            duration: new Date() - this.state.startTime
        };
        
        // Sauvegarde locale
        const savedQuizzes = JSON.parse(localStorage.getItem('quizResults') || '[]');
        savedQuizzes.push(results);
        localStorage.setItem('quizResults', JSON.stringify(savedQuizzes.slice(-20))); // Garde les 20 derniers
        
        // Tentative de sauvegarde sur l'API
        try {
            await fetch(`${this.config.apiBaseUrl}/api/quiz/results`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(results)
            });
        } catch (error) {
            console.log('Sauvegarde locale uniquement');
        }
    }

    /**
     * Affichage des résultats
     */
    showResults() {
        // Masquer le contenu du quiz
        this.elements.content.style.display = 'none';
        
        // Afficher les résultats
        this.elements.results.style.display = 'block';
        
        // Score principal
        this.elements.scorePercentage.textContent = `${this.state.score}%`;
        
        // Message selon le score
        let message = '';
        let messageClass = '';
        
        if (this.state.score >= 90) {
            message = 'Excellent ! Vous maîtrisez parfaitement ces concepts ! 🏆';
            messageClass = 'excellent';
        } else if (this.state.score >= 70) {
            message = 'Très bien ! Vous avez une bonne compréhension. 👍';
            messageClass = 'good';
        } else if (this.state.score >= 50) {
            message = 'Pas mal ! Il y a quelques concepts à revoir. 📚';
            messageClass = 'average';
        } else {
            message = 'Il faut revoir ces concepts. Ne vous découragez pas ! 💪';
            messageClass = 'needs-work';
        }
        
        this.elements.scoreMessage.textContent = message;
        this.elements.scoreMessage.className = messageClass;
        
        // Résultats détaillés
        this.showDetailedResults();
        
        // Animation du score
        this.animateScore();
    }

    /**
     * Affichage des résultats détaillés
     */
    showDetailedResults() {
        const detailedHTML = this.state.currentQuiz.questions.map((question, index) => {
            const userAnswer = this.state.userAnswers[index];
            const isCorrect = userAnswer === question.correctAnswer;
            
            return `
                <div class="result-item ${isCorrect ? 'correct' : 'incorrect'}">
                    <div class="result-question">
                        <strong>Question ${index + 1}:</strong> ${question.question}
                    </div>
                    <div class="result-answer">
                        <div class="user-answer">
                            Votre réponse: ${userAnswer !== null ? question.options[userAnswer] : 'Non répondue'}
                            ${isCorrect ? '✅' : '❌'}
                        </div>
                        ${!isCorrect ? `
                            <div class="correct-answer">
                                Bonne réponse: ${question.options[question.correctAnswer]}
                            </div>
                        ` : ''}
                        <div class="explanation">
                            💡 ${question.explanation}
                        </div>
                    </div>
                </div>
            `;
        }).join('');
        
        this.elements.detailedResults.innerHTML = detailedHTML;
    }

    /**
     * Animation du score
     */
    animateScore() {
        const target = this.state.score;
        let current = 0;
        const increment = target / 30; // Animation sur 30 frames
        
        const animate = () => {
            current += increment;
            if (current >= target) {
                current = target;
                this.elements.scorePercentage.textContent = `${target}%`;
            } else {
                this.elements.scorePercentage.textContent = `${Math.round(current)}%`;
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    }

    /**
     * Recommencer le quiz
     */
    retryQuiz() {
        this.start(this.state.selectedTopic, this.state.difficulty);
    }

    /**
     * Fermeture du quiz
     */
    close() {
        this.elements.overlay.classList.remove('active');
        this.state.isActive = false;
        
        if (this.timer) {
            clearInterval(this.timer);
            this.timer = null;
        }
        
        // Reset de l'état
        setTimeout(() => {
            this.state.currentQuiz = null;
            this.state.currentQuestionIndex = 0;
            this.state.userAnswers = [];
            this.state.score = 0;
        }, 300);
    }

    /**
     * Gestion des raccourcis clavier
     */
    handleKeyboard(e) {
        switch (e.key) {
            case 'Escape':
                this.close();
                break;
            case 'ArrowLeft':
                if (!this.elements.prevBtn.disabled) {
                    this.previousQuestion();
                }
                break;
            case 'ArrowRight':
                if (!this.elements.nextBtn.disabled) {
                    this.nextQuestion();
                }
                break;
            case '1':
            case '2':
            case '3':
            case '4':
                const optionIndex = parseInt(e.key) - 1;
                if (optionIndex < 4) {
                    this.selectOption(optionIndex);
                }
                break;
            case 'Enter':
                if (this.elements.submitBtn.style.display !== 'none' && !this.elements.submitBtn.disabled) {
                    this.submitQuiz();
                } else if (!this.elements.nextBtn.disabled) {
                    this.nextQuestion();
                }
                break;
        }
    }

    /**
     * Scroll vers le haut
     */
    scrollToTop() {
        this.elements.container.scrollTop = 0;
    }

    /**
     * Affichage d'erreur
     */
    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'quiz-error';
        errorDiv.innerHTML = `
            <div class="error-content">
                <h3>❌ Erreur</h3>
                <p>${message}</p>
                <button onclick="Quiz.close()" class="error-btn">Fermer</button>
            </div>
        `;
        
        this.elements.questionContainer.innerHTML = '';
        this.elements.questionContainer.appendChild(errorDiv);
    }

    /**
     * Statistiques des quiz
     */
    getStats() {
        const savedQuizzes = JSON.parse(localStorage.getItem('quizResults') || '[]');
        
        if (savedQuizzes.length === 0) {
            return {
                totalQuizzes: 0,
                averageScore: 0,
                bestScore: 0,
                topics: {}
            };
        }
        
        const totalScore = savedQuizzes.reduce((sum, quiz) => sum + quiz.score, 0);
        const averageScore = Math.round(totalScore / savedQuizzes.length);
        const bestScore = Math.max(...savedQuizzes.map(quiz => quiz.score));
        
        const topics = {};
        savedQuizzes.forEach(quiz => {
            if (!topics[quiz.topic]) {
                topics[quiz.topic] = [];
            }
            topics[quiz.topic].push(quiz.score);
        });
        
        return {
            totalQuizzes: savedQuizzes.length,
            averageScore,
            bestScore,
            topics
        };
    }
}

// CSS pour les résultats détaillés
const quizCSS = `
.question-wrapper {
    animation: slideInUp 0.3s ease-out;
}

.question-number {
    font-size: 0.9rem;
    color: var(--text-light);
    margin-bottom: 1rem;
}

.option {
    display: flex;
    align-items: center;
    gap: 1rem;
    transition: all var(--transition-fast);
    cursor: pointer;
}

.option-letter {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: var(--bg-tertiary);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    flex-shrink: 0;
}

.option.selected .option-letter {
    background: var(--primary-color);
    color: white;
}

.option.correct .option-letter {
    background: var(--success-color);
    color: white;
}

.option.incorrect .option-letter {
    background: var(--danger-color);
    color: white;
}

.result-item {
    margin-bottom: 2rem;
    padding: 1rem;
    border-radius: var(--radius-md);
    border: 1px solid var(--bg-tertiary);
}

.result-item.correct {
    border-color: var(--success-color);
    background: rgba(16, 185, 129, 0.05);
}

.result-item.incorrect {
    border-color: var(--danger-color);
    background: rgba(239, 68, 68, 0.05);
}

.result-question {
    margin-bottom: 0.5rem;
}

.user-answer {
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.correct-answer {
    color: var(--success-color);
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.explanation {
    font-style: italic;
    color: var(--text-secondary);
    padding: 0.5rem;
    background: var(--bg-secondary);
    border-radius: var(--radius-sm);
}

.quiz-error {
    text-align: center;
    padding: 2rem;
}

.error-content {
    background: var(--bg-secondary);
    border-radius: var(--radius-lg);
    padding: 2rem;
    border: 1px solid var(--danger-color);
}

.error-btn {
    background: var(--danger-color);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: var(--radius-md);
    cursor: pointer;
    margin-top: 1rem;
}

.score-message.excellent { color: var(--success-color); }
.score-message.good { color: var(--primary-color); }
.score-message.average { color: var(--warning-color); }
.score-message.needs-work { color: var(--danger-color); }

@media (max-width: 768px) {
    .option {
        flex-direction: column;
        text-align: center;
        gap: 0.5rem;
    }
    
    .result-item {
        padding: 0.75rem;
    }
}
`;

// Ajouter le CSS
const quizStyle = document.createElement('style');
quizStyle.textContent = quizCSS;
document.head.appendChild(quizStyle);

// Instance globale
const Quiz = new QuizManager();

// Export pour usage externe
window.Quiz = Quiz;