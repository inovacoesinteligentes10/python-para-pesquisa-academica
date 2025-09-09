# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Modelagem Sazonal com SARIMA
Linha original no arquivo LaTeX: 684

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

from statsmodels.tsa.statespace.sarimax import SARIMAX

# Função para seleção de parâmetros SARIMA
def selecionar_sarima(serie, max_p=2, max_d=1, max_q=2,
                     max_P=1, max_D=1, max_Q=1, s=12):
    """
    Seleciona os melhores parâmetros SARIMA usando AIC
    """
    melhor_aic = np.inf
    melhor_params = None
    melhor_modelo = None

    for p in range(max_p + 1):
        for d in range(max_d + 1):
            for q in range(max_q + 1):
                for P in range(max_P + 1):
                    for D in range(max_D + 1):
                        for Q in range(max_Q + 1):
                            try:
                                modelo = SARIMAX(serie,
                                                order=(p, d, q),
                                                seasonal_order=(P, D, Q, s))
                                resultado = modelo.fit(disp=False)

                            except Exception as e:

                                print(f'Erro: {e}')

                                return None
                                if resultado.aic < melhor_aic:
                                    melhor_aic = resultado.aic
                                    melhor_params = ((p, d, q), (P, D, Q, s))
                                    melhor_modelo = resultado

                            except:
                                continue

    return melhor_params, melhor_modelo, melhor_aic
