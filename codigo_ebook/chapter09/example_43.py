# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 843

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Visualizando análise espectral
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Espectro de potência
axes[0, 0].plot(periodos, magnitude, linewidth=1.5, color='navy')
axes[0, 0].scatter(periodos[picos], magnitude[picos],
                   color='red', s=50, zorder=5)
axes[0, 0].set_title('Espectro de Potência - Identificação de Ciclos')
axes[0, 0].set_xlabel('Período (meses)')
axes[0, 0].set_ylabel('Magnitude')
axes[0, 0].set_xlim(0, 24)
axes[0, 0].grid(True, alpha=0.3)

# Anotando os principais períodos detectados
for i, pico in enumerate(picos[:5]):  # Mostrando apenas os 5 principais
    periodo_detectado = periodos[pico]
    axes[0, 0].annotate(f'{periodo_detectado:.1f}m',
                        xy=(periodo_detectado, magnitude[pico]),
                        xytext=(periodo_detectado, magnitude[pico] + magnitude[pico]*0.1),
                        ha='center', fontsize=9, color='red')
