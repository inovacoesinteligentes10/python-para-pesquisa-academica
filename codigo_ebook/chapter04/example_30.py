# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Componentes Principais (PCA)
Linha original no arquivo LaTeX: 1144

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

# Criar variaveis observadas com ruido
dados_psico = pd.DataFrame({
    'ansiedade_1': fator_ansiedade + np.random.normal(0, 0.5, n_participantes),
    'ansiedade_2': fator_ansiedade + np.random.normal(0, 0.5, n_participantes),
    'ansiedade_3': fator_ansiedade + np.random.normal(0, 0.5, n_participantes),
    'depressao_1': fator_depressao + np.random.normal(0, 0.5, n_participantes),
    'depressao_2': fator_depressao + np.random.normal(0, 0.5, n_participantes),
    'depressao_3': fator_depressao + np.random.normal(0, 0.5, n_participantes),
    'autoestima_1': -fator_autoestima + np.random.normal(0, 0.5, n_participantes),
    'autoestima_2': -fator_autoestima + np.random.normal(0, 0.5, n_participantes),
})

# Executar PCA completo
dados_scaled, pca_completo, var_explicada, var_cumulativa = analise_pca_completa(dados_psico)
pca, dados_pca, loadings_df, n_componentes = pca_selecao_componentes(dados_psico, dados_scaled, var_explicada, var_cumulativa)
pca_interpretacao(pca, loadings_df, n_componentes)
axes = pca_visualizacoes(dados_psico, pca, dados_pca, loadings_df, var_explicada, var_cumulativa, n_componentes)
pca_biplot_heatmap(dados_psico, dados_pca, loadings_df, pca, n_componentes, axes)
