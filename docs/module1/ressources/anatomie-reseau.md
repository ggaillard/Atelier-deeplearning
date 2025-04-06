# Anatomie d'un réseau de neurones

Ce document contient le code et les explications pour le notebook d'exploration interactive d'un réseau de neurones. Vous pouvez copier-coller chaque section dans une cellule Google Colab.

## Cellule 1 (Markdown) - Introduction

```markdown
# Anatomie d'un réseau de neurones

## Exploration interactive du fonctionnement interne d'un réseau de neurones

Dans ce notebook, nous allons explorer de manière interactive le fonctionnement interne d'un réseau de neurones. Vous pourrez manipuler directement les composants fondamentaux (neurones, poids, biais) et observer leur impact sur les prédictions.

### Objectifs :
- Comprendre le fonctionnement d'un neurone artificiel
- Visualiser l'effet des poids et du biais sur les décisions
- Explorer le flux d'information dans un réseau multicouche
- Observer l'évolution des poids pendant l'entraînement
```

## Cellule 2 (Code) - Configuration initiale

```python
# Partie 1: Configuration initiale
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from google.colab import output
output.enable_custom_widget_manager()
import ipywidgets as widgets
from IPython.display import display, clear_output
from matplotlib.colors import LinearSegmentedColormap

print("Configuration terminée!")
```

## Cellule 3 (Markdown) - Exploration d'un neurone unique

```markdown
## Exploration d'un neurone unique

Dans cette partie, nous allons observer le fonctionnement d'un neurone artificiel, l'unité fondamentale des réseaux de neurones.

Un neurone artificiel effectue deux opérations principales :
1. Une **somme pondérée** des entrées (z = w₁x₁ + w₂x₂ + ... + b)
2. L'application d'une **fonction d'activation** qui introduit la non-linéarité (a = f(z))

Utilisez les contrôles interactifs ci-dessous pour observer comment un neurone traite l'information.
```

## Cellule 4 (Code) - Fonctions du neurone

```python
# Fonction pour calculer la sortie d'un neurone
def neuron_output(x1, x2, w1, w2, b, activation="relu"):
    # Calcul de la somme pondérée
    z = x1 * w1 + x2 * w2 + b
    
    # Application de la fonction d'activation
    if activation == "relu":
        a = max(0, z)
    elif activation == "sigmoid":
        a = 1 / (1 + np.exp(-z))
    elif activation == "tanh":
        a = np.tanh(z)
    else:
        a = z  # Linéaire
    
    return z, a

# Fonction pour visualiser un neurone
def visualize_neuron(x1, x2, w1, w2, b, activation="relu"):
    # Calculer la sortie
    z, a = neuron_output(x1, x2, w1, w2, b, activation)
    
    # Créer la figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. Représentation du neurone
    ax = axes[0]
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    
    # Dessiner le neurone
    circle = plt.Circle((1, 1), 0.4, fill=True, color='lightblue', alpha=0.7)
    ax.add_artist(circle)
    
    # Dessiner les entrées
    ax.plot(0, 0.7, 'ro', markersize=10)
    ax.plot(0, 1.3, 'ro', markersize=10)
    
    # Dessiner la sortie
    ax.plot(2, 1, 'go', markersize=10)
    
    # Ajouter les connexions
    ax.arrow(0, 0.7, 0.6, 0.1, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    ax.arrow(0, 1.3, 0.6, -0.1, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    ax.arrow(1.4, 1, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', linewidth=2)
    
    # Ajouter les textes
    ax.text(-0.1, 0.7, f"x₁ = {x1:.2f}", fontsize=12, ha='right')
    ax.text(-0.1, 1.3, f"x₂ = {x2:.2f}", fontsize=12, ha='right')
    ax.text(1, 1, f"z = {z:.2f}\na = {a:.2f}", fontsize=12, ha='center')
    ax.text(0.5, 0.95, f"w₁ = {w1:.2f}", fontsize=10, rotation=15)
    ax.text(0.5, 1.15, f"w₂ = {w2:.2f}", fontsize=10, rotation=-15)
    ax.text(2.1, 1, f"Sortie = {a:.2f}", fontsize=12, ha='left')
    ax.text(1, 0.5, f"Biais = {b:.2f}", fontsize=10)
    
    ax.set_title("Neurone artificiel", fontsize=14)
    ax.set_axis_off()
    
    # 2. Représentation de la fonction d'activation
    ax = axes[1]
    x = np.linspace(-5, 5, 100)
    
    if activation == "relu":
        y = np.maximum(0, x)
        title = "Fonction d'activation: ReLU"
    elif activation == "sigmoid":
        y = 1 / (1 + np.exp(-x))
        title = "Fonction d'activation: Sigmoid"
    elif activation == "tanh":
        y = np.tanh(x)
        title = "Fonction d'activation: Tanh"
    else:
        y = x
        title = "Fonction d'activation: Linéaire"
    
    ax.plot(x, y, 'b-', linewidth=2)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Marquer le point correspondant à z
    ax.plot(z, a, 'ro', markersize=8)
    ax.plot([z, z], [0, a], 'r--', alpha=0.5)
    ax.plot([0, z], [a, a], 'r--', alpha=0.5)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("z (somme pondérée)")
    ax.set_ylabel("a (activation)")
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # 3. Visualisation de la frontière de décision
    ax = axes[2]
    
    # Créer des points pour former une grille
    grid_size = 20
    x1_values = np.linspace(0, 1, grid_size)
    x2_values = np.linspace(0, 1, grid_size)
    x1_grid, x2_grid = np.meshgrid(x1_values, x2_values)
    
    # Calculer la sortie pour chaque point de la grille
    z_grid = x1_grid * w1 + x2_grid * w2 + b
    
    if activation == "relu":
        a_grid = np.maximum(0, z_grid)
    elif activation == "sigmoid":
        a_grid = 1 / (1 + np.exp(-z_grid))
    elif activation == "tanh":
        a_grid = np.tanh(z_grid)
    else:
        a_grid = z_grid
    
    # Créer une carte de couleur
    cmap = plt.get_cmap('coolwarm')
    
    # Tracer la heatmap
    im = ax.imshow(a_grid, origin='lower', extent=[0, 1, 0, 1], 
                   cmap=cmap, vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label="Activation")
    
    # Ajouter le point actuel
    ax.plot(x1, x2, 'ko', markersize=8)
    
    # Tracer la frontière de décision (a = 0.5)
    if activation in ["sigmoid", "tanh"]:
        threshold = 0.5
        CS = ax.contour(x1_grid, x2_grid, a_grid, levels=[threshold], 
                         colors='k', linestyles='--')
        ax.clabel(CS, inline=True, fontsize=10, fmt={threshold: "a = 0.5"})
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("x₁")
    ax.set_ylabel("x₂")
    ax.set_title("Carte d'activation", fontsize=14)
    
    plt.tight_layout()
    plt.show()
    
    return a
```

