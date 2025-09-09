# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Características dos Dados Temporais
Linha original no arquivo LaTeX: 32

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np
import pandas as pd


# Criando dados simulados de temperatura para pesquisa climática
np.random.seed(42)
datas = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')

# Simulando temperatura com tendência, sazonalidade e ruído
tendencia = np.linspace(15, 17, len(datas))  # Aquecimento gradual
sazonalidade = 10 * np.sin(2 * np.pi * np.arange(len(datas)) / 365.25)
ruido = np.random.normal(0, 2, len(datas))

temperatura = tendencia + sazonalidade + ruido
