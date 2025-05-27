# 🤖 Kit de Démarrage - Chatbot Pédagogique Deep Learning

## 🚀 Démarrage Ultra-Rapide (5 minutes)

Ce kit contient tout le nécessaire pour développer votre chatbot pédagogique en 4 heures.

### 📋 Checklist de démarrage

- [ ] **Clé API Mistral configurée** dans `backend/config.py`
- [ ] **Dépendances installées** : `pip install -r requirements.txt`
- [ ] **Serveur lancé** : `python backend/app.py`
- [ ] **Interface ouverte** : `frontend/index.html` avec Live Server

### 🎯 Votre Mission

1. **Compléter la base de connaissances** (`data/knowledge_base.json`)
2. **Personnaliser l'interface** (3 choix de difficulté)
3. **Tester et documenter** votre chatbot

## 📁 Structure du Kit

```
📦 chatbot-pedagogique-kit/
├── 📖 README.md                    ← Vous êtes ici
├── 📋 GUIDE-ETUDIANT.md            ← Instructions détaillées
├── 🎨 frontend/                    ← Interface web complète
├── ⚙️ backend/                     ← Serveur Python fonctionnel
├── 📊 data/                        ← Données à personnaliser
├── 🧪 tests/                       ← Tests automatisés
└── 📚 docs/                        ← Documentation technique
```

## 🔧 Installation Express

```bash
# 1. Installer les dépendances
pip install flask mistralai python-dotenv requests

# 2. Configurer votre clé API
echo "MISTRAL_API_KEY=votre_clé_ici" > backend/.env

# 3. Lancer le serveur
cd backend && python app.py

# 4. Ouvrir l'interface (nouveau terminal)
# Utilisez Live Server sur frontend/index.html
```

## ✨ Fonctionnalités Pré-implémentées

✅ **Interface conversationnelle complète**
✅ **Intégration API Mistral fonctionnelle**
✅ **Système de gestion des connaissances**
✅ **Tests automatisés**
✅ **3 niveaux de personnalisation au choix**

## 🎯 Niveaux de Difficulté

### 🟢 Niveau 1 - Thèmes Visuels
- Modifier les couleurs et styles CSS
- Ajouter des animations
- Personnaliser l'apparence

### 🟡 Niveau 2 - Fonctionnalités Quiz  
- Implémenter la génération de quiz
- Ajouter un système de progression
- Créer une interface de feedback

### 🔴 Niveau 3 - Optimisation IA
- Améliorer les prompts dynamiques
- Ajouter un système d'adaptation au niveau
- Implémenter l'analyse contextuelle

## 🚨 Points Critiques

⚠️ **À faire ABSOLUMENT** :
1. Remplacer `VOTRE_CLE_API` dans `backend/config.py`
2. Compléter `data/knowledge_base.json` avec vos concepts
3. Tester au moins 5 scénarios différents

## 🆘 Support Rapide

| Problème | Solution |
|----------|----------|
| Erreur API | Vérifier la clé dans `backend/config.py` |
| Import manquant | `pip install -r requirements.txt` |
| CORS Error | Utiliser Live Server, pas `file://` |
| Pas de réponse | Vérifier les logs dans le terminal |

## 📊 Evaluation

Votre projet sera évalué sur :
- ✅ **Fonctionnalité** (30%) : Le chatbot répond correctement
- ✅ **Personnalisation** (25%) : Votre niveau de difficulté choisi
- ✅ **Base de connaissances** (20%) : Qualité du contenu ajouté
- ✅ **Tests** (15%) : Scénarios testés et documentés
- ✅ **Documentation** (10%) : Rapport final complété

---

**⏱️ Temps estimé par étape :**
- Installation : 10 min
- Base de connaissances : 45 min
- Personnalisation : 90 min
- Tests : 30 min
- Documentation : 45 min

**🎉 Bon développement !**