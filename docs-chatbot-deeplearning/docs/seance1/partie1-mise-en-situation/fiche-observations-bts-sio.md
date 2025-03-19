# Fiche d'observations - Deep Learning pour BTS SIO SLAM

**Nom et prénom :** _________________________________

**Date :** _________________

## 1. Configuration et environnement de développement

- Framework utilisé : TensorFlow/Keras
- Version de TensorFlow : ________________
- GPU disponible ? ⬜ Oui  ⬜ Non
- Temps d'exécution approximatif : ________________

## 2. Jeu de données MNIST

- Nombre d'images d'entraînement : ________________
- Nombre d'images de test : ________________
- Dimensions de chaque image : ________________
- Nombre de classes : ________________

**Quel prétraitement a été appliqué aux données ? (cochez les cases)**

- ⬜ Redimensionnement
- ⬜ Normalisation
- ⬜ Encodage one-hot des labels
- ⬜ Restructuration (reshape)

**Pourquoi normalise-t-on les valeurs des pixels ?**
_______________________________________________________
_______________________________________________________

## 3. Architecture du modèle

### Couches du modèle (complétez le tableau)

| Type de couche | Nombre de filtres/neurones | Taille du noyau | Fonction d'activation |
|----------------|---------------------------|-----------------|------------------------|
| Input          | -                         | -               | -                      |
| Conv2D         |                           |                 |                        |
| MaxPooling2D   | -                         |                 | -                      |
| Conv2D         |                           |                 |                        |
| MaxPooling2D   | -                         |                 | -                      |
| Flatten        | -                         | -               | -                      |
| Dense          |                           | -               |                        |
| Dense (sortie) |                           | -               |                        |

**Nombre total de paramètres :** ________________

**Rôle de chaque type de couche :**

- Conv2D : _________________________________________________
- MaxPooling2D : ____________________________________________
- Flatten : ________________________________________________
- Dense : __________________________________________________

## 4. Compilation et entraînement

### Paramètres de compilation

- Fonction de perte : ________________
- Optimiseur : ________________
- Métrique(s) : ________________

### Paramètres d'entraînement

- Nombre d'époques : ________________
- Taille du batch : ________________
- Proportion de validation : ________________

## 5. Performances du modèle

- Précision sur l'ensemble d'entraînement : ________%
- Précision sur l'ensemble de validation : ________%
- Précision sur l'ensemble de test : ________%

## 6. Analyse des courbes d'apprentissage

**Observations sur la courbe de précision :**
_______________________________________________________
_______________________________________________________
_______________________________________________________

**Observations sur la courbe de perte :**
_______________________________________________________
_______________________________________________________
_______________________________________________________

**Y a-t-il des signes de surapprentissage (overfitting) ? Si oui, lesquels ?**
_______________________________________________________
_______________________________________________________

## 7. Test avec vos propres dessins

| Chiffre dessiné | Prédiction | Confiance | Correct ? |
|----------------|------------|-----------|-----------|
|                |            |           | ⬜ Oui ⬜ Non |
|                |            |           | ⬜ Oui ⬜ Non |
|                |            |           | ⬜ Oui ⬜ Non |

**Quelles difficultés avez-vous rencontrées lors de vos tests ?**
_______________________________________________________
_______________________________________________________

## 8. Expérimentations et optimisations

### Expérimentation 1 : ________________________________

**Modifications apportées :**
_______________________________________________________
_______________________________________________________

**Résultats observés :**
- Nouvelle précision : ________%
- Impact sur le temps d'entraînement : ________________
- Autres observations : ________________________________

### Expérimentation 2 : ________________________________

**Modifications apportées :**
_______________________________________________________
_______________________________________________________

**Résultats observés :**
- Nouvelle précision : ________%
- Impact sur le temps d'entraînement : ________________
- Autres observations : ________________________________

## 9. Application à votre projet final (chatbot pédagogique)

**Comment pourriez-vous utiliser ce que vous avez appris aujourd'hui dans votre projet de chatbot pédagogique sur le Deep Learning ?**
_______________________________________________________
_______________________________________________________
_______________________________________________________

**Quelles fonctionnalités de votre chatbot pourraient être améliorées par les réseaux de neurones convolutifs ?**
_______________________________________________________
_______________________________________________________
_______________________________________________________

## 10. Questions et concepts à approfondir

**Listez 3 concepts du Deep Learning que vous aimeriez approfondir après cette séance :**
1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

**Quelles questions vous posez-vous encore sur le Deep Learning ?**
_______________________________________________________
_______________________________________________________
_______________________________________________________

---

## Bilan de la séance (auto-évaluation)

Sur une échelle de 1 à 5, évaluez votre compréhension :

| Concept | 1 (Pas compris) | 2 | 3 | 4 | 5 (Parfaitement compris) |
|---------|----------------|---|---|---|-----------------------------|
| Structure d'un réseau de neurones convolutif | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Prétraitement des données | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Entraînement d'un modèle | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Analyse des performances | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Utilisation pratique du modèle | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

**Ce que j'ai trouvé le plus intéressant :**
_______________________________________________________

**Ce que j'ai trouvé le plus difficile :**
_______________________________________________________