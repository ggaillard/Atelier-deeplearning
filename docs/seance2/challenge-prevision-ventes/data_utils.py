"""
data_utils.py
Fonctions utilitaires pour le traitement des données de ventes pour le challenge de prévision.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def load_sales_data(filepath="sales_data.csv"):
    """
    Charge les données de ventes à partir d'un fichier CSV.
    
    Args:
        filepath (str): Chemin vers le fichier CSV des données de ventes
        
    Returns:
        pandas.DataFrame: DataFrame contenant les données de ventes
    """
    try:
        df = pd.read_csv(filepath)
        # Convertir la colonne date en datetime
        df['date'] = pd.to_datetime(df['date'])
        print(f"Données chargées avec succès: {df.shape[0]} lignes et {df.shape[1]} colonnes")
        return df
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        # Créer des données synthétiques si le fichier n'existe pas
        return generate_synthetic_data()

def generate_synthetic_data(n_samples=365*2):
    """
    Génère des données de ventes synthétiques pour le challenge.
    
    Args:
        n_samples (int): Nombre d'échantillons à générer
        
    Returns:
        pandas.DataFrame: DataFrame contenant les données synthétiques
    """
    # Date de début (2 ans de données)
    start_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(n_samples)]
    
    # Catégories de produits
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Création du DataFrame
    data = []
    for date in dates:
        for _ in range(np.random.randint(3, 8)):  # 3-7 transactions par jour
            category = np.random.choice(categories)
            
            # Prix de base selon la catégorie
            base_prices = {
                'Electronics': np.random.uniform(100, 1000),
                'Clothing': np.random.uniform(20, 200),
                'Home': np.random.uniform(50, 500),
                'Books': np.random.uniform(10, 50),
                'Sports': np.random.uniform(30, 300)
            }
            price = base_prices[category]
            
            # Remise
            discount = np.random.choice([0, 0, 0, 5, 10, 15, 20, 25], p=[0.6, 0.1, 0.1, 0.05, 0.05, 0.05, 0.03, 0.02])
            
            # Jour de la semaine (0=lundi, 6=dimanche)
            weekday = date.weekday()
            
            # Période promotionnelle (plus fréquente en fin de mois)
            is_promotional = 1 if (date.day > 25 or date.day < 5) or np.random.random() < 0.1 else 0
            
            # Température (saisonnalité)
            month = date.month
            base_temp = 15 + 10 * np.sin((month - 1) * np.pi / 6)  # Plus chaud en été
            temperature = base_temp + np.random.uniform(-5, 5)
            
            # Précipitations (plus élevées en automne/hiver)
            rainfall_prob = 0.3 + 0.2 * np.sin((month - 7) * np.pi / 6)
            rainfall = np.random.exponential(5) if np.random.random() < rainfall_prob else 0
            
            # Quantité vendue (influencée par divers facteurs)
            base_quantity = np.random.poisson(5)
            
            # Facteurs d'influence
            # - Les weekends (5,6) ont plus de ventes
            weekend_factor = 1.5 if weekday >= 5 else 1.0
            # - Les périodes promotionnelles augmentent les ventes
            promo_factor = 1.8 if is_promotional else 1.0
            # - Les ventes sont saisonnières (pics avant Noël, été pour certaines catégories)
            seasonal_factor = 1.0
            if category == 'Electronics' and (month == 11 or month == 12):
                seasonal_factor = 1.7  # Plus d'électronique avant Noël
            elif category == 'Clothing' and (month >= 3 and month <= 5):
                seasonal_factor = 1.4  # Plus de vêtements au printemps
            elif category == 'Sports' and (month >= 4 and month <= 8):
                seasonal_factor = 1.6  # Plus d'articles de sport en été
            
            # Appliquer tous les facteurs
            quantity_sold = max(1, int(base_quantity * weekend_factor * promo_factor * seasonal_factor))
            
            # Calculer le chiffre d'affaires
            revenue = price * quantity_sold * (1 - discount/100)
            
            data.append({
                'date': date,
                'product_category': category,
                'price': round(price, 2),
                'discount': discount,
                'quantity_sold': quantity_sold,
                'weekday': weekday,
                'is_promotional_period': is_promotional,
                'temperature': round(temperature, 1),
                'rainfall': round(rainfall, 1),
                'revenue': round(revenue, 2)
            })
    
    df = pd.DataFrame(data)
    print(f"Données synthétiques générées: {df.shape[0]} lignes et {df.shape[1]} colonnes")
    return df

def preprocess_data(df, target_col='revenue', test_size=0.2):
    """
    Prétraite les données pour les modèles de Deep Learning.
    
    Args:
        df (pandas.DataFrame): DataFrame contenant les données de ventes
        target_col (str): Nom de la colonne cible à prédire
        test_size (float): Proportion des données à réserver pour le test
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test, scalers) où scalers est un dictionnaire 
               contenant les objets de mise à l'échelle pour inverser les transformations
    """
    # Copie du DataFrame pour éviter les modifications inplace
    data = df.copy()
    
    # Ajouter des caractéristiques temporelles
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_year'] = data['date'].dt.dayofyear
    data['quarter'] = data['date'].dt.quarter
    
    # Encodage one-hot des catégories de produits
    encoder = OneHotEncoder(sparse=False)
    category_encoded = encoder.fit_transform(data[['product_category']])
    category_cols = [f"cat_{cat}" for cat in encoder.categories_[0]]
    category_df = pd.DataFrame(category_encoded, columns=category_cols)
    
    # Concaténer au DataFrame original
    data = pd.concat([data.reset_index(drop=True), category_df.reset_index(drop=True)], axis=1)
    
    # Sélectionner les colonnes numériques pour la normalisation
    numeric_cols = ['price', 'discount', 'quantity_sold', 'weekday', 
                    'is_promotional_period', 'temperature', 'rainfall',
                    'year', 'month', 'day', 'day_of_year', 'quarter']
    
    # Normaliser les caractéristiques numériques
    scaler_X = MinMaxScaler()
    data[numeric_cols] = scaler_X.fit_transform(data[numeric_cols])
    
    # Normaliser la cible
    scaler_y = MinMaxScaler()
    data[target_col] = scaler_y.fit_transform(data[[target_col]])
    
    # Sélectionner les caractéristiques et la cible
    features = numeric_cols + category_cols
    X = data[features].values
    y = data[target_col].values
    
    # Division temporelle en ensembles d'entraînement et de test
    split_idx = int(len(data) * (1 - test_size))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    # Stocker les scalers pour inverser les transformations plus tard
    scalers = {
        'X': scaler_X,
        'y': scaler_y,
        'features': features,
        'target': target_col
    }
    
    print(f"Données prétraitées: {len(X_train)} échantillons d'entraînement, {len(X_test)} échantillons de test")
    return X_train, X_test, y_train, y_test, scalers

def create_sequences(X, y, seq_length=7):
    """
    Crée des séquences pour l'entraînement de modèles RNN/LSTM.
    
    Args:
        X (numpy.ndarray): Caractéristiques
        y (numpy.ndarray): Cible
        seq_length (int): Longueur de la séquence (nombre de jours précédents à considérer)
        
    Returns:
        tuple: (X_seq, y_seq) où X_seq contient des séquences de caractéristiques et 
               y_seq contient les valeurs cibles correspondantes
    """
    X_seq, y_seq = [], []
    
    for i in range(len(X) - seq_length):
        X_seq.append(X[i:i+seq_length])
        y_seq.append(y[i+seq_length])
    
    return np.array(X_seq), np.array(y_seq)

def inverse_transform_predictions(y_pred, scaler_y):
    """
    Inverse la normalisation des prédictions.
    
    Args:
        y_pred (numpy.ndarray): Prédictions normalisées
        scaler_y (sklearn.preprocessing.MinMaxScaler): Scaler utilisé pour la cible
        
    Returns:
        numpy.ndarray: Prédictions dans l'échelle originale
    """
    # Reshape si nécessaire
    if len(y_pred.shape) == 1:
        y_pred = y_pred.reshape(-1, 1)
    
    # Inverse la normalisation
    return scaler_y.inverse_transform(y_pred)

def plot_predictions_vs_actual(y_true, y_pred, dates=None, title="Prédictions vs Valeurs Réelles"):
    """
    Trace un graphique des prédictions vs valeurs réelles.
    
    Args:
        y_true (numpy.ndarray): Valeurs réelles
        y_pred (numpy.ndarray): Prédictions
        dates (list, optional): Liste des dates correspondant aux données
        title (str): Titre du graphique
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
    plt.ylabel('Chiffre d\'affaires')
    plt.legend()
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    
    # Calculer et afficher les métriques
    mse = np.mean((y_true - y_pred)**2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))
    
    plt.figtext(0.5, 0.01, f'RMSE: {rmse:.2f}, MAE: {mae:.2f}', 
                ha='center', fontsize=12, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})
    
    plt.show()

