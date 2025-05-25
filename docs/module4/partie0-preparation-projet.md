
# Préparation au Projet Final

![Préparation au projet](../images/banner-preparation-projet.svg)

## Objectifs de la phase de préparation

Cette phase vous permettra de :
- Comprendre en détail les spécifications du projet de chatbot pédagogique
- Analyser des exemples concrets d'utilisation de chatbots similaires
- Explorer l'API Mistral AI en profondeur
- Planifier et organiser votre travail pour le développement

## 1. Analyse du cahier des charges (15 min)

Le cahier des charges de votre chatbot pédagogique a été présenté en détail dans le document [Projet Chatbot Pédagogique](projet-chatbot.md). Prenez le temps de le lire attentivement et de vous poser les questions suivantes :

1. **Quelles fonctionnalités sont essentielles** et lesquelles sont optionnelles ?
2. **Quels concepts du Deep Learning** devront impérativement être couverts dans la base de connaissances ?
3. **Quels sont les points techniques** qui pourraient poser problème ?
4. **Comment adapter le niveau des explications** aux différents utilisateurs ?
5. **Quelles fonctionnalités pédagogiques** apporteraient une réelle valeur ajoutée ?

### Exercice de priorisation

Établissez une liste des fonctionnalités à développer classées par ordre de priorité :

1. Fonctionnalités de base (MVP - Produit Minimum Viable)
2. Fonctionnalités importantes 
3. Fonctionnalités optionnelles (si le temps le permet)

## 2. Étude de cas d'entreprises utilisant des chatbots (15 min)

Avant de commencer le développement, examinons quelques exemples concrets d'entreprises qui ont mis en place des chatbots similaires à celui que vous allez développer.

### Cas 1: Chatbot pédagogique pour une école de programmation

**Entreprise**: CodeSchool (30 formateurs, 500+ étudiants)

**Problématique**: Les formateurs recevaient de nombreuses questions basiques identiques, ce qui limitait leur disponibilité pour des problèmes plus complexes.

**Solution**: Développement d'un chatbot assistant basé sur une API de LLM, avec une base de connaissances construite à partir du matériel de cours.

**Architecture**:
- Frontend: Interface web intégrée à la plateforme d'apprentissage
- Backend: API Flask avec mise en cache Redis
- LLM: OpenAI API avec fine-tuning spécifique aux cours
- Base de connaissances: Structurée en JSON par modules de cours

**Résultats**:
- Réduction de 40% des questions basiques aux formateurs
- Satisfaction des étudiants à 85% concernant les réponses du chatbot
- ROI positif après 4 mois d'utilisation
- Création de 15 nouveaux modules de cours grâce au temps libéré

**Leçons apprises**:
- Importance d'un système de feedback immédiat sur les réponses
- Nécessité de maintenir la base de connaissances à jour
- Valeur des réponses comportant des exemples de code fonctionnels

### Cas 2: Assistant virtuel pour la formation interne

**Entreprise**: TechConsult (cabinet de conseil IT, 120 employés)

**Problématique**: Difficulté à former rapidement les nouveaux consultants sur les technologies spécifiques utilisées par l'entreprise.

**Solution**: Chatbot de formation accessible 24/7, intégré à l'intranet, avec connaissance des processus et technologies internes.

**Architecture**:
- Interface: Application web responsive
- Backend: NodeJS avec FastAPI
- LLM: Combinaison d'API locale et Mistral AI
- Base de connaissances: Documents techniques convertis en embeddings vectoriels

**Résultats**:
- Réduction du temps d'onboarding de 3 semaines à 10 jours
- Augmentation de 25% du taux de réussite aux certifications internes
- Économie estimée de 180 heures de formation par an
- Adoption à 92% parmi les nouveaux employés

**Leçons apprises**:
- L'importance d'utiliser le vocabulaire spécifique de l'entreprise
- La valeur d'un historique de conversation persistant
- L'utilité des prompts techniques bien formulés

## 3. Exploration de l'API Mistral AI (20 min)

### Introduction à Mistral AI

Mistral AI est une entreprise française qui développe des modèles de langage de pointe, particulièrement adaptés pour des usages en français et dans un contexte éducatif. Son API permet d'accéder à ces modèles pour générer du texte, répondre à des questions, et plus encore.

### Création d'un compte et clé API

