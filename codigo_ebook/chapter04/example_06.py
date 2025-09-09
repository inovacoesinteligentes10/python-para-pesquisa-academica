# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 229

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

from scipy.stats import ttest_ind, mannwhitneyu, welch_ttest
from scipy.stats import ttest_rel, wilcoxon
from scipy.stats import f_oneway, kruskal
import pingouin as pg

def bateria_testes_comparacao(dados, grupo_col, variavel_dep, pareado=False):
    """
    Executa bateria completa de testes de comparacao entre grupos
    """

    print("BATERIA DE TESTES DE COMPARACAO")
    print("="*40)

    grupos = dados[grupo_col].unique()

    if len(grupos) == 2:
        # DOIS GRUPOS
        grupo1 = dados[dados[grupo_col] == grupos[0]][variavel_dep]
        grupo2 = dados[dados[grupo_col] == grupos[1]][variavel_dep]

        print(f"Comparando: {grupos[0]} vs {grupos[1]}")
        print(f"N1 = {len(grupo1)}, N2 = {len(grupo2)}")
        print(f"M1 = {grupo1.mean():.3f}, M2 = {grupo2.mean():.3f}")
        print(f"DP1 = {grupo1.std():.3f}, DP2 = {grupo2.std():.3f}")

        return grupo1, grupo2, grupos

    return None, None, grupos
