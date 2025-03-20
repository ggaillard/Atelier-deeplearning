## Cellules corrigées pour le notebook

### Cellule 1 (Introduction - Markdown)
```markdown
# 🚀 Hello World du Deep Learning

## Reconnaissance de chiffres manuscrits avec TensorFlow et Keras

### Objectifs de ce notebook

- Charger et préparer un jeu de données de chiffres manuscrits
- Créer un réseau de neurones simple
- Entraîner le modèle
- Visualiser les résultats
- Tester le modèle avec vos propres dessins

### BTS SIO SLAM - Découverte du Deep Learning
```

### Cellule 2 (Configuration - Code)
```python
# Importation des bibliothèques nécessaires
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Vérification de la version de TensorFlow
print(f"TensorFlow version: {tf.__version__}")
print(f"Keras version: {keras.__version__}")

# Vérification du GPU (méthode recommandée)
print("GPU disponible :", len(tf.config.list_physical_devices('GPU')) > 0)
```

### Cellule 3 (Chargement des données - Code)
```python
# Chargement du dataset MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Prétraitement des données
X_train = X_train.reshape((60000, 28, 28, 1)) / 255.0
X_test = X_test.reshape((10000, 28, 28, 1)) / 255.0

# Conversion des labels en catégories
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Affichage de quelques exemples
plt.figure(figsize=(10, 2))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap='gray')
    plt.axis('off')
plt.suptitle("Exemples de chiffres manuscrits")
plt.show()

print(f"Nombre d'exemples d'entraînement : {X_train.shape[0]}")
print(f"Nombre d'exemples de test : {X_test.shape[0]}")
print(f"Dimensions d'une image : {X_train.shape[1:3]}")
print(f"Valeurs des pixels après normalisation : de 0 à 1")
```

### Cellule 4 (Création du modèle - Code)
```python
# Création du modèle de réseau de neurones
# On utilise Input comme première couche (recommandé)
inputs = keras.Input(shape=(28, 28, 1))

# Couche de convolution
x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = layers.MaxPooling2D((2, 2))(x)

# Couche de convolution supplémentaire
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)

# Aplatissement
x = layers.Flatten()(x)

# Couche dense
x = layers.Dense(64, activation='relu')(x)

# Couche de sortie
outputs = layers.Dense(10, activation='softmax')(x)

# Création du modèle
model = keras.Model(inputs, outputs, name="mnist_model")

# Compilation du modèle
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Affichage du résumé du modèle
model.summary()
```

### Cellule 5 (Entraînement - Code)
```python
# Entraînement du modèle
# Note : Nombre d'époques réduit pour la démonstration
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)

# Évaluation du modèle
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nPrécision sur l'ensemble de test : {test_accuracy*100:.2f}%")
```

### Cellule 6 (Visualisation - Code)
```python
# Visualisation de la précision et de la perte
plt.figure(figsize=(12, 4))

# Précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Précision entraînement')
plt.plot(history.history['val_accuracy'], label='Précision validation')
plt.title('Précision du modèle')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.legend()

# Perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perte entraînement')
plt.plot(history.history['val_loss'], label='Perte validation')
plt.title('Perte du modèle')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.legend()

plt.tight_layout()
plt.show()
```

### Cellule 7 (Prédictions - Code)
```python
# Prédictions et visualisation
# Prédire sur quelques images de test
predictions = model.predict(X_test[:10])

plt.figure(figsize=(15, 6))
for i in range(10):
    plt.subplot(2, 10, i+1)
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Réel: {np.argmax(y_test[i])}")
    plt.axis('off')
    
    plt.subplot(2, 10, i+11)
    plt.bar(range(10), predictions[i])
    plt.title(f"Prédit: {np.argmax(predictions[i])}")
    plt.xticks(range(10))
    plt.ylim(0, 1)

plt.suptitle("Prédictions du modèle")
plt.tight_layout()
plt.show()
```

