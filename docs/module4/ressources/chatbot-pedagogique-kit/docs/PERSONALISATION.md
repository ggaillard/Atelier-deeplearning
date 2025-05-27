# 🎨 Guide de Personnalisation du Chatbot Pédagogique

## Choix de Personnalisation

Pour personnaliser votre chatbot pédagogique, vous avez **3 choix principaux** selon votre niveau et vos intérêts :

- **🎨 Choix A - Thèmes Visuels** (Niveau Débutant)
- **📝 Choix B - Système de Quiz** (Niveau Intermédiaire)  
- **🧠 Choix C - Optimisation IA** (Niveau Avancé)

> **Note** : Vous pouvez combiner plusieurs choix, mais il est recommandé de se concentrer sur un seul pour maximiser la qualité dans le temps imparti.

---

## 🎨 Choix A : Thèmes Visuels

### 🎯 Objectif
Créer une expérience visuelle unique en personnalisant l'apparence et l'ergonomie du chatbot.

### 📋 Tâches à Réaliser (90 min)

#### 1. Création de Thèmes Personnalisés (30 min)

**Modifier `frontend/css/themes.css`**

```css
/* Votre thème personnalisé */
[data-theme="mon-theme"] {
    /* Couleurs principales */
    --primary-color: #your-color;
    --accent-color: #your-accent;
    --bg-primary: #your-background;
    
    /* Personnalisations spécifiques */
}

/* Effets spéciaux pour votre thème */
[data-theme="mon-theme"] .logo {
    animation: mon-animation 2s infinite;
}

@keyframes mon-animation {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
```

**Ajouter le thème dans `frontend/index.html`**
```html
<select id="theme-select">
    <option value="default">Défaut</option>
    <option value="dark">Sombre</option>
    <option value="education">Éducation</option>
    <option value="tech">Tech</option>
    <option value="mon-theme">Mon Thème</option> <!-- Votre thème -->
</select>
```

#### 2. Amélioration UX/UI (30 min)

**Animations et interactions**
```css
/* Animations de messages */
.message {
    animation: slideInSmooth 0.5s ease-out;
    transition: transform 0.2s ease;
}

.message:hover {
    transform: translateX(5px);
}

/* Effets de boutons */
.quick-action {
    position: relative;
    overflow: hidden;
}

.quick-action::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.quick-action:hover::before {
    left: 100%;
}
```

**Responsive Design**
```css
/* Optimisation mobile */
@media (max-width: 768px) {
    .chat-container {
        padding: 0.5rem;
    }
    
    .message-content {
        max-width: 85%;
    }
}

/* Optimisation tablette */
@media (min-width: 769px) and (max-width: 1024px) {
    .sidebar {
        width: 250px;
    }
}
```

#### 3. Branding Personnalisé (30 min)

**Logo et identité**
```html
<!-- Personnalisation du header -->
<div class="brand">
    <div class="logo">🤖</div> <!-- Changez l'emoji ou ajoutez une image -->
    <h1>MonBot Deep Learning</h1> <!-- Personnalisez le nom -->
    <span class="subtitle">Assistant IA de [Votre École]</span>
</div>
```

**Couleurs de votre établissement**
```css
[data-theme="school-theme"] {
    --primary-color: #your-school-primary;
    --secondary-color: #your-school-secondary;
    /* Couleurs officielles de votre établissement */
}
```

### 📊 Livrables Attendus

- [ ] **2+ thèmes fonctionnels** avec noms créatifs
- [ ] **Interface responsive** testée sur mobile/desktop
- [ ] **Animations fluides** qui améliorent l'expérience
- [ ] **Branding personnalisé** (couleurs, logos, noms)
- [ ] **Documentation** des choix de design dans le rapport

### 💡 Idées de Thèmes

