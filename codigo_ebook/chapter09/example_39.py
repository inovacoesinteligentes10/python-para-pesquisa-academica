# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Modelagem Sazonal com SARIMA
Linha original no arquivo LaTeX: 755

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Visualizando comparação entre modelos
plt.figure(figsize=(15, 8))

# Dados históricos
plt.plot(treino.index, treino.values, label='Dados de Treino',
         color='blue', linewidth=1.5)
plt.plot(teste.index, teste.values, label='Valores Reais',
         color='green', linewidth=2)

# Previsões ARIMA
plt.plot(teste.index, previsoes, label=f'ARIMA{melhor_params}',
         color='red', linewidth=2, linestyle='--', alpha=0.8)

# Previsões SARIMA
plt.plot(teste.index, previsoes_sarima,
         label=f'SARIMA{melhor_params_sarima[0]}x{melhor_params_sarima[1]}',
         color='purple', linewidth=2, linestyle=':', alpha=0.8)
