# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Fundamentos do Plotly
Linha original no arquivo LaTeX: 28

Este código foi extraído automaticamente do arquivo chapter10.tex
"""
import numpy as np
import pandas as pd


# Configuração para exibição em notebooks
pyo.init_notebook_mode(connected=True)

# Criando dados de exemplo para pesquisa em ciências sociais
np.random.seed(42)
n_participantes = 500

# Simulando dados de um estudo sobre bem-estar e produtividade
dados_estudo = pd.DataFrame({
    'participante_id': range(1, n_participantes + 1),
    'idade': np.random.normal(35, 12, n_participantes).astype(int),
    'bem_estar': np.random.normal(7, 1.5, n_participantes),
    'produtividade': np.random.normal(75, 15, n_participantes),
    'horas_trabalho': np.random.normal(8, 2, n_participantes),
    'satisfacao_trabalho': np.random.normal(6.5, 1.8, n_participantes),
    'area': np.random.choice(['Tecnologia', 'Educação', 'Saúde', 'Finanças'], n_participantes),
    'experiencia': np.random.randint(1, 20, n_participantes)
})

# Adicionando correlações realistas
dados_estudo['produtividade'] += dados_estudo['bem_estar'] * 3 + np.random.normal(0, 5, n_participantes)
dados_estudo['satisfacao_trabalho'] += dados_estudo['bem_estar'] * 0.3 + np.random.normal(0, 0.5, n_participantes)

# Limitando valores aos ranges apropriados
dados_estudo['bem_estar'] = np.clip(dados_estudo['bem_estar'], 1, 10)
dados_estudo['satisfacao_trabalho'] = np.clip(dados_estudo['satisfacao_trabalho'], 1, 10)
dados_estudo['produtividade'] = np.clip(dados_estudo['produtividade'], 30, 100)
dados_estudo['horas_trabalho'] = np.clip(dados_estudo['horas_trabalho'], 4, 12)

print("Dataset criado com sucesso!")
print(dados_estudo.head())
print(f"\nEstatísticas descritivas:")
print(dados_estudo.describe())
