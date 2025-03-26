# Phase 2 : Amélioration des performances (1h30)

## Introduction à l'optimisation pratique des modèles (15 min)

**Objectif** : Comprendre les approches simples et efficaces pour améliorer les performances d'un modèle de Deep Learning sans expertise mathématique approfondie.

### Au-delà de l'architecture : facteurs clés de performance

Les performances d'un modèle de Deep Learning ne dépendent pas seulement de son architecture, mais aussi de nombreux autres facteurs que nous pouvons optimiser :

1. **Qualité des données** : Souvent plus importante que la complexité du modèle
2. **Prétraitement approprié** : Normalisation, augmentation de données, etc.
3. **Hyperparamètres** : Taux d'apprentissage, taille de batch, etc.
4. **Technique d'entraînement** : Régularisation, early stopping, etc.

### Les erreurs les plus courantes en Deep Learning

Avant d'améliorer, il faut comprendre ce qui peut poser problème :

| Erreur courante | Symptômes | Impact |
|-----------------|-----------|--------|
| Données non normalisées | Apprentissage lent ou instable | Convergence difficile |
| Surapprentissage (overfitting) | Bonnes performances sur données d'entraînement, mauvaises sur données de test | Mauvaise généralisation |
| Sous-apprentissage (underfitting) | Mauvaises performances partout | Capacité insuffisante |
| Fuite de données (data leakage) | Performances irréalistes | Modèle inutilisable en production |
| Mauvaise division train/test | Évaluation incorrecte | Fausse confiance dans le modèle |

### Approche pragmatique de l'amélioration

Nous allons suivre une approche méthodique pour améliorer nos modèles :

1. **Diagnostiquer les problèmes** : Identifier ce qui limite les performances
2. **Appliquer des solutions ciblées** : Choisir les techniques adaptées au problème identifié
3. **Évaluer correctement** : Mesurer l'impact des modifications de manière objective
4. **Itérer rapidement** : Tester, apprendre, ajuster, recommencer

## Atelier : Diagnostiquer les problèmes de performance (30 min)

**Objectif** : Apprendre à identifier et diagnostiquer les problèmes courants dans les modèles de Deep Learning.

**Matériel et ressources** :
* Notebook Colab "Diagnostic des modèles"
* Modèles pré-configurés avec différents problèmes

### Instructions

**Partie 1 : Reconnaître les signes de surapprentissage (15 min)**

1. Ouvrez le notebook "Diagnostic des modèles" dans Google Colab.
2. Accédez à la section "Cas 1 : Surapprentissage".
3. Exécutez les cellules pour entraîner le modèle et afficher les courbes d'apprentissage.
4. Observez les signes caractéristiques du surapprentissage :
   * Écart grandissant entre la performance sur données d'entraînement et de validation
   * Courbe de perte de validation qui remonte après avoir diminué
   * Performances parfaites sur l'entraînement mais médiocres sur la validation
   
5. Appliquez ces techniques pour résoudre le problème :
   * Ajout de dropout (désactivation aléatoire de neurones)
   * Régularisation L2 (weight decay)
   * Augmentation de données
   * Early stopping (arrêt anticipé)
   
6. Pour chaque technique, notez l'impact sur les courbes d'apprentissage et les performances.

**Partie 2 : Détecter les problèmes de données et de prétraitement (15 min)**

1. Passez à la section "Cas 2 : Problèmes de données".
2. Analysez les visualisations des données d'entrée.
3. Identifiez les problèmes potentiels :
   * Données non normalisées (valeurs extrêmes)
   * Distributions différentes entre entraînement et test
   * Classes déséquilibrées

4. Appliquez ces corrections :
   * Normalisation appropriée (Z-score, min-max, etc.)
   * Rééchantillonnage pour équilibrer les classes
   * Stratification de la division train/test

5. Observez comment ces corrections améliorent l'entraînement et les performances du modèle.

## TP pratique : Améliorer un modèle pour une application web (40 min)

**Objectif** : Appliquer les techniques d'amélioration à un modèle existant pour une application web réelle.

