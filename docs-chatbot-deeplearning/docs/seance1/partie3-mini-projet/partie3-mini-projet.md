# Phase 3 : Mini-projet collaboratif (1h)

## Objectif

Mettre en pratique vos connaissances en améliorant un modèle de Deep Learning existant, tout en développant vos compétences en résolution de problèmes et en travail d'équipe.

## Challenge d'amélioration d'un modèle (1h)

### Formation des équipes (5 min)

Formez des groupes de 1-2 étudiants. Chaque groupe recevra un lien vers un notebook contenant un modèle de base fonctionnel, mais avec des performances médiocres.

### Présentation du challenge (10 min)

Votre mission : améliorer la performance du modèle de base qui atteint seulement 85% de précision sur le dataset MNIST.

#### Règles du challenge

- Vous avez 40 minutes pour améliorer le modèle
- Vous pouvez modifier l'architecture, les hyperparamètres, la préparation des données
- Chaque groupe doit documenter ses modifications et justifier ses choix
- Le tableau de scores en temps réel affichera la précision de chaque modèle

#### Modèle de base

Le notebook contient un modèle CNN simple avec :
- Une couche de convolution (16 filtres, taille 3x3)
- Une couche de max pooling (2x2)
- Une couche fully connected (128 neurones)
- Une couche de sortie (10 classes)

### Travail en groupe (35 min)

1. **Analyse du modèle de base**
   - Identifiez les points faibles potentiels
   - Faites un plan d'amélioration

2. **Expérimentation**
   - Testez différentes modifications :
     - Nombre de couches de convolution
     - Nombre de filtres
     - Taille des filtres
     - Ajout de dropout
     - Modification du learning rate
   - Documentez chaque essai dans le tableau fourni

3. **Optimisation finale**
   - Sélectionnez vos meilleures modifications
   - Combinez-les pour obtenir le meilleur modèle possible
   - Assurez-vous de pouvoir expliquer votre approche

### Partage des résultats (10 min)

Chaque groupe présente brièvement :
- Les modifications apportées au modèle
- L'amélioration obtenue
- Les difficultés rencontrées et les solutions trouvées

## Tableau de suivi des modifications

Pour chaque modification testée, renseignez les informations suivantes :

| Modification | Description | Précision avant | Précision après | Observations |
|--------------|-------------|-----------------|-----------------|--------------|
| | | | | |
| | | | | |
| | | | | |

## Ressources disponibles

- Fiche récapitulative des architectures CNN
- Guide des bonnes pratiques pour l'amélioration des modèles
- Documentation TensorFlow/Keras

## Conseils pour réussir

- Commencez par des modifications simples pour établir une base de comparaison
- N'hésitez pas à vous inspirer des architectures connues (LeNet, AlexNet, etc.)
- Faites attention à l'overfitting - testez toujours sur l'ensemble de validation
- Collaborez efficacement en répartissant les tâches

[Continuer vers le débrief](../partie4-debrief/partie4-debrief.md)