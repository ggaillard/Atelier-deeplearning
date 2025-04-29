# Checklist de préparation pour le projet chatbot (4h)

Ce document contient les éléments à préparer **avant la séance** pour maximiser le temps productif lors du développement du chatbot pédagogique.

## 1. Compte et API Mistral

- [ ] Créer un compte sur [console.mistral.ai](https://console.mistral.ai/)
- [ ] Générer une clé API (Menu "API Keys" > "Create API Key")
- [ ] Noter la clé API dans un endroit sécurisé
- [ ] Tester la clé API avec un exemple simple (code fourni ci-dessous)

```python
# Script de test de l'API Mistral AI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Remplacez par votre clé API
api_key = "votre_clé_api_ici"

# Initialisation du client
client = MistralClient(api_key=api_key)

# Message test
messages = [
    ChatMessage(role="system", content="Vous êtes un assistant technique spécialisé en informatique."),
    ChatMessage(role="user", content="Expliquez-moi ce qu'est un réseau de neurones en une phrase simple.")
]

# Test de l'API
try:
    chat_response = client.chat(model="mistral-tiny", messages=messages)
    print("✅ API Mistral fonctionnelle!")
    print("Réponse:", chat_response.choices[0].message.content)
except Exception as e:
    print("❌ Erreur lors du test de l'API:", e)

2. Environnement de développement

 - [ ]Python 3.7+ installé et fonctionnel
 - [ ]Pip installé et à jour
 - [ ]Bibliothèques requises installées:
pip install mistralai flask requests

 Éditeur de code configuré (VS Code recommandé)
 Extension Live Server pour VS Code (ou équivalent)

3. Connaissances à réviser

 - [ ] Bases de HTML/CSS/JavaScript (manipulation du DOM)
 - [ ]Requêtes AJAX ou Fetch API
 - [ ]Bases de Flask (routes, templates, API)
 - [ ]Format JSON (structure, manipulation)
 - [ ]Prompt engineering (concepts de base)

4. Téléchargements préalables

 - [ ]Kit de démarrage correspondant à votre option (SISR/SLAM)
 - [ ]Document de projet avec les instructions détaillées
 - [ ]Grille d'auto-évaluation

5. Équipe et organisation

 - [ ]Former votre équipe (2-3 personnes recommandé)
 - [ ]Identifier les points forts de chaque membre
 - [ ]Choisir votre option (SISR ou SLAM)
 - [ ]Prévoir un moyen de partage de code rapide (Git, échange de fichiers)

Notes importantes

- La séance dure seulement 4 heures - Chaque minute compte!
- L'objectif est un MVP fonctionnel - Visez la simplicité et l'efficacité
- Utilisez le kit de démarrage - Ne partez pas de zéro
- Priorisez les fonctionnalités - Commencez par les éléments essentiels

