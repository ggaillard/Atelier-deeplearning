# Séance 2 : Types de réseaux et leurs applications

![Types de réseaux](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=1000&h=300)

## Objectifs de la séance

Cette séance vous permettra de :

- Comprendre et manipuler les architectures CNN pour la vision par ordinateur
- Explorer les réseaux RNN pour le traitement des séquences et du langage naturel
- Intégrer des modèles de Deep Learning dans des applications web
- Expérimenter avec l'API Mistral AI pour des tâches de génération de texte
- Développer une approche d'amélioration itérative des modèles

## Structure de la séance (4h)

<div class="mermaid">
gantt
    dateFormat  HH:mm
    axisFormat %H:%M
    section Planning
    Mini-projet CNN                  :milestone, 00:00, 1h30m
    Mini-projet RNN/LSTM             :milestone, 01:30, 1h30m
    Pause                           :milestone, 03:00, 15m
    Challenge d'amélioration        :milestone, 03:15, 45m
</div>

## Trois phases d'apprentissage

### [Phase 1 : Mini-projet CNN pour la vision par ordinateur](partie1-cnn.md) (1h30)

Plongez dans l'univers des réseaux de neurones convolutifs (CNN) et apprenez à les utiliser pour la classification d'images.

- Principes des convolutions et du pooling
- Implémentation d'un CNN avec TensorFlow/Keras
- Visualisation des filtres et feature maps
- Intégration d'un modèle CNN dans une application web

### [Phase 2 : Mini-projet RNN pour le traitement du langage](partie2-rnn.md) (1h30)

Découvrez les réseaux récurrents (RNN/LSTM) et leur application au traitement du langage naturel.

- Principes des réseaux récurrents et modèles LSTM
- Implémentation d'un modèle d'analyse de sentiment
- Expérimentation avec l'API Mistral AI
- Premier pas vers le projet de chatbot pédagogique

### [Phase 3 : Challenge d'amélioration de modèle](partie3-amelioration.md) (45min)

Travaillez en équipe pour améliorer les performances d'un modèle sous-optimal.

- Diagnostic des faiblesses d'un modèle existant
- Expérimentation avec différentes architectures et hyperparamètres
- Documentation et analyse des améliorations
- Comparaison des résultats entre équipes

Pour des instructions détaillées sur l'installation et l'utilisation des scripts d'intégration, consultez les [instructions d'intégration](../ressources/instructions-integration.md).

## Compétences développées

Cette séance vous permettra de développer plusieurs compétences du référentiel BTS SIO SLAM :

- **B2.2** : Conception de solutions applicatives (architecture CNN/RNN)
- **B2.3** : Développement (implémentation des modèles et intégration)
- **B1.4** : Exploitation des standards (APIs REST)
- **B1.3** : Gestion des données (datasets d'images et de texte)

## Livrables attendus

À l'issue de cette séance, vous devrez avoir produit :

1. Un modèle CNN fonctionnel pour la classification d'images avec visualisations
2. Un modèle RNN/LSTM pour l'analyse de sentiment avec premiers tests d'intégration API
3. Un rapport d'amélioration documentant vos expérimentations sur le modèle sous-optimal

Ces livrables seront utilisés comme base pour le développement du chatbot pédagogique lors des séances suivantes.

## Prêt à commencer ?

Commencez par la première phase pour explorer les réseaux convolutifs (CNN) et leur application à la vision par ordinateur.

[Commencer la Phase 1: CNN](partie1-cnn.md){ .md-button .md-button--primary }