# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Visualizações Avançadas para Pesquisa
Linha original no arquivo LaTeX: 532

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import pandas as pd


# Criar dataset multivariado simulado
np.random.seed(123)
n_participantes = 200

# Variáveis correlacionadas para simular dados reais
dados_pesquisa = pd.DataFrame({
    'idade': np.random.randint(18, 65, n_participantes),
    'educacao_anos': np.random.randint(8, 20, n_participantes),
    'renda': np.random.normal(50000, 15000, n_participantes),
    'stress_percebido': np.random.randint(1, 11, n_participantes),
    'satisfacao_vida': np.random.randint(1, 11, n_participantes),
    'horas_exercicio': np.random.exponential(3, n_participantes),
    'qualidade_sono': np.random.randint(1, 11, n_participantes)
})

# Introduzir correlações realistas
dados_pesquisa['renda'] += dados_pesquisa['educacao_anos'] * 2000
dados_pesquisa['satisfacao_vida'] = 10 - dados_pesquisa['stress_percebido'] + \
                                   np.random.normal(0, 1, n_participantes)
dados_pesquisa['qualidade_sono'] = 10 - dados_pesquisa['stress_percebido'] * 0.5 + \
                                  dados_pesquisa['horas_exercicio'] * 0.3 + \
                                  np.random.normal(0, 1, n_participantes)

# Limitar valores aos ranges apropriados
dados_pesquisa['satisfacao_vida'] = np.clip(dados_pesquisa['satisfacao_vida'], 1, 10)
dados_pesquisa['qualidade_sono'] = np.clip(dados_pesquisa['qualidade_sono'], 1, 10)
dados_pesquisa['horas_exercicio'] = np.clip(dados_pesquisa['horas_exercicio'], 0, 15)
