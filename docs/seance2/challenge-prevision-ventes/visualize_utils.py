import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_training_history(history):
    """
    Visualise l'évolution de la précision et de la perte pendant l'entraînement.
    
    Args:
        history: Historique retourné par la méthode fit() de Keras
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Évolution de la précision
    ax1.plot(history.history['accuracy'], label='Entraînement')
    ax1.plot(history.history['val_accuracy'], label='Validation')
    ax1.set_title('Évolution de la précision')
    ax1.set_xlabel('Époque')
    ax1.set_ylabel('Précision')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Évolution de la perte
    ax2.plot(history.history['loss'], label='Entraînement')
    ax2.plot(history.history['val_loss'], label='Validation')
    ax2.set_title('Évolution de la perte')
    ax2.set_xlabel('Époque')
    ax2.set_ylabel('Perte')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    
    # Analyse des courbes
    train_acc = history.history['accuracy'][-1]
    val_acc = history.history['val_accuracy'][-1]
    gap = train_acc - val_acc
    
    print(f"Précision finale sur l'ensemble d'entraînement: {train_acc*100:.2f}%")
    print(f"Précision finale sur l'ensemble de validation: {val_acc*100:.2f}%")
    print(f"Écart entre entraînement et validation: {gap*100:.2f}%")
    
    if gap > 0.05:
        print("⚠️ Potentiel surapprentissage: l'écart entre les précisions d'entraînement et de validation est important.")
    elif val_acc < 0.75:
        print("⚠️ Potentiel sous-apprentissage: la précision de validation est relativement faible.")
    else:
        print("✅ Bon équilibre: pas de signe évident de sur ou sous-apprentissage.")

def plot_confusion_matrix(y_true, y_pred, class_names):
    """
    Affiche la matrice de confusion avec des annotations.
    
    Args:
        y_true: Étiquettes réelles (classes numériques)
        y_pred: Prédictions (classes numériques)
        class_names: Liste des noms de classes
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Prédictions')
    plt.ylabel('Valeurs réelles')
    plt.title('Matrice de confusion')
    plt.tight_layout()
    plt.show()
    
    # Analyse des classes les plus confuses
    np.fill_diagonal(cm, 0)  # Ignorer la diagonale pour trouver les confusions
    max_confusions = []
    for i in range(len(class_names)):
        max_confusion_idx = np.argmax(cm[i])
        if cm[i, max_confusion_idx] > 0:
            max_confusions.append((class_names[i], class_names[max_confusion_idx], cm[i, max_confusion_idx]))
    
    if max_confusions:
        print("Classes les plus souvent confondues:")
        for real, pred, count in sorted(max_confusions, key=lambda x: x[2], reverse=True)[:5]:
            print(f"  • {real} confondu avec {pred}: {count} fois")

def plot_misclassified_images(X_test, y_true, y_pred, class_names, num_images=10):
    """
    Affiche des exemples d'images mal classées.
    
    Args:
        X_test: Images de test
        y_true: Étiquettes réelles (classes numériques)
        y_pred: Prédictions (classes numériques)
        class_names: Liste des noms de classes
        num_images: Nombre d'images à afficher
    """
    # Trouver les indices des images mal classées
    misclassified_indices = np.where(y_true != y_pred)[0]
    
    if len(misclassified_indices) == 0:
        print("Aucune image mal classée trouvée!")
        return
    
    # Sélectionner un sous-ensemble aléatoire d'images mal classées
    selected_indices = np.random.choice(misclassified_indices, 
                                        size=min(num_images, len(misclassified_indices)), 
                                        replace=False)
    
    # Afficher les images
    fig = plt.figure(figsize=(15, num_images * 2 // 5))
    for i, idx in enumerate(selected_indices):
        plt.subplot(num_images // 5 + 1, 5, i + 1)
        plt.imshow(X_test[idx])
        plt.title(f"Réel: {class_names[y_true[idx]]}\nPrédit: {class_names[y_pred[idx]]}")
        plt.axis('off')
    plt.tight_layout()
    plt.suptitle("Exemples d'images mal classées", y=1.02, fontsize=16)
    plt.show()