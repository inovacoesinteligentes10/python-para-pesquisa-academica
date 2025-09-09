# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Seleção e Ajuste do Modelo ARIMA
Linha original no arquivo LaTeX: 457

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Dividindo os dados em treino e teste (80%-20%)
tamanho_treino = int(len(df_academico) * 0.8)
treino = df_academico['publicacoes'][:tamanho_treino]
teste = df_academico['publicacoes'][tamanho_treino:]

print(f"Período de treino: {treino.index[0]} a {treino.index[-1]}")
print(f"Período de teste: {teste.index[0]} a {teste.index[-1]}")

# Selecionando o melhor modelo
melhor_params, modelo_ajustado, melhor_aic = selecionar_arima(treino)

print(f"")
print(f"AIC: {melhor_aic:.2f}")