## Cellule 5 (Code) - Interface interactive pour un neurone

```python
# Créer des widgets interactifs pour le neurone
w1_slider = widgets.FloatSlider(value=1.0, min=-3.0, max=3.0, step=0.1, description='Poids w₁:')
w2_slider = widgets.FloatSlider(value=1.0, min=-3.0, max=3.0, step=0.1, description='Poids w₂:')
b_slider = widgets.FloatSlider(value=0.0, min=-3.0, max=3.0, step=0.1, description='Biais:')
x1_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₁:')
x2_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₂:')
activation_dropdown = widgets.Dropdown(
    options=['relu', 'sigmoid', 'tanh', 'linear'],
    value='relu',
    description='Activation:'
)

# Fonction pour mettre à jour la visualisation
def update_neuron_visualization(w1, w2, b, x1, x2, activation):
    clear_output(wait=True)
    output = visualize_neuron(x1, x2, w1, w2, b, activation)
    print(f"Sortie du neurone: {output:.4f}")
    
    # Expliquer le calcul
    z = x1 * w1 + x2 * w2 + b
    print(f"\nCalcul détaillé:")
    print(f"z = (x₁ × w₁) + (x₂ × w₂) + b")
    print(f"z = ({x1:.2f} × {w1:.2f}) + ({x2:.2f} × {w2:.2f}) + {b:.2f}")
    print(f"z = {x1*w1:.2f} + {x2*w2:.2f} + {b:.2f}")
    print(f"z = {z:.2f}")
    
    if activation == "relu":
        print(f"a = ReLU(z) = max(0, z) = max(0, {z:.2f}) = {max(0, z):.2f}")
    elif activation == "sigmoid":
        sig_z = 1 / (1 + np.exp(-z))
        print(f"a = Sigmoid(z) = 1 / (1 + e^(-z)) = 1 / (1 + e^(-{z:.2f})) = {sig_z:.2f}")
    elif activation == "tanh":
        tanh_z = np.tanh(z)
        print(f"a = tanh(z) = tanh({z:.2f}) = {tanh_z:.2f}")
    else:
        print(f"a = z = {z:.2f}")  # Linéaire

# Interface interactive pour le neurone
neuron_output = widgets.interactive_output(
    update_neuron_visualization,
    {'w1': w1_slider, 'w2': w2_slider, 'b': b_slider, 
     'x1': x1_slider, 'x2': x2_slider, 'activation': activation_dropdown}
)

# Afficher les widgets
print("Utilisez les contrôles ci-dessous pour modifier les propriétés du neurone:")
display(widgets.VBox([
    widgets.HBox([x1_slider, x2_slider]),
    widgets.HBox([w1_slider, w2_slider]),
    widgets.HBox([b_slider, activation_dropdown])
]))
display(neuron_output)
```

