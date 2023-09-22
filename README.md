# Présentation du projet
Projet de M1 Mathématiques Appliquées et Statistiques, dont le sujet est :
> **Analyse et segmentation de clientèle d'un magasin avec campagnes de marketing**

![Résultats de modèles de classification](
img/mse-rmse-mae-models.png
"Résultats de modèles de classification"
)

# Guide de développement

## Organisation

Voici l'organisation des différents dossiers du projet :

[`📂 data`](https://github.com/Ab2nour/projet-transverse/tree/main/data)
> Contient le jeu de données, différentes versions du jeu de données transformé, ainsi que tous les résultats sauvegardés.

[`📂 img`](https://github.com/Ab2nour/projet-transverse/tree/main/img)
> Contient des illustrations du projet.

[`📂 scripts`](https://github.com/Ab2nour/projet-transverse/tree/main/scripts)
> Contient des scripts sans rapport direct avec le projet, afin d'en faciliter la maintenance.

[`📂 src`](https://github.com/Ab2nour/projet-transverse/tree/main/src)
> Contient le code source du projet.

## Gérer Jupyter + git

Supprimer les méta-données :
```bash
poetry run nbdev_clean --fname presentation.ipynb
```

Supprimer les méta-données et les résultats des cellules :
```bash
poetry run nbdev_clean --fname presentation.ipynb --clear_all
```

## Formattage

```bash
poetry run black
```

Imports
```bash
poetry run nbqa isort . --float-to-top
```
