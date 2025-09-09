# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Padrões de Qualidade para Publicação
Linha original no arquivo LaTeX: 1017

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Configurações para gráficos de publicação
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Configurações para publicação científica
def config_publicacao():
    """Configura matplotlib para gráficos de publicação"""
    rcParams['figure.figsize'] = (8, 6)
    rcParams['figure.dpi'] = 300
    rcParams['savefig.dpi'] = 300
    rcParams['font.size'] = 12
    rcParams['axes.labelsize'] = 14
    rcParams['axes.titlesize'] = 16
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['legend.fontsize'] = 12
    rcParams['font.family'] = 'serif'
    rcParams['font.serif'] = ['Times New Roman', 'Times', 'serif']
    rcParams['text.usetex'] = False  # Definir como True se LaTeX estiver disponível
    rcParams['axes.linewidth'] = 1.5
    rcParams['grid.linewidth'] = 0.5
    rcParams['lines.linewidth'] = 2
    rcParams['patch.linewidth'] = 0.5
    rcParams['xtick.major.width'] = 1.5
    rcParams['ytick.major.width'] = 1.5
    rcParams['xtick.minor.width'] = 1
    rcParams['ytick.minor.width'] = 1

# Aplicando configurações
config_publicacao()

# Paleta de cores para publicação (colorblind-friendly)
cores_publicacao = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
sns.set_palette(cores_publicacao)
