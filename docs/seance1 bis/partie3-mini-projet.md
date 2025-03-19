## Phase 3 : Mini-projet collaboratif (1h)

### Objectif

Plongez directement dans l'amélioration concrète d'un modèle de Deep Learning ! Cet atelier vous permettra de maîtriser les facteurs clés de performance des réseaux de neurones, tout en aiguisant vos compétences en résolution de problèmes et en travail d'équipe.

### Déroulement

1.  **Formation des groupes (5 min)**
    * Constitution de groupes de 3-4 étudiants.
    * Attribution d'un notebook par groupe contenant un modèle de base fonctionnel mais avec des performances médiocres.

2.  **Présentation du challenge (10 min)**
    * Explication du problème : classification d'images MNIST avec un réseau de neurones simple atteignant seulement 85% de précision.
    * Objectif : améliorer la performance en modifiant l'architecture et les hyperparamètres.
    * Règles : chaque groupe doit documenter ses modifications et justifier ses choix.
    * Présentation du tableau de scores en temps réel où la précision de chaque modèle sera affichée.

3.  **Travail en groupe (35 min)**
    * Analyse du modèle de base et identification des limitations.
    * Exploration des options d'amélioration :
        * Modification du nombre de neurones et de couches.
        * Ajustement des fonctions d'activation.
        * Changement des hyperparamètres d'apprentissage (taux d'apprentissage, taille des batchs).
        * Ajout de techniques de régularisation (dropout, batch normalization).
    * Test des modifications et observation des résultats.
    * Documentation des essais dans un tableau de suivi fourni.

4.  **Partage des résultats (10 min)**
    * Chaque groupe soumet sa meilleure version.
    * Les résultats sont compilés dans le tableau de scores.
    * Annonce des trois meilleurs modèles.

### Notebook de base fourni

Le notebook fourni à chaque groupe contient :

* Code de chargement des données MNIST.
* Modèle de base simple (1-2 couches) avec une précision d'environ 85%.
* Fonctions d'évaluation et de visualisation des résultats.
* Sections commentées suggérant des zones à modifier.

### Ressources à disposition

* Fiche récapitulative des architectures possibles de réseaux de neurones.
* Guide des hyperparamètres avec plages de valeurs recommandées.
* Documentation TensorFlow/Keras simplifiée ciblant les fonctions pertinentes.
* Système de questions/réponses pour débloquer les groupes en difficulté.

### Tableau de suivi des modifications

Chaque groupe remplit un tableau de suivi incluant :

* Description de chaque modification testée.
* Impact observé sur la performance (précision sur l'ensemble de validation).
* Temps d'entraînement.
* Commentaires et observations.

### Évaluation

L'évaluation porte sur :

* L'amélioration effective de la performance du modèle.
* La pertinence des modifications apportées.
* La qualité de l'analyse et de la documentation.
* La capacité à justifier les choix techniques.