### Cellule 8 (Dessin interactif - Code)
```python
# Interface interactive pour dessiner et prédire
# Cette cellule permet de dessiner un chiffre directement dans Colab

from google.colab import output
from IPython.display import display, HTML
import io
import base64
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour créer un canvas HTML

def create_canvas():
    canvas_html = """
    <canvas id="canvas" width="280" height="280" style="border: 2px solid black; background-color: white;"></canvas>
    <div style="margin-top: 10px;">
      <button id="predict_button" style="padding: 5px 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Prédire</button>
      <button id="clear_button" style="margin-left: 10px; padding: 5px 10px; background-color: #f44336; color: white; border: none; border-radius: 4px; cursor: pointer;">Effacer</button>
    </div>
    <div id="result" style="margin-top: 10px; font-weight: bold;"></div>

    <script>
      var canvas = document.getElementById('canvas');
      var ctx = canvas.getContext('2d');
      var isDrawing = false;

      // Remplir le fond en blanc dès le départ
      ctx.fillStyle = "white";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.lineWidth = 15;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.strokeStyle = 'black';

      canvas.addEventListener('mousedown', function(e) {
        isDrawing = true;
        ctx.beginPath();
        ctx.moveTo(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
      });

      canvas.addEventListener('mousemove', function(e) {
        if (isDrawing) {
          ctx.lineTo(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
          ctx.stroke();
        }
      });

      canvas.addEventListener('mouseup', function() {
        isDrawing = false;
      });

      canvas.addEventListener('mouseleave', function() {
        isDrawing = false;
      });

      document.getElementById('clear_button').addEventListener('click', function() {
        ctx.fillStyle = "white";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        document.getElementById('result').innerHTML = '';
      });

      document.getElementById('predict_button').addEventListener('click', function() {
        var imageData = canvas.toDataURL('image/png');
        document.getElementById('result').innerHTML = 'Analyse en cours...';
        google.colab.kernel.invokeFunction('notebook.predict', [imageData], {});
      });
    </script>
    """
    return canvas_html

# Fonction pour prétraiter l'image dessinée
def preprocess_image(image_data):
    image_data = image_data.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    
    # Convertir en niveaux de gris et redimensionner
    image = image.convert('L').resize((28, 28))
    
    # Convertir en tableau numpy
    image_array = np.array(image)
    
    # Vérification si inversion des couleurs est nécessaire
    if np.mean(image_array) > 127:  # Fond clair, chiffre sombre
        image_array = 255 - image_array
    
    # Normaliser les pixels
    image_array = image_array / 255.0
    
    return image_array

# Fonction de prédiction
def predict_digit(image_data):
    image_array = preprocess_image(image_data)
    image_array = image_array.reshape(1, 28, 28, 1)
    
    # Affichage de l'image prétraitée pour vérifier
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    plt.imshow(image_array.reshape(28, 28), cmap='gray')
    plt.title("Image prétraitée")
    plt.axis('off')
    
    # Prédiction
    prediction = model.predict(image_array)[0]
    digit = np.argmax(prediction)
    confidence = prediction[digit] * 100
    
    # Affichage du graphique des probabilités
    plt.subplot(1, 2, 2)
    plt.bar(range(10), prediction)
    plt.title(f"Prédiction: {digit}")
    plt.xlabel("Chiffre")
    plt.ylabel("Confiance")
    plt.xticks(range(10))
    plt.show()
    
    # Afficher le résultat dans le notebook
    output.eval_js(f"""
    document.getElementById('result').innerHTML = 'Prédiction: {digit} (Confiance: {confidence:.2f}%)';
    """)

# Enregistrer la fonction pour être appelée depuis JavaScript
output.register_callback('notebook.predict', predict_digit)

# Afficher le canvas
display(HTML(create_canvas()))
print("Dessinez un chiffre dans le canvas ci-dessus et cliquez sur 'Prédire'")



### Cellule 9 (Expérimentation - Markdown)
```markdown
## 🧪 Expérimentations

Voici quelques modifications que vous pouvez essayer pour améliorer ou observer les effets sur le modèle :

1. **Modifier l'architecture du réseau :**
   - Augmenter/diminuer le nombre de filtres dans les couches Conv2D
   - Ajouter/retirer des couches convolutives ou denses
   - Ajouter une couche Dropout pour réduire le surapprentissage

2. **Changer les hyperparamètres d'entraînement :**
   - Augmenter le nombre d'époques
   - Modifier la taille du batch
   - Essayer différents optimiseurs (SGD, RMSprop, etc.)

3. **Augmenter les données :**
   - Appliquer des rotations ou décalages aux images d'entraînement

Pour chaque modification, observez l'impact sur :
- La précision finale
- La vitesse d'entraînement
- Les courbes d'apprentissage
- Le comportement face à vos propres dessins

N'hésitez pas à documenter vos observations dans la fiche fournie.
```

