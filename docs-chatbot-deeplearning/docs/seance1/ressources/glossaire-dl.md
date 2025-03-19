# Glossaire du Deep Learning

## Termes fondamentaux

| Terme | Définition | Exemple concret |
|-------|------------|----------------|
| **Deep Learning** | Sous-domaine du Machine Learning utilisant des réseaux de neurones à plusieurs couches | Reconnaissance d'objets dans des photos |
| **Réseau de neurones** | Système inspiré du cerveau humain composé de nœuds (neurones) interconnectés | Réseau capable de reconnaître des chiffres manuscrits |
| **Neurone artificiel** | Unité de calcul de base qui reçoit des entrées, applique une transformation et produit une sortie | Un neurone qui s'active quand il détecte un contour vertical |
| **Couche** | Ensemble de neurones situés au même niveau dans le réseau | Couche d'entrée, couche cachée, couche de sortie |
| **Poids** | Valeurs numériques qui définissent l'importance relative de chaque connexion | Un poids élevé (ex: 0.8) indique une forte influence |
| **Biais** | Valeur ajoutée à la somme pondérée pour ajuster le seuil d'activation | Permet à un neurone de s'activer même si toutes les entrées sont nulles |
| **Fonction d'activation** | Fonction mathématique qui détermine la sortie d'un neurone | ReLU, Sigmoid, Tanh |

## Architectures de réseaux

| Terme | Définition | Cas d'utilisation |
|-------|------------|-------------------|
| **Réseau dense** | Réseau où chaque neurone est connecté à tous les neurones de la couche précédente | Classification d'images simples, prédiction de valeurs |
| **Réseau convolutif (CNN)** | Réseau spécialisé dans le traitement des données en grille comme les images | Reconnaissance d'objets, classification d'images |
| **Réseau récurrent (RNN)** | Réseau avec des connexions formant des cycles, adapté aux données séquentielles | Traduction automatique, génération de texte |
| **LSTM/GRU** | Types de RNN capables de mémoriser l'information sur de longues séquences | Analyse de texte long, prédiction de séries temporelles |

## Apprentissage

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Forward propagation** | Passage des données d'entrée à travers le réseau pour produire une prédiction | Calcul de la sortie d'un modèle pour une image d'entrée |
| **Loss (perte)** | Mesure de l'écart entre les prédictions et les valeurs réelles | Erreur quadratique moyenne, entropie croisée |
| **Backpropagation** | Algorithme qui calcule le gradient de l'erreur par rapport aux poids | Calcul de la contribution de chaque poids à l'erreur totale |
| **Descente de gradient** | Algorithme d'optimisation qui ajuste les poids pour minimiser l'erreur | Modification itérative des poids dans la direction du gradient négatif |
| **Époque** | Un passage complet à travers l'ensemble des données d'entraînement | Entraîner un modèle pendant 10 époques |
| **Batch** | Sous-ensemble des données traité avant une mise à jour des poids | Traiter les données par lots de 32 exemples |

## Hyperparamètres et optimisation

| Terme | Définition | Impact |
|-------|------------|--------|
| **Learning rate** | Taux qui contrôle l'ampleur des ajustements des poids | Trop élevé: divergence, trop faible: apprentissage lent |
| **Dropout** | Technique où des neurones sont aléatoirement désactivés pendant l'entraînement | Réduit l'overfitting en forçant le réseau à être redondant |
| **Batch normalization** | Normalisation des activations d'une couche pour stabiliser l'apprentissage | Accélère l'entraînement et améliore la convergence |
| **Early stopping** | Arrêt de l'entraînement quand les performances sur la validation cessent de s'améliorer | Évite l'overfitting en empêchant le surajustement aux données d'entraînement |

## Problèmes courants

| Terme | Définition | Solution possible |
|-------|------------|-------------------|
| **Overfitting** | Le modèle apprend trop bien les données d'entraînement au détriment de la généralisation | Régularisation, dropout, plus de données |
| **Underfitting** | Le modèle est trop simple pour capturer la complexité des données | Augmenter la complexité du modèle, entraîner plus longtemps |
| **Vanishing gradient** | Problème où le gradient devient très petit, ralentissant l'apprentissage | Utiliser ReLU, LSTM, initialisation des poids adaptée |
| **Exploding gradient** | Problème où le gradient devient très grand, déstabilisant l'apprentissage | Gradient clipping, normalisation des poids |