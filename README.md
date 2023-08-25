# Block_5
 Projet **Getaround** pour le Bloc 5 de la certification


# Introduction
Ce repository contient les répertoires des livrables pour le projet Getaround.

 
## Analyse des retards et prédiction de tarifs
Présentation vidéo du projet réalisé : https://share.vidyard.com/watch/bTYz2UfrLu4h8gyMdkchmf?

Ce projet contient plusieurs notebooks : un notebook par modèle.
* 01-Getaround_analysis.ipynb : Enoncé des besoins
* 02_Cars_delays_and_cancelations.ipynb : Analyse des retards, annulations et recommandation
* 03_Price_optimization.ipynb : Analyse des caractéristiques des voitures et prédiction de tarifs
* 04_api_test.ipynb : Test de l'API créée pour déployer le modèle (externe et dans le dashboard)
* Les notebooks s'accompagnent d'un répertoire **src** contenant les datasets originaux
 
 
## Création d'une API
Cette dimension du projet a consisté à créer une API permettant à Getaround de prédire des prix.
Il s'agit du répertoire **api**
 
 
## Création d'un dashboard (en anglais)
Il s'agit du répertoire streamlit. Ce répertoire contient un sous-répertoire src contenant les datasets.

Ce dashboard a été créé pour extraire les KPI intéressants pour répondre aux questions du marketing Getaround :
* Which share of our owner’s revenue would potentially be affected by the feature?
* How many rentals would be affected by the feature depending on the threshold and scope we choose?
* How often are drivers late for the next check-in? How does it impact the next driver?
* How many problematic cases will it solve depending on the chosen threshold and scope?

