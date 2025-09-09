# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1122

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

print(f"\nANÁLISE DE INCERTEZA:")
max_inc_idx = df_incerteza['amplitude_ic'].idxmax()
min_inc_idx = df_incerteza['amplitude_ic'].idxmin()
print(f"Período de maior incerteza: {meses_nomes[df_incerteza.loc[max_inc_idx, 'mes']-1]}")
print(f"Período de menor incerteza: {meses_nomes[df_incerteza.loc[min_inc_idx, 'mes']-1]}")
print(f"Incerteza média: +/-{df_incerteza['amplitude_ic'].mean()/2:.1f} publicações")

# Comparação com tendência histórica
crescimento_historico = df_academico.tail(12)['publicacoes'].sum()
crescimento_previsto = df_incerteza['previsao'].sum()
variacao_percentual = ((crescimento_previsto - crescimento_historico) / crescimento_historico) * 100

print(f"\nCOMPARAÇÃO COM PERÍODO ANTERIOR:")
print(f"Últimos 12 meses: {crescimento_historico:.0f} publicações")
print(f"Próximos 12 meses (previsto): {crescimento_previsto:.0f} publicações")
print(f"Variação esperada: {variacao_percentual:+.1f}%")
