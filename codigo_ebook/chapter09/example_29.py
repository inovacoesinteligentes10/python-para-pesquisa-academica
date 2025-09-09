# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão e Validação
Linha original no arquivo LaTeX: 540

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise dos resíduos
residuos = modelo_ajustado.resid

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Resíduos ao longo do tempo
axes[0, 0].plot(residuos.index, residuos.values)
axes[0, 0].set_title('Resíduos ao Longo do Tempo')
axes[0, 0].set_ylabel('Resíduos')
axes[0, 0].grid(True, alpha=0.3)

# Histograma dos resíduos
axes[0, 1].hist(residuos.dropna(), bins=20, alpha=0.7, color='orange')
axes[0, 1].set_title('Distribuição dos Resíduos')
axes[0, 1].set_xlabel('Resíduos')
axes[0, 1].set_ylabel('Frequência')
