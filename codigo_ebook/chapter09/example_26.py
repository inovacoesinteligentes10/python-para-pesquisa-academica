# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão e Validação
Linha original no arquivo LaTeX: 484

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np


# Fazendo previsões
previsoes = modelo_ajustado.forecast(steps=len(teste))
intervalo_confianca = modelo_ajustado.get_forecast(steps=len(teste))
ic = intervalo_confianca.conf_int()

# Calculando métricas de erro
mae = mean_absolute_error(teste, previsoes)
rmse = np.sqrt(mean_squared_error(teste, previsoes))
mape = np.mean(np.abs((teste - previsoes) / teste)) * 100

print(f"Métricas de Avaliação:")
print(f"MAE (Erro Absoluto Médio): {mae:.2f}")
print(f"RMSE (Raiz do Erro Quadrático Médio): {rmse:.2f}")
print(f"MAPE (Erro Percentual Absoluto Médio): {mape:.2f}%")
