# Phase 1 : Frameworks de Deep Learning (1h30)

![Frameworks pour débutants](https://images.unsplash.com/photo-1545987796-200677ee1011?auto=format&fit=crop&q=80&w=1000&h=300)

## Introduction aux frameworks dans un contexte professionnel (15 min)

**Objectif**: Comprendre l'utilité des frameworks de Deep Learning pour un développeur en entreprise et identifier ceux qui sont réellement utilisés sur le terrain.

### Les frameworks en entreprise

Avant de plonger dans le code, prenons un moment pour comprendre pourquoi les frameworks de Deep Learning sont si importants en contexte professionnel:

- **Productivité**: Ils permettent de développer des applications d'IA sans repartir de zéro
- **Maintenabilité**: Code plus standard, plus facile à comprendre par d'autres développeurs
- **Performances**: Optimisations intégrées qui seraient complexes à développer soi-même
- **Déploiement**: Outils intégrés pour mettre en production les modèles

Dans le monde professionnel actuel, plusieurs frameworks de Deep Learning sont couramment utilisés:

| Framework | Principaux cas d'usage |
|-----------|------------------------|
| TensorFlow/Keras | Applications web/mobile, systèmes en production |
| PyTorch | Recherche, prototypage, startups |
| Hugging Face | NLP, chatbots, traitement de texte |
| Scikit-learn | Prétraitement, ML classique, pipeline de données |

> "Pour un stage, la capacité à utiliser efficacement des frameworks existants est recherchée davantage que l'expertise théorique approfondie en Deep Learning." 
> 

### TensorFlow/Keras: la solution pragmatique

Pour cette séance, nous allons nous concentrer sur TensorFlow/Keras pour plusieurs raisons:

1. **Interface simple**: Keras offre une API haut niveau, parfaite pour débuter
2. **Déploiement facile**: Solutions intégrées pour mettre en production (TF Serving, TFLite)
3. **Documentation riche**: Ressources abondantes en français
4. **Modèles pré-entraînés**: Large bibliothèque de modèles prêts à l'emploi
5. **Demande professionnelle**: Le plus mentionné dans les offres de stage

### Démonstration: Applications réelles en entreprise

Voici quelques exemples concrets développés par des entreprises locales employant des anciens étudiants:

- **PME de logistique**: Application de reconnaissance de documents (bons de livraison, factures) permettant d'automatiser la saisie → Économie de 15h/semaine
- **Agence web**: Système de détection de contenu inapproprié dans les commentaires de sites e-commerce
- **Cabinet médical**: Application de classification d'images pour le tri préliminaire de photos de lésions cutanées

## Atelier pratique : Prise en main de TensorFlow/Keras (30 min)

### Objectif

Développer une première application de reconnaissance d'images simple en utilisant TensorFlow/Keras et en suivant les bonnes pratiques de l'industrie.

### Instructions pas à pas

#### Étape 1: Configuration de l'environnement (5 min)

1. Ouvrez Google Colab dans votre navigateur en allant sur [colab.research.google.com](https://colab.research.google.com)
2. Créez un nouveau notebook en cliquant sur "Nouveau notebook"
3. Renommez le notebook en "Reconnaissance d'images TensorFlow" en cliquant sur "Untitled" en haut
4. Copiez-collez le code suivant dans la première cellule et exécutez-la en cliquant sur le bouton Play ou en appuyant sur Shift+Enter:

```python
# Vérification de la version de TensorFlow
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

# Importation des bibliothèques essentielles
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
```

#### Étape 2: Utilisation d'un modèle pré-entraîné (10 min)

1. Créez une nouvelle cellule en cliquant sur le bouton "+ Code" ou en appuyant sur Alt+Enter
2. Copiez-collez le code suivant et exécutez-le:

```python
# Chargement d'un modèle pré-entraîné complet
model = MobileNetV2(weights='imagenet')

# Affichage du résumé du modèle pour comprendre son architecture
print("Structure du modèle:")
model.summary()
```

3. Observez la structure du modèle dans la sortie: notez le nombre de paramètres, les différentes couches, etc.

#### Étape 3: Préparation d'une image de test (5 min)

1. Créez une nouvelle cellule et exécutez le code suivant:

```python
# Téléchargement d'une image d'exemple
!wget -q -O test_image.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Pug_600.jpg/280px-Pug_600.jpg

# Affichage de l'image téléchargée
plt.figure(figsize=(4, 4))
plt.imshow(image.load_img('test_image.jpg'))
plt.axis('off')
plt.title("Image à classifier")
plt.show()

# Fonction pour prétraiter l'image
def preprocess_image(img_path):
    # Chargement et redimensionnement à la taille attendue par le modèle
    img = image.load_img(img_path, target_size=(224, 224))
    
    # Conversion en tableau numpy
    img_array = image.img_to_array(img)
    
    # Ajout de la dimension de batch (pour un seul échantillon)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prétraitement spécifique à MobileNetV2
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    return img_array

# Application du prétraitement à notre image
processed_image = preprocess_image('test_image.jpg')
print("Forme de l'image prétraitée:", processed_image.shape)
```

#### Étape 4: Prédiction et interprétation des résultats (10 min)

1. Créez une nouvelle cellule et exécutez le code suivant:

```python
# Utilisation du modèle pour faire une prédiction
predictions = model.predict(processed_image)

# Décodage des prédictions (conversion des indices en labels)
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
decoded_predictions = decode_predictions(predictions, top=5)[0]

# Affichage des résultats sous forme de graphique
plt.figure(figsize=(10, 3))
labels = [pred[1].replace('_', ' ') for pred in decoded_predictions]
scores = [pred[2] for pred in decoded_predictions]

plt.barh(labels, scores)
plt.xlabel('Probabilité')
plt.title('Top 5 des prédictions')
plt.xlim(0, 1.0)
plt.gca().invert_yaxis()  # Pour que le plus probable soit en haut
plt.tight_layout()
plt.show()

# Affichage des résultats détaillés
print("Prédictions:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i+1}. {label} ({score:.2f})")
```

2. Analysez les résultats:
   - Les prédictions indiquent-elles correctement qu'il s'agit d'un chien de race carlin (pug)?
   - Observez les probabilités associées à chaque classe
   - Quelles autres races de chiens sont détectées?

## Mini-projet : Application interactive de reconnaissance d'images (45 min)

### Objectif

Créer une application interactive simple qui permet de tester la reconnaissance d'images sur différentes photos.

### Instructions pas à pas

#### Étape 1: Création d'une interface interactive dans Colab (10 min)

1. Créez une nouvelle cellule et exécutez le code suivant:

```python
# Installation des widgets interactifs
!pip install -q ipywidgets
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
```

2. Dans une nouvelle cellule, créez l'interface utilisateur:

```python
# Fonction pour classifier une image téléchargée
def classify_uploaded_image(change):
    # Effacer les sorties précédentes
    clear_output(wait=True)
    
    # Afficher l'interface
    display(file_upload)
    display(output)
    
    # Récupérer le fichier téléchargé
    uploaded_file = list(change['new'].values())[0]
    content = uploaded_file['content']
    
    # Sauvegarder l'image localement
    with open('uploaded_image.jpg', 'wb') as f:
        f.write(content)
    
    # Prétraiter l'image
    img = image.load_img('uploaded_image.jpg', target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    # Afficher l'image originale
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image.load_img('uploaded_image.jpg'))
    plt.title("Image téléchargée")
    plt.axis('off')
    
    # Faire la prédiction
    predictions = model.predict(img_array)
    decoded_preds = decode_predictions(predictions, top=5)[0]
    
    # Afficher les résultats sous forme de graphique
    plt.subplot(1, 2, 2)
    labels = [pred[1].replace('_', ' ') for pred in decoded_preds]
    scores = [pred[2] for pred in decoded_preds]
    
    plt.barh(labels, scores)
    plt.xlabel('Probabilité')
    plt.title('Top 5 des prédictions')
    plt.xlim(0, 1.0)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    
    # Afficher les résultats textuels
    print("Prédictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_preds):
        print(f"{i+1}. {label.replace('_', ' ')} ({score:.2f})")

# Créer les widgets
file_upload = widgets.FileUpload(
    accept='.jpg, .jpeg, .png',
    multiple=False,
    description='Télécharger une image:'
)
output = widgets.Output()

# Lier la fonction au widget
file_upload.observe(classify_uploaded_image, names='value')

# Afficher l'interface
display(HTML("<h3>Application de reconnaissance d'images</h3>"))
display(HTML("<p>Téléchargez une image pour voir ce que le modèle peut reconnaître:</p>"))
display(file_upload)
display(output)
```

#### Étape 2: Démonstration avec des exemples variés (15 min)

1. Créez une nouvelle cellule pour télécharger différentes images de test:

```python
# Téléchargement d'images variées pour nos tests
!wget -q -O cat.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg
!wget -q -O car.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/2022_Tesla_Model_Y.jpg/1200px-2022_Tesla_Model_Y.jpg
!wget -q -O laptop.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/15-inch_MacBook_Pro_with_Touch_Bar_July_2018.jpg/1200px-15-inch_MacBook_Pro_with_Touch_Bar_July_2018.jpg

# Fonction pour classifier les images d'exemple
def classify_example_images():
    example_images = ['cat.jpg', 'car.jpg', 'laptop.jpg']
    
    for img_path in example_images:
        # Prétraiter l'image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        
        # Afficher l'image originale
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.imshow(image.load_img(img_path))
        plt.title(f"Image: {img_path}")
        plt.axis('off')
        
        # Faire la prédiction
        predictions = model.predict(img_array)
        decoded_preds = decode_predictions(predictions, top=5)[0]
        
        # Afficher les résultats sous forme de graphique
        plt.subplot(1, 2, 2)
        labels = [pred[1].replace('_', ' ') for pred in decoded_preds]
        scores = [pred[2] for pred in decoded_preds]
        
        plt.barh(labels, scores)
        plt.xlabel('Probabilité')
        plt.title('Top 5 des prédictions')
        plt.xlim(0, 1.0)
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
        
        # Afficher les résultats textuels
        print(f"Prédictions pour {img_path}:")
        for i, (imagenet_id, label, score) in enumerate(decoded_preds):
            print(f"{i+1}. {label.replace('_', ' ')} ({score:.2f})")
        print("\n" + "-"*50 + "\n")

# Exécuter la fonction
classify_example_images()
```

#### Étape 3: Création d'un outil d'analyse approfondie (20 min)

1. Créez une nouvelle cellule pour implémenter un outil qui montre les activations internes du réseau:

```python
def visualize_activations(img_path):
    """Visualise les activations intermédiaires du modèle pour mieux comprendre la reconnaissance"""
    # Charger et prétraiter l'image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    # Créer un modèle pour extraire les activations intermédiaires
    layer_outputs = [layer.output for layer in model.layers if 'block' in layer.name][:3]  # Seulement les 3 premières couches de bloc
    activation_model = tf.keras.Model(inputs=model.input, outputs=layer_outputs)
    
    # Obtenir les activations
    activations = activation_model.predict(img_array)
    
    # Afficher l'image originale
    plt.figure(figsize=(15, 10))
    plt.subplot(1, 4, 1)
    plt.title("Image originale")
    plt.imshow(image.load_img(img_path))
    plt.axis('off')
    
    # Afficher quelques activations pour chaque couche
    for i, layer_activation in enumerate(activations):
        # Seulement 9 filtres par couche
        n_features = min(9, layer_activation.shape[-1])
        layer_name = f"Couche {i+1}"
        
        plt.subplot(1, 4, i+2)
        plt.title(layer_name)
        
        # Créer une grille pour les visualisations
        n_cols = 3
        n_rows = n_features // n_cols + (1 if n_features % n_cols > 0 else 0)
        display_grid = np.zeros((n_rows * 64, n_cols * 64))
        
        # Remplir la grille avec des images
        for row in range(n_rows):
            for col in range(n_cols):
                channel_idx = row * n_cols + col
                if channel_idx < n_features:
                    # Prendre une activité moyenne sur la dimension du batch
                    channel_image = layer_activation[0, :, :, channel_idx]
                    
                    # Normaliser pour une meilleure visualisation
                    channel_image -= channel_image.mean()
                    if channel_image.std() > 0:
                        channel_image /= channel_image.std()
                    channel_image *= 64
                    channel_image += 128
                    channel_image = np.clip(channel_image, 0, 255).astype('uint8')
                    
                    # Ajouter à la grille
                    display_grid[row*64:(row+1)*64, col*64:(col+1)*64] = channel_image
        
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Faire et afficher la prédiction
    predictions = model.predict(img_array)
    decoded_preds = decode_predictions(predictions, top=5)[0]
    
    print(f"Prédictions pour {img_path}:")
    for i, (imagenet_id, label, score) in enumerate(decoded_preds):
        print(f"{i+1}. {label.replace('_', ' ')} ({score:.2f})")

# Tester l'outil sur plusieurs images
for img_path in ['cat.jpg', 'car.jpg', 'laptop.jpg']:
    print("-"*50)
    print(f"Analyse de {img_path}")
    print("-"*50)
    visualize_activations(img_path)
    print("\n")
```

## Bonnes pratiques pour les projets professionnels (15 min)

Pour conclure cette phase, passons en revue les bonnes pratiques essentielles pour développer des applications de Deep Learning en contexte professionnel:

### 1. Structure du code

- **Modularité**: Séparez clairement les différentes fonctionnalités (prétraitement, modèle, API)
- **Documentation**: Commentez votre code et créez une documentation utilisateur
- **Gestion d'erreurs**: Prévoyez des cas d'erreur et des messages adaptés
- **Logging**: Ajoutez des logs pour faciliter le débogage

### 2. Performances

- **Batch processing**: Traitez les données par lots plutôt qu'individuellement
- **Mise en cache**: Évitez de recharger le modèle à chaque requête
- **Précalcul**: Précalculez ce qui peut l'être pour accélérer les inférences
- **Optimisation matérielle**: Utilisez GPU/TPU quand disponible, CPU optimisé sinon

### 3. Sécurité

- **Validation des entrées**: Vérifiez toujours les données entrantes
- **Limitation de taille**: Fixez une taille maximale pour les fichiers
- **Rate limiting**: Limitez le nombre de requêtes par utilisateur
- **Sanitization**: Nettoyez les chemins de fichiers et autres entrées sensibles

### 4. Déploiement

- **Conteneurisation**: Utilisez Docker pour faciliter le déploiement
- **CI/CD**: Automatisez les tests et le déploiement
- **Monitoring**: Surveillez les performances et erreurs
- **Versioning**: Versionnez vos modèles et API

## Conclusion et transition

Cette phase vous a permis de découvrir comment utiliser efficacement TensorFlow/Keras dans un contexte professionnel. Vous avez appris à:

 - Utiliser un modèle pré-entraîné pour la reconnaissance d'images
 - Prétraiter des images pour l'inférence
 - Créer une interface interactive pour tester votre modèle
 - Visualiser et comprendre les activations internes du réseau

Ces compétences sont directement applicables dans des projets professionnels. Dans la prochaine partie, nous allons nous concentrer sur l'amélioration des performances de nos modèles pour les rendre plus adaptés à des environnements de production.

[Retour au Module 3](index.md){ .md-button }
[Continuer vers l'amélioration des performances](integration.md){ .md-button .md-button--primary }