1. **Thème Saisons** : Couleurs et animations saisonnières
2. **Thème Université** : Couleurs et style de votre établissement
3. **Thème Futuriste** : Effets néon et animations high-tech
4. **Thème Minimaliste** : Design épuré et élégant
5. **Thème Ludique** : Couleurs vives et animations amusantes

---

## 📝 Choix B : Système de Quiz

### 🎯 Objectif
Développer un système de quiz interactif et intelligent pour tester les connaissances des utilisateurs.

### 📋 Tâches à Réaliser (90 min)

#### 1. Interface de Quiz Interactive (30 min)

**Compléter `frontend/js/quiz.js`**

```javascript
class QuizManager {
    constructor() {
        this.init();
    }
    
    // Vos méthodes à implémenter
    async start(topic, difficulty) {
        // Génération du quiz
        const quiz = await this.generateQuiz(topic, difficulty);
        this.displayQuiz(quiz);
    }
    
    displayQuestion(question, index) {
        // Affichage d'une question avec options
        const questionHTML = `
            <div class="question-container">
                <h3>${question.question}</h3>
                <div class="options">
                    ${question.options.map((option, i) => 
                        `<button class="option" onclick="Quiz.selectOption(${i})">
                            ${option}
                        </button>`
                    ).join('')}
                </div>
            </div>
        `;
        document.getElementById('question-container').innerHTML = questionHTML;
    }
    
    calculateScore() {
        // Logique de calcul du score
    }
}
```

**Interface Quiz dans `frontend/index.html`**
```html
<!-- Modal Quiz -->
<div class="quiz-overlay" id="quiz-overlay">
    <div class="quiz-container">
        <div class="quiz-header">
            <h3>Quiz Deep Learning</h3>
            <button id="close-quiz">❌</button>
        </div>
        <div class="quiz-content">
            <div id="question-container"></div>
            <div class="quiz-progress">
                <div class="progress-bar">
                    <div class="progress-fill" id="quiz-progress"></div>
                </div>
                <span id="progress-text">Question 1 sur 5</span>
            </div>
        </div>
        <div class="quiz-results" id="quiz-results">
            <!-- Résultats détaillés -->
        </div>
    </div>
</div>
```

#### 2. Génération Intelligente de Quiz (30 min)

**Backend - Endpoint de génération**
```python
@app.route('/api/quiz/generate', methods=['POST'])
def generate_quiz():
    data = request.get_json()
    topic = data.get('topic', 'general')
    difficulty = data.get('difficulty', 'intermediate')
    count = data.get('count', 5)
    
    # Génération via base de connaissances
    quiz = knowledge_manager.generate_quiz(topic, difficulty, count)
    
    # Fallback avec Mistral si pas assez de questions
    if len(quiz['questions']) < count:
        additional_questions = generate_quiz_with_mistral(topic, difficulty, count - len(quiz['questions']))
        quiz['questions'].extend(additional_questions)
    
    return jsonify(quiz)
```

**Sélection adaptative des questions**
```python
def select_adaptive_questions(user_level, topics_seen, previous_scores):
    """
    Sélectionne des questions adaptées au profil de l'utilisateur
    """
    difficulty_weights = {
        'beginner': {'beginner': 0.7, 'intermediate': 0.3, 'advanced': 0.0},
        'intermediate': {'beginner': 0.2, 'intermediate': 0.6, 'advanced': 0.2},
        'advanced': {'beginner': 0.0, 'intermediate': 0.3, 'advanced': 0.7}
    }
    
    # Logique de sélection basée sur l'historique
    selected_questions = []
    # ... votre implémentation
    
    return selected_questions
```

#### 3. Système de Scoring et Feedback (30 min)

