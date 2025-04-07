# Auto-évaluation du Module 3

![Auto-évaluation](../images/banner-evaluation.svg)

Cette auto-évaluation vous permet de vérifier votre compréhension des concepts clés abordés dans le Module 3. Prenez le temps de répondre à chaque question, puis consultez les réponses en fin de document pour évaluer votre progression.

## QCM : Frameworks et optimisation (15 points)

Pour chaque question, cochez la ou les réponses correctes.

### 1. Parmi ces frameworks de Deep Learning, lequel est le plus adapté pour le déploiement en production sur des appareils mobiles ?
- [ ] a) PyTorch
- [ ] b) TensorFlow/Keras
- [ ] c) Scikit-learn
- [ ] d) Theano

### 2. Quels sont les avantages des modèles pré-entraînés ? (plusieurs réponses possibles)
- [ ] a) Réduction du temps de développement
- [ ] b) Besoin de moins de données d'entraînement
- [ ] c) Poids plus petits que les modèles entraînés from scratch
- [ ] d) Meilleures performances sur des datasets limités

### 3. La quantification d'un modèle consiste à :
- [ ] a) Réduire le nombre de couches du modèle
- [ ] b) Réduire la précision des poids (ex: float32 → int8)
- [ ] c) Supprimer les poids proches de zéro
- [ ] d) Combiner plusieurs modèles ensemble

### 4. Quelle technique d'optimisation consiste à supprimer les connexions les moins importantes dans un réseau ?
- [ ] a) Quantification
- [ ] b) Élagage (pruning)
- [ ] c) Distillation
- [ ] d) Factorisation matricielle

### 5. Quel format est généralement utilisé pour déployer des modèles sur des appareils mobiles ?
- [ ] a) HDF5
- [ ] b) SavedModel
- [ ] c) TensorFlow Lite
- [ ] d) ONNX

### 6. Dans une API de Deep Learning, quelle technique est recommandée pour améliorer les performances ?
- [ ] a) Recharger le modèle à chaque requête
- [ ] b) Convertir les images en CSV avant traitement
- [ ] c) Mettre en cache le modèle en mémoire
- [ ] d) Désactiver la gestion d'erreurs

### 7. Quelle architecture de modèle est spécifiquement conçue pour être légère et efficace ?
- [ ] a) VGG16
- [ ] b) MobileNetV2
- [ ] c) ResNet152
- [ ] d) InceptionV4

### 8. La distillation de connaissances consiste à :
- [ ] a) Extraire les poids d'un modèle pour les analyser
- [ ] b) Entraîner un plus petit modèle (élève) à imiter un plus grand modèle (enseignant)
- [ ] c) Décomposer un gros modèle en plusieurs petits
- [ ] d) Fusionner plusieurs modèles spécialisés

### 9. Lors de l'intégration d'un modèle dans une application web, quelle affirmation est correcte ?
- [ ] a) Le modèle doit toujours être exécuté côté client (JavaScript)
- [ ] b) Les prédictions doivent être traitées de manière synchrone
- [ ] c) Il est recommandé de prétraiter les images côté client avant envoi
- [ ] d) L'API du modèle ne nécessite pas de documentation si elle est utilisée en interne

### 10. Parmi ces paramètres, lequel peut être ajusté pour rendre les réponses d'un modèle de langage plus déterministes (moins créatives) ?
- [ ] a) Augmenter la température
- [ ] b) Diminuer la température
- [ ] c) Augmenter le nombre maximum de tokens
- [ ] d) Activer le mode streaming

## Questions à réponse courte (10 points)

Répondez brièvement aux questions suivantes (2-3 phrases par question).

### 11. Expliquez pourquoi l'optimisation des modèles de Deep Learning est importante dans un contexte professionnel.

...................................................................

...................................................................

### 12. Décrivez deux différences principales entre TensorFlow et PyTorch.

...................................................................

...................................................................

### 13. Quels sont les avantages et inconvénients de la quantification post-entraînement ?

...................................................................

...................................................................

### 14. Comment l'API Mistral AI peut-elle être utilisée pour créer un chatbot pédagogique ?

