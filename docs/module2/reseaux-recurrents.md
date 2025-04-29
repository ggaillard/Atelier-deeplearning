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

### Problématique : Pourquoi les RNN ?

Imaginons que vous surveillez des logs de sécurité :
- Un réseau classique ne verrait que des entrées isolées, sans comprendre leur séquence
- Un RNN, lui, se souvient des événements précédents pour détecter des patterns suspects

### Le RNN expliqué avec l'analogie du carnet de notes

**Analogie du carnet de notes** :
1. Vous analysez un rapport d'incident et prenez des notes importantes
2. À chaque nouvelle section du rapport, vous :
   - Lisez le nouveau contenu (nouvelle entrée)
   - Consultez vos notes précédentes (état caché / mémoire)
   - Mettez à jour vos notes avec les informations les plus pertinentes
   - Utilisez la combinaison de la nouvelle section et de vos notes pour comprendre l'incident

**Dans un RNN** :
1. Le réseau traite les données séquentiellement (log par log, événement par événement)
2. À chaque étape, il combine :
   - L'entrée actuelle (ex : le log actuel)
   - Son "état de mémoire" (ce qu'il a retenu des logs précédents)
3. Il produit :
   - Une sortie pour l'étape actuelle (ex: alerte ou non)
   - Un nouvel état de mémoire pour l'étape suivante
 - 
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

## Les LSTM (Long Short-Term Memory) en langage simple

### Solution au problème de mémoire

**Analogie du rapport de sécurité avec système de marquage** :
- Vous avez maintenant un système pour marquer les informations importantes dans votre rapport
- Vous pouvez décider explicitement quelles informations :
  * Méritent d'être conservées pour l'analyse finale
  * Doivent être mises à jour avec de nouvelles données
  * Sont pertinentes pour l'incident en cours

### Les portes (gates) expliquées simplement

Au lieu d'une explication mathématique complexe, voici le fonctionnement en langage simple :

1. **Porte d'oubli** (Forget gate) : 
   - Comme un tri dans votre rapport : "Quelles informations passées ne sont plus utiles ?"
   - Exemple SIO : Si un nouvel utilisateur se connecte, vous pouvez "oublier" certains détails des sessions précédentes

2. **Porte d'entrée** (Input gate) :
   - Filtre les nouvelles informations : "Quelles nouvelles informations sont importantes ?"
   - Exemple SIO : Dans un log "Tentative d'accès admin échouée 5 fois", le nombre de tentatives est plus important que l'heure exacte

3. **Porte de sortie** (Output gate) :
   - Décide quelles informations partager : "Quelles parties de ma mémoire sont pertinentes maintenant ?"
   - Exemple SIO : Si vous analysez une faille de sécurité, vous vous concentrez sur les logs d'authentification, pas sur les mises à jour système

### Applications pour les étudiants BTS SIO

Voici des applications concrètes des RNN/LSTM dans votre domaine :

1. **Détection d'intrusion réseau** :
   - Les RNN/LSTM analysent les séquences de logs pour détecter des comportements anormaux
   - L'ordre chronologique des événements est crucial (d'où l'intérêt des RNN)

2. **Prédiction de pannes systèmes** :
   - Les LSTM peuvent analyser les historiques de performance serveur
   - Ils détectent les signes précurseurs de problèmes potentiels

3. **Chatbots d'assistance technique** :
   - Les RNN/LSTM permettent de comprendre le contexte d'une conversation de support
   - Ils maintiennent la cohérence dans les réponses du chatbot d'aide

4. **Analyse de logs de sécurité** :
   - Les LSTM peuvent identifier des patterns d'attaque complexes s'étendant sur de longues périodes
   - Ils peuvent corréler des événements apparemment sans lien

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

Structure du script Mistral AI
Le script est organisé en plusieurs sections:

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
        print(f"Style: {style