**Calcul de score avancé**
```javascript
calculateAdvancedScore(answers, questions, timeSpent) {
    let baseScore = 0;
    let timeBonus = 0;
    let difficultyBonus = 0;
    
    answers.forEach((answer, index) => {
        const question = questions[index];
        if (answer === question.correctAnswer) {
            baseScore += 100;
            
            // Bonus de temps (réponse rapide)
            const timeForQuestion = timeSpent[index];
            if (timeForQuestion < 10) timeBonus += 10;
            
            // Bonus de difficulté
            if (question.difficulty === 'advanced') difficultyBonus += 20;
            else if (question.difficulty === 'intermediate') difficultyBonus += 10;
        }
    });
    
    return {
        baseScore,
        timeBonus,
        difficultyBonus,
        totalScore: baseScore + timeBonus + difficultyBonus,
        percentage: Math.round((baseScore / (questions.length * 100)) * 100)
    };
}
```

**Feedback personnalisé**
```javascript
generatePersonalizedFeedback(score, userLevel, topic) {
    const feedbackTemplates = {
        excellent: [
            "🏆 Parfait ! Vous maîtrisez {topic} à la perfection !",
            "⭐ Impressionnant ! Vos connaissances en {topic} sont exceptionnelles !"
        ],
        good: [
            "👍 Très bien ! Vous avez une bonne compréhension de {topic}.",
            "🎯 Bon travail ! Continuez à explorer {topic}."
        ],
        needsWork: [
            "📚 Il y a encore des concepts à revoir en {topic}.",
            "💪 Ne vous découragez pas ! Continuez à apprendre {topic}."
        ]
    };
    
    let category = score >= 90 ? 'excellent' : score >= 70 ? 'good' : 'needsWork';
    let template = feedbackTemplates[category][Math.floor(Math.random() * feedbackTemplates[category].length)];
    
    return template.replace('{topic}', topic);
}
```

### 📊 Livrables Attendus

- [ ] **Interface quiz fonctionnelle** avec navigation fluide
- [ ] **Génération intelligente** de questions adaptées au niveau
- [ ] **Système de scoring** avec feedback personnalisé
- [ ] **Statistiques utilisateur** (progression, historique)
- [ ] **Minimum 3 quiz** sur différents concepts Deep Learning

### 🎯 Fonctionnalités Avancées (Bonus)

- **Quiz adaptatif** : Difficulté qui s'ajuste selon les réponses
- **Mode challenge** : Quiz chronométrés avec classements
- **Quiz collaboratif** : Défis entre étudiants
- **Analytics** : Statistiques détaillées des performances

---

## 🧠 Choix C : Optimisation IA

### 🎯 Objectif
Développer des fonctionnalités d'intelligence artificielle avancées pour améliorer la pertinence et l'adaptation des réponses.

### 📋 Tâches à Réaliser (90 min)

#### 1. Optimisation des Prompts Dynamiques (30 min)

**Compléter `backend/prompt_optimizer.py`**

```python
class AdvancedPromptOptimizer:
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.context_analyzer = ContextAnalyzer()
        self.response_adapter = ResponseAdapter()
    
    def optimize_prompt(self, user_message, context):
        # 1. Détection d'intention
        intent = self.detect_user_intent(user_message)
        
        # 2. Analyse du contexte
        context_type = self.analyze_conversation_context(context)
        
        # 3. Génération de prompt adaptatif
        optimized_prompt = self.generate_adaptive_prompt(
            message=user_message,
            intent=intent,
            context=context_type,
            user_profile=context.get('user_profile')
        )
        
        return optimized_prompt
    
    def detect_user_intent(self, message):
        """Détection d'intention avancée"""
        patterns = {
            'explanation': r'\b(explique|comment|pourquoi|qu\'est-ce)\b',
            'example': r'\b(exemple|montre|illustration)\b',
            'comparison': r'\b(différence|compare|vs|plutôt)\b',
            'troubleshooting': r'\b(problème|erreur|bug|aide)\b',
            'deep_dive': r'\b(détail|approfondir|plus|davantage)\b'
        }
        
        for intent, pattern in patterns.items():
            if re.search(pattern, message.lower()):
                return intent
        
        return 'general'
```