1. Rendez-vous sur [console.mistral.ai](https://console.mistral.ai/)
2. Créez un compte (gratuit)
3. Une fois connecté, cliquez sur "API Keys" dans le menu
4. Cliquez sur "Create API Key", donnez-lui un nom (ex: "Projet Chatbot BTS")
5. **Important**: Copiez et sauvegardez la clé générée, elle ne sera plus affichée ensuite

### Premier test avec l'API

Commençons par un exemple simple pour tester l'API:

```python
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Configuration de l'API
api_key = "votre_clé_api_ici"  # Remplacez par votre clé
client = MistralClient(api_key=api_key)

# Messages
messages = [
    ChatMessage(role="system", content="Tu es un assistant pédagogique spécialisé dans l'explication du Deep Learning pour des étudiants de BTS SIO."),
    ChatMessage(role="user", content="Peux-tu m'expliquer simplement ce qu'est un réseau de neurones convolutif?")
]

# Appel à l'API
chat_response = client.chat(
    model="mistral-tiny",  # Modèle le plus léger
    messages=messages,
)

# Affichage de la réponse
print(chat_response.choices[0].message.content)
```

### Structure de l'API Mistral

L'API Mistral AI fonctionne avec une structure simple :

1. **Messages** : Liste de messages représentant une conversation, chacun avec un rôle (system, user, assistant)
2. **Modèle** : Choix du modèle Mistral à utiliser (mistral-tiny, mistral-small, mistral-medium...)
3. **Paramètres** : Configuration du comportement (température, nombre max de tokens, etc.)

### Gestion du contexte conversationnel

Pour maintenir un contexte de conversation, il suffit d'ajouter les messages précédents à chaque requête :

```python
# Fonction pour gérer une conversation
def chat_with_context(messages, user_input):
    # Ajouter le message de l'utilisateur
    messages.append(ChatMessage(role="user", content=user_input))
    
    # Appel à l'API
    response = client.chat(
        model="mistral-tiny",
        messages=messages,
    )
    
    # Récupérer la réponse
    assistant_message = response.choices[0].message.content
    
    # Ajouter la réponse au contexte
    messages.append(ChatMessage(role="assistant", content=assistant_message))
    
    return assistant_message, messages

# Initialiser la conversation
conversation = [
    ChatMessage(role="system", content="Tu es un assistant pédagogique spécialisé dans l'explication du Deep Learning pour des étudiants de BTS SIO.")
]

# Premier échange
response, conversation = chat_with_context(conversation, "Qu'est-ce qu'un réseau de neurones?")
print("Assistant:", response)

# Deuxième échange (avec le contexte précédent)
response, conversation = chat_with_context(conversation, "Comment fonctionne l'apprentissage?")
print("Assistant:", response)
```

### Optimisation des prompts

La qualité des réponses dépend beaucoup de la façon dont vous formulez vos instructions (prompts). Voici quelques conseils pour les optimiser :

#### 1. Instructions système claires et détaillées

```python
system_prompt = """
Tu es un assistant pédagogique spécialisé dans le Deep Learning pour des étudiants de BTS SIO. 
Quand tu réponds:
1. Utilise un langage simple et accessible
2. Fournis toujours un exemple concret
3. Structure tes explications en plusieurs points
4. Si tu n'es pas sûr d'une information, indique-le clairement
5. Adapte le niveau technique au profil de l'étudiant (débutant, intermédiaire, avancé)
"""
```

#### 2. Enrichissement avec la base de connaissances

```python
def enrich_prompt_with_knowledge(user_query, knowledge_base, user_level="débutant"):
    # Rechercher des informations pertinentes dans la base de connaissances
    relevant_info = search_knowledge_base(user_query, knowledge_base)
    
    # Enrichir le prompt avec ces informations
    enriched_prompt = f"""
Question de l'utilisateur: {user_query}

Informations pertinentes (niveau: {user_level}):
{relevant_info}

Réponds de manière pédagogique en utilisant ces informations et en adaptant ton explication au niveau {user_level}.
"""
    return enriched_prompt
```

#### 3. Paramétrage adapté

```python
# Pour des explications techniques (plus précises, moins créatives)
technical_params = {
    "temperature": 0.3,  # Faible température pour des réponses plus déterministes
    "max_tokens": 500    # Limite de longueur raisonnable
}

# Pour des exemples et analogies (plus créatifs)
creative_params = {
    "temperature": 0.7,  # Température plus élevée pour plus de créativité
    "max_tokens": 300    # Limite de longueur adaptée
}

# Fonction de choix de paramètres selon le contexte
def get_params_for_query(query):
    if "explique" in query.lower() or "définition" in query.lower():
        return technical_params
    elif "exemple" in query.lower() or "analogie" in query.lower():
        return creative_params
    else:
        return {"temperature": 0.5, "max_tokens": 400}  # Paramètres par défaut
```

## 4. Planification et organisation (10 min)

### Structure recommandée du projet

```
chatbot-pedagogique/
├── app.py                   # Application principale Flask/FastAPI
├── config.py                # Configuration (clés API, paramètres)
├── templates/               # Templates HTML
│   └── index.html           # Interface web
├── static/                  # Fichiers statiques (CSS, JS)
├── services/                # Services métier
│   ├── mistral_service.py   # Intégration API Mistral
│   └── knowledge_service.py # Gestion base de connaissances
└── knowledge_base/          # Base de connaissances
    └── concepts.json        # Structure des concepts DL
```

### Répartition des tâches

Si vous travaillez en binôme, une répartition efficace des tâches pourrait être :

**Option 1: Répartition par couche**
- **Membre 1:** Backend (Python, API Mistral, logique métier)
- **Membre 2:** Frontend (HTML/CSS/JS, interface, expérience utilisateur)

**Option 2: Répartition par fonctionnalité**
- **Membre 1:** Interface conversationnelle + intégration API
- **Membre 2:** Base de connaissances + fonctionnalités pédagogiques

### Planning recommandé

Pour le développement proprement dit (Séance 4), voici un planning suggéré :

| Temps | Tâche | Objectif |
|-------|-------|----------|
| 0h00-0h30 | Mise en place de l'environnement | Structure du projet, installation des dépendances |
| 0h30-1h15 | Développement du MVP | Interface de base, intégration API simple |
| 1h15-2h00 | Base de connaissances | Structuration et intégration |
| 2h00-2h30 | Fonctionnalités pédagogiques | Quiz, adaptation au niveau |
| 2h30-3h00 | Tests et corrections | Validation fonctionnelle |
| 3h00-3h30 | Documentation et préparation | Documentation technique et présentation |
| 3h30-4h00 | Présentations | Démonstration du chatbot |

## 5. Exemple de base de connaissances

Voici un exemple simplifié de structure pour votre base de connaissances :

```json
{
  "concepts": [
    {
      "id": "neural_network",
      "title": "Réseau de neurones",
      "description": "Modèle de calcul inspiré du fonctionnement des neurones biologiques.",
      "levels": {
        "beginner": "Un réseau de neurones est comme un ensemble de filtres interconnectés qui apprennent à reconnaître des motifs dans les données, un peu comme votre cerveau apprend à reconnaître des visages ou des objets.",
        "intermediate": "Système composé de neurones artificiels organisés en couches qui transforment des entrées en sorties à travers des poids et des fonctions d'activation, permettant d'approximer des fonctions complexes par apprentissage.",
        "advanced": "Structure mathématique composée d'unités de calcul interconnectées qui effectuent des transformations non-linéaires successives sur les données d'entrée, optimisées par rétropropagation du gradient pour minimiser une fonction de coût."
      },
      "examples": [
        "Reconnaissance d'images: un réseau peut apprendre à identifier des chats dans des photos",
        "Traduction automatique: des réseaux traduisent du texte d'une langue à une autre"
      ],
      "analogies": [
        "Un réseau de neurones ressemble à une chaîne de traitement dans une usine, où chaque station (neurone) effectue une opération spécifique sur le produit qui passe.",
        "Comme un orchestre où chaque musicien (neurone) joue une petite partie, et ensemble ils créent une symphonie complexe (prédiction)."
      ],
      "related_concepts": ["perceptron", "deep_learning", "activation_function"]
    }
  ]
}
```

## 6. Conclusion et préparation

Pour vous préparer efficacement au développement du chatbot lors de la prochaine séance :

1. **Créez votre compte Mistral AI** et obtenez votre clé API
2. **Testez l'API** avec quelques prompts simples pour vous familiariser
3. **Réfléchissez à la structure** de votre base de connaissances
4. **Organisez votre travail** en équipe si applicable
5. **Préparez des questions** sur les aspects techniques que vous ne maîtrisez pas encore complètement

Cette phase de préparation est essentielle pour garantir un développement efficace lors de la séance finale. En anticipant les défis et en planifiant votre approche, vous maximiserez vos chances de créer un chatbot pédagogique fonctionnel et de qualité.

[Retour à l'aperçu du module](index.md){ .md-button }
[Commencer le développement](partie1-developpement.md){ .md-button .md-button--primary }



