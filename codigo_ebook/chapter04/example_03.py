# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Verificação de Pressupostos
Linha original no arquivo LaTeX: 100

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
from scipy import stats


def testar_homogeneidade(dados, grupo_col, variavel_dependente):
    """Testa homogeneidade de variancias"""
    p_levene = None
    if grupo_col:
        print(f"\n2. HOMOGENEIDADE DE VARIANCIAS")
        print("-" * 30)

        # Levene's test (robusto a desvios da normalidade)
        grupos_dados = [dados[dados[grupo_col] == g][variavel_dependente]
                       for g in dados[grupo_col].unique()]

        stat_levene, p_levene = stats.levene(*grupos_dados)
        print(f"   Teste de Levene:")
        print(f"     Estatistica: {stat_levene:.4f}")
        print(f"     p-valor: {p_levene:.4f}")
        print(f"     Variancias homogeneas: {'Sim' if p_levene > 0.05 else 'Nao'}")

        # Bartlett (mais sensivel, assume normalidade)
        stat_bartlett, p_bartlett = stats.bartlett(*grupos_dados)
        print(f"   Teste de Bartlett:")
        print(f"     Estatistica: {stat_bartlett:.4f}")
        print(f"     p-valor: {p_bartlett:.4f}")
        print(f"     Variancias homogeneas: {'Sim' if p_bartlett > 0.05 else 'Nao'}")

    return p_levene
