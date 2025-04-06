Voici le glossaire du Deep Learning avec des liens vers les définitions des termes techniques mentionnés :
## Glossaire du Deep Learning

### Termes fondamentaux

| **Terme** | **Définition** | **Exemple concret** |
|-----------|----------------|---------------------|
| **Deep Learning** | Sous-domaine du Machine Learning utilisant des réseaux de neurones à plusieurs couches pour modéliser des abstractions de haut niveau dans les données. | Reconnaissance d'objets dans des photos. |
| **Réseau de neurones** | Système inspiré du cerveau humain composé de nœuds (neurones) interconnectés qui traitent les informations. | Réseau capable de reconnaître des chiffres manuscrits. |
| **Neurone artificiel** | Unité de calcul de base dans un réseau de neurones qui reçoit des entrées, applique une transformation et produit une sortie. | Un neurone qui s'active quand il détecte un contour vertical. |
| **Couche** | Ensemble de neurones situés au même niveau dans le réseau. | Couche d'entrée, couche cachée, couche de sortie. |
| **Poids** | Valeurs numériques qui définissent l'importance relative de chaque connexion entre les neurones. | Un poids élevé (ex: 0.8) indique une forte influence. |
| **Biais** | Valeur ajoutée à la somme pondérée des entrées d'un neurone pour ajuster le seuil d'activation. | Permet à un neurone de s'activer même si toutes les entrées sont nulles. |
| **Fonction d'activation** | Fonction mathématique qui détermine la sortie d'un neurone en fonction de ses entrées. | [ReLU](#relu), [Sigmoid](#sigmoid), [Tanh](#tanh). |

### Architectures de réseaux

| **Terme** | **Définition** | **Cas d'utilisation** |
|-----------|----------------|-----------------------|
| **Réseau dense** | Réseau où chaque neurone est connecté à tous les neurones de la couche précédente. | Classification d'images simples, prédiction de valeurs. |
| **Réseau convolutif (CNN)** | Réseau spécialisé dans le traitement des données en grille comme les images, utilisant des filtres pour détecter des caractéristiques. | Reconnaissance d'objets, classification d'images. |
| **Réseau récurrent (RNN)** | Réseau avec des connexions formant des cycles, adapté aux données séquentielles. | Traduction automatique, génération de texte. |
| **LSTM/GRU** | Types de RNN capables de mémoriser l'information sur de longues séquences grâce à des mécanismes de mémoire. | Analyse de texte long, prédiction de séries temporelles. |
| **Transformer** | Architecture basée sur des mécanismes d'attention, sans récurrence, permettant de traiter les données en parallèle. | Modèles de langage avancés comme [GPT](#gpt), [BERT](#bert), Mistral. |
| **Autoencoder** | Réseau qui apprend à encoder puis décoder les données pour réduire la dimensionnalité ou détecter des anomalies. | Réduction de dimensionnalité, détection d'anomalies. |
| **GAN (Generative Adversarial Network)** | Deux réseaux en compétition : un générateur crée des données et un discriminateur essaie de les distinguer des données réelles. | Création d'images réalistes, deepfakes. |

### Apprentissage

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Forward propagation** | Passage des données d'entrée à travers le réseau pour produire une prédiction. | Calcul de la sortie d'un modèle pour une image d'entrée. |
| **Loss (perte)** | Mesure de l'écart entre les prédictions du modèle et les valeurs réelles. | Erreur quadratique moyenne, entropie croisée. |
| **Backpropagation** | Algorithme qui calcule le gradient de l'erreur par rapport aux poids du réseau pour les ajuster. | Calcul de la contribution de chaque poids à l'erreur totale. |
| **Descente de gradient** | Algorithme d'optimisation qui ajuste les poids du réseau pour minimiser l'erreur. | Modification itérative des poids dans la direction du gradient négatif. |
| **Époque** | Un passage complet à travers l'ensemble des données d'entraînement. | Entraîner un modèle pendant 10 époques. |
| **Batch** | Sous-ensemble des données traité avant une mise à jour des poids. | Traiter les données par lots de 32 exemples. |
| **Optimiseur** | Algorithme qui implémente la descente de gradient pour ajuster les poids du réseau. | [Adam](#adam), [SGD](#sgd), [RMSprop](#rmsprop). |
| **Learning rate** | Taux qui contrôle l'ampleur des ajustements des poids lors de l'entraînement. | Trop élevé : divergence, trop faible : apprentissage lent. |

### Techniques spécifiques

| **Terme** | **Définition** | **Utilisation** |
|-----------|----------------|-----------------|
| **Transfer learning** | Réutilisation d'un modèle pré-entraîné sur une nouvelle tâche pour bénéficier de ses connaissances. | Adapter un modèle [ImageNet](#imagenet) pour reconnaître des maladies de plantes. |
| **Fine-tuning** | Ajustement d'un modèle pré-entraîné sur des données spécifiques pour améliorer ses performances sur une tâche particulière. | Réentraîner les dernières couches d'un modèle [BERT](#bert) pour la classification de texte. |
| **Data augmentation** | Génération de nouvelles données d'entraînement par transformation des données existantes pour augmenter la diversité. | Rotation, mise à l'échelle, distorsion d'images. |
| **Dropout** | Technique où des neurones sont aléatoirement désactivés pendant l'entraînement pour réduire l'overfitting. | Force le réseau à être redondant et robuste. |
| **Batch normalization** | Normalisation des activations d'une couche pour stabiliser et accélérer l'apprentissage. | Améliore la convergence et permet d'utiliser des taux d'apprentissage plus élevés. |
| **Early stopping** | Arrêt de l'entraînement quand les performances sur la validation cessent de s'améliorer pour éviter l'overfitting. | Empêche le surajustement aux données d'entraînement. |
| **Embedding** | Conversion de données catégorielles en vecteurs denses pour les représenter dans un espace continu. | Word embeddings dans le NLP ([Word2Vec](#word2vec), [GloVe](#glove)). |

### Convolutions et CNN

| **Terme** | **Définition** | **Rôle** |
|-----------|----------------|----------|
| **Filtre (kernel)** | Matrice de poids appliquée à une région de l'image pour détecter des caractéristiques spécifiques. | Détecte des caractéristiques spécifiques (bords, textures). |
| **Feature map** | Sortie d'un filtre de convolution appliqué à une image, représentant les caractéristiques détectées. | Carte d'activation des caractéristiques détectées. |
| **Pooling** | Opération de sous-échantillonnage réduisant les dimensions de la feature map pour généraliser les caractéristiques. | Réduit la complexité computationnelle et contrôle l'overfitting. |
| **Padding** | Ajout de pixels (généralement zéros) aux bords d'une image pour conserver les dimensions après convolution. | Permet de conserver les dimensions de l'image après l'application des filtres. |
| **Stride** | Pas de déplacement du filtre sur l'image, contrôlant le chevauchement des champs réceptifs. | Contrôle la taille de la feature map et la quantité de chevauchement. |

### Métriques d'évaluation

| **Métrique** | **Définition** | **Cas d'usage** |
|--------------|----------------|-----------------|
| **Accuracy** | Proportion de prédictions correctes parmi toutes les prédictions. | Classification équilibrée. |
| **Precision** | Proportion des prédictions positives qui sont correctes. | Quand les faux positifs sont coûteux. |
| **Recall** | Proportion des cas positifs réels correctement identifiés. | Quand les faux négatifs sont coûteux. |
| **F1-Score** | Moyenne harmonique de la précision et du rappel, équilibrant les deux métriques. | Classification avec classes déséquilibrées. |
| **ROC-AUC** | Aire sous la courbe ROC, mesurant la qualité de la discrimination entre les classes. | Évaluation des modèles de classification. |
| **MAE (Mean Absolute Error)** | Moyenne des valeurs absolues des erreurs entre les prédictions et les valeurs réelles. | Régression, quand les écarts importants ne sont pas surpondérés. |
| **RMSE (Root Mean Squared Error)** | Racine carrée de la moyenne des carrés des erreurs entre les prédictions et les valeurs réelles. | Régression, pénalise davantage les grands écarts. |

### Problèmes courants

| **Terme** | **Définition** | **Solution possible** |
|-----------|----------------|-----------------------|
| **Overfitting** | Le modèle apprend trop bien les données d'entraînement au détriment de la généralisation sur de nouvelles données. | Régularisation, dropout, plus de données. |
| **Underfitting** | Le modèle est trop simple pour capturer la complexité des données, résultant en de mauvaises performances. | Augmenter la complexité du modèle, entraîner plus longtemps. |
| **Vanishing gradient** | Problème où le gradient devient très petit, ralentissant l'apprentissage dans les couches profondes. | Utiliser [ReLU](#relu), [LSTM](#lstm), initialisation des poids adaptée. |
| **Exploding gradient** | Problème où le gradient devient très grand, déstabilisant l'apprentissage. | Gradient clipping, normalisation des poids. |
| **Imbalanced data** | Jeu de données où certaines classes sont beaucoup plus fréquentes que d'autres, biaisant le modèle. | Rééchantillonnage, pondération des classes, techniques d'augmentation. |

### Termes relatifs aux modèles de langage

| **Terme** | **Définition** | **Exemple** |
|-----------|----------------|-------------|
| **Token** | Unité de base du texte pour les modèles de langage, comme un mot, sous-mot ou caractère. | "Je suis prêt" → ["Je", "suis", "prêt"]. |
| **Tokenization** | Processus de découpage du texte en tokens pour les traiter dans un modèle de langage. | "Je suis prêt" → ["Je", "suis", "prêt"]. |
| **Prompt** | Texte initial fourni à un modèle de langage pour guider sa génération de texte. | "Rédige un poème sur le printemps:". |
| **Context window** | Nombre maximum de tokens qu'un modèle peut traiter en une fois, déterminant la quantité d'information contextuelle. | [GPT-4](#gpt-4) a une fenêtre contextuelle de 8k-32k tokens. |
| **Attention** | Mécanisme permettant au modèle de se concentrer sur différentes parties de l'entrée pour générer une sortie pertinente. | Self-attention dans les Transformers. |
| **Fine-tuning** | Adaptation d'un modèle pré-entraîné à une tâche spécifique en ajustant ses poids sur des données spécifiques. | Ajuster [GPT](#gpt) pour une tâche de customer support. |
| **Few-shot learning** | Capacité d'un modèle à apprendre à partir de très peu d'exemples, souvent en fournissant quelques exemples dans le prompt. | Donner 2-3 exemples dans le prompt pour guider le modèle. |

### Frameworks et outils

| **Terme** | **Définition** | **Cas d'utilisation** |
|-----------|----------------|-----------------------|
| **TensorFlow** | Framework de Machine Learning développé par Google, utilisé pour créer et entraîner des modèles de Deep Learning. | Déploiement en production, applications mobiles. |
| **PyTorch** | Framework de Machine Learning développé par Facebook, connu pour sa flexibilité et sa facilité d'utilisation. | Recherche, prototypage rapide. |
| **Keras** | API de haut niveau s'exécutant sur TensorFlow, facilitant le développement rapide de modèles de Deep Learning. | Développement rapide de prototypes. |
| **Hugging Face** | Bibliothèque pour les modèles de NLP pré-entraînés, facilitant leur utilisation et leur fine-tuning. | Utilisation de [BERT](#bert), [GPT](#gpt) et autres modèles de langage. |
| **ONNX** | Format d'échange pour modèles de Machine Learning, permettant l'interopérabilité entre différents frameworks. | Transfert de modèles entre TensorFlow, PyTorch, etc. |
| **TensorBoard** | Outil de visualisation pour TensorFlow, permettant de suivre les métriques d'entraînement et de visualiser les graphes de modèles. | Suivi des métriques d'entraînement. |
| **MLflow** | Plateforme pour gérer le cycle de vie des modèles de Machine Learning, incluant le suivi des expériences et la gestion des modèles. | Suivi des expériences, gestion des modèles. |

### Applications du Deep Learning

| **Application** | **Description** | **Architecture typique** |
|-----------------|-----------------|--------------------------|
| **Computer Vision** | Domaine du Deep Learning dédié à l'analyse et la compréhension d'images et de vidéos. | CNN ([ResNet](#resnet), [YOLO](#yolo), [EfficientNet](#efficientnet)). |
| **Natural Language Processing (NLP)** | Domaine du Deep Learning dédié au traitement et à la génération de texte. | Transformers ([BERT](#bert), [GPT](#gpt), T5). |
| **Speech Recognition** | Conversion de la parole en texte à l'aide de modèles de Deep Learning. | RNN, Transformers ([Wav2Vec](#wav2vec)). |
| **Recommendation Systems** | Systèmes qui suggèrent du contenu personnalisé en fonction des préférences de l'utilisateur. | Réseaux de neurones profonds, embeddings. |
| **Generative AI** | Création de contenu nouveau (images, texte, audio) à l'aide de modèles de Deep Learning. | GANs, Diffusion Models, Transformers. |
| **Reinforcement Learning** | Apprentissage par essai-erreur et récompense, où un agent apprend à prendre des décisions pour maximiser une récompense. | Deep Q-Networks, Policy Gradients. |
| **Time Series Analysis** | Prédiction de valeurs futures dans des séquences temporelles à l'aide de modèles de Deep Learning. | LSTM, Transformers temporels. |

---

### Explications des termes techniques

#### Fonctions d'activation

- **ReLU (Rectified Linear Unit)** : Fonction d'activation qui retourne 0 si l'entrée est négative et l'entrée elle-même si elle est positive. Elle est couramment utilisée dans les réseaux de neurones pour introduire de la non-linéarité.
- **Sigmoid** : Fonction d'activation qui mappe les valeurs d'entrée à une plage de 0 à 1, souvent utilisée pour les problèmes de classification binaire.
- **Tanh (Hyperbolic Tangent)** : Fonction d'activation qui mappe les valeurs d'entrée à une plage de -1 à 1, souvent utilisée dans les réseaux récurrents.

#### Optimiseurs

- **Adam (Adaptive Moment Estimation)** : Algorithme d'optimisation qui combine les avantages de deux autres extensions de la descente de gradient stochastique, à savoir AdaGrad et RMSProp. Il est largement utilisé pour entraîner des réseaux de neurones.
- **SGD (Stochastic Gradient Descent)** : Algorithme d'optimisation qui met à jour les poids du réseau en utilisant une estimation stochastique du gradient de la fonction de perte.
- **RMSprop** : Algorithme d'optimisation qui adapte le taux d'apprentissage pour chaque paramètre, ce qui permet de stabiliser et d'accélérer l'entraînement.

#### Modèles de langage

- **Word2Vec** : Modèle de langage qui apprend des représentations vectorielles des mots (embeddings) en utilisant des réseaux de neurones. Il est utilisé pour capturer les relations sémantiques entre les mots.
- **GloVe (Global Vectors for Word Representation)** : Modèle de langage qui apprend des embeddings de mots en utilisant une matrice de co-occurrence des mots dans un corpus.

#### Modèles de reconnaissance vocale

- **Wav2Vec** : Modèle de reconnaissance vocale qui apprend des représentations vectorielles des segments audio en utilisant des réseaux de neurones. Il est utilisé pour convertir la parole en texte.

#### Architectures de réseaux

- **ResNet (Residual Networks)** : Architecture de réseau de neurones convolutifs qui utilise des connexions résiduelles pour permettre l'entraînement de réseaux très profonds sans dégradation des performances.
- **YOLO (You Only Look Once)** : Architecture de réseau de neurones convolutifs utilisée pour la détection d'objets en temps réel. Elle divise l'image en une grille et prédit des boîtes englobantes et des classes pour chaque cellule de la grille.
- **EfficientNet** : Architecture de réseau de neurones convolutifs qui utilise une approche de mise à l'échelle composée pour optimiser la précision et l'efficacité du modèle.

#### Modèles de langage avancés

- **BERT (Bidirectional Encoder Representations from Transformers)** : Modèle de langage basé sur les Transformers qui utilise des mécanismes d'attention bidirectionnelle pour capturer le contexte des mots dans une phrase. Il est largement utilisé pour des tâches de traitement du langage naturel.
- **GPT (Generative Pre-trained Transformer)** : Modèle de langage basé sur les Transformers qui est pré-entraîné sur un grand corpus de texte et peut être fine-tuné pour des tâches spécifiques. Il est utilisé pour la génération de texte et d'autres tâches de traitement du langage naturel.

