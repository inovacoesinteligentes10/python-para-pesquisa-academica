# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Testes de Permutação
Linha original no arquivo LaTeX: 925

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np


# Exemplo de uso
np.random.seed(42)
controle = np.random.normal(50, 10, 25)
tratamento = np.random.normal(58, 12, 30)

print("EXEMPLO: COMPARACAO DE MEDIAS")
stat_obs, dados_comb, n1, n2 = teste_permutacao(controle, tratamento)
def diff_medias_func(g1, g2): return np.mean(g1) - np.mean(g2)
stats_perm, p_val = permutacao_distribuicao_nula(stat_obs, dados_comb, n1, n2, diff_medias_func)
permutacao_visualizacao(stat_obs, stats_perm)

# Exemplo com estatistica customizada (diferenca de medianas)
def diff_medianas(g1, g2):
    return np.median(g1) - np.median(g2)

print("\nEXEMPLO: COMPARACAO DE MEDIANAS")
stat_obs_med, dados_comb_med, n1_med, n2_med = teste_permutacao(controle, tratamento)
stats_perm_med, p_val_med = permutacao_distribuicao_nula(stat_obs_med, dados_comb_med, n1_med, n2_med, diff_medianas)
permutacao_visualizacao(stat_obs_med, stats_perm_med)
