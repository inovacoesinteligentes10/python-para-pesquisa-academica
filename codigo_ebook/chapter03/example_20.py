# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Visualizações Avançadas para Pesquisa
Linha original no arquivo LaTeX: 633

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# Relatório estatístico
print("RELATÓRIO DE ANÁLISE MULTIVARIADA")
print("="*50)
print(f"N = {len(dados_pesquisa)} participantes")
print(f"\nCorrelações mais fortes:")
correlacoes_abs = correlacoes.abs()
np.fill_diagonal(correlacoes_abs.values, 0)
maior_corr = correlacoes_abs.stack().nlargest(3)
for i, (vars, corr) in enumerate(maior_corr.items(), 1):
    print(f"{i}. {vars[0]} vs {vars[1]}: r = {correlacoes.loc[vars[0], vars[1]]:.3f}")
