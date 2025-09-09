# Auto-correção aplicada
import numpy as np
import pandas as pd

def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Regressão Linear e Não-Linear
    # Linha original no arquivo LaTeX: 548
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    #                 mse_scores = -cross_val_score(
    #                     model, X_train, y_train,
    #                     cv=5, scoring='neg_mean_squared_error'
    #                 )
    #                 results.append({
    #                     'algorithm': name,
    #                     'mean_r2': r2_scores.mean(),
    #                     'std_r2': r2_scores.std(),
    #                     'mean_mse': mse_scores.mean(),
    #                     'std_mse': mse_scores.std(),
    #                     'mean_rmse': np.sqrt(mse_scores.mean())
    #                 })
    #                 model.fit(X_train, y_train)
    #                 self.trained_models[name] = model
    #                 except Exception as e:
    #                 print(f"Erro ao treinar {name}: {e}")
    #                 continue
    #         results_df = pd.DataFrame(results)
    #         results_df = results_df.sort_values('mean_r2', ascending=False)
    # result = results_df
    #     def detailed_evaluation(self, model, X_test: pd.DataFrame,
    #                             y_test: pd.Series, model_name: str) -> Dict:
    #         """Avaliação detalhada de modelo de regressão"""
    #         y_pred = model.predict(X_test)
    #         r2 = r2_score(y_test, y_pred)
    #         mse = mean_squared_error(y_test, y_pred)
    #         rmse = np.sqrt(mse)
    #         mae = mean_absolute_error(y_test, y_pred)
    #         mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    #             return {
    #             'model_name': model_name,
    #             'r2_score': r2,
    #             'mse': mse,
    #             'rmse': rmse,
    #             'mae': mae,
    #             'mape': mape,
    #             'predictions': y_pred,
    #             'residuals': y_test - y_pred
    #         }

# Executar exemplo
    if __name__ == '__main__':
    example_function()