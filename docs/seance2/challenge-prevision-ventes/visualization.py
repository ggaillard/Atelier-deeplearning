"""
visualization.py
Fonctions de visualisation pour l'analyse des modèles et des résultats du challenge de prévision des ventes.
"""

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
    if 'accuracy' in history.history:
        ax1.plot(history.history['accuracy'], label='Entraînement')
        if 'val_accuracy' in history.history:
            ax1.plot(history.history['val_accuracy'], label='Validation')
        ax1.set_title('Évolution de la précision')
        ax1.set_xlabel('Époque')
        ax1.set_ylabel('Précision')
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.7)
    else:
        # Si pas d'accuracy (régression), on peut utiliser une autre métrique comme MSE
        for metric in history.history:
            if metric != 'loss' and metric != 'val_loss' and not metric.startswith('val_'):
                ax1.plot(history.history[metric], label=f'Entraînement ({metric})')
                if f'val_{metric}' in history.history:
                    ax1.plot(history.history[f'val_{metric}'], label=f'Validation ({metric})')
                ax1.set_title(f'Évolution de {metric}')
                ax1.set_xlabel('Époque')
                ax1.set_ylabel(metric)
                ax1.legend()
                ax1.grid(True, linestyle='--', alpha=0.7)
                break
    
    # Évolution de la perte
    ax2.plot(history.history['loss'], label='Entraînement')
    if 'val_loss' in history.history:
        ax2.plot(history.history['val_loss'], label='Validation')
    ax2.set_title('Évolution de la perte')
    ax2.set_xlabel('Époque')
    ax2.set_ylabel('Perte')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()
    
    # Analyse des courbes
    if 'accuracy' in history.history and 'val_accuracy' in history.history:
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
    elif 'loss' in history.history and 'val_loss' in history.history:
        # Pour les tâches de régression
        train_loss = history.history['loss'][-1]
        val_loss = history.history['val_loss'][-1]
        loss_ratio = val_loss / (train_loss + 1e-10)
        
        print(f"Perte finale sur l'ensemble d'entraînement: {train_loss:.4f}")
        print(f"Perte finale sur l'ensemble de validation: {val_loss:.4f}")
        print(f"Rapport validation/entraînement: {loss_ratio:.2f}")
        
        if loss_ratio > 1.3:
            print("⚠️ Potentiel surapprentissage: la perte de validation est significativement plus élevée que celle d'entraînement.")
        elif train_loss > 0.1 and val_loss > 0.1:  # Seuil arbitraire à adapter selon votre cas
            print("⚠️ Potentiel sous-apprentissage: les pertes d'entraînement et de validation sont relativement élevées.")
        else:
            print("✅ Bon équilibre: pas de signe évident de sur ou sous-apprentissage.")

def plot_predictions(y_true, y_pred, dates=None, title="Prédictions vs Valeurs Réelles"):
    """
    Trace un graphique des prédictions vs valeurs réelles pour des données de séries temporelles.
    
    Args:
        y_true: Valeurs réelles
        y_pred: Prédictions
        dates: Dates correspondantes (optionnel)
        title: Titre du graphique
    """
    plt.figure(figsize=(12, 6))
    
    if dates is not None:
        plt.plot(dates, y_true, 'b-', label='Valeurs Réelles')
        plt.plot(dates, y_pred, 'r--', label='Prédictions')
        plt.xticks(rotation=45)
    else:
        plt.plot(y_true, 'b-', label='Valeurs Réelles')
        plt.plot(y_pred, 'r--', label='Prédictions')
    
    plt.title(title)
    plt.xlabel('Temps')
    plt.ylabel('Valeur')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Calculer et afficher les métriques
    mse = np.mean((y_true - y_pred)**2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))
    
    plt.figtext(0.5, 0.01, f'RMSE: {rmse:.2f}, MAE: {mae:.2f}', 
                ha='center', fontsize=12, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})
    
    plt.tight_layout()
    plt.show()
    
    return {"rmse": rmse, "mae": mae}

def plot_residuals(y_true, y_pred):
    """
    Analyse les résidus (erreurs) entre les prédictions et les valeurs réelles.
    
    Args:
        y_true: Valeurs réelles
        y_pred: Prédictions
    """
    residuals = y_true - y_pred
    
    plt.figure(figsize=(15, 5))
    
    # Distribution des résidus
    plt.subplot(1, 3, 1)
    sns.histplot(residuals, kde=True, color='skyblue')
    plt.title('Distribution des Résidus')
    plt.xlabel('Erreur')
    plt.axvline(x=0, color='red', linestyle='--')
    
    # Résidus vs valeurs prédites
    plt.subplot(1, 3, 2)
    plt.scatter(y_pred, residuals, alpha=0.5, color='blue')
    plt.title('Résidus vs Valeurs Prédites')
    plt.xlabel('Valeurs Prédites')
    plt.ylabel('Résidus')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.grid(True, alpha=0.3)
    
    # QQ plot pour normalité
    plt.subplot(1, 3, 3)
    from scipy import stats
    stats.probplot(residuals, dist="norm", plot=plt)
    plt.title('Q-Q Plot des Résidus')
    
    plt.tight_layout()
    plt.show()
    
    # Statistiques des résidus
    print("Statistiques des résidus:")
    print(f"Moyenne: {np.mean(residuals):.4f}")
    print(f"Écart-type: {np.std(residuals):.4f}")
    print(f"Min: {np.min(residuals):.4f}")
    print(f"Max: {np.max(residuals):.4f}")
    
    # Test de normalité
    from scipy.stats import shapiro
    stat, p = shapiro(residuals)
    print(f"Test de Shapiro-Wilk pour la normalité: p-value = {p:.4f}")
    if p < 0.05:
        print("⚠️ Les résidus ne semblent pas suivre une distribution normale.")
    else:
        print("✅ Les résidus semblent suivre une distribution normale.")

