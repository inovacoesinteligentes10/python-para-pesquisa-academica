# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Tipos de Problemas e Algoritmos
Linha original no arquivo LaTeX: 16

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/ml_framework.py
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

class ResearchMLFramework:
    """Framework para aplicação de ML em pesquisa acadêmica"""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.models = {}
        self.results = {}
        self.preprocessors = {}

    def identify_problem_type(self, target: pd.Series) -> str:
        """Identifica automaticamente o tipo de problema ML"""
        # Verificar se é variável categórica
        if target.dtype == 'object' or target.nunique() < 10:
            unique_values = target.nunique()
            if unique_values == 2:
                return 'binary_classification'
            elif unique_values <= 10:
                return 'multiclass_classification'
            else:
                return 'regression'

        # Verificar se é contínua
        elif np.issubdtype(target.dtype, np.number):
            # Se muitos valores únicos, provavelmente regressão
            if target.nunique() > target.count() * 0.1:
                return 'regression'
            else:
                return 'multiclass_classification'

        return 'regression'  # fallback

    def recommend_algorithms(self, problem_type: str,
                           dataset_size: int) -> List[str]:
        """Recomenda algoritmos baseado no tipo de problema"""
        recommendations = {
            'binary_classification': {
                'small': ['logistic_regression', 'svm', 'naive_bayes'],
                'medium': ['random_forest', 'gradient_boosting', 'svm'],
                'large': ['logistic_regression', 'gradient_boosting', 'neural_network']
            },
            'multiclass_classification': {
                'small': ['random_forest', 'svm', 'knn'],
                'medium': ['random_forest', 'gradient_boosting', 'svm'],
                'large': ['gradient_boosting', 'neural_network', 'random_forest']
            },
            'regression': {
                'small': ['linear_regression', 'random_forest', 'svm'],
                'medium': ['random_forest', 'gradient_boosting', 'svm'],
                'large': ['gradient_boosting', 'neural_network', 'linear_regression']
            }
        }

        # Classificar tamanho do dataset
        if dataset_size < 1000:
            size_category = 'small'
        elif dataset_size < 10000:
            size_category = 'medium'
        else:
            size_category = 'large'

        return recommendations.get(problem_type, {}).get(size_category, ['random_forest'])

    def prepare_data(self, df: pd.DataFrame,
                    target_column: str,
                    test_size: float = 0.2) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Prepara dados para machine learning"""

        # Separar features e target
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # Tratar valores faltantes
        X = self._handle_missing_values(X)

        # Codificar variáveis categóricas
        X = self._encode_categorical_variables(X)

        # Dividir em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state,
            stratify=y if self.identify_problem_type(y) != 'regression' else None
        )

        # Escalar features numéricas
        X_train, X_test = self._scale_features(X_train, X_test)

        return X_train, X_test, y_train, y_test

    def _handle_missing_values(self, X: pd.DataFrame) -> pd.DataFrame:
        """Trata valores faltantes"""
        X_processed = X.copy()

        for column in X_processed.columns:
            if X_processed[column].isnull().any():
                if X_processed[column].dtype == 'object':
                    # Variáveis categóricas: usar moda
                    mode_value = X_processed[column].mode()[0] if len(X_processed[column].mode()) > 0 else 'Unknown'
                    X_processed[column].fillna(mode_value, inplace=True)
                else:
                    # Variáveis numéricas: usar mediana
                    median_value = X_processed[column].median()
                    X_processed[column].fillna(median_value, inplace=True)

        return X_processed

    def _encode_categorical_variables(self, X: pd.DataFrame) -> pd.DataFrame:
        """Codifica variáveis categóricas"""
        X_processed = X.copy()

        for column in X_processed.columns:
            if X_processed[column].dtype == 'object':
                # Para variáveis com muitas categorias, usar target encoding
                if X_processed[column].nunique() > 10:
                    # Por simplicidade, usar label encoding
                    le = LabelEncoder()
                    X_processed[column] = le.fit_transform(X_processed[column].astype(str))
                    self.preprocessors[f'{column}_encoder'] = le
                else:
                    # Para poucas categorias, usar one-hot encoding
                    dummies = pd.get_dummies(X_processed[column], prefix=column)
                    X_processed = pd.concat([X_processed.drop(column, axis=1), dummies], axis=1)

        return X_processed

    def _scale_features(self, X_train: pd.DataFrame,
                       X_test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Escala features numéricas"""
        scaler = StandardScaler()

        # Identificar colunas numéricas
        numeric_columns = X_train.select_dtypes(include=[np.number]).columns

        if len(numeric_columns) > 0:
            X_train_scaled = X_train.copy()
            X_test_scaled = X_test.copy()

            X_train_scaled[numeric_columns] = scaler.fit_transform(X_train[numeric_columns])
            X_test_scaled[numeric_columns] = scaler.transform(X_test[numeric_columns])

            self.preprocessors['scaler'] = scaler

            return X_train_scaled, X_test_scaled

        return X_train, X_test
