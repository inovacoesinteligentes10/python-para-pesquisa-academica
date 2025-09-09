# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Detecção de Mudanças Estruturais
Linha original no arquivo LaTeX: 272

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

from scipy import stats
import ruptures as rpt

# Detecção de pontos de mudança usando Ruptures
# Preparando os dados
serie_valores = df_academico['publicacoes'].values

# Detectando mudanças na média usando Pelt
modelo = rpt.Pelt(model="rbf").fit(serie_valores)
pontos_mudanca = modelo.predict(pen=10)

# Removendo o último ponto (que é sempre o final da série)
pontos_mudanca = pontos_mudanca[:-1]
