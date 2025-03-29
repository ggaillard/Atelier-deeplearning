# Phase 1 : Développement du chatbot (2h30)

![Développement du chatbot](https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectif

Implémenter les fonctionnalités principales de votre chatbot pédagogique en vous basant sur votre document de conception et en intégrant les connaissances acquises lors des séances précédentes.

## Fonctionnalités à implémenter

### 1. Interface conversationnelle (30 min)

L'interface du chatbot doit être simple mais fonctionnelle. Elle comprendra :

- Une zone d'affichage des messages
- Un champ de saisie pour les questions
- Un bouton d'envoi
- Une indication de chargement pendant le traitement
- Un système d'historique de conversation

**Modèle de code pour l'interface web**
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot pédagogique - Deep Learning</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>Chatbot Deep Learning</h1>
        </div>
        <div class="chat-messages" id="chat-messages">
            <!-- Les messages s'afficheront ici -->
            <div class="message bot">
                <div class="message-content">
                    Bonjour ! Je suis un chatbot spécialisé dans le Deep Learning. 
                    Comment puis-je vous aider aujourd'hui ?
                </div>
            </div>
        </div>
        <div class="chat-input">
            <input type="text" id="user-input" placeholder="Posez votre question ici...">
            <button id="send-button">Envoyer</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

**Points clés à respecter :**
 - Design responsive s'adaptant aux différentes tailles d'écran
 - Indication claire des messages utilisateur vs assistant
 - Gestion des erreurs (réseau, API, etc.)

### 2. Intégration avancée avec l'API Mistral AI (45 min)

L'objectif est d'exploiter efficacement l'API Mistral AI pour générer des réponses pertinentes et contextualisées.

**Structure d'intégration recommandée :**

```python
import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Chargement des variables d'environnement
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialisation du client
client = MistralClient(api_key=api_key)

# Système de gestion de contexte
class ConversationManager:
    def __init__(self, system_prompt):
        self.history = [
            ChatMessage(role="system", content=system_prompt)
        ]
    
    def add_user_message(self, message):
        self.history.append(ChatMessage(role="user", content=message))
        
    def add_assistant_message(self, message):
        self.history.append(ChatMessage(role="assistant", content=message))
    
    def get_response(self, model="mistral-medium", temperature=0.7):
        response = client.chat(
            model=model,
            messages=self.history,
            temperature=temperature
        )
        content = response.choices[0].message.content
        self.add_assistant_message(content)
        return content
    
    def get_history(self):
        # Exclure le message système pour l'affichage
        return self.history[1:]

# Exemple d'utilisation
system_prompt = """
Tu es un assistant pédagogique spécialisé dans le Deep Learning, conçu pour aider 
les étudiants de BTS SIO. Tu expliques les concepts de manière claire et progressive, 
en adaptant ton niveau de technicité au niveau de l'étudiant. Utilise des analogies 
et des exemples concrets quand c'est pertinent.
"""

conversation = ConversationManager(system_prompt)
```

**Aspects avancés à implémenter :**

 - **Prompt engineering** : Amélioration des instructions système pour obtenir des réponses optimales
 - **Gestion de contexte** : Préservation de l'historique pour maintenir la cohérence des conversations
 - **Paramètres ajustables** : Contrôle de la température pour moduler la créativité des réponses
 - **Contrôle de longueur** : Limiter la longueur des réponses pour des explications concises

### 3. Structuration de la base de connaissances (45 min)

La base de connaissances est le cœur de votre chatbot. Elle doit être structurée de manière logique et couvrir les concepts essentiels du Deep Learning, correspondant au programme que vous avez suivi.

**Structure recommandée (format JSON) :**

```json
{
  "topics": [
    {
      "id": "intro_dl",
      "title": "Introduction au Deep Learning",
      "subtopics": [
        {
          "id": "diff_ml_dl",
          "title": "Différence entre Machine Learning et Deep Learning",
          "content": "Le Machine Learning classique nécessite une extraction manuelle des caractéristiques (feature engineering) tandis que le Deep Learning les extrait automatiquement grâce à ses multiples couches...",
          "examples": [
            "Dans la reconnaissance d'images, le ML classique nécessite d'extraire manuellement des caractéristiques comme les contours, les textures, alors que le DL apprend directement ces caractéristiques.",
            "Pour la classification de texte, le ML classique utilise des approches comme TF-IDF ou Bag-of-Words, alors que le DL utilise des embeddings et des architectures comme LSTM."
          ],
          "related": ["neural_networks", "applications_dl"]
        },
        // Autres sous-topics...
      ]
    },
    // Autres topics principaux...
  ]
}
```

**Éléments à inclure :**
     - Concepts fondamentaux du Deep Learning
     - Types de réseaux (CNN, RNN, etc.)
     - Techniques d'entraînement et d'optimisation
     - Applications pratiques
     - Exemples de code simplifiés
     - Analogies pour faciliter la compréhension

La base de connaissances peut être utilisée pour enrichir les prompts envoyés à l'API ou pour offrir des réponses prédéfinies à certaines questions.

### 4. Fonctionnalités d'aide à l'apprentissage (30 min)

Pour rendre votre chatbot véritablement pédagogique, implémentez au moins deux des fonctionnalités suivantes :

1. **Génération de quiz** : Créer des QCM pour tester les connaissances de l'utilisateur
   ```python
   def generate_quiz(topic):
       # Exemple de structure
       questions = {
           "intro_dl": [
               {
                   "question": "Quelle est la principale différence entre Machine Learning classique et Deep Learning ?",
                   "options": [
                       "Le Deep Learning est toujours plus rapide",
                       "Le Deep Learning extrait automatiquement les caractéristiques pertinentes",
                       "Le Deep Learning utilise exclusivement des GPUs",
                       "Le Deep Learning nécessite moins de données"
                   ],
                   "correct": 1,
                   "explanation": "Le Deep Learning se distingue par sa capacité à extraire automatiquement des caractéristiques pertinentes grâce à ses multiples couches, éliminant le besoin d'extraction manuelle (feature engineering)."
               },
               # Autres questions...
           ]
       }
       return questions.get(topic, [])
   ```

2. **Système de progression** : Suivre le niveau de l'utilisateur et adapter le contenu
   ```python
   class LearnerProfile:
       def __init__(self, user_id):
           self.user_id = user_id
           self.topics_seen = set()
           self.quiz_scores = {}
           self.current_level = "beginner"  # beginner, intermediate, advanced
       
       def update_after_interaction(self, topic, subtopic):
           self.topics_seen.add(f"{topic}:{subtopic}")
           # Mise à jour du niveau selon le nombre de topics vus
           if len(self.topics_seen) > 10:
               self.current_level = "intermediate"
           if len(self.topics_seen) > 20:
               self.current_level = "advanced"
       
       def record_quiz_result(self, topic, score):
           self.quiz_scores[topic] = score
   ```

3. **Visualisations adaptatives** : Générer des schémas explicatifs selon le niveau
   ```python
   def get_visualization(concept, level):
       visualizations = {
           "neural_network": {
               "beginner": "simple_nn.svg",
               "intermediate": "detailed_nn.svg",
               "advanced": "complex_nn.svg"
           },
           # Autres concepts...
       }
       return visualizations.get(concept, {}).get(level, "default.svg")
   ```

4. **Suivi des mots-clés** : Assistant remontant les définitions des termes techniques
   ```python
   def extract_technical_terms(message):
       technical_terms = [
           "neurone", "couche", "poids", "biais", "fonction d'activation",
           "rétropropagation", "descente de gradient", "CNN", "RNN", "LSTM"
       ]
       found_terms = []
       for term in technical_terms:
           if term.lower() in message.lower():
               found_terms.append(term)
       return found_terms
   ```

## Travail d'équipe et répartition des tâches

Si vous travaillez en binôme, répartissez-vous les tâches efficacement :

**Suggestion de répartition :**
       - **Membre 1 :** Interface + Intégration API
       - **Membre 2 :** Base de connaissances + Fonctionnalités pédagogiques

Ou alternativement :
       - **Membre 1 :** Backend (API, logique, base de connaissances)
       - **Membre 2 :** Frontend (interface, interactions, expérience utilisateur)

## Points de vigilance

 - **Sécurité :** Ne stockez jamais votre clé API directement dans le code
 - **Réactivité :** Optimisez les temps de réponse, ajoutez des indicateurs de chargement
 - **Robustesse :** Gérez les erreurs (API indisponible, limite de requêtes atteinte, etc.)
 - **Qualité des réponses :** Testez régulièrement avec des questions variées pour vérifier la pertinence

## Livrables intermédiaires

À la fin de cette phase, vous devriez avoir :

- Une interface conversationnelle fonctionnelle
- Un système d'intégration avec l'API Mistral AI
- Une base de connaissances structurée
- Au moins deux fonctionnalités pédagogiques implémentées

[Retour à la vue d'ensemble](index.md){ .md-button }
[Continuer vers la Phase 2: Finalisation et tests](partie2-finalisation.md){ .md-button .md-button--primary }