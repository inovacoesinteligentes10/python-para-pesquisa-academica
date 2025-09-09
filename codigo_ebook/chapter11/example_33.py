# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Gráficos Multivariados Avançados
Linha original no arquivo LaTeX: 1183

Este código foi extraído automaticamente do arquivo chapter11.tex
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Figura composta para publicação
def criar_figura_multipla(dados, filename=None):
    """Cria figura com múltiplos painéis para publicação"""

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Painel A: Barras comparativas
    stats = dados.groupby('grupo').agg({
        'pre_teste': ['mean', 'sem'],
        'pos_teste': ['mean', 'sem']
    })

    x = np.arange(len(stats.index))
    width = 0.35

    axes[0, 0].bar(x - width/2, stats['pre_teste']['mean'], width,
                   yerr=stats['pre_teste']['sem'],
                   label='Pré-teste', capsize=5, alpha=0.8)
    axes[0, 0].bar(x + width/2, stats['pos_teste']['mean'], width,
                   yerr=stats['pos_teste']['sem'],
                   label='Pós-teste', capsize=5, alpha=0.8)

    axes[0, 0].set_title('A) Comparação Pré vs Pós-teste', fontweight='bold', loc='left')
    axes[0, 0].set_ylabel('Pontuação')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(stats.index)
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Painel B: Box plot dos ganhos
    box_data = [dados[dados['grupo'] == g]['ganho_aprendizado'] for g in dados['grupo'].unique()]
    bp = axes[0, 1].boxplot(box_data, labels=dados['grupo'].unique(), patch_artist=True)

    for i, patch in enumerate(bp['boxes']):
        patch.set_facecolor(cores_publicacao[i])
        patch.set_alpha(0.7)

    axes[0, 1].set_title('B) Distribuição dos Ganhos', fontweight='bold', loc='left')
    axes[0, 1].set_ylabel('Ganho de Aprendizado')
    axes[0, 1].grid(True, alpha=0.3)
