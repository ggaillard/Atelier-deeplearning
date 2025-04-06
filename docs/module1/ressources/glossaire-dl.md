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
| **Transformer** | Architecture basée sur des mécanismes d'attention, sans récurrence | Modèles de langage avancés comme GPT, BERT, Mistral |
| **Autoencoder** | Réseau qui apprend à encoder puis décoder les données | Réduction de dimensionnalité, détection d'anomalies |
| **GAN** | Generative Adversarial Network - Deux réseaux en compétition pour générer des données réalistes | Création d'images réalistes, deepfakes |

## Apprentissage

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Forward propagation** | Passage des données d'entrée à travers le réseau pour produire une prédiction | Calcul de la sortie d'un modèle pour une image d'entrée |
| **Loss (perte)** | Mesure de l'écart entre les prédictions et les valeurs réelles | Erreur quadratique moyenne, entropie croisée |
| **Backpropagation** | Algorithme qui calcule le gradient de l'erreur par rapport aux poids | Calcul de la contribution de chaque poids à l'erreur totale |
| **Descente de gradient** | Algorithme d'optimisation qui ajuste les poids pour minimiser l'erreur | Modification itérative des poids dans la direction du gradient négatif |
| **Époque** | Un passage complet à travers l'ensemble des données d'entraînement | Entraîner un modèle pendant 10 époques |
| **Batch** | Sous-ensemble des données traité avant une mise à jour des poids | Traiter les données par lots de 32 exemples |
| **Optimiseur** | Algorithme qui implémente la descente de gradient | Adam, SGD, RMSprop |
| **Learning rate** | Taux qui contrôle l'ampleur des ajustements des poids | Trop élevé: divergence, trop faible: apprentissage lent |

## Techniques spécifiques

| Terme | Définition | Utilisation |
|-------|------------|-------------|
| **Transfer learning** | Réutilisation d'un modèle pré-entraîné sur une nouvelle tâche | Adapter un modèle ImageNet pour reconnaître des maladies de plantes |
| **Fine-tuning** | Ajustement d'un modèle pré-entraîné sur des données spécifiques | Réentraîner les dernières couches d'un modèle BERT pour la classification de texte |
| **Data augmentation** | Génération de nouvelles données d'entraînement par transformation des données existantes | Rotation, mise à l'échelle, distorsion d'images |
| **Dropout** | Technique où des neurones sont aléatoirement désactivés pendant l'entraînement | Réduit l'overfitting en forçant le réseau à être redondant |
| **Batch normalization** | Normalisation des activations d'une couche pour stabiliser l'apprentissage | Accélère l'entraînement et améliore la convergence |
| **Early stopping** | Arrêt de l'entraînement quand les performances sur la validation cessent de s'améliorer | Évite l'overfitting en empêchant le surajustement aux données d'entraînement |
| **Embedding** | Conversion de données catégorielles en vecteurs denses | Word embeddings dans le NLP (Word2Vec, GloVe) |

## Convolutions et CNN

| Terme | Définition | Rôle |
|-------|------------|------|
| **Filtre (kernel)** | Matrice de poids appliquée à une région de l'image | Détecte des caractéristiques spécifiques (bords, textures) |
| **Feature map** | Sortie d'un filtre de convolution appliqué à une image | Carte d'activation des caractéristiques détectées |
| **Pooling** | Opération de sous-échantillonnage réduisant les dimensions | Réduit la complexité computationnelle, généralise les caractéristiques |
| **Padding** | Ajout de pixels (généralement zéros) aux bords d'une image | Permet de conserver les dimensions après convolution |
| **Stride** | Pas de déplacement du filtre sur l'image | Contrôle le chevauchement des champs réceptifs |

## Métriques d'évaluation

| Métrique | Définition | Cas d'usage |
|----------|------------|-------------|
| **Accuracy** | Proportion de prédictions correctes | Classification équilibrée |
| **Precision** | Proportion des prédictions positives qui sont correctes | Quand les faux positifs sont coûteux |
| **Recall** | Proportion des cas positifs réels correctement identifiés | Quand les faux négatifs sont coûteux |
| **F1-Score** | Moyenne harmonique de la précision et du rappel | Classification avec classes déséquilibrées |
| **ROC-AUC** | Aire sous la courbe ROC, mesure de la qualité de la discrimination | Évaluation des modèles de classification |
| **MAE** | Mean Absolute Error - Moyenne des valeurs absolues des erreurs | Régression, quand les écarts importants ne sont pas surpondérés |
| **RMSE** | Root Mean Squared Error - Racine carrée de la moyenne des carrés des erreurs | Régression, pénalise davantage les grands écarts |

