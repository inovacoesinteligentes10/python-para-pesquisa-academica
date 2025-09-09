# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 299

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def testes_pareados(grupo1, grupo2):
    """Executa testes para amostras pareadas"""
    # TESTES PARA AMOSTRAS PAREADAS
    print(f"\nTESTES PARA AMOSTRAS PAREADAS:")
    print("-" * 30)

    # 1. Teste t pareado
    t_paired, p_paired = ttest_rel(grupo1, grupo2)
    print(f"1. Teste t pareado:")
    print(f"   t = {t_paired:.3f}, p = {p_paired:.3f}")

    # 2. Wilcoxon signed-rank
    w_stat, p_w = wilcoxon(grupo1, grupo2)
    print(f"2. Wilcoxon signed-rank:")
    print(f"   W = {w_stat:.3f}, p = {p_w:.3f}")

    return t_paired
