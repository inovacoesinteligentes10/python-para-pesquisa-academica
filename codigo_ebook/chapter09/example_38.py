# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Modelagem Sazonal com SARIMA
Linha original no arquivo LaTeX: 737

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np


# Métricas de avaliação SARIMA
mae_sarima = mean_absolute_error(teste, previsoes_sarima)
rmse_sarima = np.sqrt(mean_squared_error(teste, previsoes_sarima))
mape_sarima = np.mean(np.abs((teste - previsoes_sarima) / teste)) * 100

print(f"\nMétricas SARIMA:")
print(f"MAE: {mae_sarima:.2f}")
print(f"RMSE: {rmse_sarima:.2f}")
print(f"MAPE: {mape_sarima:.2f}%")

print(f"\nComparação com ARIMA:")
print(f"ARIMA - MAE: {mae:.2f}, RMSE: {rmse:.2f}, MAPE: {mape:.2f}%")
print(f"SARIMA - MAE: {mae_sarima:.2f}, RMSE: {rmse_sarima:.2f}, MAPE: {mape_sarima:.2f}%")
