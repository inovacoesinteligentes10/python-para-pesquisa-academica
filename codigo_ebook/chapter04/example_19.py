# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Bootstrap: Estimando Distribuições
Linha original no arquivo LaTeX: 744

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

# Exemplos de uso do bootstrap
np.random.seed(123)
dados_assimetricos = np.random.exponential(2, 100)  # Dados nao-normais

print("EXEMPLO 1: MEDIA DE DISTRIBUICAO ASSIMETRICA")
print("=" * 45)
stat_orig, boot_stats = bootstrap_analise(dados_assimetricos, np.mean)
bias, erro_padrao, ci_lower, ci_upper = bootstrap_intervalos_viz(stat_orig, boot_stats)

print("\nEXEMPLO 2: CORRELACAO")
print("=" * 20)
# Dados bivariados
x = np.random.normal(0, 1, 50)
y = 0.7*x + np.random.normal(0, 0.5, 50)
dados_correlacao = np.column_stack([x, y])

def correlacao_func(dados):
    return np.corrcoef(dados[:, 0], dados[:, 1])[0, 1]

stat_orig_corr, boot_stats_corr = bootstrap_analise(dados_correlacao, correlacao_func)
bias_corr, erro_padrao_corr, ci_lower_corr, ci_upper_corr = bootstrap_intervalos_viz(stat_orig_corr, boot_stats_corr)
