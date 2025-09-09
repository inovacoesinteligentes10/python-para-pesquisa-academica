# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Decomposição de Séries Temporais
Linha original no arquivo LaTeX: 213

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Visualizando a decomposição
fig, axes = plt.subplots(4, 1, figsize=(15, 12))

# Série original
axes[0].plot(df_academico.index, df_academico['publicacoes'],
             color='black', linewidth=1.5)
axes[0].set_title('Série Original', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Publicações')
axes[0].grid(True, alpha=0.3)

# Tendência
axes[1].plot(df_academico.index, decomposicao.trend,
             color='red', linewidth=2)
axes[1].set_title('Componente de Tendência', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Tendência')
axes[1].grid(True, alpha=0.3)
