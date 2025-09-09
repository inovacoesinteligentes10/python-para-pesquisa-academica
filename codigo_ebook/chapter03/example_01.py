# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Por que NumPy é Crucial para Pesquisa
Linha original no arquivo LaTeX: 16

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

import numpy as np
import time

# Dados de exemplo: medicoes de 1 milhao de participantes
n = 1000000

# Metodo 1: Listas Python puras
dados_python = list(range(n))
inicio = time.time()
resultado_python = [x**2 for x in dados_python]
tempo_python = time.time() - inicio

# Metodo 2: Arrays NumPy
dados_numpy = np.arange(n)
inicio = time.time()
resultado_numpy = dados_numpy**2
tempo_numpy = time.time() - inicio

print(f"Tempo Python puro: {tempo_python:.3f} segundos")
print(f"Tempo NumPy: {tempo_numpy:.3f} segundos")
print(f"NumPy e {tempo_python/tempo_numpy:.1f}x mais rapido")

# Verificar se resultados sao iguais
print(f"Resultados identicos: {np.array_equal(resultado_python, resultado_numpy)}")
