Voici une version du contenu adapté pour une pratique individuelle sans l'aide de l'enseignant :

# Phase 2 : Découverte des concepts par l'expérimentation

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

### Instructions pour une pratique individuelle

1. Ouvrez deux notebooks Google Colab dans des onglets séparés :
   - [Machine Learning classique (Random Forest)](ressources/machine-learning-classique.md)
   - [Deep Learning (CNN)](ressources/deep-learning.md)

2. Suivez les instructions dans chaque notebook et exécutez les cellules dans l'ordre indiqué.

3. Pendant que vous explorez les deux approches, prenez des notes sur :
   - Comment chaque approche traite les données MNIST (chiffres manuscrits)
   - Les différences dans la préparation des données
   - La complexité d'implémentation de chaque approche
   - Le temps d'entraînement respectif
   - Les performances sur données normales et bruitées

### Points clés à identifier par vous-même

À travers cette expérimentation, identifiez ces concepts fondamentaux :

- Comment les caractéristiques (features) sont traitées dans chaque approche
- Le rôle de la représentation des données
- La capacité d'abstraction des différents modèles
- Les compromis entre temps d'entraînement et performance

### Tableau comparatif à remplir

Utilisez ce tableau pour noter vos observations :

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (CNN) |
| :------------- | :------------------------------- | :--------------------------------- |
| Préparation des données |  |  |
| Extraction de caractéristiques |  |  |
| Temps d'entraînement |  |  |
| Précision globale |  |  |
| Précision sur données bruitées |  |  |
| Facilité d'implémentation |  |  |

## Exploration pratique : Anatomie d'un réseau de neurones (45 min)

Dans cette partie, vous allez explorer individuellement le fonctionnement interne d'un réseau de neurones.

### Matériel pour la pratique individuelle

* [Notebook interactif "Anatomie d'un réseau de neurones"](ressources/anatomie-reseau.md)
* [Schéma à compléter pour la synthèse](ressources/schema-a-completer.md)
* [Fiche récapitulative des termes techniques](ressources/glossaire-dl.md)
  
### Instructions étape par étape

#### Partie 1 : Exploration d'un neurone unique (15 min)

Dans cette partie, vous allez manipuler un neurone artificiel unique pour comprendre son fonctionnement de base.

1. Ouvrez le notebook "Anatomie d'un réseau de neurones" dans Google Colab
2. Exécutez les cellules d'importation des bibliothèques et de configuration
3. Localisez la section "Neurone unique" et exécutez la cellule d'initialisation
4. Expérimentez avec les contrôles interactifs pour :
   * Modifier les valeurs d'entrée (x₁, x₂)
   * Ajuster les poids (w₁, w₂)
   * Changer la valeur du biais (b)
   * Observer l'effet sur la sortie du neurone

**Questions à explorer par vous-même :**

* Que se passe-t-il si tous les poids sont à zéro ?
* Comment pouvez-vous configurer le neurone pour qu'il s'active uniquement si les deux entrées sont élevées ?
* Quel est l'effet du biais sur le "seuil" d'activation ?
* Comment la fonction d'activation ReLU transforme-t-elle la sortie ?

#### Partie 2 : De l'unique au réseau (15 min)

Passez maintenant à un petit réseau de neurones pour comprendre comment l'information circule à travers les couches.

1. Localisez la section "Réseau simple" et exécutez les cellules d'initialisation
2. Explorez le réseau composé de :
   * Une couche d'entrée (2 neurones)
   * Une couche cachée (3 neurones)
   * Une couche de sortie (1 neurone)
3. Réalisez les expériences suivantes par vous-même :
   * Observez comment le signal se propage à travers les couches
   * Suivez le parcours d'une information spécifique (valeur d'entrée)
   * Identifiez les "motifs d'activation" qui se forment pour différentes entrées
   * Testez différentes fonctions d'activation (ReLU, Sigmoid, Tanh)

**Exercice pratique :** 
Essayez de configurer manuellement les poids pour que le réseau réalise la fonction logique XOR (entrées : [0,0]→0, [0,1]→1, [1,0]→1, [1,1]→0).

#### Partie 3 : Visualisation de l'entraînement (10 min)

Dans cette partie, vous allez observer comment un réseau apprend au fil du temps.

1. Localisez la section "Entraînement" et exécutez la cellule d'initialisation
2. Lancez la visualisation de l'entraînement en temps réel
3. Observez :
   * L'évolution des poids à chaque itération
   * Comment la "frontière de décision" se modifie
   * La diminution de l'erreur au fil des époques
4. Essayez de modifier par vous-même :
   * Le taux d'apprentissage (learning rate)
   * La complexité du problème (type de données)
   * L'architecture du réseau (nombre de neurones)

#### Partie 4 : Synthèse et verbalisation (5 min)

1. Complétez le schéma du réseau de neurones fourni en fin de notebook
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

## Défi de généralisation (10 min)

Pour approfondir votre compréhension, réalisez ce défi supplémentaire :

1. Retournez aux notebooks de la première partie (ML classique et Deep Learning)
2. Localisez la section "Défi de généralisation" dans chaque notebook
3. Exécutez les cellules qui permettent de tester les modèles sur :
   - Des images avec du bruit ajouté
   - Des images avec rotation légère
4. Notez les performances des deux approches sur ces données modifiées
5. Analysez par vous-même :
   - Lequel des modèles généralise le mieux aux nouvelles données ?
   - Pourquoi existe-t-il cette différence ?
   - Quels avantages et inconvénients présentent chaque approche ?

## Auto-évaluation

Pour vérifier votre compréhension, posez-vous ces questions :

1. Pourriez-vous expliquer à un camarade la différence principale entre ML classique et Deep Learning ?
2. Sauriez-vous décrire le fonctionnement d'un neurone artificiel et son rôle dans un réseau ?
3. Comprenez-vous comment un réseau de neurones "apprend" à partir de données ?
4. Pouvez-vous identifier les situations où le Deep Learning serait préférable au ML classique, et vice versa ?

## Ressources supplémentaires pour approfondir par vous-même

* [Visualisations interactives : Playground TensorFlow](https://playground.tensorflow.org/)
* [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) - Un livre en ligne gratuit (en anglais)
* [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) - Une excellente série de vidéos explicatives

## Conclusion

Cette phase vous a permis de passer de l'observation pure à une compréhension plus approfondie des mécanismes internes du Deep Learning, tout en conservant une approche très pratique et expérimentale. Les concepts découverts serviront de fondation pour la suite du parcours.

[Retour à la Séance 1](index.md){ .md-button } 
[Continuer vers le mini-projet(mini-projet.md)]{ .md-button .md-button--primary }