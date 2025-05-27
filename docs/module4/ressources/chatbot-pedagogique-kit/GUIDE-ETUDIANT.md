# 📋 Guide Étudiant - Chatbot Pédagogique Deep Learning

## 🎯 Votre Mission (4 heures)

Développer un chatbot pédagogique fonctionnel qui explique les concepts du Deep Learning aux étudiants de BTS SIO.

## 📅 Planning Recommandé

| Temps | Étape | Objectif | Livrable |
|-------|-------|----------|----------|
| 0h00-0h30 | **Setup & Configuration** | Environnement fonctionnel | Serveur qui démarre |
| 0h30-1h15 | **Base de Connaissances** | Contenu pédagogique | 5+ concepts dans le JSON |
| 1h15-2h45 | **Personnalisation** | Votre touche unique | Fonctionnalité au choix |
| 2h45-3h15 | **Tests & Validation** | Qualité assurée | 5+ scénarios testés |
| 3h15-4h00 | **Documentation** | Rapport final | Livrable complet |

## 🔧 Étape 1 : Setup & Configuration (30 min)

### 1.1 Installation (10 min)

```bash
# Vérifier Python
python --version  # Python 3.8+ requis

# Installer les dépendances
pip install flask mistralai python-dotenv requests

# Vérifier l'installation
python -c "import flask, mistralai; print('✅ Dépendances OK')"
```

### 1.2 Configuration API (10 min)

1. **Créer le fichier de configuration :**

```bash
# Dans backend/
echo "MISTRAL_API_KEY=votre_clé_api_ici" > .env
echo "DEBUG=True" >> .env
```

2. **Tester la connexion API :**

```bash
cd backend
python -c "
from config import MISTRAL_API_KEY
print('✅ Clé API configurée' if MISTRAL_API_KEY != 'VOTRE_CLE_API' else '❌ Clé API manquante')
"
```

### 1.3 Premier lancement (10 min)

```bash
# Lancer le serveur
cd backend
python app.py

# Dans un autre terminal, tester l'API
curl http://localhost:5000/health
# Réponse attendue : {"status": "healthy"}
```

## 📊 Étape 2 : Base de Connaissances (45 min)

### 2.1 Comprendre la structure (15 min)

Le fichier `data/knowledge_base.json` contient :

```json
{
  "concepts": [
    {
      "id": "neural_network",
      "title": "Réseau de neurones",
      "description": "...",
      "levels": {
        "beginner": "Explication simple",
        "intermediate": "Explication détaillée", 
        "advanced": "Explication technique"
      },
      "examples": ["Exemple 1", "Exemple 2"],
      "analogies": ["Analogie 1", "Analogie 2"],
      "related_concepts": ["cnn", "rnn"],
      "quiz": [
        {
          "question": "Qu'est-ce qu'un neurone artificiel ?",
          "options": ["A", "B", "C", "D"],
          "correct_answer": 1,
          "explanation": "Explication de la réponse"
        }
      ]
    }
  ]
}
```

### 2.2 Vos concepts à ajouter (30 min)

**Concepts obligatoires (minimum 5) :**

1. **Réseau de neurones** (exemple fourni)
2. **Fonction d'activation** 
3. **Rétropropagation**
4. **CNN (Réseaux convolutifs)**
5. **RNN/LSTM (Réseaux récurrents)**

**Concepts optionnels :**
- Dropout
- Batch Normalization
- Transfer Learning
- Overfitting/Underfitting

### 2.3 Template pour vos concepts

```json
{
  "id": "nom_concept",
  "title": "Titre Affiché",
  "description": "Description générale en 1-2 phrases",
  "levels": {
    "beginner": "Explication avec analogies simples, 2-3 phrases",
    "intermediate": "Explication avec exemples concrets, 1 paragraphe",
    "advanced": "Explication technique détaillée, 2-3 paragraphes"
  },
  "examples": [
    "Exemple concret d'utilisation",
    "Exemple du cours ou projet vécu"
  ],
  "analogies": [
    "Analogie avec la vie quotidienne",
    "Comparaison avec un concept connu"
  ],
  "related_concepts": ["concept1", "concept2"],
  "quiz": [
    {
      "question": "Question claire et précise ?",
      "options": [
        "Réponse incorrecte mais plausible",
        "Bonne réponse",
        "Réponse incorrecte évidente",
        "Réponse incorrecte mais proche"
      ],
      "correct_answer": 1,
      "explanation": "Pourquoi cette réponse est correcte"
    }
  ]
}
```

## 🎨 Étape 3 : Personnalisation (90 min)

### Choisissez VOTRE niveau de difficulté :

## 🟢 Choix A : Thèmes Visuels (Niveau Débutant)

**Objectif :** Personnaliser l'apparence et l'ergonomie

**Tâches (90 min) :**

1. **Créer un thème personnalisé (30 min)**
   - Modifier `frontend/css/themes.css`
   - Créer un nouveau thème (couleurs, fonts, layouts)
   - Ajouter un sélecteur de thème

2. **Améliorer l'UX (30 min)**
   - Ajouter des animations CSS
   - Améliorer les indicateurs de chargement
   - Optimiser pour mobile

3. **Branding personnalisé (30 min)**
   - Logo ou avatar du chatbot
   - Messages d'accueil personnalisés
   - Couleurs de votre école/entreprise

**Livrables :**
- [ ] 2+ thèmes fonctionnels
- [ ] Interface responsive
- [ ] Documentation des choix de design

## 🟡 Choix B : Fonctionnalités Quiz (Niveau Intermédiaire)

**Objectif :** Implémenter un système de quiz interactif

