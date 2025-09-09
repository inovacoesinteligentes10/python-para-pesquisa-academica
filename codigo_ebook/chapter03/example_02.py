# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Arrays NumPy: Fundamentos
Linha original no arquivo LaTeX: 51

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

import numpy as np

# Diferentes maneiras de criar arrays
dados_experimentais = np.array([1.2, 1.5, 1.3, 1.7, 1.1])
zeros = np.zeros(10)  # Array de zeros
uns = np.ones((3, 4))  # Matriz 3x4 de uns
sequencia = np.arange(0, 10, 0.5)  # De 0 a 10 com passo 0.5
linear = np.linspace(0, 100, 50)  # 50 pontos igualmente espaçados

# Propriedades importantes
print(f"Forma: {dados_experimentais.shape}")
print(f"Tipo de dados: {dados_experimentais.dtype}")
print(f"Numero de dimensoes: {dados_experimentais.ndim}")
print(f"Tamanho total: {dados_experimentais.size}")

# Operacoes basicas (vetorizadas)
print(f"Media: {np.mean(dados_experimentais):.3f}")
print(f"Desvio padrao: {np.std(dados_experimentais):.3f}")
print(f"Maximo: {np.max(dados_experimentais):.3f}")
print(f"Minimo: {np.min(dados_experimentais):.3f}")

# Operacoes elemento a elemento
dados_normalizados = (dados_experimentais - np.mean(dados_experimentais)) / np.std(dados_experimentais)
print(f"Dados normalizados: {dados_normalizados}")
