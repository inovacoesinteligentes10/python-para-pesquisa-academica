# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Seleção e Ajuste do Modelo ARIMA
Linha original no arquivo LaTeX: 424

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np


from itertools import product

# Função para seleção automática de parâmetros ARIMA
def selecionar_arima(serie, max_p=3, max_d=2, max_q=3):
    """
    Seleciona os melhores parâmetros ARIMA usando AIC
    """
    melhor_aic = np.inf
    melhor_params = None
    melhor_modelo = None

    # Testando diferentes combinações de parâmetros
    for p in range(max_p + 1):
        for d in range(max_d + 1):
            for q in range(max_q + 1):
                try:
                    modelo = ARIMA(serie, order=(p, d, q))
                    resultado = modelo.fit()

                except Exception as e:

                    print(f'Erro: {e}')

                    return None
                    if resultado.aic < melhor_aic:
                        melhor_aic = resultado.aic
                        melhor_params = (p, d, q)
                        melhor_modelo = resultado

                except:
                    continue

    return melhor_params, melhor_modelo, melhor_aic
