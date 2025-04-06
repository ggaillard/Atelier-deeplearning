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


# Formation Deep Learning et IA conversationnelle

![Banner Deep Learning](images/banner-dl.svg)

## Bienvenue dans ce parcours d'apprentissage

Cette formation intensive vous initie au Deep Learning à travers une approche pratique et progressive, spécialement conçue pour les étudiants de BTS SIO. Vous découvrirez les fondamentaux des réseaux de neurones, explorerez différentes architectures, et développerez un chatbot pédagogique intégrant l'API Mistral AI.

## Organisation du parcours

Notre formation se compose de 4 modules de 4 heures chacun :

| Module | Titre | Aperçu |
|--------|-------|--------|
| [Module 1](module1/index.md) | **Fondamentaux du Deep Learning** | Introduction pratique, concepts fondamentaux, anatomie des réseaux de neurones |
| [Module 2](module2/index.md) | **Architectures spécialisées** | Réseaux convolutifs (CNN) pour la vision, réseaux récurrents (RNN) pour le texte |
| [Module 3](module3/index.md) | **Développement d'applications pratiques** | Frameworks, optimisation, intégration API, préparation au projet |
| [Module 4](module4/index.md) | **Projet intégrateur - Chatbot pédagogique** | Développement du chatbot, finalisation, présentation |

## Prérequis techniques

Pour suivre efficacement cette formation, vous devez :

 - Posséder des bases en programmation Python
 - Disposer d'un compte Google pour accéder à Colab
 - Avoir une curiosité pour l'intelligence artificielle

## Navigation dans ce site

Ce site contient toutes les ressources nécessaires pour votre parcours :

- **[Carte de progression](carte-progression.md)** - Parcours d'apprentissage et compétences développées
- **[Ressources](ressources/index.md)** - Documentation technique et matériel complémentaire
- **[Évaluation](evaluation/index.md)** - Critères et modalités d'évaluation

## Commencer votre parcours

Prêt à vous lancer dans l'univers du Deep Learning ? Deux options s'offrent à vous :

[Découvrir le projet chatbot](presentation.md){ .md-button }
[Commencer le Module 1](module1/index.md){ .md-button .md-button--primary }