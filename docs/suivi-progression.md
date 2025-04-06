# Suivi de progression personnalisé
## Votre progression

<div class="progress-container">
    <div class="progress-overview">
        <div class="progress-module">
            <h3>Module 1</h3>
            <div class="progress-bar-container">
                <div class="progress-bar" id="module1-progress"></div>
                <span class="progress-text" id="module1-text">0%</span>
            </div>
        </div>
        <div class="progress-module">
            <h3>Module 2</h3>
            <div class="progress-bar-container">
                <div class="progress-bar" id="module2-progress"></div>
                <span class="progress-text" id="module2-text">0%</span>
            </div>
        </div>
        <div class="progress-module">
            <h3>Module 3</h3>
            <div class="progress-bar-container">
                <div class="progress-bar" id="module3-progress"></div>
                <span class="progress-text" id="module3-text">0%</span>
            </div>
        </div>
        <div class="progress-module">
            <h3>Module 4</h3>
            <div class="progress-bar-container">
                <div class="progress-bar" id="module4-progress"></div>
                <span class="progress-text" id="module4-text">0%</span>
            </div>
        </div>
    </div>
    <div class="global-progress">
        <h3>Progression globale</h3>
        <div class="progress-bar-container">
            <div class="progress-bar" id="global-progress"></div>
            <span class="progress-text" id="global-text">0%</span>
        </div>
    </div>
    <div class="progress-actions">
        <a href="suivi-progression/" class="progress-button">Voir le détail de ma progression</a>
        <button class="progress-button" onclick="resetProgress()">Réinitialiser ma progression</button>
    </div>
</div>

