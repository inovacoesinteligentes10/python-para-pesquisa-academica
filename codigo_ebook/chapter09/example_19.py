# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Fundamentos dos Modelos ARIMA
Linha original no arquivo LaTeX: 352

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_absolute_error, mean_squared_error
