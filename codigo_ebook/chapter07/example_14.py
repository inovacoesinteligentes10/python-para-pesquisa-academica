# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Modelagem de Tópicos
Linha original no arquivo LaTeX: 498

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# src/nlp/topic_modeling.py
import pandas as pd
import numpy as np
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class TopicModeler:
    """Modelador de tópicos para análise de grandes corpus"""

    def __init__(self, language='portuguese'):
        self.language = language
        self.vectorizer = None
        self.lda_model = None
        self.feature_names = None

    def prepare_documents(self, documents: List[str],
                         min_df: int = 2,
                         max_df: float = 0.8,
                         max_features: int = 1000) -> np.ndarray:
        """Prepara documentos para modelagem de tópicos"""
        if self.language == 'portuguese':
            stop_words = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para',
                         'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais']
        else:
            stop_words = 'english'

        self.vectorizer = TfidfVectorizer(
            max_df=max_df,
            min_df=min_df,
            max_features=max_features,
            stop_words=stop_words,
            lowercase=True
        )

        doc_term_matrix = self.vectorizer.fit_transform(documents)
        self.feature_names = self.vectorizer.get_feature_names_out()

        return doc_term_matrix
