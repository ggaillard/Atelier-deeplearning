{
  "concepts": [
    {
      "id": "dl_basics",
      "title": "Concepts fondamentaux du Deep Learning",
      "description": "Principes de base qui définissent le Deep Learning et le distinguent du Machine Learning classique",
      "subconcepts": [
        {
          "id": "neural_network",
          "title": "Réseau de neurones artificiel",
          "definition": "Un réseau de neurones artificiel est un modèle de calcul inspiré du fonctionnement des neurones biologiques. Il est composé de nœuds (neurones) interconnectés qui transforment des entrées en sorties via des pondérations et des fonctions d'activation.",
          "details": {
            "beginner": "Un réseau de neurones artificiel fonctionne comme un système de traitement d'information composé d'unités (neurones) connectées entre elles. Chaque connexion a un poids qui peut être ajusté durant l'apprentissage. On peut le visualiser comme un ensemble de nœuds organisés en couches.",
            "intermediate": "Les réseaux de neurones artificiels sont des approximateurs universels capables de modéliser des fonctions complexes. Ils utilisent des connexions pondérées et des fonctions d'activation non-linéaires pour transformer les données d'entrée en sorties prédictives.",
            "advanced": "Les réseaux de neurones sont des graphes dirigés où chaque nœud calcule une fonction de la forme f(Σ(w_i * x_i) + b) où w_i représente les poids, x_i les entrées, b le biais, et f la fonction d'activation. Leur capacité à apprendre des représentations hiérarchiques est ce qui les distingue particulièrement."
          },
          "examples": [
            "Un réseau à une seule couche peut apprendre à classifier des points dans un espace 2D en traçant une ligne droite (séparation linéaire).",
            "Un réseau multicouche peut apprendre à reconnaître des chiffres manuscrits en détectant progressivement des traits, puis des formes, puis des chiffres complets."
          ],
          "related": ["neuron", "activation_function", "weights_biases", "deep_network"]
        },
        {
          "id": "neuron",
          "title": "Neurone artificiel",
          "definition": "Unité de calcul qui applique une fonction d'activation à une somme pondérée d'entrées pour produire une sortie.",
          "details": {
            "beginner": "Un neurone artificiel fonctionne comme un petit calculateur. Il prend plusieurs entrées, les multiplie par des 'poids' (qui représentent l'importance de chaque entrée), additionne le tout, puis applique une fonction pour déterminer sa sortie.",
            "intermediate": "Le neurone artificiel est l'unité fondamentale de calcul dans un réseau de neurones. Il calcule la somme pondérée de ses entrées plus un biais, puis applique une fonction d'activation non-linéaire pour produire sa sortie.",
            "advanced": "Formellement, un neurone calcule y = f(Σ(w_i * x_i) + b) où w_i sont les poids, x_i les entrées, b le biais et f la fonction d'activation. Cette opération peut être vue comme un produit scalaire suivi d'une transformation non-linéaire."
          },
          "examples": [
            "Un neurone avec fonction d'activation ReLU renvoie la valeur 0 si la somme pondérée des entrées est négative, sinon il renvoie cette somme.",
            "Dans un réseau de classification d'images, un neurone dans la dernière couche pourrait s'activer fortement quand l'image contient un chat."
          ],
          "related": ["activation_function", "weights_biases", "forward_propagation"]
        },
        {
          "id": "weights_biases",
          "title": "Poids et biais",
          "definition": "Les poids déterminent l'importance de chaque entrée d'un neurone, tandis que le biais permet au neurone de s'activer même si toutes les entrées sont nulles.",
          "details": {
            "beginner": "Les poids sont comme des boutons de volume qui amplifient ou diminuent l'importance de chaque information entrante. Le biais est comme un seuil que la somme doit dépasser pour que le neurone s'active.",
            "intermediate": "Les poids représentent la force des connexions entre les neurones et sont le principal mécanisme d'apprentissage. Le biais permet de décaler la fonction d'activation, offrant plus de flexibilité au modèle pour s'adapter aux données.",
            "advanced": "Les poids w et biais b sont les paramètres ajustables du réseau, optimisés pendant l'entraînement via la descente de gradient. Géométriquement, les poids définissent l'orientation d'un hyperplan de décision, tandis que le biais détermine son offset par rapport à l'origine."
          },
          "examples": [
            "Un poids élevé (ex: 2.5) signifie que cette entrée a une grande influence sur la sortie du neurone.",
            "Un biais négatif (-1.0) rend le neurone plus 'réticent' à s'activer, exigeant des entrées plus fortes."
          ],
          "related": ["neuron", "gradient_descent", "backpropagation"]
        },
        {
          "id": "activation_function",
          "title": "Fonction d'activation",
          "definition": "Fonction non-linéaire appliquée à la somme pondérée des entrées d'un neurone pour introduire de la complexité et permettre au réseau d'apprendre des relations non-linéaires.",
          "details": {
            "beginner": "Les fonctions d'activation transforment la sortie d'un neurone, généralement en la limitant à un certain intervalle comme [0,1] ou [-1,1]. Sans elles, les réseaux ne pourraient modéliser que des relations linéaires.",
            "intermediate": "Les fonctions d'activation introduisent la non-linéarité nécessaire pour que le réseau puisse approximer des fonctions complexes. Les plus courantes sont ReLU, Sigmoid et Tanh, chacune avec ses avantages spécifiques.",
            "advanced": "Le choix de la fonction d'activation influence grandement les propriétés du gradient durant l'apprentissage. ReLU résout partiellement le problème de la disparition du gradient présent dans Sigmoid et Tanh, mais introduit le problème du 'dying ReLU' où des neurones peuvent devenir inactifs."
          },
          "examples": [
            "ReLU (Rectified Linear Unit): f(x) = max(0, x) - Renvoie x si positif, 0 sinon",
            "Sigmoid: f(x) = 1/(1+e^(-x)) - Transforme les valeurs entre 0 et 1",
            "Tanh: f(x) = (e^x - e^(-x))/(e^x + e^(-x)) - Transforme les valeurs entre -1 et 1"
          ],
          "related": ["neuron", "relu", "sigmoid", "tanh"]
        },
        {
          "id": "layer",
          "title": "Couche de neurones",
          "definition": "Groupe de neurones qui traitent l'information au même niveau d'abstraction dans un réseau de neurones.",
          "details": {
            "beginner": "Une couche est comme une équipe de neurones qui travaillent ensemble au même niveau. Différentes couches se spécialisent dans la détection de différentes caractéristiques.",
            "intermediate": "Les couches forment une hiérarchie de transformations, chacune extrayant des caractéristiques de plus en plus abstraites. Les couches profondes combinent les motifs détectés par les couches précédentes.",
            "advanced": "Formellement, une couche applique une transformation de la forme f(W·x + b) où W est une matrice de poids, x le vecteur d'entrée, b le vecteur de biais et f la fonction d'activation. L'architecture en couches permet la factorisation hiérarchique des représentations."
          },
          "examples": [
            "Dans un réseau de reconnaissance d'images, les premières couches détectent des bords et des textures, les couches intermédiaires des formes, et les dernières couches des objets complets.",
            "Un réseau pour la traduction automatique aurait une couche d'entrée pour les mots de la langue source, des couches cachées pour l'analyse, et une couche de sortie pour générer les mots dans la langue cible."
          ],
          "related": ["input_layer", "hidden_layer", "output_layer", "deep_network"]
        },
        {
          "id": "hidden_layer",
          "title": "Couche cachée",
          "definition": "Couche située entre la couche d'entrée et la couche de sortie, où se fait l'extraction des caractéristiques complexes.",
          "details": {
            "beginner": "Les couches cachées sont comme les étapes intermédiaires du cerveau pour analyser l'information. Elles transforment les données brutes en caractéristiques de plus en plus utiles pour la tâche finale.",
            "intermediate": "Ces couches apprennent des représentations abstraites des données qui ne sont pas directement observables. Un réseau avec plusieurs couches cachées peut apprendre des hiérarchies de caractéristiques complexes.",
            "advanced": "Les représentations apprises dans les couches cachées forment un espace latent qui capture la structure sous-jacente des données. L'augmentation du nombre de couches cachées accroît la capacité du réseau à modéliser des fonctions complexes, mais augmente aussi le risque de surapprentissage."
          },
          "examples": [
            "Dans un réseau reconnaissant des visages, une couche cachée pourrait se spécialiser dans la détection des yeux, une autre dans celle du nez, etc.",
            "Pour un réseau analysant des textes, les couches cachées peuvent capturer progressivement la syntaxe, puis la sémantique, puis le contexte plus large."
          ],
          "related": ["layer", "feature_extraction", "deep_network", "representation_learning"]
        },
        {
          "id": "forward_propagation",
          "title": "Propagation avant",
          "definition": "Processus de calcul de la sortie d'un réseau de neurones à partir des entrées, en propageant les valeurs à travers toutes les couches du réseau.",
          "details": {
            "beginner": "La propagation avant est comme une chaîne de montage: les données entrent d'un côté, passent par chaque couche de neurones qui les transforment, et ressortent sous forme de prédiction finale.",
            "intermediate": "Durant la propagation avant, chaque neurone calcule sa sortie en fonction des sorties de la couche précédente. Ces calculs sont effectués couche par couche, de l'entrée vers la sortie, pour produire la prédiction finale.",
            "advanced": "Mathématiquement, pour chaque couche l, on calcule a^(l) = f(W^(l)·a^(l-1) + b^(l)) où a^(l) représente les activations de la couche l, W^(l) la matrice de poids, b^(l) le vecteur de biais, et f la fonction d'activation. Ce processus est efficacement implémenté via des opérations matricielles."
          },
          "examples": [
            "Pour classifier une image de chat, la propagation avant transforme les pixels bruts en valeurs d'activation de plus en plus abstraites jusqu'à obtenir un score élevé pour la classe 'chat'.",
            "Dans un réseau de traduction, la propagation avant convertit progressivement la phrase source en une représentation interne puis en la phrase cible."
          ],
          "related": ["backpropagation", "inference", "activation_function"]
        }
      ]
    },
    {
      "id": "learning_concepts",
      "title": "Concepts d'apprentissage",
      "description": "Mécanismes et techniques qui permettent aux réseaux de neurones d'apprendre à partir des données",
      "subconcepts": [
        {
          "id": "gradient_descent",
          "title": "Descente de gradient",
          "definition": "Algorithme d'optimisation qui ajuste itérativement les poids d'un réseau pour minimiser l'erreur de prédiction.",
          "details": {
            "beginner": "La descente de gradient est comme descendre une colline dans le brouillard en suivant la pente. À chaque pas, on ressent la direction de la pente et on avance dans cette direction pour atteindre le point le plus bas (erreur minimale).",
            "intermediate": "Cet algorithme calcule le gradient (la direction de la pente la plus raide) de la fonction de perte par rapport aux poids du réseau. Il ajuste ensuite les poids dans la direction opposée au gradient pour minimiser l'erreur.",
            "advanced": "À chaque itération, les poids sont mis à jour selon la règle w_new = w_old - η∇L(w) où η est le taux d'apprentissage et ∇L(w) le gradient de la fonction de perte L par rapport aux poids w. La descente par mini-batch offre un compromis entre la descente stochastique (bruitée mais rapide) et la descente par batch (précise mais lente)."
          },
          "examples": [
            "L'algorithme Adam est une version améliorée de la descente de gradient qui adapte le taux d'apprentissage pour chaque paramètre.",
            "La descente de gradient par mini-batch traite de petits lots d'exemples à la fois, offrant un bon compromis entre vitesse et stabilité."
          ],
          "related": ["learning_rate", "optimization", "backpropagation", "loss_function"]
        },
        {
          "id": "backpropagation",
          "title": "Rétropropagation",
          "definition": "Algorithme qui calcule le gradient de l'erreur par rapport à chaque poids du réseau en propageant l'erreur de la sortie vers l'entrée.",
          "details": {
            "beginner": "La rétropropagation est comme un système de feedback qui indique à chaque neurone comment il devrait changer pour améliorer le résultat final. L'erreur est propagée à rebours depuis la sortie vers chaque neurone des couches précédentes.",
            "intermediate": "Cet algorithme utilise la règle de chaîne du calcul différentiel pour calculer efficacement comment chaque poids influence l'erreur finale. Il permet d'attribuer à chaque poids sa part de responsabilité dans l'erreur totale.",
            "advanced": "Pour chaque poids w_ij, on calcule ∂L/∂w_ij en propageant à rebours le gradient de l'erreur. Cette technique exploite la structure en couches du réseau pour factoriser les calculs, réduisant la complexité de O(n²) à O(n) où n est le nombre de poids."
          },
          "examples": [
            "Si un réseau prédit qu'une image contient un chien avec 90% de confiance alors que c'est un chat, la rétropropagation ajustera davantage les poids qui ont le plus contribué à cette erreur.",
            "Les techniques modernes comme le momentum et la normalisation par lots améliorent la stabilité de la rétropropagation, accélérant ainsi la convergence."
          ],
          "related": ["gradient_descent", "chain_rule", "optimization", "learning_rate"]
        },
        {
          "id": "loss_function",
          "title": "Fonction de perte",
          "definition": "Mesure de l'écart entre les prédictions du modèle et les valeurs réelles, utilisée pour guider l'apprentissage.",
          "details": {
            "beginner": "La fonction de perte (ou coût) est comme un score qui indique à quel point le modèle se trompe. Plus la valeur est basse, meilleur est le modèle. L'entraînement vise à minimiser cette fonction.",
            "intermediate": "Cette fonction quantifie la différence entre les sorties prédites et les valeurs cibles. Elle est choisie en fonction du type de problème (classification, régression) et guide l'optimisation des paramètres du réseau.",
            "advanced": "Le choix de la fonction de perte définit l'espace des solutions et influence significativement la convergence. L'entropie croisée est optimale pour la classification car elle pénalise davantage les prédictions confiantes mais incorrectes, tandis que l'erreur quadratique moyenne convient mieux à la régression."
          },
          "examples": [
            "Entropie croisée (classification): L = -Σ[y_i log(p_i)] - Mesure l'écart entre distributions de probabilités",
            "Erreur quadratique moyenne (régression): L = (1/n)Σ(y_i - ŷ_i)² - Mesure la moyenne des carrés des erreurs"
          ],
          "related": ["gradient_descent", "optimization", "cross_entropy", "mse"]
        },
        {
          "id": "learning_rate",
          "title": "Taux d'apprentissage",
          "definition": "Paramètre qui contrôle l'ampleur des ajustements de poids à chaque itération de la descente de gradient.",
          "details": {
            "beginner": "Le taux d'apprentissage est comme la taille des pas que fait l'algorithme pour descendre la colline d'erreur. Un taux trop grand peut faire dépasser le minimum, un taux trop petit rend la progression très lente.",
            "intermediate": "Ce paramètre détermine dans quelle mesure les poids sont ajustés à chaque itération. Sa valeur optimale dépend de la forme de la fonction de perte et évolue souvent au cours de l'entraînement.",
            "advanced": "Le choix du taux d'apprentissage implique un compromis: trop élevé, et les mises à jour oscillent ou divergent; trop faible, et la convergence est lente ou s'arrête dans des minima locaux. Les techniques adaptatives (Adam, RMSprop) ajustent automatiquement le taux pour chaque paramètre en fonction de l'historique des gradients."
          },
          "examples": [
            "Un taux d'apprentissage courant est 0.001, mais les valeurs optimales varient entre 0.1 et 0.00001 selon les applications.",
            "La diminution progressive du taux d'apprentissage (learning rate decay) permet des ajustements grossiers au début et fins à la fin de l'entraînement."
          ],
          "related": ["gradient_descent", "optimization", "hyperparameters", "learning_rate_decay"]
        },
        {
          "id": "epoch",
          "title": "Époque",
          "definition": "Un passage complet à travers l'ensemble des données d'entraînement durant l'apprentissage d'un modèle.",
          "details": {
            "beginner": "Une époque est un cycle complet d'entraînement où le modèle voit chaque exemple une fois. L'apprentissage se fait généralement sur plusieurs époques, le modèle s'améliorant progressivement.",
            "intermediate": "À chaque époque, le modèle traite tous les exemples d'entraînement, calcule les gradients, et met à jour ses paramètres. Les performances sur les données de validation sont souvent évaluées à la fin de chaque époque.",
            "advanced": "Le nombre optimal d'époques dépend de la complexité du problème, de la taille du dataset, et de la propension du modèle au surapprentissage. L'arrêt précoce (early stopping) utilise les performances sur un ensemble de validation pour déterminer quand cesser l'entraînement."
          },
          "examples": [
            "Un modèle de reconnaissance d'images sur MNIST peut atteindre 95% de précision après seulement 5 époques, mais nécessiter 20 époques pour atteindre 99%.",
            "Pour les très grands jeux de données, une seule époque peut suffire, tandis que pour les petits jeux de données, des centaines d'époques peuvent être nécessaires."
          ],
          "related": ["batch", "iteration", "overfitting", "early_stopping"]
        },
        {
          "id": "batch",
          "title": "Batch",
          "definition": "Sous-ensemble des données traité avant une mise à jour des poids du réseau.",
          "details": {
            "beginner": "Un batch est comme une portion de données que le modèle traite avant d'ajuster ses paramètres. Au lieu d'examiner tous les exemples d'un coup, le réseau les traite par petits groupes.",
            "intermediate": "L'utilisation de batches permet d'équilibrer la précision des mises à jour et la vitesse d'entraînement. Les batches introduisent également une forme de régularisation stochastique qui peut améliorer la généralisation.",
            "advanced": "La taille du batch influence la dynamique d'optimisation: des batches plus grands donnent des estimations de gradient plus précises mais requièrent plus de mémoire; des batches plus petits introduisent plus de bruit, ce qui peut aider à échapper aux minima locaux, mais ralentit la convergence."
          },
          "examples": [
            "Une taille de batch typique est 32 ou 64, mais peut varier de 1 (descente de gradient stochastique) à la taille complète du jeu de données (descente de gradient par batch).",
            "L'utilisation d'une taille de batch adaptée aux capacités matérielles (mémoire GPU) est essentielle pour optimiser l'entraînement."
          ],
          "related": ["epoch", "iteration", "sgd", "mini_batch_gradient_descent"]
        },
        {
          "id": "overfitting",
          "title": "Surapprentissage",
          "definition": "Situation où le modèle performe bien sur les données d'entraînement mais mal sur de nouvelles données, ayant mémorisé les exemples au lieu de généraliser.",
          "details": {
            "beginner": "Le surapprentissage est comme apprendre par cœur les réponses d'un examen sans comprendre les principes sous-jacents. Le modèle devient excellent sur les exemples vus, mais échoue face à de nouveaux cas.",
            "intermediate": "Ce phénomène se produit lorsque le modèle capture le bruit dans les données d'entraînement plutôt que les tendances générales. Il se manifeste par un écart croissant entre les performances sur les données d'entraînement et de validation.",
            "advanced": "Du point de vue statistique, le surapprentissage survient lorsque le modèle a trop de capacité (degrés de liberté) par rapport à la complexité inhérente du problème et à la quantité de données disponibles. Il peut être analysé via le compromis biais-variance."
          },
          "examples": [
            "Un modèle qui atteint 99% de précision sur les données d'entraînement mais seulement 70% sur les données de test est probablement en surapprentissage.",
            "Les techniques de régularisation comme le dropout, la normalisation par lots et la régularisation L1/L2 sont conçues pour atténuer le surapprentissage."
          ],
          "related": ["regularization", "dropout", "early_stopping", "bias_variance_tradeoff"]
        },
        {
          "id": "regularization",
          "title": "Régularisation",
          "definition": "Techniques pour prévenir le surapprentissage en introduisant des contraintes ou des pénalités sur les paramètres du modèle.",
          "details": {
            "beginner": "La régularisation est comme imposer des règles supplémentaires au modèle pour l'empêcher de mémoriser les exemples. Elle force le modèle à trouver des solutions plus simples et généralisables.",
            "intermediate": "Ces techniques ajoutent des termes de pénalité à la fonction de perte ou modifient le processus d'entraînement pour limiter la complexité du modèle et améliorer sa capacité à généraliser.",
            "advanced": "La régularisation peut être vue comme l'introduction d'un a priori bayésien sur la distribution des paramètres. Les méthodes comme L1 induisent la parcimonie (beaucoup de poids à zéro), tandis que L2 favorise des poids de faible magnitude, se traduisant par des frontières de décision plus lisses."
          },
          "examples": [
            "L1 (Lasso): Ajoute un terme λΣ|w_i| à la perte, favorisant la sparsité des poids",
            "L2 (Ridge): Ajoute un terme λΣw_i² à la perte, contraignant les poids à rester petits",
            "Dropout: Désactive aléatoirement des neurones pendant l'entraînement, forçant le réseau à être redondant"
          ],
          "related": ["overfitting", "dropout", "l1_regularization", "l2_regularization", "early_stopping"]
        }
      ]
    },
    {
      "id": "network_architecture",
      "title": "Architectures de réseaux",
      "description": "Différentes structures de réseaux de neurones spécialisées pour divers types de problèmes",
      "subconcepts": [
        {
          "id": "cnn",
          "title": "Réseau de neurones convolutif (CNN)",
          "definition": "Type de réseau spécialisé dans le traitement des données en grille comme les images, utilisant des opérations de convolution pour détecter des motifs spatiaux.",
          "details": {
            "beginner": "Les CNN sont des réseaux spécialisés pour analyser les images. Ils utilisent des filtres qui 'glissent' sur l'image pour détecter des motifs comme les contours, les textures, puis des formes plus complexes.",
            "intermediate": "Ces réseaux exploitent trois idées clés: les connexions locales (chaque neurone voit seulement une petite région), le partage de paramètres (les mêmes filtres sont appliqués partout), et la mise en commun (pooling) pour réduire la dimensionnalité tout en préservant les caractéristiques importantes.",
            "advanced": "L'opération de convolution peut être vue comme un produit de tenseurs avec un noyau partagé, ce qui réduit considérablement le nombre de paramètres par rapport à un réseau entièrement connecté. Cette inductive bias de localité et d'invariance à la translation est particulièrement adaptée aux données visuelles."
          },
          "examples": [
            "LeNet-5 (1998): Premier CNN efficace, utilisé pour la reconnaissance de chiffres manuscrits",
            "ResNet (2015): Architecture introduisant les connexions résiduelles pour entraîner des réseaux très profonds",
            "EfficientNet (2019): Famille de CNN optimisés pour le rapport performance/nombre de paramètres"
          ],
          "related": ["convolution", "pooling", "image_recognition", "feature_map"]
        },
        {
          "id": "rnn",
          "title": "Réseau de neurones récurrent (RNN)",
          "definition": "Type de réseau spécialisé dans le traitement des séquences, avec des connexions qui forment des cycles permettant de maintenir un état interne (mémoire).",
          "details": {
            "beginner": "Les RNN sont comme des réseaux avec mémoire: ils retiennent des informations sur ce qu'ils ont vu précédemment dans la séquence. Cela les rend parfaits pour analyser du texte, de la parole ou toute donnée séquentielle.",
            "intermediate": "Contrairement aux réseaux feed-forward, les RNN partagent des paramètres à travers le temps et maintiennent un état caché qui est mis à jour à chaque pas de temps. Cette récurrence leur permet de capturer des dépendances temporelles.",
            "advanced": "Un RNN classique calcule h_t = tanh(W_h·h_{t-1} + W_x·x_t + b) où h_t est l'état caché au temps t, x_t l'entrée au temps t, et W_h, W_x, b les paramètres appris. Cette formulation souffre du problème de disparition/explosion du gradient sur les longues séquences, ce qui a motivé le développement des architectures LSTM et GRU."
          },
          "examples": [
            "Un RNN peut prédire le prochain mot dans une phrase en se basant sur les mots précédents",
            "Les RNN sont utilisés dans la traduction automatique, la génération de texte, et la reconnaissance vocale",
            "LSTM et GRU sont des variantes améliorées des RNN capables de capturer des dépendances à plus long terme"
          ],
          "related": ["lstm", "gru", "sequence_modeling", "vanishing_gradient"]
        },
        {
          "id": "lstm",
          "title": "Long Short-Term Memory (LSTM)",
          "definition": "Variante avancée de RNN conçue pour capturer les dépendances à long terme dans les séquences grâce à des mécanismes de portes qui contrôlent le flux d'information.",
          "details": {
            "beginner": "Les LSTM sont comme des RNN avec une mémoire améliorée. Ils utilisent des 'portes' spéciales qui décident quelles informations conserver, oublier ou mettre à jour, permettant ainsi de retenir des informations importantes sur de longues périodes.",
            "intermediate": "L'architecture LSTM introduit un état cellulaire distinct de l'état caché, ainsi que trois portes (d'entrée, d'oubli et de sortie) qui contrôlent le