# projet-transverse

# Développement

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