def calculate_metrics(y_true, y_pred):
    """
    Calcule diverses métriques d'évaluation.
    
    Args:
        y_true (numpy.ndarray): Valeurs réelles
        y_pred (numpy.ndarray): Prédictions
        
    Returns:
        dict: Dictionnaire contenant les métriques d'évaluation
    """
    mse = np.mean((y_true - y_pred)**2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_true - y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / (y_true + 1e-10))) * 100
    
    metrics = {
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'mape': mape
    }
    
    return metrics

def plot_metrics_by_category(df, y_true, y_pred, category_col='product_category'):
    """
    Trace les métriques d'erreur par catégorie de produit.
    
    Args:
        df (pandas.DataFrame): DataFrame contenant les données
        y_true (numpy.ndarray): Valeurs réelles
        y_pred (numpy.ndarray): Prédictions
        category_col (str): Nom de la colonne de catégorie
    """
    # S'assurer que les données ont la même longueur
    n_samples = min(len(df), len(y_true), len(y_pred))
    df_subset = df.iloc[-n_samples:].copy()
    df_subset['true'] = y_true[-n_samples:]
    df_subset['pred'] = y_pred[-n_samples:]
    df_subset['abs_error'] = np.abs(df_subset['true'] - df_subset['pred'])
    
    # Calculer l'erreur moyenne par catégorie
    error_by_category = df_subset.groupby(category_col)['abs_error'].mean().sort_values(ascending=False)
    
    # Tracer le graphique
    plt.figure(figsize=(10, 6))
    error_by_category.plot(kind='bar', color='coral')
    plt.title('Erreur Moyenne Absolue par Catégorie de Produit')
    plt.ylabel('Erreur Moyenne Absolue')
    plt.xlabel('Catégorie de Produit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, axis='y', alpha=0.3)
    plt.show()

def analyze_residuals(y_true, y_pred):
    """
    Analyse les résidus du modèle.
    
    Args:
        y_true (numpy.ndarray): Valeurs réelles
        y_pred (numpy.ndarray): Prédictions
    """
    residuals = y_true - y_pred
    
    plt.figure(figsize=(15, 5))
    
    # Histogramme des résidus
    plt.subplot(1, 2, 1)
    plt.hist(residuals, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.axvline(x=0, color='red', linestyle='--')
    plt.title('Distribution des Résidus')
    plt.xlabel('Résidu')
    plt.ylabel('Fréquence')
    
    # Graphique des résidus par rapport aux valeurs prédites
    plt.subplot(1, 2, 2)
    plt.scatter(y_pred, residuals, alpha=0.5, color='blue')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Résidus vs Valeurs Prédites')
    plt.xlabel('Valeurs Prédites')
    plt.ylabel('Résidus')
    
    plt.tight_layout()
    plt.show()
    
    # Statistiques des résidus
    print("Statistiques des résidus:")
    print(f"Moyenne: {np.mean(residuals):.4f}")
    print(f"Écart-type: {np.std(residuals):.4f}")
    print(f"Min: {np.min(residuals):.4f}")
    print(f"Max: {np.max(residuals):.4f}")