**Prompts contextuels intelligents**
```python
def generate_contextual_prompt(self, intent, user_level, conversation_history):
    """Génère des prompts en fonction du contexte conversationnel"""
    
    # Analyse de l'historique pour détecter les patterns
    recent_topics = self.extract_recent_topics(conversation_history)
    user_confusion_signals = self.detect_confusion_signals(conversation_history)
    learning_progression = self.assess_learning_progression(conversation_history)
    
    # Template de base adaptatif
    base_template = self.select_base_template(intent, user_level)
    
    # Enrichissement contextuel
    if user_confusion_signals:
        base_template += "\n\nL'utilisateur semble confus. Reprends avec une approche plus simple et plus d'exemples."
    
    if learning_progression == 'advanced':
        base_template += "\n\nL'utilisateur progresse bien. Tu peux introduire des concepts plus avancés."
    
    # Connexions avec les sujets récents
    if recent_topics:
        base_template += f"\n\nRelie ta réponse aux concepts déjà vus: {', '.join(recent_topics[-3:])}"
    
    return base_template
```

#### 2. Système d'Adaptation au Niveau (30 min)

**Détection automatique du niveau utilisateur**
```python
class UserLevelDetector:
    def __init__(self):
        self.vocabulary_analyzer = VocabularyAnalyzer()
        self.question_complexity_analyzer = ComplexityAnalyzer()
    
    def detect_user_level(self, user_messages):
        """Détecte automatiquement le niveau de l'utilisateur"""
        
        # Analyse du vocabulaire utilisé
        vocab_score = self.analyze_vocabulary_complexity(user_messages)
        
        # Analyse de la complexité des questions
        question_complexity = self.analyze_question_complexity(user_messages)
        
        # Analyse des concepts mentionnés
        concepts_mastery = self.assess_concept_mastery(user_messages)
        
        # Score composite
        level_score = (vocab_score * 0.3 + 
                      question_complexity * 0.4 + 
                      concepts_mastery * 0.3)
        
        if level_score < 0.3:
            return 'beginner'
        elif level_score < 0.7:
            return 'intermediate'
        else:
            return 'advanced'
    
    def analyze_vocabulary_complexity(self, messages):
        """Analyse la complexité du vocabulaire"""
        technical_terms = [
            'algorithme', 'optimisation', 'hyperparamètre',
            'gradient', 'backpropagation', 'convolution'
        ]
        
        total_words = 0
        technical_words = 0
        
        for message in messages:
            words = message.lower().split()
            total_words += len(words)
            technical_words += sum(1 for word in words if word in technical_terms)
        
        return technical_words / max(total_words, 1)
```

**Adaptation dynamique des réponses**
```python
def adapt_response_to_level(self, base_response, detected_level, user_history):
    """Adapte dynamiquement la réponse au niveau détecté"""
    
    if detected_level == 'beginner':
        # Simplification et ajout d'analogies
        adapted_response = self.simplify_response(base_response)
        adapted_response = self.add_analogies(adapted_response)
        
    elif detected_level == 'intermediate':
        # Équilibre théorie/pratique
        adapted_response = self.balance_theory_practice(base_response)
        adapted_response = self.add_practical_examples(adapted_response)
        
    elif detected_level == 'advanced':
        # Enrichissement technique
        adapted_response = self.add_technical_details(base_response)
        adapted_response = self.add_mathematical_formulations(adapted_response)
    
    return adapted_response
```

#### 3. Analyse Sémantique et Suggestions Intelligentes (30 min)

