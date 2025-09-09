# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: DataFrames: Planilhas Inteligentes
Linha original no arquivo LaTeX: 196

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

import pandas as pd
import numpy as np

# Criar DataFrame a partir de dicionario
dados_participantes = {
    'id': range(1, 101),
    'idade': np.random.randint(18, 65, 100),
    'genero': np.random.choice(['M', 'F'], 100),
    'grupo': np.random.choice(['controle', 'tratamento'], 100),
    'pre_teste': np.random.normal(50, 10, 100),
    'pos_teste': np.random.normal(55, 12, 100),
    'satisfacao': np.random.randint(1, 11, 100)
}

df = pd.DataFrame(dados_participantes)

# Exploracao inicial
print("Informacoes basicas:")
print(df.info())
print(f"")
print(f"\nPrimeiras 5 linhas:")
print(df.head())

print(f"\nEstatisticas descritivas:")
print(df.describe())

# Verificar valores ausentes
print(f"\nValores ausentes por coluna:")
print(df.isnull().sum())