**Tâches (90 min) :**

1. **Interface de quiz (30 min)**
   - Compléter `frontend/js/quiz.js`
   - Créer l'interface de question/réponse
   - Ajouter le système de scoring

2. **Génération intelligente (30 min)**
   - Sélection aléatoire de questions
   - Adaptation selon le niveau de difficulté
   - Système de progression

3. **Feedback pédagogique (30 min)**
   - Explications détaillées des réponses
   - Suggestions de concepts à revoir
   - Statistiques de performance

**Livrables :**
- [ ] Système de quiz fonctionnel
- [ ] Minimum 3 quiz par concept
- [ ] Interface de feedback

## 🔴 Choix C : Optimisation IA (Niveau Avancé)

**Objectif :** Améliorer l'intelligence du chatbot

**Tâches (90 min) :**

1. **Optimisation des prompts (30 min)**
   - Compléter `backend/prompt_optimizer.py`
   - Prompts dynamiques selon le contexte
   - Système de templates avancés

2. **Adaptation contextuelle (30 min)**
   - Détection du niveau de l'utilisateur
   - Historique de conversation intelligent
   - Personnalisation des réponses

3. **Analyse sémantique (30 min)**
   - Recherche de concepts dans la base
   - Suggestions de sujets connexes
   - Détection d'incompréhension

**Livrables :**
- [ ] Prompts dynamiques fonctionnels
- [ ] Système d'adaptation au niveau
- [ ] Recherche sémantique dans la base

## 🧪 Étape 4 : Tests & Validation (30 min)

### 4.1 Tests automatisés (15 min)

```bash
# Lancer les tests de base
cd tests
python test_basic.py

# Lancer les tests de scénarios
python test_scenarios.py
```

### 4.2 Tests manuels (15 min)

**Scénarios obligatoires à tester :**

1. **Conversation basique**
   - Question : "Qu'est-ce qu'un réseau de neurones ?"
   - Vérifier : Réponse cohérente et pédagogique

2. **Gestion du niveau**
   - Tester niveau débutant, intermédiaire, avancé
   - Vérifier : Adaptation du langage

3. **Concepts liés**
   - Demander un concept puis un concept lié
   - Vérifier : Cohérence et continuité

4. **Erreur de compréhension**
   - Poser une question hors sujet
   - Vérifier : Réponse d'aide appropriée

5. **Quiz (si implémenté)**
   - Lancer un quiz sur un concept
   - Vérifier : Questions pertinentes et feedback

### 4.3 Documentation des tests

Remplir `tests/resultats_tests.md` avec :
- Scénarios testés
- Résultats obtenus
- Bugs identifiés
- Améliorations suggérées

## 📚 Étape 5 : Documentation (45 min)

### 5.1 Rapport technique (30 min)

Compléter `docs/RAPPORT-TEMPLATE.md` avec :

1. **Architecture** (10 min)
   - Schéma de votre architecture
   - Justification des choix techniques
   - Interactions entre composants

2. **Fonctionnalités** (10 min)
   - Fonctionnalités implémentées
   - Votre personnalisation choisie
   - Difficultés rencontrées

3. **Tests et évaluation** (10 min)
   - Résultats des tests
   - Performance du chatbot
   - Limitations identifiées

### 5.2 Guide utilisateur (15 min)

Créer `docs/GUIDE-UTILISATEUR.md` avec :
- Comment utiliser votre chatbot
- Fonctionnalités disponibles
- Conseils d'utilisation optimale

## ✅ Checklist Finale

Avant de rendre votre projet, vérifiez :

### Fonctionnalités de base
- [ ] Le chatbot répond aux questions de base
- [ ] L'API Mistral est bien intégrée
- [ ] Au moins 5 concepts dans la base de connaissances
- [ ] Interface web fonctionnelle

### Votre personnalisation
- [ ] **Choix A :** Thèmes visuels fonctionnels
- [ ] **Choix B :** Système de quiz implémenté
- [ ] **Choix C :** Optimisations IA fonctionnelles

### Qualité
- [ ] Tests automatisés qui passent
- [ ] 5+ scénarios manuels testés
- [ ] Documentation complète
- [ ] Code commenté et lisible

### Livrable final
- [ ] Dossier complet avec tous les fichiers
- [ ] README personnalisé
- [ ] Rapport technique complété
- [ ] Guide utilisateur créé

## 🆘 Aide Rapide

### Problèmes Courants

| Symptôme | Cause Probable | Solution |
|----------|---------------|----------|
| "Module not found" | Dépendances manquantes | `pip install -r requirements.txt` |
| "API Key error" | Clé non configurée | Vérifier `backend/.env` |
| "CORS error" | Mauvaise URL | Utiliser Live Server, pas `file://` |
| Pas de réponse | Erreur serveur | Vérifier logs dans terminal |
| Réponse vide | Base de connaissances vide | Compléter `data/knowledge_base.json` |

### Ressources Utiles

- 📖 [Documentation Mistral AI](https://docs.mistral.ai/)
- 🐍 [Flask Quickstart](https://flask.palletsprojects.com/quickstart/)
- 🎨 [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- 🧪 [JavaScript Testing](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing)

## 🎉 Objectif Final

À la fin de ces 4 heures, vous devriez avoir un chatbot pédagogique fonctionnel qui :

✅ Répond de manière intelligente aux questions sur le Deep Learning
✅ Adapte ses réponses au niveau de l'utilisateur
✅ Possède une interface engageante et fonctionnelle
✅ Inclut votre personnalisation unique
✅ Est documenté et testé

**Bonne chance et bon développement ! 🚀**