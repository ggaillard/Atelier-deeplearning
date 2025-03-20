# 📋 Fiche d'observations - Hello World du Deep Learning (CORRIGÉ)

*Cette fiche d'observations vous accompagne étape par étape dans l'exploration du notebook. Pour chaque section, notez les références aux cellules correspondantes du notebook.*

## Informations générales

**Nom et prénom :** ____________________________

**Date :** ____________________________

**Groupe :** ____________________________

## Partie 1 : Configuration et vérification de l'environnement *(Cellule 2)*

| Question | Observation |
|----------|-------------|
| Version de TensorFlow détectée | 2.x.x (la version exacte dépendra de l'environnement Colab) |
| GPU disponible ? (Oui/Non) | Oui (généralement disponible dans Colab) |
| Quelle est l'importance d'avoir un GPU pour le Deep Learning ? | Les GPUs sont essentiels pour accélérer l'entraînement des modèles de Deep Learning car ils peuvent effectuer des calculs matriciels en parallèle, réduisant considérablement le temps d'entraînement par rapport aux CPUs. Sans GPU, l'entraînement de modèles complexes peut prendre des heures, voire des jours au lieu de minutes. |

## Partie 2 : Chargement et préparation des données *(Cellule 3)*

| Question | Observation |
|----------|-------------|
| Combien d'exemples d'entraînement sont disponibles ? | 60 000 exemples |
| Combien d'exemples de test sont disponibles ? | 10 000 exemples |
| Quelle est la dimension des images ? | 28 x 28 pixels |
| Pourquoi normalise-t-on les valeurs des pixels entre 0 et 1 ? | La normalisation permet d'avoir des valeurs dans une plage uniforme, ce qui améliore la stabilité et la vitesse de convergence lors de l'entraînement. Sans normalisation, les gradients peuvent exploser ou disparaître pendant la rétropropagation. |
| D'après les exemples affichés, quelles difficultés pourrait rencontrer le modèle ? | Variations dans l'écriture (forme, épaisseur, inclinaison), certains chiffres qui se ressemblent (comme 1 et 7, ou 3 et 8), qualité variable des images, positions légèrement différentes des chiffres dans l'image. |

## Partie 3 : Architecture du modèle *(Cellule 4)*

Dessinez le schéma simplifié de l'architecture du réseau de neurones utilisé :

```
Input (28x28x1) → Conv2D (32 filtres) → MaxPooling → Conv2D (64 filtres) → MaxPooling → Flatten → Dense (64) → Dense (10, softmax)
```

| Question | Observation |
|----------|-------------|
| Combien de couches comporte le modèle ? | 7 couches (Input, 2 couches Conv2D, 2 couches MaxPooling, Flatten, 2 couches Dense) |
| Combien de paramètres entraînables au total ? | Environ 93,322 paramètres (le nombre exact dépend de l'implémentation) |
| Quel est le rôle des couches de convolution ? | Les couches de convolution appliquent des filtres sur l'image pour détecter des caractéristiques (bords, textures, formes). Elles permettent d'extraire des informations spatiales en analysant des régions locales de l'image d'entrée. |
| Quel est le rôle des couches de pooling ? | Les couches de pooling réduisent la dimension spatiale (hauteur et largeur) pour diminuer le nombre de paramètres et la complexité du calcul, tout en conservant les caractéristiques les plus importantes. Elles rendent aussi le modèle plus robuste aux petites variations de position. |
| Pourquoi utilise-t-on 'softmax' comme activation de la dernière couche ? | Softmax transforme les sorties en une distribution de probabilités (somme = 1) sur les 10 classes (chiffres 0-9), ce qui permet d'interpréter les sorties comme des probabilités d'appartenance à chaque classe. |

## Partie 4 : Entraînement du modèle *(Cellule 5)*

| Question | Observation |
|----------|-------------|
| Combien d'époques ont été effectuées ? | 5 époques |
| Quelle est la précision finale sur les données d'entraînement ? | ~99% (la valeur exacte varie légèrement à chaque exécution) |
| Quelle est la précision finale sur les données de validation ? | ~98-99% (varie légèrement) |
| Quelle est la précision sur l'ensemble de test ? | ~98-99% (varie légèrement) |
| Y a-t-il un signe de surapprentissage (overfitting) ? Pourquoi ? | Très léger ou inexistant car l'écart entre la précision d'entraînement et de validation est faible. Le modèle généralise bien aux données non vues pendant l'entraînement. |

## Partie 5 : Visualisation des résultats *(Cellule 6)*

Analysez les graphiques d'apprentissage :

| Question | Observation |
|----------|-------------|
| La courbe de précision d'entraînement est-elle croissante ? | Oui, elle augmente rapidement au début puis se stabilise. |
| La courbe de perte d'entraînement est-elle décroissante ? | Oui, elle diminue rapidement au début puis se stabilise. |
| Y a-t-il un écart important entre les courbes d'entraînement et de validation ? | Non, l'écart est faible, ce qui indique une bonne généralisation. |
| D'après vous, l'entraînement a-t-il été suffisant (nombre d'époques) ? | Oui, les courbes semblent se stabiliser après 3-4 époques, donc 5 époques semblent suffisantes pour ce modèle et ce jeu de données. Augmenter davantage pourrait amener à du surapprentissage. |

## Partie 6 : Prédictions sur des exemples de test *(Cellule 7)*

Observez les 10 exemples de prédiction :

| Question | Observation |
|----------|-------------|
| Combien de prédictions sont correctes sur les 10 exemples ? | Généralement 9-10 sur 10 (peut varier selon l'initialisation aléatoire) |
| Pour les prédictions incorrectes, quelles pourraient être les raisons d'erreur ? | Similitudes visuelles entre certains chiffres (ex: 4/9, 3/8), écritures atypiques, bruit dans l'image, ou manque d'exemples similaires dans les données d'entraînement. |
| Certains chiffres semblent-ils plus difficiles à reconnaître que d'autres ? | Généralement, les chiffres 4, 7, 9 peuvent se confondre, ainsi que 3 et 8. Le modèle peut hésiter davantage sur ces paires de chiffres comme le montrent les barres de probabilité. |

## Partie 7 : Test avec votre propre dessin *(Cellule 8)*

| Question | Observation |
|----------|-------------|
| Quels chiffres avez-vous dessinés ? | [Réponses variables selon les essais des étudiants] |
| Combien ont été correctement prédits ? | [Réponses variables] |
| Pour ceux mal prédits, quelle était la prédiction et pourquoi selon vous ? | Raisons possibles : style d'écriture différent de MNIST, épaisseur du trait, centrage de l'image, prétraitement qui modifie trop l'image, etc. |
| Comment le prétraitement de l'image a-t-il transformé votre dessin ? | L'image est redimensionnée à 28x28 pixels, convertie en niveaux de gris, et les couleurs sont inversées si nécessaire pour avoir un fond noir et un chiffre blanc comme dans le jeu de données MNIST original. |

## Partie 8 : Expérimentations *(Cellule 9)*

Documentez vos expérimentations en modifiant le modèle ou les paramètres :

### Expérimentation 1

**Modification effectuée :** Augmentation du nombre d'époques à 10

| Paramètre | Valeur originale | Nouvelle valeur | 
|-----------|------------------|----------------|
| epochs | 5 | 10 |
| | | |

**Résultats :**
- Précision test : ~99%
- Observations : Légère amélioration de la précision, mais risque d'overfitting accru. Les courbes montrent une stabilisation après 6-7 époques.

### Expérimentation 2

**Modification effectuée :** Ajout d'une couche Dropout après la première couche Dense

| Paramètre | Valeur originale | Nouvelle valeur | 
|-----------|------------------|----------------|
| Architecture | Sans Dropout | Avec Dropout (0.2) |
| | | |

**Résultats :**
- Précision test : ~98.8%
- Observations : Légère diminution de la précision sur les données d'entraînement mais meilleure généralisation, écart réduit entre courbes d'entraînement et validation.

## Conclusion

| Question | Réponse |
|----------|---------|
| Quels sont les 3 principaux apprentissages de ce TP ? | 1. Les réseaux de neurones convolutifs sont particulièrement adaptés à la reconnaissance d'images.<br>2. La préparation des données (normalisation) est cruciale pour la performance du modèle.<br>3. L'architecture du réseau (nombre et types de couches) détermine sa capacité à extraire des caractéristiques pertinentes. |
| Quelles améliorations pourriez-vous suggérer pour ce modèle ? | Augmentation de données (rotations, translations), architecture plus profonde, utilisation de techniques de régularisation comme le Dropout, ajout de couches Batch Normalization, ou essayer des architectures plus avancées comme ResNet. |
| Comment ce modèle se compare-t-il aux capacités humaines de reconnaissance de chiffres ? | Le modèle atteint ~99% de précision, comparable aux performances humaines sur MNIST (~98%). Cependant, il est moins robuste face aux variations extrêmes ou aux styles d'écriture très différents de ceux des données d'entraînement. |
| Quelles autres applications de la vision par ordinateur vous intéressent ? | Reconnaissance faciale, détection d'objets, segmentation d'images médicales, systèmes de conduite autonome, reconnaissance de gestes, analyse d'images satellites, etc. |

---

## Glossaire des termes clés rencontrés

| Terme | Votre définition |
|-------|------------------|
| Convolution | Opération mathématique qui applique un filtre à une image pour extraire des caractéristiques spécifiques comme les bords, les textures ou les formes. |
| Pooling | Technique de réduction de dimension qui conserve les informations importantes tout en diminuant la taille des représentations. Max pooling prend la valeur maximale dans une région définie. |
| Epoch (époque) | Un passage complet à travers l'ensemble des données d'entraînement pendant l'apprentissage d'un modèle. |
| Batch | Sous-ensemble des données d'entraînement traité en une seule fois avant la mise à jour des poids. |
| Dropout | Technique de régularisation qui désactive aléatoirement certains neurones pendant l'entraînement pour éviter le surapprentissage. |
| Softmax | Fonction d'activation utilisée en sortie qui transforme un vecteur de nombres réels en distribution de probabilités. |
| Overfitting (surapprentissage) | Phénomène où un modèle apprend trop bien les données d'entraînement, incluant le bruit, ce qui diminue sa capacité de généralisation à de nouvelles données. |