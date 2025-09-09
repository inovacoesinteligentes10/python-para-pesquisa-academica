# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Arrays Multidimensionais para Dados Complexos
Linha original no arquivo LaTeX: 113

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


# Calcular potencial evocado (media atraves de trials)
potencial_evocado = np.mean(dados_eeg, axis=2)

# Encontrar pico máximo no tempo
tempo_max = np.unravel_index(np.argmax(np.abs(potencial_evocado)),
                            potencial_evocado.shape)
print(f"Pico maximo no eletrodo {tempo_max[0]}, tempo {tempo_max[1]}")
