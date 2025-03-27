D'accord, je vais remplacer la validation collective par un encadré avec des points importants à retenir avant de passer à l'implémentation pratique :

### Étape 4 : Analogie Star Wars (3 min)

Pour comprendre le fonctionnement d'un CNN, voyons comment il pourrait identifier un personnage célèbre comme Dark Vador :

![Analogie Star Wars pour comprendre les CNN](cnn-star-wars-analogy)

- **La couche de convolution** repère les caractéristiques distinctives : "Je détecte un casque noir, un respirateur, une cape..."
- **La couche de pooling** ignore les détails non pertinents : "Peu importe l'angle de vue, l'éclairage, s'il est de face ou de profil..."
- **La couche fully connected** prend la décision finale : "D'après toutes ces caractéristiques combinées, c'est Dark Vador à 99.8%!"

Cette analogie montre comment un CNN analyse une image de manière hiérarchique, comme notre cerveau le fait naturellement.

### Points importants à retenir

> **À savoir avant de passer à la pratique :**
> 
> 1. Les CNN sont conçus spécifiquement pour traiter les données en grille comme les images.
>
> 2. Les filtres de convolution agissent comme des détecteurs de motifs qui s'appliquent à toute l'image.
>
> 3. Le pooling permet de réduire les dimensions tout en conservant l'information importante.
>
> 4. Les poids du réseau sont ajustés automatiquement pendant l'entraînement.
>
> 5. Un CNN profond permet de détecter des motifs de plus en plus complexes et abstraits.
>
> 6. Le grand avantage des CNN est qu'ils apprennent automatiquement les caractéristiques pertinentes, sans qu'on ait à les programmer manuellement.

### Transition vers l'implémentation

Maintenant que vous avez conceptualisé l'architecture d'un CNN et compris ses principes fondamentaux, passons à l'implémentation pratique pour voir ces concepts en action. Gardez votre schéma complété à portée de main - vous pourrez vous y référer pendant la partie pratique.