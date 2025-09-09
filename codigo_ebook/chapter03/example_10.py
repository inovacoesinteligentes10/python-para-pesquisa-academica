# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Limpeza e Transformação de Dados
Linha original no arquivo LaTeX: 305

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import pandas as pd


# Simular dados com problemas comuns
np.random.seed(42)
dados_sujos = pd.DataFrame({
    'participante_id': range(1, 201),
    'idade': np.random.randint(16, 80, 200),
    'score': np.random.normal(75, 15, 200),
    'grupo': np.random.choice(['A', 'B', 'C'], 200),
    'data_coleta': pd.date_range('2024-01-01', periods=200, freq='D')
})

# Introduzir problemas nos dados
# 1. Valores ausentes
indices_na = np.random.choice(200, 20, replace=False)
dados_sujos.loc[indices_na, 'score'] = np.nan

# 2. Outliers extremos
indices_outliers = np.random.choice(200, 5, replace=False)
dados_sujos.loc[indices_outliers, 'score'] = [200, -50, 300, -100, 250]

# 3. Idades impossíveis
dados_sujos.loc[190:195, 'idade'] = [150, 5, 200, 0, -10]

print("Dados antes da limpeza:")
print(f"Valores ausentes: {dados_sujos.isnull().sum().sum()}")
print(f"Forma: {dados_sujos.shape}")
print(f"\nEstatísticas do score:")
print(dados_sujos['score'].describe())
