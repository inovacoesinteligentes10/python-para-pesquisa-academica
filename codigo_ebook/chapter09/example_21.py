# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Fundamentos dos Modelos ARIMA
Linha original no arquivo LaTeX: 383

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Testando estacionariedade da série original
teste_estacionariedade(df_academico['publicacoes'], 'Original')

# Aplicando diferenciação se necessário
df_academico['pub_diff1'] = df_academico['publicacoes'].diff()
teste_estacionariedade(df_academico['pub_diff1'], 'Primeira Diferença')
