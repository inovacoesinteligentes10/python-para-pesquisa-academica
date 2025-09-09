# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Identificação de Padrões Sazonais
Linha original no arquivo LaTeX: 583

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise sazonal detalhada
from statsmodels.tsa.seasonal import STL

# Decomposição STL (Seasonal and Trend decomposition using Loess)
stl = STL(df_academico['publicacoes'], seasonal=13)  # seasonal=13 para dados mensais
resultado_stl = stl.fit()

# Visualizando decomposição STL
fig = resultado_stl.plot()
fig.suptitle('Decomposição STL - Publicações Científicas',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
