# 🔍 Phase 1: Système de tickets intelligent (2h)

![Système de tickets](https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&q=80&w=1000&h=300)

## 🎯 Objectif de la phase

Dans cette phase, vous allez :

- Découvrir un système de tickets d'assistance pré-développé
- Intégrer une API d'IA pour classifier automatiquement les demandes
- Tester l'application avec différents types de demandes d'assistance
- Adapter les catégories aux besoins spécifiques d'une entreprise informatique

## 🔍 Introduction au système de tickets intelligent (30 min)

### Contexte professionnel

En tant que technicien SIO, vous serez souvent confronté à la gestion de demandes d'assistance. Un système de tickets permet d'organiser et de prioriser ces demandes, mais la classification manuelle prend du temps et manque parfois de cohérence.

L'intégration d'une IA pour classifier automatiquement les demandes permet de :
- Gagner du temps sur le traitement initial
- Assurer une catégorisation cohérente
- Diriger plus rapidement les demandes vers les bons interlocuteurs
- Faciliter l'analyse des types de problèmes récurrents

### Présentation du système pré-développé

Notre système de tickets est une application Flask simple qui permet :
- La soumission de nouvelles demandes
- La classification automatique par IA
- L'affichage d'une liste de tickets organisée par catégories
- L'ajout de commentaires et la résolution des tickets

