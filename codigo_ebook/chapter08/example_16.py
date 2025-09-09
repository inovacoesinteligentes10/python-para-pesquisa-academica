# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Clustering e Análise de Componentes
Linha original no arquivo LaTeX: 912

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# Exemplo de uso
unsupervised_toolkit = UnsupervisedToolkit()

# Dados exemplo
np.random.seed(42)
X_example = pd.DataFrame({
    'feature1': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(3, 1, 100)]),
    'feature2': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(3, 1, 100)]),
    'feature3': np.concatenate([np.random.normal(1, 0.5, 100), np.random.normal(2, 0.5, 100)])
})

# Análise do número ótimo de clusters
optimal_analysis = unsupervised_toolkit.optimal_clusters_analysis(X_example)
print(f"Número ótimo de clusters (cotovelo): {optimal_analysis['optimal_k_elbow']}")
print(f"Número ótimo de clusters (silhouette): {optimal_analysis['optimal_k_silhouette']}")

# Aplicar algoritmos de clustering
clustering_results = unsupervised_toolkit.apply_clustering_algorithms(X_example, n_clusters=2)

# Redução de dimensionalidade
reduction_results = unsupervised_toolkit.dimensionality_reduction(X_example)

print(f"Variância explicada pelo PCA: {reduction_results['pca']['explained_variance_ratio']}")