...................................................................

...................................................................

### 15. Quelles sont les deux bonnes pratiques essentielles pour sécuriser une API de reconnaissance d'images ?

...................................................................

...................................................................

## Exercice pratique : Optimisation d'un modèle (15 points)

Complétez le code suivant pour optimiser un modèle MobileNetV2 avec la quantification TensorFlow Lite.

```python
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
import numpy as np

# Chargement du modèle pré-entraîné
base_model = MobileNetV2(weights='imagenet', include_top=True)

# 1. Convertir le modèle en TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(base_model)
tflite_model = ................................. # À compléter

# 2. Appliquer la quantification post-entraînement
converter = tf.lite.TFLiteConverter.from_keras_model(base_model)
converter.optimizations = ........................... # À compléter
quantized_model = converter.convert()

# 3. Comparer les tailles des modèles
original_size = .................. # À compléter : calculer la taille du modèle original
tflite_size = len(tflite_model) / (1024 * 1024)  # Taille en Mo
quantized_size = len(quantized_model) / (1024 * 1024)  # Taille en Mo

print(f"Taille du modèle original: {original_size:.2f} Mo")
print(f"Taille du modèle TFLite: {tflite_size:.2f} Mo")
print(f"Taille du modèle quantifié: {quantized_size:.2f} Mo")
print(f"Réduction de taille: {(1 - quantized_size/original_size) * 100:.2f}%")

# 4. Fonction pour prétraiter une image pour l'inférence
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = .................. # À compléter : convertir l'image en tableau
    img_array = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

# 5. Création d'un interpréteur TFLite
interpreter = tf.lite.Interpreter(model_content=quantized_model)
....................... # À compléter : allouer les tenseurs

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 6. Fonction d'inférence avec le modèle quantifié
def predict_with_tflite(image_path):
    # Prétraitement de l'image
    input_data = preprocess_image(image_path)
    
    # Définir les données d'entrée
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    # Exécuter l'inférence
    ...................... # À compléter : invoquer l'interpréteur
    
    # Obtenir les résultats
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    # Traiter les résultats
    results = tf.keras.applications.mobilenet_v2.decode_predictions(output_data)
    return results[0]
```

## Exercice de réflexion : Cas pratique d'intégration (10 points)

Vous êtes développeur dans une petite entreprise qui propose des solutions de reconnaissance d'objets pour le commerce de détail. On vous demande de créer une API qui permettra d'identifier les produits à partir de photos prises par les employés sur leurs smartphones.

1. Quelle architecture de modèle choisiriez-vous et pourquoi ? (2 points)

...................................................................

...................................................................

2. Quelles techniques d'optimisation mettriez-vous en place ? (2 points)

...................................................................

...................................................................

3. Comment structureriez-vous votre API REST ? Décrivez les endpoints et leurs paramètres. (3 points)

...................................................................

...................................................................

...................................................................

4. Quelles mesures de sécurité implémenteriez-vous ? (3 points)

...................................................................

...................................................................

...................................................................

## Corrigé

### QCM
1. b) TensorFlow/Keras
2. a) b) d)
3. b) Réduire la précision des poids (ex: float32 → int8)
4. b) Élagage (pruning)
5. c) TensorFlow Lite
6. c) Mettre en cache le modèle en mémoire
7. b) MobileNetV2
8. b) Entraîner un plus petit modèle (élève) à imiter un plus grand modèle (enseignant)
9. c) Il est recommandé de prétraiter les images côté client avant envoi
10. b) Diminuer la température

### Questions à réponse courte (éléments attendus)
11. L'optimisation permet de réduire les coûts d'infrastructure, diminuer la latence pour une meilleure expérience utilisateur, économiser l'énergie (crucial pour les appareils mobiles) et rendre les modèles accessibles sur des appareils à ressources limitées.

12. TensorFlow utilise des graphes statiques (plus efficaces en production) tandis que PyTorch utilise des graphes dynamiques (plus flexibles pour la recherche). TensorFlow a un écosystème plus complet pour le déploiement (TFLite, TF Serving) alors que PyTorch est généralement considéré comme plus intuitif pour le développement.

