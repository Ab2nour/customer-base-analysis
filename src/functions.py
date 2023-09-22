from sklearn.metrics import mean_squared_error, mean_absolute_error


def affiche_score(modele, y_test, y_pred) -> None:
    """Affiche la MSE, RMSE et MAE du modèle."""
    print(f"MSE = {mean_squared_error(y_test, y_pred)}")
    print(f"RMSE = {mean_squared_error(y_test, y_pred, squared=False)}")
    print(f"MAE = {mean_absolute_error(y_test, y_pred)}")