## Problèmes courants

| Terme | Définition | Solution possible |
|-------|------------|-------------------|
| **Overfitting** | Le modèle apprend trop bien les données d'entraînement au détriment de la généralisation | Régularisation, dropout, plus de données |
| **Underfitting** | Le modèle est trop simple pour capturer la complexité des données | Augmenter la complexité du modèle, entraîner plus longtemps |
| **Vanishing gradient** | Problème où le gradient devient très petit, ralentissant l'apprentissage | Utiliser ReLU, LSTM, initialisation des poids adaptée |
| **Exploding gradient** | Problème où le gradient devient très grand, déstabilisant l'apprentissage | Gradient clipping, normalisation des poids |
| **Imbalanced data** | Jeu de données où certaines classes sont beaucoup plus fréquentes que d'autres | Rééchantillonnage, pondération des classes, techniques d'augmentation |

## Termes relatifs aux modèles de langage

| Terme | Définition | Exemple |
|-------|------------|---------|
| **Token** | Unité de base du texte pour les modèles de langage | Mot, sous-mot ou caractère |
| **Tokenization** | Processus de découpage du texte en tokens | "Je suis prêt" → ["Je", "suis", "prêt"] |
| **Prompt** | Texte initial fourni à un modèle de langage pour guider sa génération | "Rédige un poème sur le printemps:" |
| **Context window** | Nombre maximum de tokens qu'un modèle peut traiter en une fois | GPT-4 a une fenêtre contextuelle de 8k-32k tokens |
| **Attention** | Mécanisme permettant au modèle de se concentrer sur différentes parties de l'entrée | Self-attention dans les Transformers |
| **Fine-tuning** | Adaptation d'un modèle pré-entraîné à une tâche spécifique | Ajuster GPT pour une tâche de customer support |
| **Few-shot learning** | Capacité d'apprendre avec peu d'exemples | Donner 2-3 exemples dans le prompt pour guider le modèle |

## Frameworks et outils

| Terme | Définition | Cas d'utilisation |
|-------|------------|-------------------|
| **TensorFlow** | Framework de ML développé par Google | Déploiement en production, applications mobiles |
| **PyTorch** | Framework de ML développé par Facebook | Recherche, prototypage rapide |
| **Keras** | API de haut niveau s'exécutant sur TensorFlow | Développement rapide de prototypes |
| **Hugging Face** | Bibliothèque pour les modèles de NLP pré-entraînés | Utilisation de BERT, GPT et autres modèles de langage |
| **ONNX** | Format d'échange pour modèles de ML | Interopérabilité entre frameworks |
| **TensorBoard** | Outil de visualisation pour TensorFlow | Suivi des métriques d'entraînement |
| **MLflow** | Plateforme pour gérer le cycle de vie des modèles ML | Suivi des expériences, gestion des modèles |

## Applications du Deep Learning

| Application | Description | Architecture typique |
|-------------|-------------|----------------------|
| **Computer Vision** | Analyse et compréhension d'images et vidéos | CNN (ResNet, YOLO, EfficientNet) |
| **Natural Language Processing** | Traitement et génération de texte | Transformers (BERT, GPT, T5) |
| **Speech Recognition** | Conversion de parole en texte | RNN, Transformers (Wav2Vec) |
| **Recommendation Systems** | Suggestion de contenu personnalisé | Réseaux de neurones profonds, embeddings |
| **Generative AI** | Création de contenu nouveau (images, texte, audio) | GANs, Diffusion Models, Transformers |
| **Reinforcement Learning** | Apprentissage par essai-erreur et récompense | Deep Q-Networks, Policy Gradients |
| **Time Series Analysis** | Prédiction de valeurs futures dans des séquences temporelles | LSTM, Transformers temporels |

---

Ce glossaire regroupe les termes essentiels du Deep Learning. Il est conçu pour servir de référence rapide pendant votre parcours d'apprentissage. N'hésitez pas à y revenir chaque fois que vous rencontrez un terme non familier dans les autres modules du cours.