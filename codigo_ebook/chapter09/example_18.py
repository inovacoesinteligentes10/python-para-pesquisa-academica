# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Detecção de Mudanças Estruturais
Linha original no arquivo LaTeX: 324

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise estatística dos períodos
print("\nAnálise estatística por período:")
pontos_completos = [0] + pontos_mudanca + [len(df_academico)]

for i in range(len(pontos_completos)-1):
    inicio = pontos_completos[i]
    fim = pontos_completos[i+1]
    periodo_dados = df_academico.iloc[inicio:fim]['publicacoes']

    data_inicio = df_academico.index[inicio].strftime('%Y-%m')
    data_fim = df_academico.index[fim-1].strftime('%Y-%m')

    print(f"Período {i+1} ({data_inicio} a {data_fim}):")
    print(f"  Média: {periodo_dados.mean():.2f}")
    print(f"  Desvio padrão: {periodo_dados.std():.2f}")
    print(f"  Mediana: {periodo_dados.median():.2f}")
    print()
