# Phase 1 : Mini-projet CNN pour la vision par ordinateur

![CNN Architecture](https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la phase

Dans cette phase, vous allez :

- Comprendre les principes fondamentaux des réseaux de neurones convolutifs (CNN)
- Implémenter un CNN pour la classification d'images avec TensorFlow/Keras
- Visualiser et interpréter les filtres et feature maps d'un CNN
- Intégrer un modèle CNN dans une application web simple

## Partie 1: Principes des CNN (20 min)

### Défi de réflexion initiale

Avant de plonger dans les CNN, prenez 2 minutes pour réfléchir à cette question :
> **Question à méditer** : Comment reconnaissez-vous un visage dans une photo, quelle que soit sa position ou l'éclairage ? Qu'est-ce qui rend cette tâche si facile pour vous et si difficile pour un ordinateur ?

### Activité guidée : Découverte de l'architecture CNN

**Étape 1 : Observation (3 min)**
Examinez ces deux visualisations en parallèle :
- L'image originale d'un chiffre '7' manuscrit et son traitement par les différentes couches d'un CNN

![Transformation progressive d'une image dans un CNN](../images/cnn-comparative-processing.svg)

- Les différentes caractéristiques extraites à chaque niveau d'un CNN déjà entraîné

![Hiérarchie des caractéristiques dans un CNN](../images/cnn-hierarchical-features.svg)

**Étape 2 : Mini-investigation (5 min)**
Formez des binômes et discutez :
- Que semble détecter la première couche du réseau ? (contours, textures...)
- Comment évoluent les formes détectées en avançant dans le réseau ?
- Pourquoi le réseau semble-t-il "simplifier" l'image à chaque étape ?

**Étape 3 : Construction du modèle mental (5 min)**
Sur votre feuille de travail, complétez le schéma simplifié d'un CNN :

![Schéma d'architecture CNN à compléter](../images/cnn-architecture-schema.svg)

1. Identifiez et nommez les trois types principaux de couches
2. Pour chaque type, précisez brièvement sa fonction
3. Listez les trois avantages majeurs des CNN

**Étape 4 : Analogie concrète (3 min)**
Imaginez que vous êtes un inspecteur cherchant à identifier un suspect :
- La **couche de convolution** est comme votre attention aux détails spécifiques (cicatrice, forme du nez...)
- La **couche de pooling** est comme votre capacité à ignorer les éléments non pertinents (éclairage, angle de vue...)
- La **couche fully connected** est comme votre processus de décision finale ("C'est lui !")

### Validation collective (4 min)

Comparez votre schéma avec celui de vos voisins et discutez des trois avantages majeurs des CNN pour un développeur d'applications :
- Pourquoi est-ce important de réduire le nombre de paramètres ?
- Comment l'invariance à la translation facilite-t-elle la reconnaissance d'objets ?
- Pourquoi l'extraction automatique de caractéristiques est-elle révolutionnaire ?

### Transition vers l'implémentation

Maintenant que vous avez conceptualisé l'architecture d'un CNN, passons à l'implémentation pratique pour voir ces concepts en action. Gardez votre schéma à portée de main - vous pourrez le compléter avec des observations pratiques.

## Partie 2: Implémentation d'un CNN pour MNIST (40 min)

### Instructions

1. Ouvrez le notebook Jupyter [cnn-classification](ressources/cnn-classification.md) dans Google Colab
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

Dans cette partie, vous allez découvrir comment intégrer un modèle CNN pré-entraîné dans une application web interactive.

# Mini-projet : Reconnaissance de chiffres manuscrits 

## Contexte professionnel

Vous êtes stagiaire dans une PME où les employés doivent régulièrement saisir manuellement des codes à partir de documents papier (bons de commande, formulaires clients, etc.). Votre responsable informatique souhaite explorer des solutions d'automatisation et vous demande de tester une application de reconnaissance de chiffres manuscrits.


### Étape 1: Préparation de l'environnement (8 minutes)

Pour la partie web, vous aurez besoin d'un fichier `mnist_cnn_model.h5` contenant votre modèle CNN entraîné. Ce fichier doit être généré sur Google Colab en suivant ces étapes:

### Génération du modèle sur Google Colab

1. Coller dans un nouveau notebook Google Colab le code du fichier suivant :[`create_model.py`](ressources/create_model.py).

3. Exécutez la cellule en cliquant sur le bouton de lecture ▶️ à gauche de la cellule, ou en appuyant sur Shift+Enter

## Attendre l'entraînement et télécharger le modèle

1. L'exécution durera environ 3-5 minutes sur Google Colab (qui utilise des GPU/TPU)
2. Vous verrez la progression de l'entraînement pour chaque époque
3. À la fin, votre navigateur démarrera automatiquement le téléchargement du fichier `mnist_cnn_model.h5`
4. Enregistrez ce fichier dans le dossier de votre projet web

## Avantages de cette approche:
- Aucune installation locale requise
- Utilisation gratuite des ressources GPU de Google
- Exécution plus rapide que sur un ordinateur standard
- Interface familière et intuitive
- Pas de problème d'installation ou de performance de TensorFlow sur sa machine locale.

### Étape 2 : Configuration (5 minutes)

1. **Préparation de l'environnement VS Code**
   - Ouvrez Visual Studio Code
   - Créez un nouveau dossier pour le projet: `File > Open Folder` et créez un dossier nommé `reconnaissance-chiffres`
   - Dans VS Code, créez la structure de dossiers suivante via l'explorateur:
     - Créez un dossier `templates`
     - Créez un dossier `static`
     - Dans `static`, créez les sous-dossiers `css` et `js`


2.  **Téléchargement des fichiers de l'application web** :
        * Téléchargez les fichiers suivants nécessaires à l'application web et placez-les dans les dossiers indiqués :
  
        * [web-integration.py](code-app-web/web-integration.py) - Script principal de l'application Flask.
        * [templates/index.html](code-app-web/index.html) - Template HTML pour l'interface utilisateur.
        * [static/css/style.css](code-app-web/style.css) - Feuille de style CSS.
        * [static/js/app.js](code-app-web/app.js) - Script JavaScript pour l'interactivité.

3.  **Structure des dossiers** :

   *Assurez-vous que votre structure de dossiers est la suivante:
   
   ```
   votre_dossier_de_travail/
   ├── mnist_cnn_model.h5      # Votre modèle sauvegardé ou le modèle fourni
   ├── web-integration.py      # Script principal Flask
   ├── templates/              
   │   └── index.html
   └── static/                 # Dossier pour CSS, JS, images
       ├── css/
       │   └── style.css
       └── js/
           └── app.js

### Étape 3 : Installation et lancement (5 minutes)

1. **Création du modèle via Google Colab**
   - Suivez les instructions pour créer le modèle avec Google Colab (voir sections précédentes)
   - Une fois le fichier `mnist_cnn_model.h5` téléchargé, déplacez-le dans le dossier racine de votre projet

2. **Ouverture du Terminal intégré à VS Code**
   - Dans VS Code, ouvrez un terminal en allant dans `Terminal > New Terminal`
   - Vous verrez un terminal s'ouvrir en bas de la fenêtre

3. **Installation des dépendances**
   - Dans le terminal VS Code, tapez la commande suivante:
   ```
   pip install flask tensorflow pillow numpy
   ```
   - Attendez que l'installation se termine

4. **Lancement de l'application**
   - Dans le même terminal, tapez:
   ```
   python web-integration.py
   ```
   - Vous devriez voir un message indiquant que l'application est en cours d'exécution
   - VS Code peut vous proposer d'ouvrir le lien - cliquez dessus, ou
   - Ouvrez votre navigateur et accédez à http://localhost:5001

### Étape 4 : Tests pratiques (10 minutes)

1. **Test avec dessins à la souris**
   - Dans l'interface web, dessinez clairement un chiffre (de 0 à 9) dans la zone prévue
   - Cliquez sur le bouton "Prédire"
   - Notez la prédiction et le niveau de confiance
   - Répétez ce processus avec 5 chiffres différents
   - Gardez une trace de vos résultats (tableau simple : chiffre réel / prédiction / confiance)

2. **Test avec image importée**
   - Sur une feuille de papier, écrivez clairement un chiffre
   - Prenez une photo de ce chiffre avec votre smartphone ou appareil photo
   - Transférez l'image sur votre ordinateur (par email, cloud, câble USB, etc.)
   - Dans l'application, cliquez sur "Charger une image"
   - Sélectionnez l'image que vous venez de prendre
   - Observez la prédiction et le niveau de confiance

3. **Test avec feature maps (optionnel)**
   - Cochez la case "Visualiser les feature maps"
   - Dessinez un nouveau chiffre et cliquez sur "Prédire"
   - Observez les feature maps qui s'affichent (représentations visuelles de ce que "voit" le réseau)

### Étape 5 : Évaluation et rapport (10 minutes)

1. **Remplissage du formulaire d'évaluation**
   - Ouvrez le document [evaluation](ressources/evaluation.md) fourni par votre formateur
   - Remplissez les sections suivantes :
     - Nombre de prédictions correctes/incorrectes
     - Chiffres les mieux reconnus
     - Chiffres les plus difficiles à reconnaître
     - Niveau de confiance moyen observé

2. **Analyse critique**
   - Dans le formulaire, notez au moins 3 points forts de l'application
   - Notez également au moins 3 limitations ou problèmes rencontrés

3. **Propositions d'amélioration**
   - Proposez 2-3 idées concrètes pour améliorer l'outil dans un contexte professionnel
   - Exemple : "Ajouter une fonction pour traiter plusieurs chiffres à la fois"

4. **Conclusion professionnelle**
   - Rédigez une brève conclusion (2-3 phrases) sur l'utilité potentielle de cet outil dans l'entreprise

## Livrable à rendre

## Instructions de remise

À la fin de la session (30 minutes), veuillez :

1. **Copier et Compléter** entièrement ce [formulaire d'évaluation](ressources/evaluationCNN.md)
2. **Enregistrer**  le document  sous le nom "Eval_CNN_NOM_Prenom.doc"
3. **Partager** votre évaluation avec l'enseignant sur l'espace de cours:
   
**IMPORTANT :** La remise de ce document complété est obligatoire et fait partie de l'évaluation du mini-projet.

Date limite de remise : À la fin de la séance

## Pour aller plus loin (si vous terminez en avance)

Si vous avez terminé avant la fin du temps imparti, vous pouvez explorer ces pistes :
- Testez les limites du modèle en dessinant des chiffres de différentes tailles/styles
- Observez comment le bruit ou les distorsions affectent la précision
- Essayez de comprendre le code source dans `web-integration.py` pour voir comment l'application fonctionne


# Ressources complémentaires

- [Tutoriel TensorFlow sur les CNN](https://www.tensorflow.org/tutorials/images/cnn) - Guide officiel de TensorFlow sur l'implémentation des réseaux de neurones convolutifs
- [Visualisation de CNN (Distill.pub)](https://distill.pub/2017/feature-visualization/) - Article interactif sur la visualisation et l'interprétation des réseaux convolutifs
- [Documentation Flask](https://flask.palletsprojects.com/en/2.3.x/) - Documentation officielle du framework Flask pour le développement web


Retour à la Séance 2{ .md-button }
Continuer vers la Phase 2: RNN{ .md-button .md-button--primary }