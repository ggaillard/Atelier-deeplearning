# 🧩 Phase 2 : Découverte des concepts par l'expérimentation

![Comparaison Machine Learning vs Deep Learning](https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000&h=300)

## 🎯 Objectifs de la phase

Dans cette phase, vous allez :

  - Comparer expérimentalement le Machine Learning classique et le Deep Learning
  - Observer les différences fondamentales en termes de préparation des données et de performances
  - Découvrir l'anatomie d'un réseau de neurones en manipulant directement ses composants
  - Comprendre par la pratique comment l'information circule dans un réseau de neurones

## 📋 Fiche d'observations à compléter

> **IMPORTANT** : Tout au long de cette phase, vous devrez compléter la **Fiche d'observations** disponible ci-dessous. Ce document sera votre livrable principal et vous aidera à structurer votre apprentissage.
>
> 📥 **Téléchargez et consultez la fiche dès maintenant** pour comprendre les éléments à observer et à documenter pendant les activités.
>
> ✏️ **Complétez-la progressivement** pendant chaque exercice pratique.

## Comparaison pratique : Machine Learning vs Deep Learning (30 min)

### Objectif
Comprendre par l'observation directe les différences fondamentales entre le Machine Learning classique et le Deep Learning, en les appliquant au même jeu de données.

### Instructions pour une pratique individuelle

1. Ouvrez deux notebooks Google Colab dans des onglets séparés :
   
    - [Machine Learning classique (Random Forest)](ressources/machine-learning-classique.md)
    - [Deep Learning (CNN)](ressources/deep-learning.md)

2. Suivez les instructions dans chaque notebook et exécutez les cellules dans l'ordre indiqué.

3. **Pour la fiche d'observations** : Pendant que vous explorez les deux approches, notez dans la section "Partie 1" de votre fiche :
   
    - Comment chaque approche traite les données MNIST (chiffres manuscrits)
    - Les différences dans la préparation des données
    - La complexité d'implémentation de chaque approche
    - Le temps d'entraînement respectif
    - Les performances sur données normales et bruitées

### Points clés à identifier et à noter sur votre fiche

À travers cette expérimentation, identifiez ces concepts fondamentaux et notez-les dans votre fiche :

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

**Pour la fiche d'observations** : Dans la "Partie 2" de votre fiche, répondez aux questions suivantes :

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

**Pour la fiche d'observations** : Complétez la section "Structure du réseau" de votre fiche en précisant :
- Le nombre de neurones approprié pour chaque couche
- Les fonctions d'activation recommandées
- Comment l'information circule dans le réseau

**Exercice pratique pour la fiche** : 
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

**Pour la fiche d'observations** : Dans la section "Processus d'apprentissage" de votre fiche, décrivez les étapes clés que vous avez observées lors de l'entraînement du réseau.

#### Partie 4 : Synthèse et verbalisation (5 min)

**Pour la fiche d'observations** :
1. Complétez le schéma du réseau de neurones fourni dans votre fiche
2. Identifiez et nommez correctement :
   * Les entrées et sorties
   * Les poids et biais
   * Les fonctions d'activation
   * Les couches cachées
3. Rédigez un court paragraphe (5-7 lignes) dans la section "Réflexion et synthèse personnelle" expliquant avec vos propres mots :
   * Comment un réseau de neurones traite l'information
   * Comment il peut apprendre à partir d'exemples

## Défi de généralisation (10 min)

Pour approfondir votre compréhension, réalisez ce défi supplémentaire :

1. Retournez aux notebooks de la première partie (ML classique et Deep Learning)
2. Localisez la section "Défi de généralisation" dans chaque notebook
3. Exécutez les cellules qui permettent de tester les modèles sur :
   - Des images avec du bruit ajouté
   - Des images avec rotation légère
4. **Pour la fiche d'observations** : Dans la section "Comparaison ML vs Deep Learning" de votre fiche, notez :
   - Lequel des modèles généralise le mieux aux nouvelles données ?
   - Pourquoi existe-t-il cette différence ?
   - Quels avantages et inconvénients présente chaque approche ?

## Remise de la fiche d'observations

À la fin de cette phase, assurez-vous que votre fiche d'observations est complètement remplie. Ce document constitue un livrable essentiel qui démontre votre compréhension des concepts fondamentaux du Deep Learning.

**Modalités de remise :**
- Format : Document numérique (Word, PDF) ou copie manuscrite propre et lisible
- Nom du fichier : "NOM_Prenom_Fiche_Concepts_DL.pdf"
- Délai : À remettre au plus tard à la fin de la séance

## Ressources complémentaires

- [Guide d'utilisation de Google Colab](ressources/guide-colab.md) - Pour vous aider à utiliser cet environnement
- [Glossaire du Deep Learning](ressources/glossaire-dl.md) - Définitions des termes techniques rencontrés
- [TensorFlow Playground](https://playground.tensorflow.org/) - Interface interactive pour expérimenter avec des réseaux de neurones simples

[Retour au Module 1](index.md){ .md-button }
[Continuer vers le mini-projet](mini-projet.md){ .md-button .md-button--primary }