def plot_feature_importance(model, feature_names):
    """
    Visualise l'importance des caractéristiques pour un modèle qui fournit feature_importances_.
    
    Args:
        model: Modèle entraîné (doit avoir un attribut feature_importances_)
        feature_names: Liste des noms des caractéristiques
    """
    if not hasattr(model, 'feature_importances_'):
        print("Ce modèle ne fournit pas d'attribut feature_importances_.")
        return
    
    # Obtenir les importances et les trier
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(12, 6))
    plt.title('Importance des Caractéristiques')
    plt.bar(range(len(importances)), importances[indices], align='center', color='skyblue')
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.show()
    
    # Afficher les 10 caractéristiques les plus importantes
    print("Les 10 caractéristiques les plus importantes:")
    for i in range(min(10, len(feature_names))):
        print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")

def plot_comparison_metrics(models_results, metrics=['rmse', 'mae']):
    """
    Compare les performances de différents modèles selon plusieurs métriques.
    
    Args:
        models_results: Dictionnaire {nom_modèle: {métrique1: valeur1, métrique2: valeur2, ...}}
        metrics: Liste des métriques à comparer
    """
    n_models = len(models_results)
    n_metrics = len(metrics)
    
    plt.figure(figsize=(12, 5 * n_metrics))
    
    for i, metric in enumerate(metrics):
        plt.subplot(n_metrics, 1, i+1)
        
        model_names = list(models_results.keys())
        metric_values = [models_results[model].get(metric, np.nan) for model in model_names]
        
        # Trier par performance (valeurs plus basses sont meilleures pour rmse, mae)
        sorted_indices = np.argsort(metric_values)
        sorted_names = [model_names[i] for i in sorted_indices]
        sorted_values = [metric_values[i] for i in sorted_indices]
        
        bars = plt.bar(sorted_names, sorted_values, color='skyblue')
        
        # Ajouter les valeurs au-dessus des barres
        for bar, value in zip(bars, sorted_values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
                    f'{value:.4f}', ha='center', va='bottom', fontsize=11)
        
        plt.title(f'Comparaison des Modèles - {metric.upper()}')
        plt.ylabel(metric.upper())
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plot_sales_by_category(df, target_col='revenue', category_col='product_category'):
    """
    Visualise les ventes par catégorie de produit.
    
    Args:
        df: DataFrame contenant les données
        target_col: Colonne cible (ex: 'revenue')
        category_col: Colonne de catégorie
    """
    # Agréger par catégorie
    category_sales = df.groupby(category_col)[target_col].agg(['sum', 'mean']).sort_values('sum', ascending=False)
    
    plt.figure(figsize=(14, 7))
    
    # Ventes totales par catégorie
    plt.subplot(1, 2, 1)
    sns.barplot(x=category_sales.index, y=category_sales['sum'], palette='viridis')
    plt.title('Ventes Totales par Catégorie')
    plt.xlabel('Catégorie')
    plt.ylabel(f'Total des {target_col}')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    
    # Ventes moyennes par catégorie
    plt.subplot(1, 2, 2)
    sns.barplot(x=category_sales.index, y=category_sales['mean'], palette='viridis')
    plt.title('Ventes Moyennes par Catégorie')
    plt.xlabel('Catégorie')
    plt.ylabel(f'Moyenne des {target_col}')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plot_seasonal_patterns(df, date_col='date', target_col='revenue'):
    """
    Visualise les patterns saisonniers dans les ventes.
    
    Args:
        df: DataFrame contenant les données
        date_col: Colonne de date
        target_col: Colonne cible (ex: 'revenue')
    """
    # S'assurer que la colonne date est au format datetime
    df[date_col] = pd.to_datetime(df[date_col])
    
    # Extraire les composantes temporelles
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['day'] = df[date_col].dt.day
    df['weekday'] = df[date_col].dt.weekday
    
    plt.figure(figsize=(15, 10))
    
    # Ventes par mois
    plt.subplot(2, 2, 1)
    monthly_avg = df.groupby('month')[target_col].mean()
    sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette='coolwarm')
    plt.title('Ventes Moyennes par Mois')
    plt.xlabel('Mois')
    plt.ylabel(f'Moyenne des {target_col}')
    plt.xticks(range(0, 12), ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
    plt.grid(axis='y', alpha=0.3)
    
    # Ventes par jour de la semaine
    plt.subplot(2, 2, 2)
    weekday_avg = df.groupby('weekday')[target_col].mean()
    sns.barplot(x=weekday_avg.index, y=weekday_avg.values, palette='coolwarm')
    plt.title('Ventes Moyennes par Jour de la Semaine')
    plt.xlabel('Jour de la Semaine')
    plt.ylabel(f'Moyenne des {target_col}')
    plt.xticks(range(0, 7), ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'])
    plt.grid(axis='y', alpha=0.3)
    
    # Tendance au fil du temps
    plt.subplot(2, 1, 2)
    df_grouped = df.groupby(pd.Grouper(key=date_col, freq='M'))[target_col].sum().reset_index()
    plt.plot(df_grouped[date_col], df_grouped[target_col], marker='o', linestyle='-')
    plt.title('Tendance des Ventes au Fil du Temps')
    plt.xlabel('Date')
    plt.ylabel(f'Total des {target_col}')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()