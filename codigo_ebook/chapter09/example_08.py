# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Visualização Inicial dos Dados
Linha original no arquivo LaTeX: 132

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Criando visualizações exploratórias
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico principal da série
axes[0, 0].plot(df_academico.index, df_academico['publicacoes'],
                linewidth=1.5, color='steelblue')
axes[0, 0].set_title('Série Temporal: Publicações Científicas por Mês',
                     fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Número de Publicações')
axes[0, 0].grid(True, alpha=0.3)