## Cellule 6 (Markdown) - De l'unique au réseau

```markdown
## De l'unique au réseau

Maintenant que nous avons exploré un neurone unique, passons à un réseau simple. Un réseau de neurones est composé de plusieurs neurones organisés en couches, où l'information se propage de l'entrée vers la sortie.

Le réseau ci-dessous contient :
- Une couche d'entrée (2 neurones)
- Une couche cachée (nombre ajustable de neurones)
- Une couche de sortie (1 neurone)

Observez comment l'information circule à travers le réseau et comment les différents poids affectent les activations.
```

## Cellule 7 (Code) - Fonctions du réseau

```python
# Fonction pour créer et visualiser un réseau simple
def create_simple_network(hidden_units=3, activation='relu'):
    # Créer un modèle séquentiel
    model = Sequential([
        Dense(hidden_units, activation=activation, input_shape=(2,)),
        Dense(1, activation='sigmoid')
    ])
    
    # Compiler le modèle (bien que nous ne l'entraînerons pas)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

# Fonction pour visualiser un réseau simple
def visualize_network(inputs, weights1=None, biases1=None, weights2=None, biases2=None, hidden_units=3, activation='relu'):
    # Créer le modèle si non fourni
    model = create_simple_network(hidden_units, activation)
    
    # Si des poids sont fournis, les appliquer
    if weights1 is not None and biases1 is not None and weights2 is not None and biases2 is not None:
        model.layers[0].set_weights([weights1, biases1])
        model.layers[1].set_weights([weights2, biases2])
    
    # Convertir les entrées pour prédiction
    x = np.array([inputs])
    
    # Obtenir les activations intermédiaires
    intermediate_layer_model = tf.keras.Model(inputs=model.input,
                                             outputs=model.layers[0].output)
    intermediate_activations = intermediate_layer_model.predict(x)[0]
    
    # Obtenir les activations de sortie
    output_activation = model.predict(x)[0][0]
    
    # Extraire les poids et biais
    weights1, biases1 = model.layers[0].get_weights()
    weights2, biases2 = model.layers[1].get_weights()
    
    # Créer la figure pour visualiser le réseau
    plt.figure(figsize=(12, 8))
    
    # Définir les positions des neurones
    input_layer_y = np.array([0.2, 0.8])
    hidden_layer_y = np.linspace(0.1, 0.9, hidden_units)
    output_layer_y = np.array([0.5])
    
    input_layer_x = 0.1
    hidden_layer_x = 0.5
    output_layer_x = 0.9
    
    # Dessiner les neurones d'entrée
    for i, y in enumerate(input_layer_y):
        plt.scatter(input_layer_x, y, s=200, c='blue', alpha=0.7)
        plt.text(input_layer_x, y, f"x{i+1}={inputs[i]:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner les neurones cachés
    for i, y in enumerate(hidden_layer_y):
        # Calculer la somme pondérée
        z = np.dot(inputs, weights1[:, i]) + biases1[i]
        
        # Appliquer l'activation
        if activation == 'relu':
            a = max(0, z)
        elif activation == 'sigmoid':
            a = 1 / (1 + np.exp(-z))
        elif activation == 'tanh':
            a = np.tanh(z)
        else:
            a = z
        
        # Couleur basée sur l'activation
        color = plt.cm.viridis(a)
        
        plt.scatter(hidden_layer_x, y, s=200, c=[color], alpha=0.7)
        plt.text(hidden_layer_x, y, f"{a:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner le neurone de sortie
    plt.scatter(output_layer_x, output_layer_y, s=200, c='red', alpha=0.7)
    plt.text(output_layer_x, output_layer_y, f"{output_activation:.2f}", fontsize=12, ha='center', va='center', color='white')
    
    # Dessiner les connexions entre couches d'entrée et cachée
    for i, y_in in enumerate(input_layer_y):
        for j, y_hid in enumerate(hidden_layer_y):
            # Couleur et épaisseur basées sur le poids
            weight = weights1[i, j]
            width = abs(weight) * 3
            color = 'red' if weight < 0 else 'green'
            alpha = min(abs(weight), 1.0)
            
            plt.plot([input_layer_x, hidden_layer_x], [y_in, y_hid], 
                    c=color, linewidth=width, alpha=alpha)
    
    # Dessiner les connexions entre couche cachée et sortie
    for i, y_hid in enumerate(hidden_layer_y):
        # Couleur et épaisseur basées sur le poids
        weight = weights2[i, 0]
        width = abs(weight) * 3
        color = 'red' if weight < 0 else 'green'
        alpha = min(abs(weight), 1.0)
        
        plt.plot([hidden_layer_x, output_layer_x], [y_hid, output_layer_y], 
                c=color, linewidth=width, alpha=alpha)
    
    # Étiquettes
    plt.text(input_layer_x, 0.03, "Couche d'entrée", fontsize=14, ha='center')
    plt.text(hidden_layer_x, 0.03, "Couche cachée", fontsize=14, ha='center')
    plt.text(output_layer_x, 0.03, "Couche de sortie", fontsize=14, ha='center')
    
    # Enlever les axes
    plt.axis('off')
    plt.title(f"Réseau de neurones - Activation cachée: {activation}", fontsize=16)
    plt.tight_layout()
    plt.show()
    
    # Afficher les calculs détaillés
    print("\nCalculs détaillés pour chaque neurone de la couche cachée:")
    for i in range(hidden_units):
        z = np.dot(inputs, weights1[:, i]) + biases1[i]
        print(f"\nNeurone caché {i+1}:")
        print(f"z = (x₁ × w₁,{i+1}) + (x₂ × w₂,{i+1}) + b{i+1}")
        print(f"z = ({inputs[0]:.2f} × {weights1[0, i]:.2f}) + ({inputs[1]:.2f} × {weights1[1, i]:.2f}) + {biases1[i]:.2f}")
        print(f"z = {inputs[0] * weights1[0, i]:.2f} + {inputs[1] * weights1[1, i]:.2f} + {biases1[i]:.2f} = {z:.2f}")
        
        if activation == 'relu':
            a = max(0, z)
            print(f"a = ReLU(z) = max(0, {z:.2f}) = {a:.2f}")
        elif activation == 'sigmoid':
            a = 1 / (1 + np.exp(-z))
            print(f"a = Sigmoid(z) = 1 / (1 + e^(-{z:.2f})) = {a:.2f}")
        elif activation == 'tanh':
            a = np.tanh(z)
            print(f"a = tanh(z) = tanh({z:.2f}) = {a:.2f}")
        else:
            a = z
            print(f"a = z = {z:.2f}")
    
    print("\nCalcul pour le neurone de sortie:")
    z_out = np.dot(intermediate_activations, weights2[:, 0]) + biases2[0]
    print(f"z = Σ(a_caché × w_sortie) + b_sortie = {z_out:.2f}")
    print(f"sortie = Sigmoid(z) = 1 / (1 + e^(-{z_out:.2f})) = {output_activation:.2f}")
    
    return model, weights1, biases1, weights2, biases2

# Fonction pour générer des poids aléatoires
def generate_random_weights(hidden_units=3):
    # Générer des poids aléatoires pour la première couche
    weights1 = np.random.normal(0, 1, (2, hidden_units))
    biases1 = np.random.normal(0, 1, hidden_units)
    
    # Générer des poids aléatoires pour la couche de sortie
    weights2 = np.random.normal(0, 1, (hidden_units, 1))
    biases2 = np.random.normal(0, 1, 1)
    
    return weights1, biases1, weights2, biases2
```

