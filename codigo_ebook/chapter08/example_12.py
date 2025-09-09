# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Clustering e Análise de Componentes
Linha original no arquivo LaTeX: 713

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# src/ml/unsupervised_toolkit.py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, adjusted_rand_score
import matplotlib.pyplot as plt
import seaborn as sns

class UnsupervisedToolkit:
    """Toolkit para aprendizado não supervisionado em pesquisa"""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.clustering_models = {}
        self.dimensionality_models = {}

    def optimal_clusters_analysis(self, X: pd.DataFrame,
                                 max_clusters: int = 10) -> Dict:
        """Determina número ótimo de clusters usando múltiplos métodos"""
        X_scaled = StandardScaler().fit_transform(X)

        # Método do cotovelo (inércia)
        inertias = []
        silhouette_scores = []
        k_range = range(2, max_clusters + 1)

        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            cluster_labels = kmeans.fit_predict(X_scaled)

            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(X_scaled, cluster_labels))

        # Encontrar cotovelo
        optimal_k_elbow = self._find_elbow_point(k_range, inertias)
        optimal_k_silhouette = k_range[np.argmax(silhouette_scores)]

        return {
            'k_range': list(k_range),
            'inertias': inertias,
            'silhouette_scores': silhouette_scores,
            'optimal_k_elbow': optimal_k_elbow,
            'optimal_k_silhouette': optimal_k_silhouette,
            'max_silhouette_score': max(silhouette_scores)
        }
