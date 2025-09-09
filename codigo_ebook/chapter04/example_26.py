# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 1007

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
import pandas as pd


def pca_selecao_componentes(dados, dados_scaled, var_explicada, var_cumulativa, n_componentes=None):
    """Seleciona numero ideal de componentes e executa PCA final"""
    # Determinar numero ideal de componentes
    if n_componentes is None:
        # Criterio de Kaiser (eigenvalues > 1)
        eigenvalues = pca_completo.explained_variance_
        n_kaiser = np.sum(eigenvalues > 1)

        # Criterio de 95% da variancia
        n_95 = np.argmax(var_cumulativa >= 0.95) + 1

        print(f"\nCriterios para selecao de componentes:")
        print(f"  Kaiser (eigenvalue > 1): {n_kaiser} componentes")
        print(f"  95% da variancia: {n_95} componentes")

        n_componentes = min(n_kaiser, n_95)
        print(f"  Recomendado: {n_componentes} componentes")

    # PCA final com numero escolhido
    pca = PCA(n_components=n_componentes)
    dados_pca = pca.fit_transform(dados_scaled)

    print(f" componentes:")
    print(f"Variancia total explicada: {pca.explained_variance_ratio_.sum():.3f} ({pca.explained_variance_ratio_.sum()*100:.1f}%)")

    # Loadings (pesos das variaveis originais)
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    loadings_df = pd.DataFrame(loadings,
                              index=dados.columns,
                              columns=[f'PC{i+1}' for i in range(n_componentes)])

    print(f"\nLoadings das variaveis:")
    print(loadings_df.round(3))

    return pca, dados_pca, loadings_df, n_componentes
