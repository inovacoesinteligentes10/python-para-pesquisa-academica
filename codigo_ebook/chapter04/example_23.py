# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Testes de Permutação
Linha original no arquivo LaTeX: 886

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def permutacao_visualizacao(stat_observada, stats_permutacao):
    """Cria visualizacao do teste de permutacao"""
    # Visualizacao
    plt.figure(figsize=(10, 6))

    plt.hist(stats_permutacao, bins=50, alpha=0.7, density=True,
             label='Distribuicao nula')
    plt.axvline(stat_observada, color='red', linestyle='--', linewidth=2,
                label=f'Estatistica observada: {stat_observada:.3f}')
    plt.axvline(-stat_observada, color='red', linestyle='--', linewidth=2, alpha=0.7)

    # Marcar regiao critica
    critico_superior = np.percentile(stats_permutacao, 97.5)
    critico_inferior = np.percentile(stats_permutacao, 2.5)

    x_fill = np.linspace(critico_superior, max(stats_permutacao), 100)
    plt.fill_between(x_fill, 0, stats.norm.pdf(x_fill, np.mean(stats_permutacao),
                                              np.std(stats_permutacao)),
                     alpha=0.3, color='red', label='Regiao critica (alpha=0.05)')

    x_fill2 = np.linspace(min(stats_permutacao), critico_inferior, 100)
    plt.fill_between(x_fill2, 0, stats.norm.pdf(x_fill2, np.mean(stats_permutacao),
                                               np.std(stats_permutacao)),
                     alpha=0.3, color='red')

    plt.xlabel('Estatistica de Teste')
    plt.ylabel('Densidade')
    plt.title('Teste de Permutacao: Distribuicao Nula')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
