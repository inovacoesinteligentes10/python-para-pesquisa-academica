# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 747

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import matplotlib.pyplot as plt


def pipeline_visualizacoes_1_2(dados_limpos, controle, experimental):
    # 4. VISUALIZACAO
    print("4. Criando visualizações...")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Grafico 1: Boxplot da melhoria por grupo
    dados_limpos.boxplot(column='melhoria', by='grupo', ax=ax1)
    ax1.set_title('Melhoria por Grupo')
    ax1.set_xlabel('Grupo')
    ax1.set_ylabel('Melhoria (pontos)')

    # Gráfico 2: Histograma sobreposto
    ax2.hist(controle, alpha=0.7, label='Controle', bins=20)
    ax2.hist(experimental, alpha=0.7, label='Experimental', bins=20)
    ax2.set_xlabel('Melhoria')
    ax2.set_ylabel('Frequência')
    ax2.set_title('Distribuição da Melhoria')
    ax2.legend()

    return fig, ax1, ax2, ax3, ax4
