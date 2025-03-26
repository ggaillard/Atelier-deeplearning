# Quiz : Frameworks de Deep Learning

Ce quiz vous permet d'évaluer vos connaissances sur les frameworks de Deep Learning vus durant la séance 3. 
Répondez aux questions suivantes en choisissant la ou les bonnes réponses.

## Questions à choix multiples

### 1. Parmi ces affirmations sur TensorFlow/Keras, lesquelles sont vraies ?
- [ ] a) TensorFlow et Keras sont deux frameworks complètement indépendants
- [ ] b) Keras est une API de haut niveau qui s'exécute au-dessus de TensorFlow
- [ ] c) TensorFlow ne peut pas être utilisé sans Keras
- [ ] d) Keras permet d'écrire du code plus concis que TensorFlow pur
- [ ] e) TensorFlow est principalement utilisé pour le traitement d'images uniquement

### 2. Quels avantages présentent les modèles pré-entraînés ?
- [ ] a) Ils permettent de gagner du temps de développement
- [ ] b) Ils nécessitent moins de données pour être adaptés à une nouvelle tâche
- [ ] c) Ils fonctionnent uniquement sur des images
- [ ] d) Ils sont généralement plus performants qu'un modèle entraîné from scratch sur un petit dataset
- [ ] e) Ils ne peuvent pas être modifiés une fois téléchargés

### 3. Dans une API Flask pour l'intelligence artificielle, quelles fonctionnalités sont importantes à implémenter ?
- [ ] a) Un endpoint pour les prédictions
- [ ] b) Une documentation des entrées/sorties attendues
- [ ] c) Un prétraitement des données entrantes
- [ ] d) Un stockage permanent de toutes les prédictions
- [ ] e) Une gestion des erreurs appropriée

### 4. Parmi ces techniques, lesquelles permettent d'améliorer les performances d'un modèle de Deep Learning ?
- [ ] a) Augmentation de données
- [ ] b) Transfer learning
- [ ] c) Diminution systématique du learning rate
- [ ] d) Normalisation des entrées
- [ ] e) Utilisation exclusive de modèles avec plus de couches

### 5. Pour intégrer un modèle de Deep Learning dans une application professionnelle, quelles approches sont recommandées ?
- [ ] a) Entraîner le modèle directement sur le serveur de production
- [ ] b) Sauvegarder le modèle entraîné dans un format standardisé (h5, pb, onnx)
- [ ] c) Créer une API REST pour servir les prédictions
- [ ] d) Implémenter une interface pour surveiller les performances du modèle
- [ ] e) Toujours utiliser le GPU même pour l'inférence simple

## Questions à réponse courte

### 6. Expliquez en 2-3 phrases comment vous pourriez adapter un modèle pré-entraîné à votre propre jeu de données.

[Votre réponse ici]

### 7. Quels sont les avantages d'exposer un modèle de ML via une API plutôt que de l'intégrer directement dans une application ?

[Votre réponse ici]

### 8. Citez 3 erreurs courantes à éviter lors du développement d'une application basée sur le Deep Learning.

[Votre réponse ici]

### 9. Comment expliqueriez-vous à un client non technique l'intérêt d'utiliser un modèle pré-entraîné plutôt que d'en créer un de zéro ?

[Votre réponse ici]

### 10. Dans le contexte d'un stage en BTS SIO, comment pourriez-vous valoriser vos compétences en Deep Learning auprès d'une entreprise ?

[Votre réponse ici]

## Corrigé (pour l'enseignant)

### Réponses aux QCM
1. b, d
2. a, b, d
3. a, b, c, e
4. a, b, d
5. b, c, d

### Éléments de réponse aux questions ouvertes

6. Pour adapter un modèle pré-entraîné : congeler les premières couches du modèle qui contiennent les caractéristiques générales, remplacer les dernières couches par des couches adaptées à notre tâche spécifique, puis entraîner uniquement ces nouvelles couches sur notre jeu de données.

7. Avantages d'une API : séparation des préoccupations (front/back), scalabilité indépendante, réutilisation du modèle par plusieurs applications, mise à jour du modèle sans toucher aux applications clientes, isolation des ressources intensives.

8. Erreurs courantes : ne pas normaliser les données d'entrée, utiliser des architectures trop complexes pour le problème, ne pas diviser correctement les données (train/validation/test), ne pas gérer les cas d'erreur dans l'application, déployer sans surveillance des performances.

9. Explication client : Utiliser un modèle pré-entraîné, c'est comme acheter une voiture prête à rouler qu'on personnalise légèrement, plutôt que de construire une voiture entière à partir de pièces détachées. C'est plus rapide, moins coûteux, et souvent plus fiable car le modèle a déjà "appris" sur des millions d'exemples.

10. Valorisation en stage : montrer des exemples concrets d'applications développées (API de reconnaissance d'images, chatbot), expliquer comment ces technologies peuvent résoudre des problèmes business spécifiques, présenter la capacité à intégrer des solutions d'IA dans des applications existantes, mettre en avant la compréhension des limites et possibilités réelles de ces technologies.