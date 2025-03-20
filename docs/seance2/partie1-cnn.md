### Mini-projet CNN (partie1-cnn.md)

```markdown
# Copier dans docs/seance2/partie1-cnn.md
# Phase 1 : Mini-projet CNN pour la vision par ordinateur

![CNN Architecture](https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la phase

Dans cette phase, vous allez :
- Comprendre les principes fondamentaux des réseaux de neurones convolutifs (CNN)
- Implémenter un CNN pour la classification d'images avec TensorFlow/Keras
- Visualiser et interpréter les filtres et feature maps d'un CNN
- Intégrer un modèle CNN dans une application web simple

## Partie 1: Principes des CNN (20 min)

### Architecture d'un CNN

Les réseaux de neurones convolutifs (CNN) sont spécialement conçus pour traiter des données structurées en grille, comme les images. Leur architecture s'inspire du cortex visuel biologique et comprend plusieurs types de couches spécialisées :

1. **Couches de convolution** : appliquent des filtres qui glissent sur l'image pour détecter des motifs locaux (contours, textures, etc.)
2. **Couches de pooling** : réduisent la dimension spatiale pour diminuer le nombre de paramètres
3. **Couches fully connected** : combinent les caractéristiques extraites pour la classification finale

Avantages majeurs pour un développeur d'applications :
- Réduction significative du nombre de paramètres (partage de poids)
- Invariance à la translation (détection de motifs quelle que soit leur position)
- Capacité d'extraire automatiquement des caractéristiques pertinentes

## Partie 2: Implémentation d'un CNN pour MNIST (40 min)

### Instructions

1. Ouvrez le notebook Jupyter [cnn-classification.ipynb](../ressources/notebooks/cnn-classification.ipynb) dans Google Colab
2. Suivez les instructions étape par étape pour implémenter un CNN pour la classification des chiffres manuscrits (MNIST)
3. Exécutez chaque cellule et observez les résultats
4. Portez une attention particulière aux sections suivantes :
   - Architecture du modèle CNN
   - Processus d'entraînement
   - Visualisation des filtres et feature maps
   - Analyse des performances et des erreurs

### Points clés à explorer

- Comment les couches de convolution extraient-elles des caractéristiques de plus en plus abstraites ?
- Quel est l'impact du nombre de filtres et de couches sur les performances ?
- Comment les feature maps révèlent-elles ce que "voit" le réseau ?
- Quelles sont les limites du modèle face à des données bruitées ou déformées ?

## Partie 3: Intégration dans une application web (30 min)

### Instructions

1. Téléchargez et examinez le script Python [web-integration.py](../ressources/code/web-integration.py)
2. Ce script implémente une application Flask qui :
   - Charge un modèle CNN pré-entraîné
   - Fournit une interface web pour uploader des images
   - Prétraite les images pour les adapter au modèle
   - Affiche les prédictions et visualisations

3. Pour exécuter l'application :
   ```bash
   # Installer les dépendances
   pip install flask tensorflow pillow matplotlib numpy
   
   # Exécuter l'application
   python web-integration.py

4. Explorez l'application à l'adresse http://localhost:5001

5. Analysez le code pour comprendre :

- Comment le modèle est chargé et utilisé pour l'inférence
- Comment les images sont prétraitées
- Comment l'API Flask expose le modèle
- Comment le frontend interagit avec l'API


## Points clés à explorer

- Quels sont les défis d'intégration d'un modèle de Deep Learning dans une application web ?
- Comment gérer le prétraitement des images côté serveur ?
- Quelles améliorations pourriez-vous apporter à cette application ?
- Comment pourriez-vous adapter cette approche pour d'autres types de modèles CNN ?

# Exercices supplémentaires

Si vous terminez en avance, essayez ces défis :

1. Modification de l'architecture : Ajoutez des couches supplémentaires au CNN et observez l'impact sur les performances
2. Test avec vos propres images : Dessinez vos propres chiffres et testez-les avec l'application web
3. Robustesse : Expérimentez avec différentes perturbations (bruit, rotation) et analysez la robustesse du modèle
Optimisation du frontend : Améliorez l'interface utilisateur de l'application web

# Ressources complémentaires

- Tutoriel TensorFlow sur les CNN
- Visualisation de CNN (Distill.pub)
- Documentation Flask

Retour à la Séance 2{ .md-button }
Continuer vers la Phase 2: RNN{ .md-button .md-button--primary }