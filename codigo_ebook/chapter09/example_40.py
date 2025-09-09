# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Modelagem Sazonal com SARIMA
Linha original no arquivo LaTeX: 777

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Intervalo de confiança SARIMA
plt.fill_between(teste.index, ic_sarima.iloc[:, 0], ic_sarima.iloc[:, 1],
                 color='purple', alpha=0.2, label='IC 95% SARIMA')

plt.title('Comparação: ARIMA vs SARIMA - Publicações Científicas',
          fontsize=14, fontweight='bold')
plt.xlabel('Data')
plt.ylabel('Número de Publicações')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
