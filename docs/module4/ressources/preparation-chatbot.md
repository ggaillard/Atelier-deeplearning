# 📋 Phase 3: Préparation au chatbot d'assistance (30 min)

![Préparation au chatbot](https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80&w=1000&h=300)

## 🎯 Objectif de la phase

Dans cette phase, vous allez :

- Explorer un exemple de chatbot d'assistance informatique
- Comprendre la structure d'une base de connaissances technique
- Découvrir comment personnaliser le chatbot pour des besoins spécifiques

## 🔍 Découverte du chatbot d'assistance informatique (15 min)

### Contexte professionnel

Un chatbot d'assistance informatique peut considérablement améliorer le support utilisateur en :
- Répondant aux questions fréquentes 24h/24
- Guidant les utilisateurs à travers des procédures de dépannage
- Documentant automatiquement les problèmes récurrents
- Dirigeant vers un technicien uniquement les cas complexes

### Exemple de chatbot SIO

Voici une démonstration d'un chatbot d'assistance spécialisé pour le domaine SIO :

![Chatbot SIO](../images/chatbot-sio-screenshot.png)

**Exemples d'interactions :**

| Question utilisateur | Réponse du chatbot |
|---------------------|-------------------|
| "Je n'arrive pas à me connecter au réseau WiFi" | "Plusieurs raisons peuvent expliquer ce problème. Vérifions ensemble :<br>1. Le WiFi est-il activé sur votre appareil?<br>2. Êtes-vous à portée du réseau?<br>3. Avez-vous le bon mot de passe?<br><br>Quel est le message d'erreur exact que vous voyez?" |
| "Comment installer une imprimante réseau?" | "Pour installer une imprimante réseau, suivez ces étapes :<br>1. Ouvrez Paramètres > Imprimantes et scanners<br>2. Cliquez sur 'Ajouter une imprimante'<br>3. Sélectionnez 'Imprimante réseau'<br>4. Soit l'imprimante apparaîtra dans la liste, soit vous devrez entrer son adresse IP<br><br>Avez-vous besoin d'aide pour trouver l'adresse IP de l'imprimante?" |

### Structure du chatbot

Le chatbot d'assistance est composé de trois éléments principaux :

1. **Interface utilisateur** : Interface web simple pour la conversation
2. **Logique de traitement** : Analyse des questions et génération de réponses via l'API
3. **Base de connaissances** : Structure JSON contenant les problèmes informatiques courants

## 📋 Exploration de la base de connaissances (15 min)

### Structure de la base de connaissances

La base de connaissances du chatbot est structurée en catégories de problèmes informatiques. Voici un extrait de cette structure :

