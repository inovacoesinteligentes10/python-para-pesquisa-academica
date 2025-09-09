# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Verificação de Pressupostos
Linha original no arquivo LaTeX: 168

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def detectar_outliers(dados, variavel_dependente, axes):
    """Detecta e visualiza outliers"""
    # Teste de outliers
    q1 = dados[variavel_dependente].quantile(0.25)
    q3 = dados[variavel_dependente].quantile(0.75)
    iqr = q3 - q1
    outliers = dados[(dados[variavel_dependente] < q1 - 1.5*iqr) |
                    (dados[variavel_dependente] > q3 + 1.5*iqr)]

    axes[1,1].scatter(range(len(dados)), dados[variavel_dependente], alpha=0.6)
    if len(outliers) > 0:
        outlier_indices = outliers.index
        axes[1,1].scatter(outlier_indices, outliers[variavel_dependente],
                         color='red', s=50, label=f'{len(outliers)} outliers')
        axes[1,1].legend()
    axes[1,1].set_title('Deteccao de Outliers')
    axes[1,1].set_xlabel('Indice')
    axes[1,1].set_ylabel(variavel_dependente)

    plt.tight_layout()
    plt.savefig("temp_plot.png", bbox_inches="tight")
    plt.close()  # plt.show() substituído para execução não-interativa

    print(f"   Outliers detectados: {len(outliers)}")
    if len(outliers) > 0:
        print(f"   Indices dos outliers: {list(outliers.index)}")

    return outliers

# Exemplo de uso
np.random.seed(42)
dados_exemplo = pd.DataFrame({
    'grupo': np.repeat(['controle', 'experimental'], 50),
    'score': np.concatenate([
        np.random.normal(50, 10, 50),  # controle
        np.random.normal(58, 12, 50)   # experimental
    ])
})

# Adicionar alguns outliers
dados_exemplo.loc[5, 'score'] = 100  # outlier
dados_exemplo.loc[55, 'score'] = 20  # outlier

# Executar verificacao completa
dados, grupo_col, var_dep = verificar_pressupostos(dados_exemplo, 'grupo', 'score')
p_final = testar_normalidade(dados, grupo_col, var_dep)
p_levene = testar_homogeneidade(dados, grupo_col, var_dep)
axes = diagnosticos_visuais(dados, grupo_col, var_dep)
outliers = detectar_outliers(dados, var_dep, axes)
