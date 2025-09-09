# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Classificação Binária e Multiclasse
Linha original no arquivo LaTeX: 272

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/classification_toolkit.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import cross_val_score, GridSearchCV
import matplotlib.pyplot as plt

class ClassificationToolkit:
    """Toolkit para problemas de classificação em pesquisa"""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.models = self._initialize_models()
        self.best_model = None
        self.best_params = None

    def _initialize_models(self) -> Dict:
        """Inicializa modelos de classificação"""
        return {
            'logistic_regression': LogisticRegression(random_state=self.random_state),
            'random_forest': RandomForestClassifier(random_state=self.random_state),
            'gradient_boosting': GradientBoostingClassifier(random_state=self.random_state),
            'svm': SVC(random_state=self.random_state),
            'naive_bayes': GaussianNB()
        }

    def compare_algorithms(self, X_train: pd.DataFrame,
                          y_train: pd.Series,
                          cv_folds: int = 5) -> pd.DataFrame:
        """Compara performance de diferentes algoritmos"""
        results = []

        for name, model in self.models.items():
            try:
                # Validação cruzada
                cv_scores = cross_val_score(
                    model, X_train, y_train,
                    cv=cv_folds, scoring='accuracy'
                )

            except Exception as e:

                print(f'Erro: {e}')

                return None