```json
{
  "categories": [
    {
      "id": "reseau",
      "nom": "Problèmes réseau",
      "problemes": [
        {
          "id": "wifi_connexion",
          "titre": "Problème de connexion WiFi",
          "mots_cles": ["wifi", "sans fil", "connexion", "réseau", "internet"],
          "symptomes": [
            "Impossible de se connecter au réseau WiFi",
            "Connexion instable ou qui se déconnecte",
            "Message d'erreur d'authentification"
          ],
          "solutions": {
            "debutant": [
              "Vérifiez que le WiFi est activé sur votre appareil (bouton physique ou dans les paramètres)",
              "Assurez-vous d'être à portée du réseau WiFi",
              "Vérifiez que vous utilisez le bon mot de passe",
              "Redémarrez votre appareil"
            ],
            "technicien": [
              "Vérifier les paramètres de sécurité WiFi (WPA2, WPA3)",
              "Contrôler les interférences avec d'autres réseaux (changer de canal)",
              "Vérifier la configuration du DHCP",
              "Contrôler les filtres MAC sur le point d'accès"
            ]
          },
          "questions_diagnostic": [
            "Voyez-vous le réseau WiFi dans la liste des réseaux disponibles?",
            "Quel message d'erreur s'affiche exactement?",
            "D'autres appareils peuvent-ils se connecter au même réseau?"
          ]
        },
        {
          "id": "ethernet_connexion",
          "titre": "Problème de connexion Ethernet",
          "mots_cles": ["ethernet", "câble", "RJ45", "réseau filaire"],
          "symptomes": [
            "Pas de connexion avec câble Ethernet",
            "Message 'Câble réseau déconnecté'",
            "Connexion très lente en filaire"
          ],
          "solutions": {
            "debutant": [
              "Vérifiez que le câble est bien branché des deux côtés",
              "Essayez un autre port sur le switch/routeur",
              "Essayez un autre câble si possible",
              "Redémarrez votre ordinateur et votre routeur"
            ],
            "technicien": [
              "Vérifier les voyants d'activité sur la carte réseau et le switch",
              "Tester la vitesse de négociation (10/100/1000)",
              "Contrôler la configuration IP (statique vs DHCP)",
              "Vérifier l'état de la carte réseau dans le gestionnaire de périphériques"
            ]
          },
          "questions_diagnostic": [
            "Les voyants du port réseau sont-ils allumés?",
            "Avez-vous récemment modifié des paramètres réseau?",
            "Le problème concerne-t-il tous les ordinateurs connectés?"
          ]
        }
      ]
    },
    {
      "id": "logiciel",
      "nom": "Problèmes logiciels",
      "problemes": [
        {
          "id": "logiciel_plantage",
          "titre": "Application qui plante ou ne répond plus",
          "mots_cles": ["plante", "freeze", "ne répond plus", "bloqué", "lent"],
          "symptomes": [
            "L'application se ferme inopinément",
            "Message 'Ne répond pas'",
            "Application figée ou très lente"
          ],
          "solutions": {
            "debutant": [
              "Fermez l'application avec le gestionnaire des tâches (Ctrl+Alt+Suppr)",
              "Redémarrez l'application",
              "Redémarrez l'ordinateur",
              "Vérifiez les mises à jour de l'application"
            ],
            "technicien": [
              "Consulter les logs d'événements pour identifier la cause",
              "Vérifier la compatibilité avec le système d'exploitation",
              "Tester en désactivant les extensions ou plugins",
              "Réparer ou réinstaller l'application"
            ]
          }
        }
      ]
    }
  ]
}

Personnalisation pour votre projet
Pour votre projet de chatbot, vous devrez créer une base de connaissances similaire, adaptée au domaine que vous choisirez. Voici les étapes à suivre :

Choisir un domaine : Assistance informatique, Support d'applications, Réseau, Sécurité...
Identifier les problèmes fréquents : Listez 5 à 10 problèmes communs dans ce domaine
Structurer chaque problème :

Titre et mots-clés
Symptômes observables
Solutions adaptées au niveau de l'utilisateur
Questions de diagnostic


Organiser par catégories : Regroupez les problèmes en 3-5 catégories logiques

Intégration avec l'API
Le chatbot utilisera l'API pour :

Analyser la question de l'utilisateur et identifier le problème correspondant
Récupérer les informations pertinentes dans la base de connaissances
Formuler une réponse adaptée au niveau technique de l'utilisateur
Poser des questions de diagnostic si nécessaire pour préciser le problème

📝 Conclusion du module
Dans cette dernière phase, vous avez découvert comment un chatbot d'assistance informatique peut être structuré pour répondre efficacement aux problèmes techniques. Cette exploration vous prépare pour votre projet final où vous développerez votre propre chatbot spécialisé.
Les compétences acquises dans ce module vous permettront de :

Intégrer des API d'IA dans des applications professionnelles concrètes
Adapter des solutions existantes à des besoins spécifiques
Structurer une base de connaissances technique efficace

Pour le prochain module, réfléchissez au domaine informatique que vous souhaitez aborder avec votre chatbot et commencez à identifier les problèmes fréquents que vous pourriez y inclure.
N'oubliez pas de compléter la dernière partie de votre fiche d'observations avec vos idées pour le chatbot à développer.
Retour au Module 3{ .md-button }
Passer au Module 4{ .md-button .md-button--primary }