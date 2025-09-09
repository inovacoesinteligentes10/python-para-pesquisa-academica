# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Gráficos Básicos para Publicação
Linha original no arquivo LaTeX: 399

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo para publicação
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18
})

# Dados para visualização
grupos = ['Controle', 'Tratamento A', 'Tratamento B']
pre_teste = [72.5, 73.1, 72.8]
pos_teste = [74.2, 81.3, 85.7]
erros_pre = [2.1, 2.3, 2.0]
erros_pos = [2.5, 2.8, 3.1]

# Criar figura com múltiplos subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