![Capture d'écran du système de tickets](../images/ticket-system-screenshot.svg)

### Démonstration du fonctionnement

Voici un exemple de classification automatique :

| Description de la demande | Catégorie détectée | Priorité estimée |
|---------------------------|-------------------|-----------------|
| "Mon ordinateur ne s'allume plus depuis ce matin" | Matériel | Haute |
| "Je n'arrive pas à me connecter à la messagerie" | Accès / Compte | Moyenne |
| "Comment puis-je installer le nouveau logiciel ?" | Logiciel | Basse |

## 📋 Intégration de l'API de classification (1h30)

### Exploration du code existant (30 min)

Commençons par explorer le code du système de tickets :

```python
# app.py - Application principale
from flask import Flask, request, render_template, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Charger les tickets existants
def load_tickets():
    try:
        with open('tickets.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Sauvegarder les tickets
def save_tickets(tickets):
    with open('tickets.json', 'w') as f:
        json.dump(tickets, f, indent=4)

# Fonction de classification à compléter
def classify_ticket(description):
    # Cette fonction doit être complétée pour intégrer l'API d'IA
    # En attendant, elle retourne une catégorie par défaut
    return {
        "category": "Non classé",
        "priority": "Moyenne",
        "confidence": 0.0
    }

@app.route('/')
def index():
    tickets = load_tickets()
    return render_template('index.html', tickets=tickets)

@app.route('/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        # Classifier le ticket
        classification = classify_ticket(description)
        
        # Créer le nouveau ticket
        ticket = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S'),
            'title': title,
            'description': description,
            'category': classification['category'],
            'priority': classification['priority'],
            'status': 'Ouvert',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'comments': []
        }
        
        # Sauvegarder
        tickets = load_tickets()
        tickets.append(ticket)
        save_tickets(tickets)
        
        return redirect(url_for('index'))
    
    return render_template('new_ticket.html')

@app.route('/ticket/')
def view_ticket(ticket_id):
    tickets = load_tickets()
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    
    if ticket:
        return render_template('ticket_detail.html', ticket=ticket)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Examinez également les templates HTML principaux :

```html
<!-- templates/index.html -->



    Système de Tickets d'Assistance
    


    
        Système de Tickets d'Assistance
        Nouveau Ticket
    
    
    
        
            Tickets en cours
            
            {% if tickets %}
                
                    
                        
                            ID
                            Titre
                            Catégorie
                            Priorité
                            Statut
                            Date
                            Actions
                        
                    
                    
                        {% for ticket in tickets %}
                            
                                {{ ticket.id }}
                                {{ ticket.title }}
                                {{ ticket.category }}
                                {{ ticket.priority }}
                                {{ ticket.status }}
                                {{ ticket.created_at }}
                                
                                    Voir
                                
                            
                        {% endfor %}
                    
                
            {% else %}
                Aucun ticket pour le moment.
            {% endif %}
        
    


```

### Implémentation de la classification (30 min)

Maintenant, complétez la fonction `classify_ticket` pour intégrer l'API d'IA :

```python
# Code à compléter dans app.py
import requests

def classify_ticket(description):
    # Configuration de l'API (clé fournie en cours)
    api_key = "VOTRE_CLE_API"  # À remplacer par la clé fournie
    api_url = "https://api.example.com/classify"
    
    # Préparation des données
    data = {
        "text": description,
        "categories": ["Matériel", "Logiciel", "Réseau", "Accès / Compte", "Autre"]
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Appel à l'API
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Vérifier si l'appel a réussi
        
        result = response.json()
        
        # Déterminer la priorité en fonction de mots-clés et de la catégorie
        priority = determine_priority(description, result["category"])
        
        return {
            "category": result["category"],
            "priority": priority,
            "confidence": result["confidence"]
        }
        
    except Exception as e:
        print(f"Erreur lors de la classification: {e}")
        return {
            "category": "Non classé",
            "priority": "Moyenne",
            "confidence": 0.0
        }

def determine_priority(description, category):
    # Mots-clés qui indiquent une priorité haute
    high_priority_keywords = ["urgent", "bloqué", "impossible", "critique", "production"]
    
    # Vérifier si des mots-clés de haute priorité sont présents
    if any(keyword in description.lower() for keyword in high_priority_keywords):
        return "Haute"
    
    # Priorité basée sur la catégorie
    category_priorities = {
        "Matériel": "Moyenne",
        "Logiciel": "Basse",
        "Réseau": "Haute",
        "Accès / Compte": "Moyenne",
        "Autre": "Basse"
    }
    
    return category_priorities.get(category, "Moyenne")
```

### Test et adaptation (30 min)

Testez l'application avec différentes demandes pour vérifier la classification :

**Exemples de tickets à tester :**

1. "Mon ordinateur ne démarre plus, écran noir après le logo Windows"
2. "Je n'arrive pas à me connecter à la messagerie professionnelle"
3. "Comment installer le logiciel de comptabilité sur mon poste ?"
4. "Le site web de l'entreprise est inaccessible depuis l'extérieur"
5. "J'ai besoin d'un nouveau câble HDMI pour mon moniteur"

### Adaptation des catégories

Modifiez le code pour adapter les catégories à votre contexte :

```python
# Personnalisation des catégories
def classify_ticket(description):
    # Configuration de l'API (inchangée)
    
    # Catégories personnalisées
    data = {
        "text": description,
        "categories": [
            "Poste de travail", 
            "Applications métier", 
            "Infrastructure réseau", 
            "Sécurité / Accès", 
            "Demande d'équipement",
            "Formation / Aide"
        ]
    }
    
    # Reste du code inchangé
```

### Ajustement des priorités

Personnalisez également la logique de détermination des priorités :

```python
def determine_priority(description, category):
    # Mots-clés personnalisés
    high_priority_keywords = ["urgent", "bloqué", "impossible", "critique", "production", "sécurité"]
    medium_priority_keywords = ["problème", "erreur", "ne fonctionne pas", "bug"]
    
    # Vérifier les mots-clés
    if any(keyword in description.lower() for keyword in high_priority_keywords):
        return "Haute"
    if any(keyword in description.lower() for keyword in medium_priority_keywords):
        return "Moyenne"
    
    # Priorités par catégorie personnalisées
    category_priorities = {
        "Poste de travail": "Moyenne",
        "Applications métier": "Haute",
        "Infrastructure réseau": "Haute",
        "Sécurité / Accès": "Haute",
        "Demande d'équipement": "Basse",
        "Formation / Aide": "Basse"
    }
    
    return category_priorities.get(category, "Moyenne")
```

## 📝 Conclusion et transition

Dans cette première phase, vous avez découvert comment intégrer une API d'IA dans un système de tickets pour automatiser la classification des demandes d'assistance. Cette compétence est directement applicable dans un contexte professionnel et vous permettra de gagner en efficacité dans la gestion des incidents.

Vous avez également appris à personnaliser la logique de classification et de priorisation pour l'adapter aux besoins spécifiques d'une entreprise informatique.

Dans la prochaine phase, nous explorerons une autre application pratique : un assistant pour la documentation technique, qui vous aidera à générer et améliorer vos documentations professionnelles.

N'oubliez pas de compléter la première partie de votre fiche d'observations avec vos tests et adaptations.

[Retour au Module 3](index.md){ .md-button }
[Continuer vers la Phase 2: Assistant de documentation technique](assistant-documentation.md){ .md-button .md-button--primary }