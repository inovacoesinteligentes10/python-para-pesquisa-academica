# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Verificação de Pressupostos
Linha original no arquivo LaTeX: 52

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def testar_normalidade(dados, grupo_col, variavel_dependente):
    """Testa normalidade dos dados"""
    # 1. TESTE DE NORMALIDADE
    print("1. TESTE DE NORMALIDADE")
    print("-" * 25)

    if grupo_col:
        # Testar normalidade por grupo
        grupos = dados[grupo_col].unique()
        for grupo in grupos:
            subset = dados[dados[grupo_col] == grupo][variavel_dependente]

            # Shapiro-Wilk (melhor para n < 50)
            if len(subset) < 50:
                stat_sw, p_sw = stats.shapiro(subset)
                teste_usado = "Shapiro-Wilk"
                stat_final, p_final = stat_sw, p_sw
            else:
                # Lilliefors (modificacao do KS para normalidade)
                stat_lf, p_lf = lilliefors(subset)
                teste_usado = "Lilliefors"
                stat_final, p_final = stat_lf, p_lf

            print(f"   {grupo}: {teste_usado}")
            print(f"     Estatistica: {stat_final:.4f}")
            print(f"     p-valor: {p_final:.4f}")
            print(f"     Normal: {'Sim' if p_final > 0.05 else 'Nao'}")
    else:
        # Teste geral de normalidade
        if len(dados[variavel_dependente]) < 50:
            stat, p = stats.shapiro(dados[variavel_dependente])
            teste = "Shapiro-Wilk"
        else:
            stat, p = lilliefors(dados[variavel_dependente])
            teste = "Lilliefors"

        print(f"   {teste}: estatistica = {stat:.4f}, p = {p:.4f}")
        print(f"   Distribuicao normal: {'Sim' if p > 0.05 else 'Nao'}")
        p_final = p

    return p_final
