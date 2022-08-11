# Aurion Planning to ICS
Export du planning Aurion vers ICS en Python !

## Description  :
Ce projet reprend le travail de [Mylow](https://github.com/MylowMntr) et son projet [PyAurion](https://github.com/MylowMntr/PyAurion). 

Aurion est la plateforme web (progiciel développé par Auriga) utilisé par les étudiants de Junia pour accéder à leurs plannings, notes, absences et autres informations.

L'intérêt d'exporter le planning est d'en simplifier l'accès. 
En évitent les contraintes suivantes de la plateforme web :
- Reconnexion nécessaire toutes les 30 min d'inactivité
- Chargement jusqu'à 6 sec pour 1 semaine de planning
- Format peut adapter
- Inaccessibilité hors connexion


## Fonctionnement :

### Exécution
Dans le dossier du projet, exécuter le fichier `main.py`
Indiqué votre prénom.nom puis votre mot de passe et le nombre de mois à exporter (6 par défaut).
Il suffit ensuite de double-cliquer sur le fichier / de l'importer dans votre application calendrier.

### Code
Écrit en python avec les fichiers de connexion et requête du planning Aurion du projet [PyAurion](https://github.com/MylowMntr/PyAurion). 

Login avec : `validelogs.py`
Récupération du planning : `getplanning.py`
Transformation du format utilisé (FullCalendar) vers iCalendar : `parse.py`

### iCalendar (.ics)
Format de données pour les échanges de données de calendrier. 
Chaque événement est identifié avec un ID pour éviter les doublons lors de la modification des informations d'un évènement.


## Fonctionnalités :

### Actuellement
- Création d'un fichier `planning.ics` dans les téléchargements
- Input des identifiants avec le terminal.

### À faire
- Interface pour la configuration
- Enregistrement et chiffrement du mot de passe
- Exécution automatique
- ICS feed


---

# Sources
[Aurion](https://aurion.junia.com)

[PyAurion](https://github.com/MylowMntr/PyAurion)
[Scorpion](https://github.com/LiamAbyss/Scorpion)

[FullCalendar](https://github.com/kkarimi/flask-fullcalendar)
[iCalendar](https://fr.wikipedia.org/wiki/ICalendar)