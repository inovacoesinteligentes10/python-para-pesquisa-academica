# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Controle de Erro Tipo I em Múltiplas Comparações
Linha original no arquivo LaTeX: 1251

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
import matplotlib.pyplot as plt


def visualizar_correcoes(p_valores, resultados, metodos):
    """Cria visualizacoes das correcoes"""
    # Visualizacao
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Comparacao dos p-valores
    x = np.arange(len(p_valores))
    largura = 0.2

    ax1.bar(x - largura, p_valores, largura, label='Original', alpha=0.8)

    for i, metodo in enumerate(metodos):
        offset = largura * (i - len(metodos)/2 + 1)
        ax1.bar(x + offset, resultados[metodo]['p_corrigidos'], largura,
               label=metodo.replace('_', ' ').title(), alpha=0.8)

    ax1.axhline(y=0.05, color='red', linestyle='--', alpha=0.7, label='alpha = 0.05')
    ax1.set_xlabel('Indice do Teste')
    ax1.set_ylabel('P-valor')
    ax1.set_title('Comparacao de P-valores')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Numero de descobertas significativas
    metodos_plot = ['Original'] + metodos
    n_sig_plot = [np.sum(p_valores < 0.05)] + [resultados[m]['n_significativos'] for m in metodos]

    cores = ['red'] + ['blue', 'green', 'orange'][:len(metodos)]
    bars = ax2.bar(metodos_plot, n_sig_plot, color=cores, alpha=0.7)

    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom')

    ax2.set_xlabel('Metodo de Correcao')
    ax2.set_ylabel('Numero de Testes Significativos')
    ax2.set_title('Impacto das Correcoes')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa

    return resultados
