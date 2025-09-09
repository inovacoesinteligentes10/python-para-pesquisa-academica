# Auto-correção aplicada
import numpy as np
import pandas as pd

def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Classificação Binária e Multiclasse
    # Linha original no arquivo LaTeX: 395
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    #     def evaluate_model(self, model, X_test: pd.DataFrame,
    #                         y_test: pd.Series) -> Dict:
    #         """Avalia performance detalhada do modelo"""
    #         y_pred = model.predict(X_test)
    #         accuracy = accuracy_score(y_test, y_pred)
    #         precision, recall, f1, support = precision_recall_fscore_support(
    #             y_test, y_pred, average='weighted'
    #         )
    #         precision_per_class, recall_per_class, f1_per_class, _ = \
    #             precision_recall_fscore_support(y_test, y_pred, average=None)
    #         from sklearn.metrics import confusion_matrix
    #         cm = confusion_matrix(y_test, y_pred)
    #             return {
    #             'accuracy': accuracy,
    #             'precision': precision,
    #             'recall': recall,
    #             'f1_score': f1,
    #             'precision_per_class': precision_per_class,
    #             'recall_per_class': recall_per_class,
    #             'f1_per_class': f1_per_class,
    #             'confusion_matrix': cm,
    #             'predictions': y_pred
    #         }
    #     def feature_importance_analysis(self, model,
    #                                     feature_names: List[str]) -> pd.DataFrame:
    #         """Analisa importância das features"""
    #             if hasattr(model, 'feature_importances_'):
    #             importances = model.feature_importances_
    #         elif hasattr(model, 'coef_'):
    #             importances = np.abs(model.coef_[0] if len(model.coef_.shape) > 1 else model.coef_)
    #         else:
    #             print("Modelo não suporta análise de importância")
    #                 return pd.DataFrame()

# Executar exemplo
    if __name__ == '__main__':
    example_function()