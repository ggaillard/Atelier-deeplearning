# Guide simplifié de diagnostic des problèmes de performance en Deep Learning

Ce guide vous aidera à identifier et résoudre les problèmes de performance les plus courants dans vos modèles de Deep Learning, sans nécessiter de connaissances mathématiques avancées.

## 1. Reconnaître les signes de surapprentissage (overfitting)

### Symptômes
- Performances excellentes sur les données d'entraînement mais médiocres sur les données de test
- Écart grandissant entre les courbes d'apprentissage d'entraînement et de validation
- Courbe de perte de validation qui remonte après avoir diminué

### Solutions
- **Ajouter du Dropout** (ex: `layers.Dropout(0.2)` après les couches denses)
- **Utiliser la régularisation L2** (ex: `kernel_regularizer=tf.keras.regularizers.l2(0.001)`)
- **Augmenter les données** (rotations, translations, zoom pour les images)
- **Simplifier le modèle** (réduire le nombre de couches ou de neurones)
- **Utiliser l'Early Stopping** pour arrêter l'entraînement avant le surapprentissage

```python
# Exemple d'Early Stopping
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

model.fit(X_train, y_train, 
          validation_data=(X_val, y_val),
          callbacks=[early_stopping],
          epochs=100)  # Nombre maximum d'époques
```

## 2. Identifier le sous-apprentissage (underfitting)

### Symptômes
- Performances médiocres sur les données d'entraînement ET de validation
- Courbes d'apprentissage qui stagnent rapidement
- Erreurs systématiques sur certains types d'exemples

### Solutions
- **Augmenter la complexité du modèle** (plus de couches ou de neurones)
- **Entraîner plus longtemps** (augmenter le nombre d'époques)
- **Réduire la régularisation** si elle est trop forte
- **Optimiser l'architecture** pour le problème spécifique

## 3. Problèmes liés aux données

### Symptômes
- Performances incohérentes ou erratiques
- Biais inexpliqués dans les prédictions
- Difficultés d'apprentissage sur certaines classes

### Solutions
- **Normaliser correctement les données**
```python
# Normalisation Z-score (moyenne=0, écart-type=1)
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std  # Utiliser les statistiques de l'entraînement
```

- **Équilibrer les classes** (rééchantillonnage ou pondération)
```python
# Pondération des classes
class_weights = {0: 1.0, 1: 5.0}  # Si classe 1 sous-représentée
model.fit(X_train, y_train, class_weight=class_weights)
```

- **Vérifier la qualité des données** (valeurs aberrantes, erreurs d'étiquetage)
- **Stratifier la division train/test** pour maintenir les distributions

## 4. Problèmes d'optimisation

### Symptômes
- Apprentissage trop lent ou instable
- Courbe de perte qui oscille fortement
- Convergence vers un minimum local sous-optimal

### Solutions
- **Ajuster le taux d'apprentissage**
```python
# Taux d'apprentissage adaptatif
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=3
)
```

- **Changer d'optimiseur** (essayer Adam, RMSprop ou SGD selon le problème)
- **Utiliser le Batch Normalization** pour stabiliser l'entraînement
```python
model = tf.keras.Sequential([
    layers.Dense(128),
    layers.BatchNormalization(),
    layers.Activation('relu')
])
```

- **Ajuster la taille du batch** (plus petit pour plus de stabilité, plus grand pour plus de vitesse)

## 5. Processus de diagnostic pas à pas

1. **Observer les courbes d'apprentissage**
   - Comparer les courbes d'entraînement et de validation
   - Identifier les tendances (surapprentissage, sous-apprentissage, etc.)

2. **Analyser les erreurs**
   - Examiner les cas les plus mal prédits
   - Rechercher des patterns dans les erreurs

3. **Tester des hypothèses**
   - Modifier un seul paramètre à la fois
   - Mesurer l'impact de chaque changement

4. **Itérer et documenter**
   - Garder trace des expérimentations
   - Progresser par petites améliorations successives

## 6. Checklist de diagnostic rapide

- [ ] Les données sont-elles correctement normalisées?
- [ ] Y a-t-il un écart important entre performances d'entraînement et de validation?
- [ ] Le modèle est-il adapté à la complexité du problème?
- [ ] L'optimiseur et le taux d'apprentissage sont-ils appropriés?
- [ ] Y a-t-il un déséquilibre dans les données?
- [ ] Les hyperparamètres ont-ils été ajustés?

## 7. Tableau de référence des problèmes et solutions

| Problème | Symptômes | Solutions principales |
|----------|-----------|----------------------|
| Surapprentissage | Bonne perf. entraînement, mauvaise perf. test | Dropout, régularisation, plus de données |
| Sous-apprentissage | Mauvaise perf. partout | Modèle plus complexe, plus d'entraînement |
| Données non normalisées | Apprentissage instable | Normalisation adaptée au problème |
| Classes déséquilibrées | Biais vers classe majoritaire | Rééchantillonnage, pondération |
| Taux d'apprentissage inapproprié | Convergence lente ou oscillations | Ajustement du taux, schedulers |

N'oubliez pas que l'amélioration des performances est souvent un processus itératif. Commencez par les problèmes les plus évidents et progressez vers des optimisations plus fines.