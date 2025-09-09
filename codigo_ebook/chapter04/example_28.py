# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 1070

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import matplotlib.pyplot as plt


def pca_visualizacoes(dados, pca, dados_pca, loadings_df, var_explicada, var_cumulativa, n_componentes):
    """Cria visualizacoes do PCA"""
    # Visualizacoes
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Scree plot
    axes[0,0].plot(range(1, len(var_explicada[:10])+1), var_explicada[:10], 'bo-')
    axes[0,0].axhline(y=1/len(dados.columns), color='r', linestyle='--',
                     label='Media da variancia')
    axes[0,0].set_xlabel('Componente')
    axes[0,0].set_ylabel('Variancia Explicada')
    axes[0,0].set_title('Scree Plot')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)

    # 2. Variancia cumulativa
    axes[0,1].plot(range(1, len(var_cumulativa[:10])+1), var_cumulativa[:10], 'go-')
    axes[0,1].axhline(y=0.95, color='r', linestyle='--', label='95%')
    axes[0,1].set_xlabel('Numero de Componentes')
    axes[0,1].set_ylabel('Variancia Cumulativa')
    axes[0,1].set_title('Variancia Cumulativa Explicada')
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)

    return axes
