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

# 📋 Fiche d'observations - Concepts fondamentaux du Deep Learning

## Partie 1 : Comparaison Machine Learning vs Deep Learning

*Remplissez ce tableau comparatif après avoir expérimenté avec les deux approches.*

| Aspect observé | Machine Learning (Random Forest) | Deep Learning (CNN) |
|----------------|----------------------------------|---------------------|
| Préparation des données | | |
| Extraction de caractéristiques | | |
| Temps d'entraînement | | |
| Précision globale | | |
| Précision sur données bruitées | | |
| Précision sur données avec rotation | | |
| Facilité d'implémentation | | |
| Interprétabilité | | |
| Capacité de généralisation | | |

## Partie 2 : Schéma conceptuel du réseau de neurones

*Complétez le schéma ci-dessous en identifiant les éléments numérotés.*

```
                    ┌─────────────┐
                    │             │
                    │      1      │
                    │             │
                    └─────────────┘
                          │
                          ▼
            ┌───────────────────────────┐
            │                           │
            │             2             │
            │                           │
            └───────────────────────────┘
                          │
                          ▼
      ┌───────────────────────────────────┐
      │                                   │
      │               3                   │
      │                                   │
      └───────────────────────────────────┘
                          │
                          ▼
            ┌───────────────────────────┐
            │                           │
            │             4             │
            │                           │
            └───────────────────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │             │
                    │      5      │
                    │             │
                    └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │             │
                    │      6      │
                    │             │
                    └─────────────┘
                          ▲
                          │
                    ┌─────────────┐
                    │             │
                    │      7      │
                    │             │
                    └─────────────┘
```

### Identification des éléments

1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________
5. ________________________________
6. ________________________________
7. ________________________________

## Partie 3 : Structure du réseau de neurones

*Pour un réseau de neurones dédié à la reconnaissance de chiffres manuscrits (MNIST), précisez :*

| Couche | Nombre de neurones |
|--------|-------------------|
| Couche d'entrée | _______ |
| Première couche cachée | _______ |
| Deuxième couche cachée | _______ |
| Couche de sortie | _______ |

### Fonctions d'activation

*Indiquez quelle fonction d'activation serait la plus appropriée pour :*

- Les couches cachées : _______________________
- La couche de sortie : _______________________

## Partie 4 : Processus d'apprentissage

*Décrivez brièvement les étapes du processus d'apprentissage d'un réseau de neurones :*

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

4. _________________________________________________________________

## Partie 5 : Réflexion et synthèse personnelle

*Pour vérifier votre compréhension, répondez à ces questions :*

### Comparaison ML classique et Deep Learning

Comment expliqueriez-vous la différence principale entre ML classique et Deep Learning à un camarade ?

_________________________________________________________________

_________________________________________________________________

### Fonctionnement d'un neurone artificiel

Décrivez le fonctionnement d'un neurone artificiel et son rôle dans un réseau :

_________________________________________________________________

_________________________________________________________________

### Processus d'apprentissage

Comment un réseau de neurones "apprend"-il à partir de données ?

_________________________________________________________________

_________________________________________________________________

### Applications pratiques

Dans quelles situations le Deep Learning serait-il préférable au ML classique, et vice versa ?

_________________________________________________________________

_________________________________________________________________

## Conclusion

Cette fiche d'observations vous a permis de documenter votre apprentissage des concepts fondamentaux du Deep Learning à travers une approche expérimentale et comparative. Les observations que vous avez notées serviront de base solide pour la suite de votre parcours et pour votre projet final de chatbot pédagogique.

## Ressources complémentaires

- [Guide d'utilisation de Google Colab](ressources/guide-colab.md) - Pour vous aider à utiliser cet environnement
- [Glossaire du Deep Learning](ressources/glossaire-dl.md) - Définitions des termes techniques rencontrés
- [TensorFlow Playground](https://playground.tensorflow.org/) - Interface interactive pour expérimenter avec des réseaux de neurones simples

## Informations sur le rendu

**Nom et prénom :** ____________________________

**Date :** ____________________________


[Retour au Module 1](index.md){ .md-button }
[Continuer vers le mini-projet](mini-projet.md){ .md-button .md-button--primary }