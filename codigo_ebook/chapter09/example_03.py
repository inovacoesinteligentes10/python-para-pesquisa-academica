# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Características dos Dados Temporais
Linha original no arquivo LaTeX: 47

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import pandas as pd


# Criando DataFrame
df_clima = pd.DataFrame({
    'data': datas,
    'temperatura': temperatura
})

print("Estrutura dos dados temporais:")
print(df_clima.head())
print(f"Período: {df_clima['data'].min()} a {df_clima['data'].max()}")
print(f"Número de observações: {len(df_clima)}")
