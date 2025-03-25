Je vais compléter la partie 2 du mini-projet RNN pour le traitement du langage.

# Phase 2 : Mini-projet RNN pour le traitement du langage

![RNN Architecture](https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la phase

Dans cette phase, vous allez :

- Comprendre les principes des réseaux récurrents (RNN) et de leurs variantes (LSTM, GRU)
- Implémenter un modèle LSTM pour l'analyse de sentiment
- Visualiser et interpréter le fonctionnement interne d'un RNN
- Expérimenter avec l'API Mistral AI pour la génération de texte
- Établir les bases pour le projet de chatbot pédagogique

## Partie 1: Principes des RNN (20 min)

### Architecture et fonctionnement des RNN

Les réseaux de neurones récurrents (RNN) sont spécialement conçus pour traiter des données séquentielles, comme du texte, des séries temporelles ou des signaux audio. Leur architecture inclut des connections récurrentes qui leur permettent de "mémoriser" les informations précédentes :

1. **Principe de base** : contrairement aux réseaux feed-forward, les RNN possèdent des boucles de rétroaction
2. **Mémoire à court terme** : chaque état caché dépend de l'état précédent et de l'entrée actuelle
3. **Problème de la disparition du gradient** : difficulté à capturer les dépendances à long terme
4. **Architectures avancées** : LSTM (Long Short-Term Memory) et GRU (Gated Recurrent Unit) qui résolvent ce problème

Avantages pour un développeur d'applications :

- Traitement de séquences de longueur variable
- Capacité à "mémoriser" des informations importantes
- Applications diverses : analyse de texte, traduction, génération de contenu

## Partie 2: Implémentation d'un LSTM pour l'analyse de sentiment (40 min)

### Instructions

1. Ouvrez le notebook Jupyter [rnn-sequence.ipynb](../ressources/notebooks/rnn-sequence.ipynb) dans Google Colab
2. Suivez les instructions étape par étape pour implémenter un modèle LSTM pour l'analyse de sentiment
3. Exécutez chaque cellule et observez les résultats
4. Portez une attention particulière aux sections suivantes :
   - Prétraitement du texte (tokenisation)
   - Architecture du modèle LSTM
   - Visualisation des embeddings de mots
   - Analyse des performances et des erreurs

### Points clés à explorer

- Comment le texte est-il transformé en entrées numériques pour le réseau ?
- Comment les cellules LSTM gèrent-elles l'information à long terme ?
- Quelle est la différence entre les embeddings de mots positifs et négatifs ?
- Comment le modèle LSTM peut-il comprendre le contexte d'une phrase ?
- Quelles sont les limitations de cette approche pour l'analyse de sentiment ?
- Comment pourriez-vous améliorer ce modèle pour des tâches plus complexes ?

## Partie 3: Intégration avec l'API Mistral AI (30 min)

### Introduction à Mistral AI

Mistral AI est une plateforme avancée d'intelligence artificielle spécialisée dans le traitement du langage naturel (NLP). Contrairement à nos modèles LSTM simples, Mistral utilise des architectures de type transformer, beaucoup plus puissantes pour comprendre et générer du texte.

Avantages de l'API Mistral AI:
- Modèles pré-entraînés sur d'immenses corpus de texte
- Compréhension contextuelle profonde
- Capacités multilingues
- Flexibilité pour différents cas d'usage NLP

### Instructions

1. Ouvrez le script [mistral-integration.py](../ressources/code/mistral-integration.py)
2. Examinez comment l'API Mistral AI est intégrée pour améliorer les capacités de traitement du langage
3. Vous aurez besoin d'une clé API (une clé de démonstration sera fournie pendant la séance)
4. Pour exécuter le script:

```bash
# Installer les dépendances
pip install requests pandas matplotlib 

# Configurer votre clé API (sur Windows)
set MISTRAL_API_KEY=votre_clé_api_ici

# Exécuter le script
python mistral-integration.py
```

### Structure du script Mistral AI

Le script est organisé en plusieurs sections:

```python
# Structure du script mistral-integration.py

# 1. Configuration et imports
import requests
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# 2. Configuration de l'API
API_KEY = os.environ.get("MISTRAL_API_KEY")
API_URL = "https://api.mistral.ai/v1/chat/completions"

# 3. Fonction pour envoyer des requêtes à l'API
def query_mistral(prompt, system_message=None, temperature=0.7, max_tokens=256):
    """
    Envoie une requête à l'API Mistral et retourne la réponse.
    
    Args:
        prompt (str): Le message utilisateur
        system_message (str): Instructions système pour guider le modèle
        temperature (float): Contrôle la créativité (0.0-1.0)
        max_tokens (int): Limite de tokens pour la réponse
        
    Returns:
        str: Réponse du modèle
    """
    # Construction des messages
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})
    
    # Configuration de la requête
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistral-small",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    # Envoi de la requête
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Erreur lors de la requête à l'API: {e}")
        return None

# 4. Démonstrations d'applications
# 4.1 Analyse de sentiment avancée
def analyze_sentiment_mistral(text):
    """Analyse le sentiment d'un texte avec Mistral AI"""
    system_message = """
    Vous êtes un expert en analyse de sentiment.
    Analysez le sentiment du texte fourni et répondez uniquement par:
    POSITIF, NÉGATIF ou NEUTRE, suivi d'un score de -1.0 à 1.0 entre parenthèses.
    Exemple: POSITIF (0.8) ou NÉGATIF (-0.5)
    """
    prompt = f"Analysez le sentiment du texte suivant: '{text}'"
    return query_mistral(prompt, system_message, temperature=0.3)

# 4.2 Génération de texte contrôlée
def generate_continuation(text, style="informatif"):
    """Génère une continuation de texte dans un style spécifié"""
    style_instructions = {
        "informatif": "Continuez ce texte dans un style informatif et factuel.",
        "persuasif": "Continuez ce texte dans un style persuasif et convaincant.",
        "narratif": "Continuez ce texte dans un style narratif engageant."
    }
    
    system_message = f"""
    Vous êtes un expert en rédaction et génération de texte.
    {style_instructions.get(style, style_instructions['informatif'])}
    """
    
    prompt = f"Voici le début d'un texte. Continuez-le de manière cohérente:\n\n{text}"
    return query_mistral(prompt, system_message, temperature=0.7, max_tokens=150)

# 4.3 Question-réponse contextuelle
def answer_question(context, question):
    """Répond à une question basée sur un contexte donné"""
    system_message = """
    Vous êtes un assistant spécialisé en compréhension de texte et question-réponse.
    Répondez à la question uniquement à partir des informations fournies dans le contexte.
    Si la réponse n'est pas dans le contexte, répondez "Je ne peux pas répondre à cette question d'après le contexte fourni."
    """
    
    prompt = f"""
    Contexte: {context}
    
    Question: {question}
    """
    
    return query_mistral(prompt, system_message, temperature=0.3)

# 5. Démonstration interactive
def run_demos():
    print("=== Démonstration d'intégration de Mistral AI ===\n")
    
    # Test d'analyse de sentiment
    print("1. Analyse de sentiment avancée")
    sample_texts = [
        "J'ai adoré ce film, c'était vraiment captivant !",
        "Le service était médiocre et la nourriture froide.",
        "Cette application semble intéressante mais manque de fonctionnalités."
    ]
    
    results = []
    for text in sample_texts:
        sentiment = analyze_sentiment_mistral(text)
        print(f"Texte: '{text}'")
        print(f"Sentiment: {sentiment}\n")
        
        # Extraction du score pour visualisation
        if sentiment:
            score_str = sentiment.split('(')[1].split(')')[0]
            try:
                score = float(score_str)
                results.append({"text": text, "score": score})
            except:
                pass
    
    # Visualisation des scores de sentiment
    if results:
        df = pd.DataFrame(results)
        plt.figure(figsize=(10, 6))
        bars = plt.barh(df['text'], df['score'], color=['green' if x > 0 else 'red' for x in df['score']])
        plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        plt.xlim(-1, 1)
        plt.xlabel('Score de sentiment')
        plt.title('Analyse de sentiment avec Mistral AI')
        plt.tight_layout()
        plt.savefig('sentiment_analysis.png')
        print("Visualisation sauvegardée dans 'sentiment_analysis.png'\n")
    
    # Test de génération de texte
    print("2. Génération de texte contrôlée")
    sample_text = "L'intelligence artificielle transforme notre manière de travailler."
    for style in ["informatif", "persuasif", "narratif"]:
        continuation = generate_continuation(sample_text, style)
        print(f"Style: {style}")
        print(f"Texte initial: {sample_text}")
        print(f"Continuation: {continuation}\n")
    
    # Test de Q&A contextuel
    print("3. Question-réponse contextuelle")
    context = """
    Les réseaux de neurones récurrents (RNN) sont une classe de réseaux de neurones artificiels
    où les connexions entre les nœuds forment un graphe orienté le long d'une séquence temporelle.
    Contrairement aux réseaux de neurones à propagation avant, les RNN peuvent utiliser leur état interne
    (mémoire) pour traiter des séquences d'entrées, ce qui les rend applicables à des tâches
    comme la reconnaissance vocale ou la traduction automatique.
    
    Les LSTM (Long Short-Term Memory) sont une architecture spéciale de RNN capable d'apprendre
    les dépendances à long terme. Les LSTM ont été conçus pour résoudre le problème de la disparition
    du gradient qui peut être rencontré lors de l'entraînement des RNN traditionnels.
    """
    
    questions = [
        "Quelle est la principale différence entre les RNN et les réseaux à propagation avant?",
        "Pourquoi les LSTM ont-ils été développés?",
        "Qui a inventé les réseaux de neurones récurrents?"
    ]
    
    for question in questions:
        answer = answer_question(context, question)
        print(f"Question: {question}")
        print(f"Réponse: {answer}\n")

# 6. Point d'entrée principal
if __name__ == "__main__":
    if not API_KEY:
        print("Erreur: Clé API Mistral non configurée. Utilisez 'set MISTRAL_API_KEY=votre_clé' (Windows) ou 'export MISTRAL_API_KEY=votre_clé' (Linux/Mac)")
    else:
        run_demos()
```

### Exercices pratiques avec Mistral AI

1. Modifiez le script pour ajouter une fonction qui génère des explications pédagogiques sur les concepts du Deep Learning

2. Implémentez une fonction simple de dialogue qui permettrait à un utilisateur de poser des questions sur un sujet spécifique

3. Comparez les résultats d'analyse de sentiment entre votre modèle LSTM et Mistral AI:
   - Quelles sont les différences principales?
   - Dans quels cas Mistral AI semble-t-il plus performant?
   - Pourquoi les grands modèles de langage comme Mistral surpassent-ils les architectures LSTM simples?

## Partie 4: Comparaison et synthèse (20 min)

### Tableau comparatif CNN vs RNN

| Caractéristique | CNN | RNN/LSTM |
|-----------------|-----|----------|
| Type de données | Structurées spatialement (images) | Séquentielles (texte, séries temporelles) |
| Avantage principal | Extraction automatique de caractéristiques | Mémoire contextuelle |
| Architecture clé | Convolution + Pooling | Cellules récurrentes + portes |
| Applications | Vision par ordinateur, classification d'images | NLP, traduction, génération de texte |
| Défi principal | Invariance à la rotation/échelle | Dépendances à long terme |
| Interprétabilité | Visualisation des feature maps | États cachés et portes d'oubli |

### Discussion collective

En groupes de 3-4, discutez des questions suivantes et préparez une synthèse à partager:

1. Quelles sont les forces et faiblesses respectives des CNN et RNN?
2. Comment les deux types d'architectures pourraient-ils être combinés?
3. Quels défis spécifiques posent les données textuelles par rapport aux images?
4. Comment l'architecture Transformer (utilisée par Mistral) a-t-elle révolutionné le NLP?
5. Comment ces technologies pourraient-elles être intégrées dans notre projet de chatbot pédagogique?

## Ressources complémentaires

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Documentation de l'API Mistral AI](https://docs.mistral.ai/)

[Retour à la Séance 2](index.md){ .md-button }
[Continuer vers la Phase 3: Amélioration des modèles](partie3-amelioration.md){ .md-button .md-button--primary }