## Cellule 8 (Code) - Interface interactive pour le réseau

```python
# Créer des widgets interactifs pour le réseau
x1_net_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₁:')
x2_net_slider = widgets.FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='Entrée x₂:')
hidden_units_slider = widgets.IntSlider(value=3, min=1, max=5, description='Neurones cachés:')
activation_net_dropdown = widgets.Dropdown(
    options=['relu', 'sigmoid', 'tanh', 'linear'],
    value='relu',
    description='Activation:'
)
random_button = widgets.Button(description="Poids aléatoires")

# Variables pour stocker les poids courants
current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights()

# Fonction pour visualiser le réseau
def update_network_visualization(x1, x2, hidden_units, activation):
    global current_weights1, current_biases1, current_weights2, current_biases2
    
    # Ajuster les dimensions des poids si nécessaire
    if current_weights1.shape[1] != hidden_units:
        current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights(hidden_units)
    
    # Visualiser le réseau
    inputs = np.array([x1, x2])
    _, w1, b1, w2, b2 = visualize_network(
        inputs, current_weights1, current_biases1, current_weights2, current_biases2, 
        hidden_units, activation
    )
    
    # Mettre à jour les poids courants
    current_weights1, current_biases1 = w1, b1
    current_weights2, current_biases2 = w2, b2

# Fonction pour générer de nouveaux poids aléatoires
def regenerate_weights(b):
    global current_weights1, current_biases1, current_weights2, current_biases2
    current_weights1, current_biases1, current_weights2, current_biases2 = generate_random_weights(
        hidden_units_slider.value
    )
    # Mettre à jour la visualisation
    update_network_visualization(
        x1_net_slider.value, x2_net_slider.value,
        hidden_units_slider.value, activation_net_dropdown.value
    )

# Associer la fonction au bouton
random_button.on_click(regenerate_weights)

# Interface interactive pour le réseau
network_output = widgets.interactive_output(
    update_network_visualization,
    {'x1': x1_net_slider, 'x2': x2_net_slider, 
     'hidden_units': hidden_units_slider, 'activation': activation_net_dropdown}
)

# Afficher les widgets pour le réseau
print("\nExplorez le comportement d'un réseau simple:")
display(widgets.VBox([
    widgets.HBox([x1_net_slider, x2_net_slider]),
    widgets.HBox([hidden_units_slider, activation_net_dropdown]),
    random_button
]))
display(network_output)
```