**Matériel et ressources** :
* Notebook "Amélioration pour application web"
* Application web simple de reconnaissance d'objets
* Modèle de base fonctionnel mais limité

### Instructions

**Partie 1 : Analyse du modèle existant (10 min)**

1. Ouvrez le notebook "Amélioration pour application web".
2. Exécutez les cellules qui chargent et évaluent le modèle existant.
3. Analysez ses performances et limitations :
   * Précision globale et par classe
   * Matrice de confusion
   * Temps d'inférence
   * Robustesse aux variations (rotation, luminosité, etc.)

4. Documentez au moins trois problèmes spécifiques à résoudre.

**Partie 2 : Amélioration des performances (15 min)**

Choisissez et implémentez au moins trois techniques d'amélioration parmi :

1. **Prétraitement amélioré** :
   * Normalisation adaptée au dataset
   * Détection et recadrage automatique des objets
   * Correction de luminosité et de contraste

2. **Augmentation de données** :
   * Rotations et translations
   * Modifications de luminosité et contraste
   * Zoom et recadrage aléatoire
V
3. **Optimisation du modèle** :
   * Ajustement de l'architecture (nombre de couches, neurones)
   * Techniques de régularisation (dropout, batch normalization)
   * Transfer learning avec un modèle pré-entraîné

4. **Optimisation du temps d'inférence** :
   * Quantification du modèle (réduction de précision)
   * Élagage (pruning) des connexions peu importantes
   * Optimisation pour CPU ou mobile

**Partie 3 : Tests et documentation (15 min)**

1. Évaluez le modèle amélioré sur le jeu de test.
2. Comparez les performances avec le modèle original :
   * Précision globale (avant vs après)
   * Temps d'inférence (avant vs après)
   * Taille du modèle (avant vs après)
   * Robustesse aux variations

3. Créez un rapport concis au format suivant :

```
# Rapport d'amélioration du modèle

## Problèmes identifiés
1. [Problème 1]
2. [Problème 2]
3. [Problème 3]

## Solutions implémentées
1. [Solution 1] → Impact: [résultat]
2. [Solution 2] → Impact: [résultat]
3. [Solution 3] → Impact: [résultat]

## Performances comparées
| Métrique | Avant | Après | Amélioration |
|----------|-------|-------|--------------|
| Précision | x% | y% | +z% |
| Temps d'inférence | x ms | y ms | -z% |
| Taille du modèle | x MB | y MB | -z% |

## Conclusion
[Résumé des améliorations et recommandations]
```

4. Exportez le modèle amélioré pour l'intégration dans l'application web.

## Bonnes pratiques pour l'optimisation en production (5 min)

### Checklist d'optimisation pour vos futurs projets

✅ **Données** :
- Normalisation adaptée au problème
- Augmentation pertinente (pas excessive)
- Division train/validation/test stratifiée
- Vérification de la qualité des données (valeurs manquantes, erreurs)

✅ **Modèle** :
- Architecture adaptée à la complexité du problème
- Régularisation appropriée (dropout, L1/L2)
- Batch normalization pour stabiliser l'entraînement
- Learning rate adaptatif (Adam, RMSprop)

✅ **Entraînement** :
- Early stopping avec patience appropriée
- Réduction du learning rate sur plateau
- Validation croisée pour les petits datasets
- Sauvegarde du meilleur modèle, pas forcément le dernier

✅ **Déploiement** :
- Quantification pour réduire la taille (TFLite, ONNX)
- Tests sur les plateformes cibles
- Monitoring des performances
- Re-entraînement périodique avec de nouvelles données

### Conclusion et transition vers la phase finale (5 min)

**Ce que vous avez appris** :
- Identifier les problèmes limitant les performances d'un modèle
- Appliquer des techniques ciblées pour résoudre ces problèmes
- Évaluer objectivement l'impact des améliorations
- Optimiser un modèle pour un déploiement en production

**Prochaine étape** : Préparer le développement de votre chatbot pédagogique en appliquant ces techniques d'optimisation.

[Passer à la Phase 3](partie3-preparation-projet.md){ .md-button .md-button--primary }