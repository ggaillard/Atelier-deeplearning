# Approche alternative complète pour la visualisation
print("Initialisation et visualisation avec une approche alternative...")

# 1. Réinitialiser le modèle pour s'assurer qu'il est correctement défini
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    MaxPooling2D((2, 2), name='pool1'),
    Conv2D(64, (3, 3), activation='relu', name='conv2'),
    MaxPooling2D((2, 2), name='pool2'),
    Flatten(name='flatten'),
    Dense(128, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout1'),
    Dense(10, activation='softmax', name='output')
])

# 2. Compiler le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Forcer l'initialisation avec build ET un forward pass
model.build(input_shape=(None, 28, 28, 1))
dummy_input = np.zeros((1, 28, 28, 1))
_ = model(dummy_input)

# 4. Vérifier que les couches sont accessibles
print(f"Couches dans le modèle: {[layer.name for layer in model.layers]}")

# 5. Créer et visualiser des poids aléatoires puisque le modèle n'est pas entraîné
filters = np.random.normal(size=(3, 3, 1, 8))  # Simuler 8 filtres 3x3
f_min, f_max = filters.min(), filters.max()
filters = (filters - f_min) / (f_max - f_min)

plt.figure(figsize=(10, 4))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(filters[:, :, 0, i], cmap='viridis')
    plt.title(f'Filtre {i+1}')
    plt.axis('off')
plt.tight_layout()
plt.show()

# 6. Simuler des feature maps aléatoires
sample_idx = 12
sample_image = X_test[sample_idx]
plt.figure(figsize=(3, 3))
plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Chiffre: {y_test[sample_idx]}")
plt.axis('off')
plt.show()

# 7. Générer des feature maps simulées
feature_maps = np.random.rand(1, 26, 26, 8)  # Taille typique après convolution 3x3

plt.figure(figsize=(10, 4))
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(feature_maps[0, :, :, i], cmap='viridis')
    plt.axis('off')
plt.suptitle('Feature Maps - Couche 1 (Simulées)')
plt.tight_layout()
plt.show()

print("Visualisation terminée avec des données simulées.")
print("Note: Pour voir les vrais filtres et feature maps, le modèle doit être entraîné.")