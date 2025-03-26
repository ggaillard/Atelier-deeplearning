# Phase 3 : Préparation au projet final (45min)

## Présentation du projet chatbot pédagogique (15 min)

**Objectif** : Comprendre les attentes concrètes pour le projet final et voir comment les technologies vues jusqu'à présent s'intègrent dans ce contexte.

### Vue d'ensemble du projet

Le projet consiste à développer un chatbot pédagogique capable d'expliquer les concepts du Deep Learning à des étudiants de BTS SIO.

![Schéma du chatbot](../ressources/images/schema-chatbot.png)

Les composants principaux du projet sont :

1. **Interface conversationnelle** : Interface simple permettant de dialoguer avec le chatbot
2. **API Mistral AI** : Moteur de génération de réponses intelligentes
3. **Base de connaissances** : Structure contenant les informations sur le Deep Learning
4. **Système de gestion de contexte** : Maintien de la cohérence dans les conversations

### Objectifs pédagogiques du projet

Ce projet vous permettra de :
- Appliquer vos connaissances en frameworks IA dans un contexte concret
- Développer des compétences pratiques en intégration d'API
- Créer une application web avec fonctionnalités d'IA
- Structurer des connaissances pour un usage pédagogique

### Exemple de chatbot fonctionnel

Démonstration d'un exemple de chatbot similaire à celui que vous développerez, montrant :
- La qualité des réponses attendues
- La structure de l'interface
- Les fonctionnalités de base

### Niveau de complexité attendu

Ce projet est intentionnellement dimensionné pour être réalisable avec vos compétences actuelles :

| Aspect | Niveau attendu | Remarque |
|--------|----------------|----------|
| Interface | Simple mais fonctionnelle | Pas besoin de design complexe |
| Base de connaissances | Couvrant les concepts principaux | Qualité > Quantité |
| Intégration API | Fonctionnelle avec gestion d'erreurs | Pas besoin d'optimisations avancées |
| Fonctionnalités | 3-4 fonctionnalités bien implémentées | Mieux vaut peu mais bien |

## Étude de cas réels d'utilisation des chatbots (15 min)

**Objectif** : Comprendre comment les chatbots sont utilisés en entreprise pour mieux orienter votre projet.

### Cas d'étude 1 : Chatbot d'assistance technique

**Entreprise** : PME de services informatiques (20 employés)
**Problématique** : Support technique de premier niveau surchargé

**Solution mise en place** :
- Chatbot capable de gérer les questions fréquentes
- Base de connaissances structurée par catégories de problèmes
- Redirection vers un technicien humain pour les cas complexes
- Disponible 24/7, réduisant les temps d'attente

**Résultats** :
- 45% des demandes traitées sans intervention humaine
- Temps de réponse initial réduit de 4h à 5min
- Meilleure satisfaction client
- Techniciens concentrés sur des problèmes à plus forte valeur ajoutée

**Technologies utilisées** :
- API LLM similaire à Mistral AI
- Base de données MongoDB pour la base de connaissances
- Interface web React avec design responsive

### Cas d'étude 2 : Chatbot pédagogique pour formation interne

**Entreprise** : Centre de formation professionnelle
**Problématique** : Besoin d'assistance pour les apprenants en dehors des heures de cours

**Solution mise en place** :
- Chatbot spécialisé dans les formations techniques
- Capacité à expliquer des concepts, fournir des exemples et proposer des exercices
- Suivi de la progression des apprenants
- Disponible sur la plateforme e-learning existante

**Résultats** :
- Augmentation de 30% du taux de complétion des formations
- Réduction du nombre de questions basiques aux formateurs
- Meilleure adaptation aux différents rythmes d'apprentissage
- Collecte de données sur les concepts les plus difficiles à assimiler

**Technologies utilisées** :
- API GPT (similaire à Mistral AI)
- Structure JSON pour la base de connaissances
- Interface web intégrée à la plateforme existante

### Enseignements à retenir pour votre projet

1. **Clarté du périmètre** : Définir précisément ce que le chatbot peut et ne peut pas faire
2. **Structure de l'information** : Organiser la base de connaissances de manière logique
3. **Expérience utilisateur** : Privilégier la fluidité et la simplicité
4. **Gestion des limites** : Prévoir comment réagir quand le chatbot ne connaît pas la réponse
## Premiers pas avec l'API Mistral AI (15 min)

**Objectif** : Découvrir l'API Mistral AI et réaliser un premier test fonctionnel.

### Introduction à Mistral AI

