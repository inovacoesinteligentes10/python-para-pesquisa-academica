# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 957

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

def analise_pca_completa(dados, n_componentes=None, padronizar=True):
    """
    Realiza PCA completa com interpretacao e visualizacao

    Parametros:
    -----------
    dados : DataFrame
        Dados numericos para PCA
    n_componentes : int, optional
        Numero de componentes a reter
    padronizar : bool
        Se deve padronizar as variaveis
    """

    print("ANALISE DE COMPONENTES PRINCIPAIS")
    print("=" * 35)

    # Preparar dados
    if padronizar:
        scaler = StandardScaler()
        dados_scaled = scaler.fit_transform(dados)
        print("Dados padronizados (media=0, dp=1)")
    else:
        dados_scaled = dados.values
        print("Dados originais (sem padronizacao)")

    # PCA inicial para ver todas as componentes
    pca_completo = PCA()
    pca_completo.fit(dados_scaled)

    # Variancia explicada
    var_explicada = pca_completo.explained_variance_ratio_
    var_cumulativa = np.cumsum(var_explicada)

    print(f"\nVariancia explicada por componente:")
    for i, var in enumerate(var_explicada[:min(10, len(var_explicada))]):
        print(f"  PC{i+1}: {var:.3f} ({var*100:.1f}%)")

    return dados_scaled, pca_completo, var_explicada, var_cumulativa
