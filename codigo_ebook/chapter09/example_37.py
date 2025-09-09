# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Modelagem Sazonal com SARIMA
Linha original no arquivo LaTeX: 722

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Selecionando o melhor modelo SARIMA
print("Selecionando modelo SARIMA... (pode demorar alguns minutos)")
melhor_params_sarima, modelo_sarima, melhor_aic_sarima = selecionar_sarima(treino)

print(f"x{melhor_params_sarima[1]}")
print(f"AIC: {melhor_aic_sarima:.2f}")

# Fazendo previsões com SARIMA
previsoes_sarima = modelo_sarima.forecast(steps=len(teste))
ic_sarima = modelo_sarima.get_forecast(steps=len(teste)).conf_int()
