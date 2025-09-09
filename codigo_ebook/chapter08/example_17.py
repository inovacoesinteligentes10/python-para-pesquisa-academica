# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Técnicas de Validação Cruzada
Linha original no arquivo LaTeX: 946

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/model_validation.py
import pandas as pd
import numpy as np
from sklearn.model_selection import (
    cross_val_score, StratifiedKFold, TimeSeriesSplit,
    validation_curve, learning_curve
)
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple

class ModelValidation:
    """Classe para validação rigorosa de modelos ML"""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def comprehensive_cross_validation(self, model, X: pd.DataFrame,
                                     y: pd.Series,
                                     problem_type: str = 'classification') -> Dict:
        """Validação cruzada abrangente"""
        results = {}

        # Escolher estratégia de validação
        if problem_type == 'classification':
            cv_strategy = StratifiedKFold(n_splits=5, shuffle=True,
                                        random_state=self.random_state)
            scoring_metrics = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
        else:  # regression
            cv_strategy = 5  # KFold padrão
            scoring_metrics = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']

        # Calcular métricas
        for metric in scoring_metrics:
            scores = cross_val_score(model, X, y, cv=cv_strategy, scoring=metric)
            results[metric] = {
                'scores': scores,
                'mean': scores.mean(),
                'std': scores.std(),
                'ci_95': (scores.mean() - 1.96*scores.std(),
                         scores.mean() + 1.96*scores.std())
            }

        return results
