# Application d'Analyse des Données Climatiques

## Contexte

Dans un monde où les changements climatiques ont un impact croissant sur notre environnement, il est essentiel de disposer d'outils efficaces pour analyser et visualiser les données climatiques. Ce projet vise à développer une application interactive qui permet aux utilisateurs d'explorer les données climatiques à partir de fichiers Excel, facilitant ainsi la prise de décision basée sur des données précises et actualisées.

## Objectif

L'objectif principal de cette application est de fournir une interface utilisateur intuitive qui permet aux chercheurs, aux météorologues, et aux passionnés de climat d'analyser les températures et les précipitations dans différentes régions et localités. Grâce à des visualisations interactives, les utilisateurs peuvent facilement identifier des tendances climatiques, évaluer des seuils de température, et comprendre la répartition des jours de pluie.

## Fonctionnalités Principales

1. **Chargement des Données** : Les utilisateurs peuvent télécharger des fichiers Excel contenant des données climatiques. L'application extrait automatiquement les données pertinentes pour l'analyse.

2. **Sélection Interactive** : Les utilisateurs peuvent choisir une région et une localité spécifiques. L'application filtre les données en conséquence, permettant une analyse ciblée.

3. **Visualisation Graphique** :
   - **Graphiques Températures et Précipitations** : Affichage des températures maximales et minimales ainsi que des précipitations au fil du temps.
   - **Analyse des Jours Chauds** : Possibilité d'entrer un seuil de température pour compter le nombre de jours dépassant cette valeur.
   - **Jours de Pluie** : Affichage du nombre total de jours de pluie dans la localité choisie.

4. **Résumé Régional** : Fournit un aperçu des tendances climatiques pour toutes les localités d'une région donnée, facilitant la comparaison entre différentes zones.

5. **Interactivité** : Les graphiques sont interactifs, permettant aux utilisateurs d'explorer les données en détail grâce à des fonctionnalités telles que le survol pour afficher des valeurs précises.

## Technologies Utilisées

- **Streamlit** : Pour le développement de l'interface utilisateur interactive.
- **Pandas** : Pour la manipulation et l'analyse des données.
- **Plotly** : Pour la création de visualisations graphiques interactives.

## Public Cible

Cette application s'adresse à un large éventail d'utilisateurs :
- Chercheurs en climatologie
- Étudiants en sciences environnementales
- Professionnels travaillant dans le domaine agricole
- Toute personne intéressée par l'analyse climatique

## Impact Attendu

En fournissant un outil accessible et facile à utiliser pour l'analyse des données climatiques, ce projet vise à sensibiliser le public aux enjeux climatiques et à encourager une prise de décision éclairée basée sur des données fiables. L'application peut également servir de base pour des recherches futures ou pour le développement d'outils similaires dans d'autres domaines liés aux sciences environnementales.

## Conclusion

Ce projet représente une avancée significative dans l'analyse des données climatiques, alliant technologie moderne et accessibilité. En facilitant l'exploration et la visualisation des données, il contribue à une meilleure compréhension des tendances climatiques et encourage une action proactive face aux défis environnementaux actuels.

## Installation

Pour exécuter cette application, assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez les dépendances requises :

pip install streamlit pandas plotly openpyxl

## Lancement de l'Application

Pour démarrer l'application, exécutez la commande suivante dans votre terminal :

streamlit run app.py

Remplacez `app.py` par le nom du fichier contenant votre code Streamlit.

## Auteurs

- [POUM Bimbar Paul](https://github.com/Dev-Onacc/) - Développeur principal

## License
Ce projet est sous licence MIT.

## Remerciements
Merci à tous ceux qui ont contribué à ce projet et à ceux qui ont partagé leurs connaissances sur l'analyse climatique.