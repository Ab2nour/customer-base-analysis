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

[`📂 data`](data)
> Contient le jeu de données, différentes versions du jeu de données transformé, ainsi que tous les résultats sauvegardés.

[`📂 docs`](docs)
> Contient la documentation du projet.

[`📂 img`](img)
> Contient des illustrations du projet.

[`📂 scripts`](scripts)
> Contient des scripts sans rapport direct avec le projet, afin d'en faciliter la maintenance.

[`📂 src`](src)
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

## Formatage

```bash
poetry run black
```

Imports
```bash
poetry run nbqa isort . --float-to-top
```
