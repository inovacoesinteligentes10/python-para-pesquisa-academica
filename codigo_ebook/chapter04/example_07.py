# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 264

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def testes_independentes(grupo1, grupo2):
    """Executa testes para amostras independentes"""
    # TESTES PARA AMOSTRAS INDEPENDENTES
    print(f"\nTESTES PARA AMOSTRAS INDEPENDENTES:")
    print("-" * 35)

    # 1. Teste t de Student (assume variancias iguais)
    t_stat, p_t = ttest_ind(grupo1, grupo2)
    print(f"1. Teste t de Student:")
    print(f"   t = {t_stat:.3f}, p = {p_t:.3f}")

    # 2. Teste t de Welch (nao assume variancias iguais)
    t_welch, p_welch = ttest_ind(grupo1, grupo2, equal_var=False)
    print(f"2. Teste t de Welch:")
    print(f"   t = {t_welch:.3f}, p = {p_welch:.3f}")

    # 3. Mann-Whitney U (nao-parametrico)
    u_stat, p_u = mannwhitneyu(grupo1, grupo2, alternative='two-sided')
    print(f"3. Mann-Whitney U:")
    print(f"   U = {u_stat:.3f}, p = {p_u:.3f}")

    # 4. Teste robusto (usando pingouin)
    resultado_robusto = pg.ttest(grupo1, grupo2, paired=False)
    print(f"4. Teste robusto (Yuen):")
    print(f"   T = {resultado_robusto['T'].iloc[0]:.3f}")
    print(f"   p = {resultado_robusto['p-val'].iloc[0]:.3f}")

    return t_stat
