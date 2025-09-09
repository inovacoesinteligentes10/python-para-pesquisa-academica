# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Bootstrap: Estimando Distribuições
Linha original no arquivo LaTeX: 653

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np


from sklearn.utils import resample

def bootstrap_analise(dados, estatistica_func, n_bootstrap=10000, alpha=0.05):
    """
    Realiza analise bootstrap para qualquer estatistica

    Parametros:
    -----------
    dados : array-like
        Dados originais
    estatistica_func : function
        Funcao que calcula a estatistica de interesse
    n_bootstrap : int
        Numero de amostras bootstrap
    alpha : float
        Nivel de significancia para IC
    """

    print("ANALISE BOOTSTRAP")
    print("="*20)

    # Estatistica original
    stat_original = estatistica_func(dados)
    print(f"Estatistica original: {stat_original:.4f}")

    # Gerar amostras bootstrap
    bootstrap_stats = []

    for i in range(n_bootstrap):
        # Reamostragem com reposicao
        amostra_boot = resample(dados, n_samples=len(dados), replace=True)
        stat_boot = estatistica_func(amostra_boot)
        bootstrap_stats.append(stat_boot)

    bootstrap_stats = np.array(bootstrap_stats)

    return stat_original, bootstrap_stats
