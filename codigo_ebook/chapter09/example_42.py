# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 833

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np


# Aplicando análise espectral
periodos, magnitude = analise_espectral(df_academico['publicacoes'].values)

# Identificando picos no espectro
picos, propriedades = find_peaks(magnitude, height=np.max(magnitude)*0.1)
