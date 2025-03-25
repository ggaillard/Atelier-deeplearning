# Phase 2 : Découverte des concepts par l'expérimentation (1h30)

![Comparaison Machine Learning vs Deep Learning](https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la phase

Dans cette phase, vous allez :
- Comparer expérimentalement le Machine Learning classique et le Deep Learning
- Observer les différences fondamentales en termes de préparation des données et de performances
- Découvrir l'anatomie d'un réseau de neurones en manipulant directement ses composants
- Comprendre par la pratique comment l'information circule dans un réseau de neurones

## Comparaison pratique : Machine Learning vs Deep Learning (30 min)

### Objectif
Comprendre par l'observation directe les différences fondamentales entre le Machine Learning classique et le Deep Learning, en les appliquant au même jeu de données.

### Instructions

1. Suivre les [instructions](partie2-decouverte-concepts/ml-vs-dl-comparaison.md) pour ouvrez le notebook dans Google Colab 
2. Exécutez les cellules dans l'ordre indiqué
3. Observez comment chaque approche traite les données MNIST (chiffres manuscrits)
4. Notez les différences en termes de :
   - Préparation des données
   - Complexité d'implémentation
   - Temps d'entraînement
   - Performance sur données normales et bruitées

### Points clés à identifier

À travers cette expérimentation, identifiez par vous-mêmes ces concepts fondamentaux :

- Comment les caractéristiques (features) sont traitées dans chaque approche
- Le rôle de la représentation des données
- La capacité d'abstraction des différents modèles
- Les compromis entre temps d'entraînement et performance

### Tableau comparatif

Utilisez ce tableau pour noter vos observations :

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (CNN) |
| :------------- | :------------------------------- | :--------------------------------- |
| Préparation des données |  |  |
| Extraction de caractéristiques |  |  |
| Temps d'entraînement |  |  |
| Précision globale |  |  |
| Précision sur données bruitées |  |  |
| Facilité d'implémentation |  |  |

## Atelier pratique "Boîte noire" : Machine Learning vs Deep Learning (30 min)

### Contexte et préparation (5 min)

Nous allons explorer les différences fondamentales entre le Machine Learning classique et le Deep Learning non pas par la théorie, mais en observant leurs comportements sur un même jeu de données.

**Organisation :**
- Travaillez en binôme
- Chaque binôme doit explorer en parallèle les deux notebooks fournis

**Matériel nécessaire :**

- Compte Google (pour accéder à Google Colab)
- Liens vers deux notebooks complémentaires :
  - [Notebook A : Classification avec un algorithme classique (Random Forest)](../ressources/notebooks/machine-learning-classique.ipynb)
  - [Notebook B : Classification avec un réseau de neurones simple](../ressources/notebooks/deep-learning.ipynb)

**Jeu de données :** MNIST (chiffres manuscrits)

### Étape 1 : Exploration parallèle (25 min)

1. Ouvrez les deux notebooks (A et B) dans deux onglets séparés.
2. Exécutez les cellules dans l'ordre indiqué (Ctrl+Enter ou bouton ▶️).
3. Pour chaque notebook, observez et notez :
   * Comment les données sont préparées
   * Quels paramètres peuvent être ajustés
   * Le temps nécessaire à l'entraînement
   * Les performances obtenues (précision, rappel, F1-score)
   * Les types d'erreurs commises par chaque modèle
4. Utilisez ce tableau comparatif pour vos notes :

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (Réseau de neurones) |
| :------------- | :------------------------------- | :--------------------------------- |
| Préparation des données |  |  |
| Paramètres principaux |  |  |
| Temps d'entraînement |  |  |
| Précision globale |  |  |
| Types d'erreurs fréquentes |  |  |

### Étape 2 : Défi de généralisation (10 min)

1. Dans chaque notebook, localisez la section "Défi de généralisation".
2. Exécutez les cellules qui chargent le nouveau jeu de test.
3. Observez comment chaque modèle performe sur ces nouvelles données.
4. Notez les différences de performance entre les deux approches.

**Questions à discuter :**

* Lequel des modèles généralise le mieux aux nouvelles données ?
* Pourquoi pensez-vous qu'il y a cette différence ?
* Quels avantages et inconvénients voyez-vous pour chaque approche ?

### Étape 3 : Mise en commun (5 min)

Préparez-vous à partager vos observations avec le reste de la classe :

* Principales différences constatées
* Surprises ou découvertes intéressantes
* Questions que cette expérimentation a soulevées

**Concepts clés à identifier**

À travers cette expérimentation, essayez d'identifier par vous-mêmes ces concepts fondamentaux :

* Comment les caractéristiques (features) sont traitées dans chaque approche
* Le rôle de la représentation des données
* La capacité d'abstraction des différents modèles
* Les compromis entre temps d'entraînement et performance

**Ressources supplémentaires**

* [Documentation scikit-learn (Random Forest)](https://scikit-learn.org/stable/modules/ensemble.html#forest)
* [Documentation TensorFlow/Keras](https://www.tensorflow.org/guide/keras/sequential_model)
* [Visualisations interactives TensorFlow Playground](https://playground.tensorflow.org/)

## TP guidé : Anatomie d'un réseau de neurones (45 min)

Dans cette seconde partie, vous allez plonger au cœur des réseaux de neurones pour comprendre leur fonctionnement interne.

### Matériel et ressources

* [Notebook interactif "Anatomie d'un réseau de neurones"](../ressources/notebooks/anatomie-reseau.ipynb)
* [Schéma à compléter pour la synthèse](ressources/schema-a-completer.md)
* [Fiche récapitulative des termes techniques](ressources/glossaire-dl.md)
  
### Instructions

#### Partie 1 : Exploration d'un neurone unique (15 min)

Dans cette partie, vous allez manipuler un neurone artificiel unique pour comprendre son fonctionnement de base.

1. Exécutez les cellules d'importation des bibliothèques et de configuration.
2. Localisez la section "Neurone unique" et exécutez la cellule d'initialisation.
3. Expérimentez avec les contrôles interactifs pour :
   * Modifier les valeurs d'entrée (x₁, x₂)
   * Ajuster les poids (w₁, w₂)
   * Changer la valeur du biais (b)
   * Observer l'effet sur la sortie du neurone

**Questions à explorer :**

* Que se passe-t-il si tous les poids sont à zéro ?
* Comment pouvez-vous configurer le neurone pour qu'il s'active uniquement si les deux entrées sont élevées ?
* Quel est l'effet du biais sur le "seuil" d'activation ?
* Comment la fonction d'activation ReLU transforme-t-elle la sortie ?

#### Partie 2 : De l'unique au réseau (15 min)

Nous allons maintenant passer à un petit réseau de neurones pour comprendre comment l'information circule à travers les couches.

1. Localisez la section "Réseau simple" et exécutez les cellules d'initialisation.
2. Explorez le réseau composé de :
   * Une couche d'entrée (2 neurones)
   * Une couche cachée (3 neurones)
   * Une couche de sortie (1 neurone)
3. Réalisez les expériences suivantes :
   * Observez comment le signal se propage à travers les couches
   * Suivez le parcours d'une information spécifique (valeur d'entrée)
   * Identifiez les "motifs d'activation" qui se forment pour différentes entrées
   * Testez différentes fonctions d'activation (ReLU, Sigmoid, Tanh)

**Exercice pratique :
** Essayez de configurer manuellement les poids pour que le réseau réalise la fonction logique XOR (entrées : [0,0]→0, [0,1]→1, [1,0]→1, [1,1]→0).

#### Partie 3 : Visualisation de l'entraînement (10 min)

Dans cette partie, vous allez observer comment un réseau apprend au fil du temps.

1. Localisez la section "Entraînement" et exécutez la cellule d'initialisation.
2. Lancez la visualisation de l'entraînement en temps réel.
3. Observez :
   * L'évolution des poids à chaque itération
   * Comment la "frontière de décision" se modifie
   * La diminution de l'erreur au fil des époques
4. Essayez de modifier :
   * Le taux d'apprentissage (learning rate)
   * La complexité du problème (type de données)
   * L'architecture du réseau (nombre de neurones)

#### Partie 4 : Synthèse et verbalisation (5 min)

1. Complétez le schéma du réseau de neurones fourni en fin de notebook.
2. Identifiez et nommez correctement :
   * Les entrées et sorties
   * Les poids et biais
   * Les fonctions d'activation
   * Les couches cachées
3. Rédigez un court paragraphe (5-7 lignes) expliquant avec vos propres mots :
   * Comment un réseau de neurones traite l'information
   * Comment il peut apprendre à partir d'exemples

### Points clés à retenir

À travers cette exploration, vous devriez avoir découvert :

* Le rôle fondamental des poids et biais
* L'importance des fonctions d'activation pour introduire la non-linéarité
* Comment l'information se propage à travers un réseau (forward propagation)
* Les bases du processus d'apprentissage (ajustement des poids)

### Ressources supplémentaires

* [Visualisations interactives : Playground TensorFlow](https://playground.tensorflow.org/)
* [Tutoriel : Comprendre les réseaux de neurones](https://www.tensorflow.org/tutorials)
* [Document : Mathématiques des réseaux de neurones simplifiées](ressources/math-simplified-nn.md)

## Conclusion

Cette phase vous a permis de passer de l'observation pure à une compréhension plus approfondie des mécanismes internes du Deep Learning, tout en conservant une approche très pratique et expérimentale. Les concepts découverts serviront de fondation pour la suite du parcours.

[Retour à la Séance 1](index.md){ .md-button } 
[Continuer vers la Phase 3](partie3-debrief.md){ .md-button .md-button--primary }