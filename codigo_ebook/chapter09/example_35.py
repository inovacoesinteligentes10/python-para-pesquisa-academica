# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Identificação de Padrões Sazonais
Linha original no arquivo LaTeX: 657

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Teste estatístico de sazonalidade
from scipy.stats import kruskal

# Teste de Kruskal-Wallis para sazonalidade mensal
grupos_mensais = [df_academico[df_academico.index.month == m]['publicacoes'].values
                  for m in range(1, 13)]
stat_kruskal, p_valor = kruskal(*grupos_mensais)

print(f"Teste de Kruskal-Wallis para Sazonalidade Mensal:")
print(f"Estatística: {stat_kruskal:.4f}")
print(f"p-valor: {p_valor:.6f}")

if p_valor < 0.05:
    print("Resultado: Há evidência significativa de sazonalidade mensal")
else:
    print("Resultado: Não há evidência significativa de sazonalidade mensal")