## Cellule 9 (Markdown) - Visualisation de l'entraînement

```markdown
## Visualisation de l'entraînement

Dans cette dernière partie, nous allons observer l'évolution des poids pendant l'entraînement d'un réseau de neurones sur un problème classique : le problème XOR.

Le problème XOR (OU exclusif) consiste à prédire la sortie de la fonction logique XOR :
- (0,0) → 0
- (0,1) → 1
- (1,0) → 1
- (1,1) → 0

Ce problème n'est pas linéairement séparable, ce qui signifie qu'il ne peut pas être résolu par un seul neurone.
```

## Cellule 10 (Code) - Génération de données XOR

```python
# Générer des données XOR
def generate_xor_data(n_samples=100):
    X = np.random.rand(n_samples, 2)
    y = np.logical_xor(X[:, 0] > 0.5, X[:, 1] > 0.5).astype(np.float32)
    return X, y

# Afficher quelques exemples de données XOR
X_sample, y_sample = generate_xor_data(20)
plt.figure(figsize=(6, 6))
plt.scatter(X_sample[:, 0], X_sample[:, 1], c=y_sample, cmap='coolwarm', s=100)
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Problème XOR')
plt.grid(True, alpha=0.3)
plt.show()

print("Exemples de données XOR:")
for i in range(5):
    x1, x2 = X_sample[i]
    y = y_sample[i]
    print(f"x1={x1:.2f}, x2={x2:.2f} → y={y:.0f}")
```

## Cellule 11 (Code) - Création et entraînement du modèle XOR

```python
# Créer un modèle pour résoudre XOR
learning_rate = 0.1
hidden_units = 4
epochs = 20

# Générer des données
X_train, y_train = generate_xor_data(200)

# Créer un modèle
model = Sequential([
    Dense(hidden_units, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

# Compiler avec un optimiseur personnalisé
optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
history = model.fit(
    X_train, y_train,
    epochs=epochs,
    batch_size=32,
    verbose=1
)

# Afficher les résultats d'entraînement
plt.figure(figsize=(12, 5))

# Graphique de précision
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], '-o')
plt.title('Précision pendant l\'entraînement')
plt.xlabel('Époque')
plt.ylabel('Précision')
plt.grid(True, alpha=0.3)

# Graphique de perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], '-o')
plt.title('Perte pendant l\'entraînement')
plt.xlabel('Époque')
plt.ylabel('Perte')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## Cellule 12 (Code) - Visualisation de la frontière de décision

```python
# Visualiser la frontière de décision finale
h = 0.01
x_min, x_max = 0, 1
y_min, y_max = 0, 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
grid_points = np.c_[xx.ravel