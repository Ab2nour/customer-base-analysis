import xgboost
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.base import BaseEstimator
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier


def create_classification_models(seed: int) -> list[list[BaseEstimator, str], ...]:
    models = [
        [
            DummyClassifier(strategy="uniform", random_state=seed),
            "DummyClassifier_Uniform",
        ],
        [
            DummyClassifier(strategy="constant", constant=1, random_state=seed),
            "DummyClassifier_Constant1",
        ],
        [LogisticRegression(random_state=seed), "LogisticRegression"],
        [LinearDiscriminantAnalysis(), "LinearDiscriminantAnalysis"],
        [DecisionTreeClassifier(random_state=seed), "DecisionTreeClassifier"],
        [RandomForestClassifier(random_state=seed), "RandomForestClassifier"],
        [xgboost.XGBClassifier(random_state=seed), "XGBClassifier"],
        [CatBoostClassifier(random_state=seed, verbose=False), "CatBoostClassifier"],
        [LGBMClassifier(random_state=seed), "LGBMClassifier"],
        [LinearSVC(random_state=seed), "LinearSVC"],
        # [BernoulliNB(), "BernoulliNB"],
        # [ComplementNB(), "ComplementNB"],
        [KNeighborsClassifier(), "KNeighborsClassifier5"],
        [KNeighborsClassifier(n_neighbors=15), "KNeighborsClassifier15"],
        [
            VotingClassifier(
                estimators=[
                    ("lr", LogisticRegression(random_state=seed)),
                    ("lda", LinearDiscriminantAnalysis()),
                    ("dt", RandomForestClassifier(random_state=seed)),
                    ("xgb", xgboost.XGBClassifier(random_state=seed)),
                    ("catboost", CatBoostClassifier(random_state=seed, verbose=False)),
                ],
                voting="soft",
            ),
            "VotingClassifier",
        ],
    ]

    return models
