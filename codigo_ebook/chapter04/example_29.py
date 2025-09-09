# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 1102

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def pca_biplot_heatmap(dados, dados_pca, loadings_df, pca, n_componentes, axes):
    """Cria biplot e heatmap"""
    # 3. Biplot (se temos pelo menos 2 componentes)
    if n_componentes >= 2:
        loadings = loadings_df.values
        # Scatter dos scores
        axes[1,0].scatter(dados_pca[:, 0], dados_pca[:, 1], alpha=0.7)

        # Adicionar vetores das variaveis
        for i, var in enumerate(dados.columns):
            axes[1,0].arrow(0, 0, loadings[i, 0]*3, loadings[i, 1]*3,
                           head_width=0.1, head_length=0.1, fc='red', ec='red')
            axes[1,0].text(loadings[i, 0]*3.2, loadings[i, 1]*3.2, var,
                          fontsize=9, ha='center')

        axes[1,0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
        axes[1,0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
        axes[1,0].set_title('Biplot PC1 vs PC2')
        axes[1,0].grid(True, alpha=0.3)

    # 4. Heatmap dos loadings
    sns.heatmap(loadings_df.T, annot=True, cmap='RdBu_r', center=0,
                ax=axes[1,1], fmt='.2f')
    axes[1,1].set_title('Heatmap dos Loadings')

    plt.tight_layout()
    plt.show()

# Dados de exemplo: simulando questionario psicologico
np.random.seed(42)
n_participantes = 200

# Simular fatores latentes
fator_ansiedade = np.random.normal(0, 1, n_participantes)
fator_depressao = np.random.normal(0, 1, n_participantes)
fator_autoestima = np.random.normal(0, 1, n_participantes)
