# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão e Validação
Linha original no arquivo LaTeX: 503

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Visualizando previsões
plt.figure(figsize=(15, 8))

# Dados de treino
plt.plot(treino.index, treino.values, label='Dados de Treino',
         color='blue', linewidth=1.5)

# Dados de teste (valores reais)
plt.plot(teste.index, teste.values, label='Valores Reais',
         color='green', linewidth=2)

# Previsões
plt.plot(teste.index, previsoes, label='Previsões ARIMA',
         color='red', linewidth=2, linestyle='--')

# Intervalo de confiança
plt.fill_between(teste.index, ic.iloc[:, 0], ic.iloc[:, 1],
                 color='red', alpha=0.2, label='IC 95%')
