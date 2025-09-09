# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Regressão Linear e Não-Linear
Linha original no arquivo LaTeX: 654

Este código foi extraído automaticamente do arquivo chapter8.tex
"""
import numpy as np
import pandas as pd


def feature_importance_regression(self, model,
                                    feature_names: List[str]) -> pd.DataFrame:
        """Analisa importância das features em regressão"""
        if hasattr(model, 'feature_importances_'):
            # Modelos baseados em árvores
            importances = model.feature_importances_
        elif hasattr(model, 'coef_'):
            # Modelos lineares
            importances = np.abs(model.coef_)
        else:
            print("Modelo não suporta análise de importância")
            return pd.DataFrame()

        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importances
        }).sort_values('importance', ascending=False)

        return importance_df

# Exemplo de uso
regression_toolkit = RegressionToolkit()

# Dados exemplo (substituir por dados reais)
X_train = pd.DataFrame(np.random.randn(1000, 5),
                      columns=['var1', 'var2', 'var3', 'var4', 'var5'])
y_train = pd.Series(2*X_train['var1'] + X_train['var2'] + np.random.randn(1000)*0.5)

# Comparar modelos de regressão
regression_comparison = regression_toolkit.compare_regression_models(X_train, y_train)
print("Comparação de Modelos de Regressão:")
print(regression_comparison[['algorithm', 'mean_r2', 'mean_rmse']])

# Avaliar melhor modelo
best_model_name = regression_comparison.iloc[0]['algorithm']
best_model = regression_toolkit.trained_models[best_model_name]

# Criar dados de teste
X_test = pd.DataFrame(np.random.randn(200, 5),
                     columns=['var1', 'var2', 'var3', 'var4', 'var5'])
y_test = pd.Series(2*X_test['var1'] + X_test['var2'] + np.random.randn(200)*0.5)

# Avaliação detalhada
evaluation = regression_toolkit.detailed_evaluation(best_model, X_test, y_test, best_model_name)
print(f":")
print(f"R2 Score: {evaluation['r2_score']:.4f}")
print(f"RMSE: {evaluation['rmse']:.4f}")
print(f"MAE: {evaluation['mae']:.4f}")
