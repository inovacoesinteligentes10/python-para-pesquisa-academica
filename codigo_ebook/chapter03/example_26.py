# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 822

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

def pipeline_relatorio_final(dados_limpos, controle, experimental, t_stat, p_valor, d):
    # 5. RELATÓRIO FINAL
    print("\n5. RELATÓRIO FINAL")
    print("="*30)
    print(f"Amostra final: N = {len(dados_limpos)}")
    print(f"Melhoria Controle: M = {controle.mean():.2f}, DP = {controle.std():.2f}")
    print(f"Melhoria Experimental: M = {experimental.mean():.2f}, DP = {experimental.std():.2f}")
    print(f"Teste t: t({len(dados_limpos)-2}) = {t_stat:.3f}, p = {p_valor:.3f}")
    print(f"Tamanho do efeito: d = {d:.3f}")

    if p_valor < 0.05:
        significancia = "significativa"
    else:
        significancia = "não significativa"

    if abs(d) < 0.2:
        interpretacao_d = "trivial"
    elif abs(d) < 0.5:
        interpretacao_d = "pequeno"
    elif abs(d) < 0.8:
        interpretacao_d = "médio"
    else:
        interpretacao_d = "grande"

    print(f" com efeito {interpretacao_d}")

    return dados_limpos

# Executar pipeline completo
dados_brutos = pipeline_completo_pesquisa()
dados_limpos, resultados = pipeline_limpeza_analise(dados_brutos)
controle, experimental, t_stat, p_valor, d = pipeline_testes_estatisticos(dados_limpos)
fig, ax1, ax2, ax3, ax4 = pipeline_visualizacoes_1_2(dados_limpos, controle, experimental)
pipeline_visualizacoes_3_4(dados_limpos, ax3, ax4)
dados_finais = pipeline_relatorio_final(dados_limpos, controle, experimental, t_stat, p_valor, d)
