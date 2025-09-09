# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Decomposição de Séries Temporais
Linha original no arquivo LaTeX: 202

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Decomposição da série temporal
decomposicao = seasonal_decompose(df_academico['publicacoes'],
                                  model='additive', period=12)