<style>
.progress-container {
    background-color: #f8f9fa;
    border-radius: 8px;
    padding: 20px;
    margin: 30px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.progress-overview {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.progress-module h3, .global-progress h3 {
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 1.1rem;
}

.progress-bar-container {
    background-color: #e9ecef;
    border-radius: 5px;
    height: 24px;
    position: relative;
    overflow: hidden;
}

.progress-bar {
    background-color: #3498db;
    height: 100%;
    width: 0%;
    transition: width 0.3s ease;
}

.progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #333;
    font-weight: bold;
    mix-blend-mode: difference;
}

.global-progress {
    margin-bottom: 30px;
}

.global-progress .progress-bar-container {
    height: 30px;
}

.global-progress .progress-bar {
    background-color: #27ae60;
}

.progress-actions {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
}

.progress-button {
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
    transition: background-color 0.3s;
    font-size: 14px;
}

.progress-button:hover {
    background-color: #2980b9;
}
</style>

<script>
// Configuration des sections par module
const moduleConfig = {
    module1: {
        sections: [
            'module1-intro-pratique',
            'module1-concepts-fondamentaux',
            'module1-mini-projet',
            'module1-auto-evaluation'
        ],
        totalActivities: 10
    },
    module2: {
        sections: [
            'module2-reseaux-convolutifs',
            'module2-reseaux-recurrents',
            'module2-challenge-amelioration'
        ],
        totalActivities: 10
    },
    module3: {
        sections: [
            'module3-frameworks',
            'module3-integration',
            'module3-preparation-projet'
        ],
        totalActivities: 9
    },
    module4: {
        sections: [
            'module4-developpement',
            'module4-finalisation',
            'module4-presentation'
        ],
        totalActivities: 10
    }
};

// Calculer et afficher la progression
function updateProgressBars() {
    const progress = JSON.parse(localStorage.getItem('dl-progress') || '{}');
    
    // Progression par module
    let totalCompleted = 0;
    let totalActivities = 0;
    
    Object.keys(moduleConfig).forEach(moduleId => {
        const module = moduleConfig[moduleId];
        let moduleCompleted = 0;
        
        // Compter les sections complétées dans ce module
        module.sections.forEach(section => {
            if (progress[section] && progress[section].completed) {
                moduleCompleted++;
            }
        });
        
        // Calculer le pourcentage pour ce module
        const modulePercentage = Math.round((moduleCompleted / module.totalActivities) * 100);
        
        // Mettre à jour la barre de progression du module
        document.getElementById(`${moduleId}-progress`).style.width = `${modulePercentage}%`;
        document.getElementById(`${moduleId}-text`).textContent = `${modulePercentage}%`;
        
        // Mettre à jour les totaux pour la progression globale
        totalCompleted += moduleCompleted;
        totalActivities += module.totalActivities;
    });
    
    // Calculer et afficher la progression globale
    const globalPercentage = Math.round((totalCompleted / totalActivities) * 100);
    document.getElementById('global-progress').style.width = `${globalPercentage}%`;
    document.getElementById('global-text').textContent = `${globalPercentage}%`;
}

// Réinitialiser toute la progression
function resetProgress() {
    if (confirm('Êtes-vous sûr de vouloir réinitialiser toute votre progression ? Cette action est irréversible.')) {
        localStorage.removeItem('dl-progress');
        updateProgressBars();
        alert('Votre progression a été réinitialisée.');
    }
}

// Mettre à jour les barres de progression au chargement de la page
window.addEventListener('DOMContentLoaded', updateProgressBars);
</script>
## Tableau de bord

Ce tableau de bord vous permet de suivre votre progression à travers les différents modules et activités de la formation Deep Learning. Cochez les cases au fur et à mesure que vous complétez chaque partie.

### Module 1 : Fondamentaux du Deep Learning

| Section | Activité | Statut | Date de complétion |
|---------|----------|--------|-------------------|
| **Introduction pratique** | Démonstrations d'applications | ⬜ | |
| | Premier contact avec un réseau de neurones | ⬜ | |
| | Expérimentations guidées | ⬜ | |
| **Concepts fondamentaux** | Atelier "Boîte noire" | ⬜ | |
| | Défi de généralisation | ⬜ | |
| | Exploration d'un neurone et d'un réseau | ⬜ | |
| **Mini-projet individuel** | Modification et amélioration d'un réseau | ⬜ | |
| | Documentation des résultats | ⬜ | |
| **Auto-évaluation** | QCM sur les concepts fondamentaux | ⬜ | |
| | Schéma conceptuel complété | ⬜ | |

### Module 2 : Architectures spécialisées

| Section | Activité | Statut | Date de complétion |
|---------|----------|--------|-------------------|
| **Réseaux convolutifs (CNN)** | Principes des CNN | ⬜ | |
| | Implémentation d'un CNN pour MNIST | ⬜ | |
| | Visualisation des filtres et feature maps | ⬜ | |
| | Intégration dans une application web | ⬜ | |
| **Réseaux récurrents (RNN)** | Principes des RNN/LSTM | ⬜ | |
| | Implémentation d'un modèle d'analyse de sentiment | ⬜ | |
| | Expérimentation avec l'API Mistral AI | ⬜ | |
| **Challenge d'amélioration** | Diagnostic d'un modèle sous-optimal | ⬜ | |
| | Expérimentation avec différentes architectures | ⬜ | |
| | Documentation des améliorations | ⬜ | |

### Module 3 : Développement d'applications pratiques

| Section | Activité | Statut | Date de complétion |
|---------|----------|--------|-------------------|
| **Frameworks pour débutants** | Installation et configuration de TensorFlow/Keras | ⬜ | |
| | Utilisation de modèles pré-entraînés | ⬜ | |
| | Développement d'une API simple | ⬜ | |
| **Amélioration des performances** | Techniques d'optimisation | ⬜ | |
| | Bonnes pratiques | ⬜ | |
| | TP pratique d'amélioration | ⬜ | |
| **Préparation au projet final** | Étude du cahier des charges | ⬜ | |
| | Analyse de cas réels | ⬜ | |
| | Prototype avec API Mistral | ⬜ | |

### Module 4 : Projet intégrateur - Chatbot pédagogique

| Section | Activité | Statut | Date de complétion |
|---------|----------|--------|-------------------|
| **Développement du chatbot** | Interface conversationnelle | ⬜ | |
| | Intégration avec API Mistral AI | ⬜ | |
| | Base de connaissances | ⬜ | |
| | Fonctionnalités pédagogiques | ⬜ | |
| **Finalisation et tests** | Tests fonctionnels | ⬜ | |
| | Optimisation des performances | ⬜ | |
| | Documentation technique | ⬜ | |
| | Guide utilisateur | ⬜ | |
| **Présentation** | Préparation de la démonstration | ⬜ | |
| | Présentation finale | ⬜ | |

## Livrables soumis

| Livrable | Module | Statut | Date de soumission | Note |
|----------|--------|--------|-------------------|------|
| Fiche d'observations "Hello World" | 1 | ⬜ | | |
| Tableau comparatif ML vs DL | 1 | ⬜ | | |
| Schéma annoté d'un réseau de neurones | 1 | ⬜ | | |
| Rapport du mini-projet | 1 | ⬜ | | |
| Application CNN fonctionnelle | 2 | ⬜ | | |
| Modèle RNN pour analyse de sentiment | 2 | ⬜ | | |
| Rapport d'analyse comparative | 2 | ⬜ | | |
| Modèle optimisé et documentation | 3 | ⬜ | | |
| Document de conception du chatbot | 3 | ⬜ | | |
| Code source du chatbot | 4 | ⬜ | | |
| Base de connaissances | 4 | ⬜ | | |
| Documentation technique | 4 | ⬜ | | |
| Guide utilisateur | 4 | ⬜ | | |
| Présentation finale | 4 | ⬜ | | |

## Graphique de progression

Pour visualiser votre progression globale, calculez le pourcentage d'activités complétées pour chaque module :

- Module 1 : ____ / 10 activités complétées (____%)
- Module 2 : ____ / 10 activités complétées (____%)
- Module 3 : ____ / 9 activités complétées (____%)
- Module 4 : ____ / 10 activités complétées (____%)

**Progression globale** : ____ / 39 activités complétées (____%)

## Mes badges

<div class="badges-container" id="badges-container">
    <div class="badge-placeholder">Complétez des sections pour débloquer des badges!</div>
</div>

## Instructions d'utilisation

1. Téléchargez ou imprimez cette page pour votre suivi personnel
2. Cochez les cases (remplacez ⬜ par ✅) au fur et à mesure de votre progression
3. Notez la date de complétion pour chaque activité
4. Calculez régulièrement votre pourcentage de progression
5. Partagez votre progression avec votre formateur lors des points d'étape

## Notes personnelles et réflexions

Utilisez cet espace pour noter vos observations, difficultés rencontrées et points forts identifiés au cours de votre formation.

[Retour à l'accueil](index.md){ .md-button }