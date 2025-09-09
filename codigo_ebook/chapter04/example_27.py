# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 1049

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def pca_interpretacao(pca, loadings_df, n_componentes):
    """Interpreta os componentes principais"""
    # Interpretacao dos componentes
    print(f"\nINTERPRETACAO DOS COMPONENTES:")
    for i in range(n_componentes):
        print(f"i+1 (variancia explicada: {pca.explained_variance_ratio_[i]:.3f}):")

        # Variaveis com maior peso (positivo e negativo)
        pc_loadings = loadings_df[f'PC{i+1}'].abs().sort_values(ascending=False)
        print(f"  Variaveis mais importantes:")

        for var in pc_loadings.head(3).index:
            loading = loadings_df.loc[var, f'PC{i+1}']
            print(f"    {var}: {loading:.3f}")
