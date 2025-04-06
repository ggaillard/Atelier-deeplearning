# Schéma conceptuel à compléter

## Instructions

Le schéma ci-dessous représente l'architecture et le fonctionnement d'un réseau de neurones. Complétez-le en plaçant les étiquettes appropriées aux emplacements numérotés.

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

## Éléments à placer

Choisissez dans la liste suivante les éléments à placer aux emplacements numérotés :

1. Couche d'entrée (Input Layer)
2. Première couche cachée (Hidden Layer 1)
3. Deuxième couche cachée (Hidden Layer 2)
4. Couche de sortie (Output Layer)
5. Prédiction (Prediction)
6. Calcul de l'erreur (Loss Calculation)
7. Données réelles (Ground Truth)
8. Forward Propagation
9. Backward Propagation
10. Fonction d'activation
11. Ajustement des poids (Weight Update)
12. Preprocessing des données

## Structure du réseau

En plus de compléter le schéma, indiquez :

1. Quel type de réseau de neurones est représenté ici ? _______________________

2. Combien de neurones pourrait contenir chaque couche pour un problème de reconnaissance de chiffres manuscrits (MNIST) ?
   - Couche d'entrée : _______
   - Première couche cachée : _______
   - Deuxième couche cachée : _______
   - Couche de sortie : _______

3. Quelle fonction d'activation serait appropriée pour :
   - Les couches cachées : _______________________
   - La couche de sortie : _______________________

## Processus d'apprentissage

Décrivez brièvement les étapes du processus d'apprentissage en utilisant les termes appropriés :

1. _________________________________________________________________

2. _________________________________________________________________

3. _________________________________________________________________

4. _________________________________________________________________

## Rendu

Une fois complété, incluez ce schéma dans votre synthèse personnelle en expliquant comment ces différentes composantes interagissent pour permettre l'apprentissage du réseau.