13. Avantages : Réduction significative de la taille du modèle (jusqu'à 4x), accélération de l'inférence, pas besoin de réentraînement. Inconvénients : Perte potentielle de précision, surtout pour les tâches complexes, incompatibilité avec certaines opérations avancées.

14. L'API Mistral AI peut être utilisée pour créer un chatbot pédagogique en envoyant des requêtes avec un prompt système adapté à l'enseignement, en enrichissant les prompts avec une base de connaissances spécifique au domaine enseigné, et en maintenant un contexte conversationnel pour assurer la cohérence des échanges.

15. Validation des entrées (vérification du format et de la taille des images), limitation du taux de requêtes (rate limiting), authentification par clé API, sanitization des chemins de fichiers, restriction des types MIME acceptés.

### Exercice pratique (éléments de correction)
```python
# 1. Convertir le modèle en TensorFlow Lite
tflite_model = converter.convert()

# 2. Appliquer la quantification post-entraînement
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 3. Comparer les tailles des modèles
original_size = sum(np.prod(w.shape) * w.dtype.size for w in base_model.weights) / (1024 * 1024)

# 4. Fonction pour prétraiter une image pour l'inférence
img_array = tf.keras.preprocessing.image.img_to_array(img)

# 5. Création d'un interpréteur TFLite
interpreter.allocate_tensors()

# 6. Fonction d'inférence avec le modèle quantifié
interpreter.invoke()
```

### Exercice de réflexion
Les réponses peuvent varier, mais devraient inclure des points comme:

1. Architecture: MobileNetV2 ou EfficientNet serait un bon choix car ils offrent un bon équilibre entre précision et performance, sont optimisés pour les appareils mobiles, et peuvent être facilement affinés pour des tâches spécifiques.

2. Techniques d'optimisation: Quantification post-entraînement pour réduire la taille du modèle, transfer learning sur un petit dataset de produits spécifiques, et éventuellement pruning pour réduire davantage la taille.

3. Structure API REST:
   - POST /predict - Pour envoyer une image et recevoir des prédictions
   - GET /categories - Pour récupérer la liste des catégories de produits
   - POST /feedback - Pour recueillir les retours sur les prédictions incorrectes
   Paramètres pour /predict: image (fichier ou base64), top_k (nombre de prédictions), confidence_threshold.

4. Sécurité:
   - Authentification par clé API
   - Rate limiting pour prévenir les abus
   - Validation des entrées (taille et format d'image)
   - HTTPS pour le chiffrement des données
   - Logging sécurisé pour l'audit

## Barème et auto-évaluation

| Section | Points maximum | Mes points |
|---------|----------------|------------|
| QCM | 15 | |
| Questions à réponse courte | 10 | |
| Exercice pratique | 15 | |
| Exercice de réflexion | 10 | |
| **Total** | **50** | |

### Évaluation des compétences

| Note | Niveau | Commentaire |
|------|--------|-------------|
| 40-50 | Expert | Vous maîtrisez les concepts avancés et êtes prêt pour le projet final |
| 30-39 | Confirmé | Bonne compréhension globale, quelques points à approfondir |
| 20-29 | Intermédiaire | Compréhension des bases, mais besoin de renforcement |
| 0-19 | Débutant | Nécessite une révision approfondie avant le projet final |

## Questions pour approfondir

Si vous avez obtenu un bon score, vous pouvez explorer ces questions pour aller plus loin :

1. Comment implémenteriez-vous un système de mise à jour progressive des modèles en production ?
2. Quelles stratégies pourriez-vous utiliser pour gérer les biais potentiels dans un modèle de vision par ordinateur ?
3. Comment adapter l'architecture d'une API de Deep Learning pour gérer des millions de requêtes par jour ?
4. Quelles techniques permettraient d'optimiser les prompts pour un modèle de langage au-delà des exemples vus dans ce module ?

[Retour au Module 3](index.md){ .md-button }
[Continuer vers le Module 4](../module4/index.md){ .md-button .md-button--primary }