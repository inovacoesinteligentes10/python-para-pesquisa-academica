# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Bootstrap: Estimando Distribuições
Linha original no arquivo LaTeX: 697

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def bootstrap_intervalos_viz(stat_original, bootstrap_stats, alpha=0.05):
    """Calcula intervalos de confianca e cria visualizacoes"""
    # Calcular intervalos de confianca
    ci_lower = np.percentile(bootstrap_stats, (alpha/2) * 100)
    ci_upper = np.percentile(bootstrap_stats, (1 - alpha/2) * 100)

    # Bias e erro padrao
    bias = np.mean(bootstrap_stats) - stat_original
    erro_padrao = np.std(bootstrap_stats)

    print(f"Bias bootstrap: {bias:.4f}")
    print(f"Erro padrao bootstrap: {erro_padrao:.4f}")
    print(f"IC {(1-alpha)*100:.0f}%: [{ci_lower:.4f}, {ci_upper:.4f}]")

    # Visualizacao
    plt.figure(figsize=(12, 4))

    # Histograma das estatisticas bootstrap
    plt.subplot(1, 2, 1)
    plt.hist(bootstrap_stats, bins=50, alpha=0.7, density=True)
    plt.axvline(stat_original, color='red', linestyle='--',
                label=f'Original: {stat_original:.3f}')
    plt.axvline(ci_lower, color='green', linestyle='--', alpha=0.7)
    plt.axvline(ci_upper, color='green', linestyle='--', alpha=0.7,
                label=f'IC {(1-alpha)*100:.0f}%')
    plt.xlabel('Valor da Estatistica')
    plt.ylabel('Densidade')
    plt.title('Distribuicao Bootstrap')
    plt.legend()

    # Q-Q plot para verificar normalidade da distribuicao bootstrap
    plt.subplot(1, 2, 2)
    stats.probplot(bootstrap_stats, dist="norm", plot=plt)
    plt.title('Q-Q Plot: Distribuicao Bootstrap')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return bias, erro_padrao, ci_lower, ci_upper
