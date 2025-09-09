# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 986

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Previsão estendida com análise de incerteza sazonal
horizonte_previsao = 12  # 12 meses à frente

# Previsão com modelo SARIMA
previsao_futura = modelo_sarima.forecast(steps=horizonte_previsao)
ic_futuro = modelo_sarima.get_forecast(steps=horizonte_previsao).conf_int()

# Criando datas futuras
ultima_data = df_academico.index[-1]
datas_futuras = pd.date_range(start=ultima_data + pd.DateOffset(months=1),
                              periods=horizonte_previsao, freq='M')
