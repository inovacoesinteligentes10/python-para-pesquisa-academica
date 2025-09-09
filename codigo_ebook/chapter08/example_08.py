# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Regressão Linear e Não-Linear
Linha original no arquivo LaTeX: 502

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/regression_toolkit.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

class RegressionToolkit:
    """Toolkit para problemas de regressão em pesquisa"""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.models = self._initialize_models()
        self.trained_models = {}

    def _initialize_models(self) -> Dict:
        """Inicializa modelos de regressão"""
        return {
            'linear_regression': LinearRegression(),
            'ridge_regression': Ridge(random_state=self.random_state),
            'lasso_regression': Lasso(random_state=self.random_state),
            'elastic_net': ElasticNet(random_state=self.random_state),
            'random_forest': RandomForestRegressor(random_state=self.random_state),
            'gradient_boosting': GradientBoostingRegressor(random_state=self.random_state),
            'svr': SVR()
        }

    def compare_regression_models(self, X_train: pd.DataFrame,
                                 y_train: pd.Series) -> pd.DataFrame:
        """Compara diferentes modelos de regressão"""
        results = []

        for name, model in self.models.items():
            try:
                # Validação cruzada para R2
                r2_scores = cross_val_score(
                    model, X_train, y_train,
                    cv=5, scoring='r2'
                )

            except Exception as e:

                print(f'Erro: {e}')

                return None
