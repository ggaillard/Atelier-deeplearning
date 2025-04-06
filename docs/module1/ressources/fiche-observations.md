# 📋 Fiche d'observations - Hello World du Deep Learning

*Cette fiche d'observations vous accompagne étape par étape dans l'exploration du notebook. Pour chaque section, notez les références aux cellules correspondantes du notebook.*

## Informations générales

**Nom et prénom :** ____________________________

**Date :** ____________________________

**Groupe :** ____________________________

## Partie 1 : Configuration et vérification de l'environnement *(Cellule 2)*

| Question | Observation |
|----------|-------------|
| Version de TensorFlow détectée | |
| GPU disponible ? (Oui/Non) | |
| Quelle est l'importance d'avoir un GPU pour le Deep Learning ? | |

## Partie 2 : Chargement et préparation des données *(Cellule 3)*

| Question | Observation |
|----------|-------------|
| Combien d'exemples d'entraînement sont disponibles ? | |
| Combien d'exemples de test sont disponibles ? | |
| Quelle est la dimension des images ? | |
| Pourquoi normalise-t-on les valeurs des pixels entre 0 et 1 ? | |
| D'après les exemples affichés, quelles difficultés pourrait rencontrer le modèle ? | |

## Partie 3 : Architecture du modèle *(Cellule 4)*

Dessinez le schéma simplifié de l'architecture du réseau de neurones utilisé :

```
[Schéma à compléter]
```

| Question | Observation |
|----------|-------------|
| Combien de couches comporte le modèle ? | |
| Combien de paramètres entraînables au total ? | |
| Quel est le rôle des couches de convolution ? | |
| Quel est le rôle des couches de pooling ? | |
| Pourquoi utilise-t-on 'softmax' comme activation de la dernière couche ? | |

## Partie 4 : Entraînement du modèle *(Cellule 5)*

| Question | Observation |
|----------|-------------|
| Combien d'époques ont été effectuées ? | |
| Quelle est la précision finale sur les données d'entraînement ? | |
| Quelle est la précision finale sur les données de validation ? | |
| Quelle est la précision sur l'ensemble de test ? | |
| Y a-t-il un signe de surapprentissage (overfitting) ? Pourquoi ? | |

## Partie 5 : Visualisation des résultats *(Cellule 6)*

Analysez les graphiques d'apprentissage :

| Question | Observation |
|----------|-------------|
| La courbe de précision d'entraînement est-elle croissante ? | |
| La courbe de perte d'entraînement est-elle décroissante ? | |
| Y a-t-il un écart important entre les courbes d'entraînement et de validation ? | |
| D'après vous, l'entraînement a-t-il été suffisant (nombre d'époques) ? | |

## Partie 6 : Prédictions sur des exemples de test *(Cellule 7)*

Observez les 10 exemples de prédiction :

| Question | Observation |
|----------|-------------|
| Combien de prédictions sont correctes sur les 10 exemples ? | |
| Pour les prédictions incorrectes, quelles pourraient être les raisons d'erreur ? | |
| Certains chiffres semblent-ils plus difficiles à reconnaître que d'autres ? | |

## Partie 7 : Test avec votre propre dessin *(Cellule 8)*

| Question | Observation |
|----------|-------------|
| Quels chiffres avez-vous dessinés ? | |
| Combien ont été correctement prédits ? | |
| Pour ceux mal prédits, quelle était la prédiction et pourquoi selon vous ? | |
| Comment le prétraitement de l'image a-t-il transformé votre dessin ? | |

## Partie 8 : Expérimentations *(Cellule 9)*

Documentez vos expérimentations en modifiant le modèle ou les paramètres :

### Expérimentation 1

**Modification effectuée :** _________________________

| Paramètre | Valeur originale | Nouvelle valeur | 
|-----------|------------------|----------------|
| | | |
| | | |

**Résultats :**
- Précision test : _______%
- Observations : _______________________

### Expérimentation 2

**Modification effectuée :** _________________________

| Paramètre | Valeur originale | Nouvelle valeur | 
|-----------|------------------|----------------|
| | | |
| | | |

**Résultats :**
- Précision test : _______%
- Observations : _______________________

## Conclusion

| Question | Réponse |
|----------|---------|
| Quels sont les 3 principaux apprentissages de ce TP ? | 1.<br>2.<br>3. |
| Quelles améliorations pourriez-vous suggérer pour ce modèle ? | |
| Comment ce modèle se compare-t-il aux capacités humaines de reconnaissance de chiffres ? | |
| Quelles autres applications de la vision par ordinateur vous intéressent ? | |

---

## Glossaire des termes clés rencontrés

| Terme | Votre définition |
|-------|------------------|
| Convolution | |
| Pooling | |
| Epoch (époque) | |
| Batch | |
| Dropout | |
| Softmax | |
| Overfitting (surapprentissage) | |