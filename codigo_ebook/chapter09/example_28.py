# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão e Validação
Linha original no arquivo LaTeX: 526

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


plt.title(f'Previsão ARIMA{melhor_params} - Publicações Científicas',
          fontsize=14, fontweight='bold')
plt.xlabel('Data')
plt.ylabel('Número de Publicações')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
