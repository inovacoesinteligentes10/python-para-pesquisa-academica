# Auto-correção aplicada
import numpy as np
import pandas as pd

def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Técnicas de Validação Cruzada
    # Linha original no arquivo LaTeX: 1077
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    #     def statistical_significance_test(self, model1_scores: np.ndarray,
    #                                     model2_scores: np.ndarray,
    #                                     alpha: float = 0.05) -> Dict:
    #         """Teste de significância estatística entre modelos"""
    #         from scipy import stats
    #         t_stat, p_value = stats.ttest_rel(model1_scores, model2_scores)
    #         wilcoxon_stat, wilcoxon_p = stats.wilcoxon(model1_scores, model2_scores)
    #             return {
    #             't_statistic': t_stat,
    #             't_test_p_value': p_value,
    #             't_test_significant': p_value < alpha,
    #             'wilcoxon_statistic': wilcoxon_stat,
    #             'wilcoxon_p_value': wilcoxon_p,
    #             'wilcoxon_significant': wilcoxon_p < alpha,
    #             'mean_difference': np.mean(model1_scores - model2_scores)
    #         }
    #     def bootstrap_confidence_interval(self, model, X: pd.DataFrame,
    #                                     y: pd.Series,
    #                                     n_bootstrap: int = 1000,
    #                                     confidence: float = 0.95) -> Dict:

# Executar exemplo
    if __name__ == '__main__':
    example_function()