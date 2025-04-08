# QCM d'auto-évaluation - Module 2 : Architectures spécialisées

Ce QCM vous permettra d'évaluer votre compréhension des réseaux convolutifs (CNN) et récurrents (RNN) étudiés dans ce module.

## Instructions
- Cochez la ou les réponses correctes pour chaque question
- Certaines questions peuvent avoir plusieurs réponses correctes
- À la fin du questionnaire, calculez votre score grâce au corrigé fourni
- Durée recommandée : 15 minutes

## Partie A : Réseaux Convolutifs (CNN)

### 1. Dans un réseau convolutif, à quoi sert principalement l'opération de convolution ?
- [ ] À réduire la dimension des données
- [ ] À détecter des caractéristiques locales dans les données d'entrée
- [ ] À connecter tous les neurones entre eux
- [ ] À accélérer le temps d'entraînement

### 2. Qu'est-ce qu'un filtre (ou noyau) dans un CNN ?
- [ ] Une fonction qui supprime les pixels indésirables de l'image
- [ ] Une matrice de poids qui s'applique localement sur les données d'entrée
- [ ] Un seuil qui élimine les valeurs en dessous d'un certain niveau
- [ ] Une technique pour sélectionner les meilleures images d'entraînement

### 3. Quel est le rôle principal de l'opération de pooling dans un CNN ?
- [ ] Augmenter la taille des feature maps
- [ ] Réduire la dimensionnalité tout en préservant les informations importantes
- [ ] Ajouter de la non-linéarité au réseau
- [ ] Connecter les différentes couches de convolution

### 4. Quels sont les avantages des CNN pour le traitement d'images ? (plusieurs réponses possibles)
- [ ] Partage des paramètres entre différentes positions spatiales
- [ ] Invariance à la translation
- [ ] Réduction significative du nombre de paramètres par rapport aux réseaux entièrement connectés
- [ ] Capacité à traiter des images de n'importe quelle taille sans redimensionnement

### 5. Dans quelle couche d'un CNN typique se trouvent généralement le plus grand nombre de paramètres ?
- [ ] Couches de convolution
- [ ] Couches de pooling
- [ ] Couches entièrement connectées (fully connected)
- [ ] Couches de normalisation par lots (batch normalization)

### 6. Qu'est-ce qu'une feature map dans un CNN ?
- [ ] Une carte qui indique les régions d'intérêt dans l'image originale
- [ ] Le résultat de l'application d'un filtre de convolution sur une entrée
- [ ] Un graphique montrant la progression de l'entraînement
- [ ] La liste des caractéristiques extraites manuellement avant l'entraînement

### 7. Comment évoluent les caractéristiques détectées à mesure qu'on avance dans les couches d'un CNN ?
- [ ] Elles deviennent de plus en plus simples et élémentaires
- [ ] Elles restent de même nature mais deviennent plus précises
- [ ] Elles deviennent de plus en plus abstraites et complexes
- [ ] Elles concernent des régions de plus en plus petites de l'image

## Partie B : Réseaux Récurrents (RNN)

### 8. Quelle est la principale caractéristique des réseaux de neurones récurrents (RNN) ?
- [ ] Ils utilisent des opérations de convolution pour traiter les données
- [ ] Ils contiennent des connexions formant des boucles permettant de mémoriser les informations
- [ ] Ils traitent chaque élément d'une séquence de manière complètement indépendante
- [ ] Ils sont spécialisés dans le traitement d'images

### 9. Pour quels types de données les RNN sont-ils particulièrement adaptés ?
- [ ] Images 2D
- [ ] Données tabulaires (comme des tableaux Excel)
- [ ] Données séquentielles (texte, séries temporelles, audio)
- [ ] Nuages de points 3D

### 10. Quel problème majeur affecte les RNN classiques lors du traitement de séquences longues ?
- [ ] Surconsommation de mémoire
- [ ] Temps de traitement exponentiel
- [ ] Problème de disparition ou d'explosion du gradient
- [ ] Incapacité à paralléliser les calculs

### 11. Quelle est la principale innovation des cellules LSTM par rapport aux RNN classiques ?
- [ ] Elles utilisent des opérations de convolution
- [ ] Elles possèdent des mécanismes de portes contrôlant le flux d'information
- [ ] Elles peuvent traiter plusieurs séquences en parallèle
- [ ] Elles ne nécessitent pas d'entraînement

### 12. Dans un réseau LSTM, à quoi sert la "porte d'oubli" (forget gate) ?
- [ ] À déterminer quelles informations de l'état précédent doivent être conservées ou supprimées
- [ ] À réinitialiser complètement le réseau quand la séquence est trop longue
- [ ] À sauter certaines étapes de calcul pour accélérer le traitement
- [ ] À ignorer les données d'entrée corrompues ou bruitées

### 13. Quelles applications typiques utilisent les RNN/LSTM ? (plusieurs réponses possibles)
- [ ] Reconnaissance de caractères manuscrits
- [ ] Traduction automatique
- [ ] Prédiction de séries temporelles
- [ ] Génération de texte
- [ ] Segmentation d'images

### 14. Qu'est-ce qui différencie principalement les GRU (Gated Recurrent Units) des LSTM ?
- [ ] Les GRU n'ont aucune forme de mémoire
- [ ] Les GRU ont une architecture plus simple avec moins de portes
- [ ] Les GRU sont spécifiquement conçus pour les données non séquentielles
- [ ] Les GRU ne peuvent pas être entraînés par rétropropagation

## Partie C : Intégration pratique

### 15. Lors de l'intégration d'un modèle CNN dans une application web, quelles considérations sont importantes ? (plusieurs réponses possibles)
- [ ] Prétraitement des images côté client avant envoi au serveur
- [ ] Optimisation de la taille du modèle pour réduire les temps de chargement
- [ ] Gestion des erreurs en cas de prédictions incertaines
- [ ] Compatibilité avec différents navigateurs web

### 16. Dans notre expérience avec l'API Mistral AI, quels avantages avons-nous observés par rapport aux modèles RNN que nous avons implémentés ? (plusieurs réponses possibles)
- [ ] Meilleure compréhension du contexte à long terme
- [ ] Capacité à générer des réponses plus cohérentes et naturelles
- [ ] Temps d'entraînement réduit
- [ ] Facilité d'utilisation sans besoin d'expertise en Deep Learning

## Auto-évaluation

Une fois le QCM complété, vérifiez vos réponses avec le corrigé ci-dessous.

### Corrigé
1. b
2. b
3. b
4. a, b, c
5. c
6. b
7. c
8. b
9. c
10. c
11. b
12. a
13. b, c, d
14. b
15. a, b, c, d
16. a, b, d

### Calcul de votre score
Comptez 1 point par réponse correcte. Pour les questions à choix multiples, comptez 1 point uniquement si toutes vos sélections sont correctes.

**Total des points possibles : 16**

### Interprétation
- **13-16 points** : Excellente maîtrise des architectures spécialisées de Deep Learning
- **10-12 points** : Bonne compréhension, quelques points à clarifier
- **7-9 points** : Compréhension de base, révision nécessaire de certains concepts
- **0-6 points** : Révision approfondie recommandée avant de poursuivre

## Pour approfondir
Si vous avez obtenu moins de 13 points, nous vous recommandons de revoir les concepts sur lesquels vous avez fait des erreurs. Consultez les ressources suivantes :
- Les notebooks CNN et RNN du module
- Les visualisations des architectures CNN et RNN
- La documentation des mini-projets pratiques réalisés