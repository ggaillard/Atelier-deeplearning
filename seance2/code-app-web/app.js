document.addEventListener('DOMContentLoaded', function() {
    // Éléments du DOM
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const predictBtn = document.getElementById('predictBtn');
    const clearBtn = document.getElementById('clearBtn');
    const imageUpload = document.getElementById('imageUpload');
    const predictedDigit = document.getElementById('predictedDigit');
    const confidence = document.getElementById('confidence');
    const processedImage = document.getElementById('processedImage');
    const resultsSection = document.getElementById('resultsSection');
    const visualizationSection = document.getElementById('visualizationSection');
    const featureMapsContainer = document.getElementById('featureMapsContainer');
    
    // Variables pour le dessin
    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;
    
    // Configuration du canvas
    ctx.lineWidth = 15;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.strokeStyle = 'black';
    
    // Remplir le canvas avec du blanc
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Variables pour le graphique de probabilités
    let probabilitiesChart = null;
    
    // Fonctions de dessin
    function startDrawing(e) {
        isDrawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
    }
    
    function draw(e) {
        if (!isDrawing) return;
        
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
        
        [lastX, lastY] = [e.offsetX, e.offsetY];
    }
    
    function stopDrawing() {
        isDrawing = false;
    }
    
    // Événements du canvas
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);
    
    // Gestion des événements tactiles
    canvas.addEventListener('touchstart', function(e) {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousedown', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    });
    
    canvas.addEventListener('touchmove', function(e) {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    });
    
    canvas.addEventListener('touchend', function(e) {
        e.preventDefault();
        const mouseEvent = new MouseEvent('mouseup', {});
        canvas.dispatchEvent(mouseEvent);
    });
    
    // Fonction pour effacer le canvas
    function clearCanvas() {
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Cacher les résultats
        resultsSection.style.display = 'none';
        visualizationSection.style.display = 'none';
    }
    
    // Événement pour le bouton d'effacement
    clearBtn.addEventListener('click', clearCanvas);
    
    // Fonction pour prédire à partir du dessin
    function predictFromCanvas() {
        // Convertir le canvas en image base64
        const imageData = canvas.toDataURL('image/png');
        
        // Envoyer l'image au serveur
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: imageData })
        })
        .then(response => response.json())
        .then(handlePredictionResponse)
        .catch(error => console.error('Erreur:', error));
    }
    
    // Fonction pour prédire à partir d'un fichier image
    function predictFromFile(file) {
        const formData = new FormData();
        formData.append('image', file);
        
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(handlePredictionResponse)
        .catch(error => console.error('Erreur:', error));
    }
    
    // Gestion de la réponse de prédiction
    function handlePredictionResponse(data) {
        if (!data.success) {
            alert('Erreur: ' + data.error);
            return;
        }
        
        // Afficher les résultats
        predictedDigit.textContent = data.prediction;
        confidence.textContent = data.confidence.toFixed(2);
        
        // Afficher l'image prétraitée
        processedImage.src = 'data:image/png;base64,' + data.processed_image;
        
        // Afficher les feature maps
        displayFeatureMaps(data.feature_maps);
        
        // Mettre à jour le graphique des probabilités
        updateProbabilitiesChart(data.all_probabilities);
        
        // Afficher les sections de résultats
        resultsSection.style.display = 'block';
        visualizationSection.style.display = 'block';
    }
    
    // Affichage des feature maps
    function displayFeatureMaps(featureMaps) {
        featureMapsContainer.innerHTML = '';
        
        featureMaps.forEach((featureMap, index) => {
            const wrapper = document.createElement('div');
            wrapper.className = 'feature-map';
            
            const heading = document.createElement('h3');
            heading.textContent = `Couche de convolution ${index + 1}`;
            
            const img = document.createElement('img');
            img.src = 'data:image/png;base64,' + featureMap;
            img.alt = `Feature maps couche ${index + 1}`;
            
            wrapper.appendChild(heading);
            wrapper.appendChild(img);
            featureMapsContainer.appendChild(wrapper);
        });
    }
    
    // Mise à jour du graphique des probabilités
    function updateProbabilitiesChart(probabilities) {
        const ctx = document.getElementById('probabilitiesChart').getContext('2d');
        
        // Détruire le graphique existant s'il existe
        if (probabilitiesChart) {
            probabilitiesChart.destroy();
        }
        
        // Labels pour les chiffres
        const labels = Array.from({length: 10}, (_, i) => i.toString());
        
        // Créer un nouveau graphique
        probabilitiesChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Probabilité (%)',
                    data: probabilities.map(p => p * 100),
                    backgroundColor: labels.map((_, i) => 
                        i === probabilities.indexOf(Math.max(...probabilities)) 
                            ? '#3498db' 
                            : '#95a5a6'
                    ),
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        title: {
                            display: true,
                            text: 'Probabilité (%)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Chiffre'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `Probabilité: ${context.raw.toFixed(2)}%`;
                            }
                        }
                    }
                }
            }
        });
    }
    
    // Événement pour le bouton de prédiction
    predictBtn.addEventListener('click', predictFromCanvas);
    
    // Événement pour l'upload d'image
    imageUpload.addEventListener('change', function(e) {
        if (e.target.files.length > 0) {
            predictFromFile(e.target.files[0]);
        }
    });
});