# Auto-correção aplicada
def example_function():
    """Código do exemplo"""
    pass
    # import pandas as pd
    # import numpy as np
    # from typing import List, Dict, Optional
    # class ExampleClass:
    #     def __init__(self):
    #         pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Regressão Linear e Não-Linear
    # Linha original no arquivo LaTeX: 607
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    #     def plot_regression_diagnostics(self, evaluation_results: Dict):
    #         """Cria gráficos de diagnóstico para regressão"""
    #         y_true = evaluation_results['predictions'] + evaluation_results['residuals']
    #         y_pred = evaluation_results['predictions']
    #         residuals = evaluation_results['residuals']
    #         fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    #         axes[0,0].scatter(y_true, y_pred, alpha=0.6)
    #         axes[0,0].plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
    #         axes[0,0].set_xlabel('Valores Reais')
    #         axes[0,0].set_ylabel('Valores Preditos')
    #         axes[0,0].set_title('Predições vs Valores Reais')
    #         axes[0,1].scatter(y_pred, residuals, alpha=0.6)
    #         axes[0,1].axhline(y=0, color='r', linestyle='--')
    #         axes[0,1].set_xlabel('Valores Preditos')
    #         axes[0,1].set_ylabel('Resíduos')
    #         axes[0,1].set_title('Resíduos vs Valores Preditos')
    #         axes[1,0].hist(residuals, bins=30, alpha=0.7, color='skyblue')
    #         axes[1,0].set_xlabel('Resíduos')
    #         axes[1,0].set_ylabel('Frequência')
    #         axes[1,0].set_title('Distribuição dos Resíduos')
    #         from scipy import stats
    #         stats.probplot(residuals, dist="norm", plot=axes[1,1])
    #         axes[1,1].set_title('Q-Q Plot dos Resíduos')
    #         plt.tight_layout()
    #         plt.show()
    #         print(f"Estatísticas dos Resíduos:")
    #         print(f"Média: {residuals.mean():.4f}")
    #         print(f"Desvio Padrão: {residuals.std():.4f}")
    #         print(f"Teste de Normalidade (Shapiro-Wilk): {stats.shapiro(residuals)[1]:.4f}")

# Executar exemplo
if __name__ == '__main__':
    example_function()