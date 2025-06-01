# 🚨 Simulateur de pannes - Tests de résilience sécuritaire

Ce simulateur vous guide dans les tests de résistance du chatbot face à différents scénarios d'échec pour valider la robustesse sécuritaire.

## 🎯 Objectif des tests de panne

Les tests de résilience permettent de :
- **Vérifier** que le système ne révèle pas d'informations sensibles en cas d'erreur
- **Valider** les mécanismes de récupération automatique
- **Identifier** les vulnérabilités exposées uniquement lors de dysfonctionnements
- **Optimiser** la gestion d'erreurs pour maintenir la sécurité

## ⚠️ Instructions de sécurité

**Tests éthiques et contrôlés :**
- Effectuez ces tests UNIQUEMENT sur votre environnement de développement
- Ne jamais tester sur des systèmes de production sans autorisation
- Documentez tous les tests pour traçabilité
- Restaurez l'état normal après chaque test

## 🔧 Scénario 1 : API Mistral en maintenance

### Contexte de simulation
L'API Mistral AI devient temporairement indisponible (maintenance, quota épuisé, problème réseau).

### Méthodes de simulation

#### Option A : Clé API temporairement invalide
```python
# Dans votre configuration de test
MISTRAL_API_KEY_BACKUP = os.getenv("MISTRAL_API_KEY")
os.environ["MISTRAL_API_KEY"] = "sk-invalid-key-for-testing"

# Effectuer le test
response = test_chatbot_query("Explique les CNN")

# Restaurer la clé
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY_BACKUP
```

#### Option B : URL API modifiée
```python
# Modifier temporairement l'endpoint
MISTRAL_URL_BACKUP = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_URL_TEST = "https://api-maintenance.mistral.ai/v1/chat/completions"

# Test avec URL invalide
```

#### Option C : Simulation de timeout
```python
# Configurer un timeout très court
import requests

session = requests.Session()
session.timeout = 0.001  # 1ms = garantit timeout

try:
    response = session.post(mistral_url, headers=headers, json=data)
except requests.Timeout:
    # Observer la gestion du timeout
    pass
```

### Éléments à observer et documenter

| Aspect | Questions à analyser | Résultat observé |
|--------|---------------------|------------------|
| **Message d'erreur** | Le message révèle-t-il des infos sensibles ? | |
| **Détails techniques** | URL, clé API, structure sont-ils exposés ? | |
| **Fallback** | Y a-t-il un mode dégradé fonctionnel ? | |
| **UX** | L'utilisateur comprend-il la situation ? | |
| **Logging** | L'incident est-il correctement tracé ? | |
| **Récupération** | Le système récupère-t-il automatiquement ? | |

### Messages d'erreur sécurisés vs non-sécurisés

**❌ Exemple NON sécurisé :**
```
Erreur: Impossible de contacter l'API Mistral à l'URL https://api.mistral.ai 
avec la clé sk-abc123... 
Code d'erreur 401: Invalid API key
Stack trace: /home/app/mistral_client.py line 45
```

**✅ Exemple sécurisé :**
```
Le service est temporairement indisponible. 
Veuillez réessayer dans quelques minutes.
Si le problème persiste, contactez l'assistance.
```

### Questions d'audit spécifiques

1. **Exposition d'informations :** Quelles données techniques sont visibles ?
2. **Gestion d'état :** Les conversations en cours sont-elles préservées ?
3. **Communication :** Le message utilisateur est-il approprié ?
4. **Monitoring :** L'incident génère-t-il les bonnes alertes ?

## 🌐 Scénario 2 : Connexion réseau coupée

### Contexte de simulation
La connexion réseau entre votre serveur et l'API Mistral est interrompue pendant une requête.

### Méthodes de simulation

#### Option A : Simulation par proxy
```python
# Configurer un proxy qui coupe la connexion
proxies = {
    'http': 'http://127.0.0.1:9999',  # Proxy inexistant
    'https': 'http://127.0.0.1:9999'
}

try:
    response = requests.post(url, proxies=proxies, timeout=5)
except requests.exceptions.ProxyError:
    # Observer la gestion d'erreur réseau
    pass
```

#### Option B : Firewall temporaire
```bash
# Linux/Mac - Bloquer temporairement l'accès
# ATTENTION: Nécessite des droits admin
sudo iptables -A OUTPUT -d api.mistral.ai -j DROP

# Test de votre application

# Restaurer
sudo iptables -D OUTPUT -d api.mistral.ai -j DROP
```

