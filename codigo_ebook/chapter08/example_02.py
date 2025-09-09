# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Tipos de Problemas e Algoritmos
Linha original no arquivo LaTeX: 187

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/academic_success_predictor.py
from ml_framework import ResearchMLFramework
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

class AcademicSuccessPredictor:
    """Preditor de sucesso acadêmico usando ML"""

    def __init__(self):
        self.ml_framework = ResearchMLFramework()
        self.models = {}

    def load_and_analyze_data(self, filepath: str) -> pd.DataFrame:
        """Carrega e analisa dados acadêmicos"""
        df = pd.read_csv(filepath)

        # Análise exploratória básica
        print("Análise Exploratória dos Dados:")
        print(f"Dimensões: {df.shape}")
        print(f"Valores faltantes: {df.isnull().sum().sum()}")
        print(f"Variáveis categóricas: {df.select_dtypes(include=['object']).columns.tolist()}")

        return df

    def create_success_variable(self, df: pd.DataFrame) -> pd.DataFrame:
        """Cria variável binária de sucesso acadêmico"""
        # Assumindo que temos uma coluna 'nota_final'
        df_processed = df.copy()

        # Definir sucesso como nota >= 7.0
        df_processed['sucesso_academico'] = (df_processed['nota_final'] >= 7.0).astype(int)

        return df_processed

    def train_models(self, df: pd.DataFrame) -> Dict:
        """Treina múltiplos modelos para comparação"""
        # Preparar dados
        X_train, X_test, y_train, y_test = self.ml_framework.prepare_data(
            df, 'sucesso_academico'
        )

        # Modelos a serem testados
        models_to_test = {
            'logistic_regression': LogisticRegression(random_state=42),
            'random_forest': RandomForestClassifier(random_state=42, n_estimators=100)
        }

        results = {}

        for name, model in models_to_test.items():
            # Treinar modelo
            model.fit(X_train, y_train)

            # Fazer predições
            y_pred = model.predict(X_test)

            # Avaliar performance
            report = classification_report(y_test, y_pred, output_dict=True)

            results[name] = {
                'model': model,
                'predictions': y_pred,
                'classification_report': report,
                'accuracy': report['accuracy']
            }

            print(f":")
            print(f"Acurácia: {report['accuracy']:.3f}")
            print(f"F1-Score: {report['macro avg']['f1-score']:.3f}")

        self.models = results
        return results
