# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Decomposição de Séries Temporais
Linha original no arquivo LaTeX: 256

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise dos componentes
print("Análise da Decomposição:")
print(f"Variabilidade da tendência: {decomposicao.trend.std():.2f}")
print(f"Variabilidade sazonal: {decomposicao.seasonal.std():.2f}")
print(f"Variabilidade do ruído: {decomposicao.resid.std():.2f}")