[Mistral AI](https://mistral.ai/) est une entreprise française qui développe des modèles de langage performants. Son API permet d'accéder à ces modèles pour créer des applications conversationnelles.

Avantages pour votre projet :
- Modèles performants, y compris en français
- API simple à utiliser
- Quota gratuit suffisant pour le développement
- Entreprise européenne (conformité RGPD)

### Configuration de l'accès à l'API

1. **Création d'un compte** :
   - Rendez-vous sur [https://console.mistral.ai/](https://console.mistral.ai/)
   - Inscrivez-vous avec votre adresse email
   - Confirmez votre compte

2. **Obtention d'une clé API** :
   - Dans le tableau de bord, accédez à "API Keys"
   - Cliquez sur "Create API Key"
   - Donnez un nom à votre clé (ex: "projet-chatbot-bts")
   - Copiez la clé générée (elle ne sera plus accessible ensuite)

3. **Conservation de la clé** :
   - Créez un fichier `.env` pour stocker votre clé
   - Ne partagez jamais votre clé dans vos dépôts Git (utilisez .gitignore)
   - Format du fichier `.env` :
     ```
     MISTRAL_API_KEY=votre_clé_api_ici
     ```

### Premier test avec l'API

Nous allons réaliser un test simple pour vérifier que l'API fonctionne correctement :

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

# Créer une liste de messages (incluant un prompt système et un message utilisateur)
messages = [
    ChatMessage(role="system", content="Tu es un assistant pédagogique spécialisé dans le Deep Learning pour des étudiants de BTS SIO."),
    ChatMessage(role="user", content="Peux-tu m'expliquer ce qu'est un réseau de neurones convolutif (CNN) en termes simples ?")
]

# Envoyer la requête à l'API
chat_response = client.chat(
    model="mistral-tiny",  # Modèle de base, économique et rapide
    messages=messages
)

# Afficher la réponse
print(chat_response.choices[0].message.content)
```

### Structure de base de votre chatbot

Voici une structure de base pour votre futur chatbot :

```python
# Structure simplifiée du chatbot
def chatbot_educatif(question, historique=None):
    """
    Répond à une question sur le Deep Learning
    
    Args:
        question (str): Question de l'utilisateur
        historique (list, optional): Historique de la conversation
    
    Returns:
        str: Réponse du chatbot
        list: Historique mis à jour
    """
    # Initialiser l'historique si nécessaire
    if historique is None:
        historique = [
            ChatMessage(role="system", content="Tu es un assistant pédagogique...")
        ]
    
    # Ajouter la question à l'historique
    historique.append(ChatMessage(role="user", content=question))
    
    # Obtenir la réponse via l'API
    response = client.chat(
        model="mistral-tiny",
        messages=historique
    )
    
    # Extraire le contenu de la réponse
    reponse_texte = response.choices[0].message.content
    
    # Ajouter la réponse à l'historique
    historique.append(ChatMessage(role="assistant", content=reponse_texte))
    
    return reponse_texte, historique
```

## Présentation du cahier des charges (15 min)

### Fonctionnalités minimales requises

Votre chatbot doit implémenter au minimum :

1. **Interface conversationnelle** :
   - Zone de saisie et d'affichage des messages
   - Historique de conversation visible
   - Indication visuelle pendant le chargement des réponses

2. **Intégration de l'API Mistral AI** :
   - Gestion du contexte de conversation
   - Configuration des paramètres de génération
   - Gestion des erreurs d'API

3. **Base de connaissances** :
   - Structuration des informations sur le Deep Learning
   - Couverture des concepts principaux du cours
   - Format JSON ou similaire

4. **Fonctionnalités pédagogiques** :
   - Possibilité de demander des explications sur les concepts
   - Génération d'exemples concrets
   - Au moins une fonctionnalité supplémentaire au choix

### Livrables attendus

1. **Code source** du chatbot (fichiers Python, HTML/CSS/JS)
2. **Base de connaissances** structurée
3. **Documentation technique** expliquant :
   - L'architecture de la solution
   - Les choix d'implémentation
   - Les instructions d'installation et d'utilisation
   - Les possibilités d'évolution
4. **Présentation** pour la démonstration finale

### Planning et jalons

| Date | Jalon | Livrable intermédiaire |
|------|-------|------------------------|
| Fin séance 3 | Document de conception | Structure du projet et maquette |
| +1 semaine | Prototype fonctionnel | Interface basique + API connectée |
| +2 semaines | Version alpha | Toutes fonctionnalités implémentées |
| +3 semaines | Version finale | Solution complète et documentation |

### Conseils pour réussir votre projet

1. **Commencez simple** et ajoutez des fonctionnalités progressivement
2. **Travaillez en équipe** en répartissant clairement les tâches
3. **Testez régulièrement** pour identifier les problèmes tôt
4. **Documentez au fur et à mesure** pour éviter la surcharge à la fin
5. **Demandez de l'aide** si vous rencontrez des blocages

## Conclusion de la séance (5 min)

### Récapitulatif des apprentissages

Au cours de cette séance, vous avez :
- Découvert les frameworks de Deep Learning utilisés en entreprise
- Appris à améliorer les performances des modèles
- Exploré des cas d'utilisation réels de chatbots
- Fait vos premiers pas avec l'API Mistral AI
- Pris connaissance du cahier des charges du projet final

### Prochaines étapes

Pour la prochaine séance, vous devrez :
1. Former votre équipe projet (1-2 personnes)
2. Rédiger un document de conception initial
3. Créer un dépôt Git pour votre projet
4. Préparer une maquette simple de l'interface

### Questions et clarifications

Profitez de ces dernières minutes pour poser vos questions sur :
- Le format du projet
- Les attentes techniques
- Les ressources disponibles
- Les prochaines étapes

[Retour à l'index de la séance 3](index.md){ .md-button .md-button--primary }