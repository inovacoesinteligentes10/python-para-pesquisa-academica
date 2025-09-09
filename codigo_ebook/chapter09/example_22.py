# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Fundamentos dos Modelos ARIMA
Linha original no arquivo LaTeX: 394

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Visualizando ACF e PACF para identificar parâmetros ARIMA
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Série original
axes[0, 0].plot(df_academico.index, df_academico['publicacoes'])
axes[0, 0].set_title('Série Original')
axes[0, 0].grid(True, alpha=0.3)

# Série diferenciada
axes[0, 1].plot(df_academico.index, df_academico['pub_diff1'])
axes[0, 1].set_title('Primeira Diferença')
axes[0, 1].grid(True, alpha=0.3)

# ACF da série diferenciada
plot_acf(df_academico['pub_diff1'].dropna(), ax=axes[1, 0], lags=24)
axes[1, 0].set_title('Função de Autocorrelação (ACF)')

# PACF da série diferenciada
plot_pacf(df_academico['pub_diff1'].dropna(), ax=axes[1, 1], lags=24)
axes[1, 1].set_title('Função de Autocorrelação Parcial (PACF)')

plt.tight_layout()
plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
