# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 364

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def testes_multiplos_grupos(dados, grupo_col, variavel_dep):
    """Executa testes para multiplos grupos"""
    grupos = dados[grupo_col].unique()
    print(f"Comparando {len(grupos)} grupos: {list(grupos)}")

    # Extrair dados por grupo
    grupos_dados = [dados[dados[grupo_col] == g][variavel_dep]
                   for g in grupos]

    print(f"\nESTATISTICAS DESCRITIVAS:")
    print("-" * 25)
    for i, grupo in enumerate(grupos):
        subset = grupos_dados[i]
        print(f"{grupo}: N={len(subset)}, M={subset.mean():.3f}, DP={subset.std():.3f}")

    print(f"\nTESTES OMNIBUS:")
    print("-" * 15)

    # 1. ANOVA one-way
    f_stat, p_anova = f_oneway(*grupos_dados)
    print(f"1. ANOVA one-way:")
    print(f"   F = {f_stat:.3f}, p = {p_anova:.3f}")

    # 2. Kruskal-Wallis (nao-parametrico)
    h_stat, p_kruskal = kruskal(*grupos_dados)
    print(f"2. Kruskal-Wallis:")
    print(f"   H = {h_stat:.3f}, p = {p_kruskal:.3f}")

    # 3. ANOVA robusta (usando pingouin)
    dados_long = dados.copy()
    anova_robusta = pg.welch_anova(data=dados_long, dv=variavel_dep, between=grupo_col)
    print(f"3. ANOVA de Welch (robusta):")
    print(f"   F = {anova_robusta['F'].iloc[0]:.3f}")
    print(f"   p = {anova_robusta['p-unc'].iloc[0]:.3f}")

    return grupos_dados, p_anova, dados_long
