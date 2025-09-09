# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1030

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Visualizando previsões com análise de incerteza
fig, axes = plt.subplots(2, 1, figsize=(15, 12))

# Gráfico principal de previsão
ultimos_24_meses = df_academico.tail(24)
axes[0].plot(ultimos_24_meses.index, ultimos_24_meses['publicacoes'],
             'o-', label='Dados Históricos', color='blue', linewidth=2)

axes[0].plot(datas_futuras, previsao_futura, 'o-',
             label='Previsão SARIMA', color='red', linewidth=2)

axes[0].fill_between(datas_futuras, df_incerteza['ic_inferior'],
                     df_incerteza['ic_superior'],
                     alpha=0.3, color='red', label='IC 95%')