**Recherche sémantique avancée**
```python
class SemanticAnalyzer:
    def __init__(self):
        self.concept_embeddings = self.load_concept_embeddings()
        self.similarity_threshold = 0.7
    
    def find_related_concepts(self, user_query, context):
        """Trouve des concepts liés sémantiquement"""
        
        # Vectorisation de la requête
        query_embedding = self.vectorize_text(user_query)
        
        # Calcul de similarité avec tous les concepts
        similarities = {}
        for concept_id, embedding in self.concept_embeddings.items():
            similarity = self.cosine_similarity(query_embedding, embedding)
            if similarity > self.similarity_threshold:
                similarities[concept_id] = similarity
        
        # Tri par pertinence
        related_concepts = sorted(similarities.items(), 
                                key=lambda x: x[1], 
                                reverse=True)[:5]
        
        return [concept_id for concept_id, _ in related_concepts]
    
    def generate_smart_suggestions(self, current_response, user_level):
        """Génère des suggestions intelligentes de suivi"""
        
        # Extraction des concepts mentionnés
        mentioned_concepts = self.extract_concepts_from_response(current_response)
        
        suggestions = []
        
        for concept in mentioned_concepts:
            # Concepts liés
            related = self.find_related_concepts(concept, {})
            
            # Génération de questions selon le niveau
            if user_level == 'beginner':
                suggestions.append(f"Peux-tu me donner un exemple simple de {concept} ?")
            elif user_level == 'intermediate':
                suggestions.append(f"Comment {concept} s'utilise-t-il en pratique ?")
            else:
                suggestions.append(f"Quelles sont les optimisations possibles pour {concept} ?")
        
        return suggestions[:3]  # Max 3 suggestions
```

**Système de recommandations personnalisées**
```python
def generate_personalized_recommendations(self, user_profile, learning_history):
    """Génère des recommandations personnalisées d'apprentissage"""
    
    # Analyse des lacunes de connaissances
    knowledge_gaps = self.identify_knowledge_gaps(learning_history)
    
    # Concepts prérequis non maîtrisés
    prerequisites = self.find_missing_prerequisites(user_profile.concepts_seen)
    
    # Concepts de niveau supérieur accessibles
    next_level_concepts = self.find_accessible_advanced_concepts(user_profile)
    
    recommendations = {
        'review': prerequisites,
        'learn_next': next_level_concepts,
        'practice': knowledge_gaps
    }
    
    return recommendations
```

### 📊 Livrables Attendus

- [ ] **Prompts dynamiques** qui s'adaptent au contexte
- [ ] **Détection automatique du niveau** utilisateur
- [ ] **Recherche sémantique** dans la base de connaissances
- [ ] **Suggestions intelligentes** de questions de suivi
- [ ] **Système de recommandations** personnalisées

### 🔬 Fonctionnalités Avancées (Bonus)

- **Analyse des émotions** dans les messages utilisateur
- **Génération automatique de contenu** pédagogique
- **Système d'évaluation** de la qualité des réponses
- **Apprentissage continu** basé sur les interactions

---

## 🚀 Conseils de Réalisation

### ⏰ Gestion du Temps

1. **Planification (10 min)** : Choisissez votre option et planifiez les étapes
2. **Développement (70 min)** : Focus sur les fonctionnalités core
3. **Tests (10 min)** : Validation rapide du fonctionnement

### 🔧 Bonnes Pratiques

- **Commencez simple** : Implémentez d'abord les fonctionnalités de base
- **Testez régulièrement** : Vérifiez chaque fonctionnalité au fur et à mesure
- **Documentez vos choix** : Notez les décisions importantes pour le rapport
- **Gardez des traces** : Screenshots et exemples de votre travail

### 🆘 En Cas de Problème

1. **Problème technique** : Consultez la documentation et les exemples fournis
2. **Manque de temps** : Priorisez les fonctionnalités essentielles
3. **Bug bloquant** : Implémentez une version simplifiée qui fonctionne

### 📋 Checklist Finale

- [ ] Fonctionnalité principale développée et testée
- [ ] Code propre et commenté
- [ ] Interface utilisateur intuitive
- [ ] Documentation des choix techniques
- [ ] Préparation de la démonstration

**Bonne personnalisation ! 🎯**