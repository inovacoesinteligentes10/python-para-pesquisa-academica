# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Padrões de Qualidade para Publicação
Linha original no arquivo LaTeX: 1057

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Função para criar gráficos de publicação
def criar_grafico_publicacao(dados, tipo='barras', titulo='',
                            xlabel='', ylabel='', filename=None):
    """
    Cria gráficos adequados para publicação científica
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    if tipo == 'barras':
        # Gráfico de barras com erro padrão
        stats = dados.groupby('grupo').agg({
            'pre_teste': ['mean', 'sem'],
            'pos_teste': ['mean', 'sem']
        })

        x = np.arange(len(stats.index))
        width = 0.35

        bars1 = ax.bar(x - width/2, stats['pre_teste']['mean'], width,
                      yerr=stats['pre_teste']['sem'],
                      label='Pré-teste', capsize=5, alpha=0.8)
        bars2 = ax.bar(x + width/2, stats['pos_teste']['mean'], width,
                      yerr=stats['pos_teste']['sem'],
                      label='Pós-teste', capsize=5, alpha=0.8)

        ax.set_xlabel(xlabel if xlabel else 'Grupo')
        ax.set_ylabel(ylabel if ylabel else 'Pontuação')
        ax.set_xticks(x)
        ax.set_xticklabels(stats.index)
        ax.legend()

    elif tipo == 'boxplot':
        # Box plot com pontos individuais
        box_data = [dados[dados['grupo'] == g]['ganho_aprendizado'] for g in dados['grupo'].unique()]
        box_labels = dados['grupo'].unique()

        bp = ax.boxplot(box_data, labels=box_labels, patch_artist=True, showmeans=True)

        # Personalizando cores
        for i, patch in enumerate(bp['boxes']):
            patch.set_facecolor(cores_publicacao[i])
            patch.set_alpha(0.7)

        ax.set_xlabel(xlabel if xlabel else 'Grupo')
        ax.set_ylabel(ylabel if ylabel else 'Ganho de Aprendizado')