#### Option C : Simulation de déconnexion en cours de requête
```python
import threading
import time

def interrupt_connection():
    time.sleep(2)  # Attendre 2s puis couper
    # Simulation d'interruption réseau
    
# Lancer en parallèle avec votre requête
```

### Éléments à observer

| Aspect | Critères d'évaluation | Score |
|--------|----------------------|-------|
| **Détection timeout** | Temps avant détection de la panne | ⬜ <5s ⬜ 5-15s ⬜ >15s |
| **Gestion utilisateur** | Information claire de l'incident | ⬜ Claire ⬜ Acceptable ⬜ Confuse |
| **Retry automatique** | Tentatives de reconnexion | ⬜ Oui ⬜ Partiel ⬜ Non |
| **Préservation état** | Données utilisateur conservées | ⬜ Totale ⬜ Partielle ⬜ Perdue |
| **Récupération** | Retour automatique quand réseau OK | ⬜ Auto ⬜ Manuel ⬜ Aucune |

### Tests de robustesse réseau

**Test 1 : Coupure brève (5 secondes)**
- Observer : Le système attend-il et reprend-il ?
- Attendu : Retry automatique avec succès

**Test 2 : Coupure longue (2 minutes)**  
- Observer : Abandon avec message approprié ?
- Attendu : Timeout propre et message utilisateur

**Test 3 : Reconnexion avec nouvelle requête**
- Observer : Le système fonctionne-t-il normalement ?
- Attendu : Retour complet à la normale

## 🔐 Scénario 3 : Clé API compromise (révoquée)

### Contexte de simulation
La clé API Mistral a été compromise et révoquée côté fournisseur, générant des erreurs 401/403.

### Méthodes de simulation

#### Option A : Clé volontairement invalide
```python
# Sauvegarder la vraie clé
REAL_KEY = os.getenv("MISTRAL_API_KEY")

# Utiliser une clé syntaxiquement correcte mais invalide
os.environ["MISTRAL_API_KEY"] = "sk-" + "x" * 45  # Format correct, contenu invalide

# Effectuer les tests

# Restaurer
os.environ["MISTRAL_API_KEY"] = REAL_KEY
```

#### Option B : Clé avec permissions révoquées
```python
# Si vous avez accès à une clé expirée ou révoquée
REVOKED_KEY = "sk-ancienne-cle-revoquee..."
os.environ["MISTRAL_API_KEY"] = REVOKED_KEY
```

### Éléments critiques à évaluer

| Sécurité | Question | Conforme | Non-conforme |
|----------|----------|----------|--------------|
| **Exposition clé** | La clé compromise est-elle visible dans les logs ? | ⬜ | ⬜ |
| **Stack trace** | Les traces d'erreur révèlent-elles des chemins ? | ⬜ | ⬜ |
| **Arrêt sécurisé** | Le service s'arrête-t-il pour éviter d'autres dégâts ? | ⬜ | ⬜ |
| **Notification** | L'incident est-il notifié aux administrateurs ? | ⬜ | ⬜ |
| **Procédure** | Y a-t-il une procédure documentée de réponse ? | ⬜ | ⬜ |

### Scénario de compromission réaliste

**Étape 1 : Détection initiale**
```
12:34:56 - ERROR: API call failed with 401 Unauthorized
12:34:57 - ERROR: API call failed with 401 Unauthorized  
12:34:58 - ERROR: API call failed with 401 Unauthorized
```

**Étape 2 : Questions d'analyse**
1. Combien de tentatives avant arrêt automatique ?
2. Les erreurs 401 déclenchent-elles une alerte ?
3. Le système continue-t-il à exposer la clé compromise ?
4. Y a-t-il un mécanisme de clé de secours ?

**Étape 3 : Procédure de réponse attendue**
1. Arrêt immédiat des appels API
2. Notification équipe sécurité
3. Révocation côté Mistral (si pas déjà fait)
4. Génération nouvelle clé
5. Redéploiement sécurisé

## 💾 Scénario 4 : Surcharge serveur (CPU/Mémoire)

### Contexte de simulation
Le serveur hébergeant le chatbot atteint ses limites de ressources (CPU 100%, RAM saturée).

### Méthodes de simulation

#### Option A : Charge CPU artificielle
```python
import threading
import time

def cpu_stress():
    """Fonction pour saturer un cœur CPU"""
    end_time = time.time() + 30  # 30 secondes de stress
    while time.time() < end_time:
        pass  # Boucle vide = 100% CPU

#