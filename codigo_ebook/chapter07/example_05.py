# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Limpeza e Normalização de Texto
Linha original no arquivo LaTeX: 157

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# src/nlp/public_consultation_analyzer.py
from text_preprocessor import TextPreprocessor
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

class PublicConsultationAnalyzer:
    """Analisador para comentários de consultas públicas"""

    def __init__(self):
        self.preprocessor = TextPreprocessor(language='portuguese')
        self.comments_df = None

    def load_and_clean_comments(self, filepath: str) -> pd.DataFrame:
        """Carrega e limpa comentários de consulta pública"""
        # Carregar dados
        self.comments_df = pd.read_csv(filepath)

        # Limpar textos
        self.comments_df['comment_cleaned'] = self.comments_df['comment'].apply(
            lambda x: self.preprocessor.clean_text(x, remove_hashtags=False)
        )

        # Tokenizar
        self.comments_df['tokens'] = self.comments_df['comment_cleaned'].apply(
            lambda x: self.preprocessor.tokenize(x)
        )

        # Filtrar comentários muito curtos
        self.comments_df = self.comments_df[
            self.comments_df['tokens'].apply(len) >= 3
        ]

        return self.comments_df

    def extract_key_themes(self, min_frequency: int = 5) -> Dict[str, int]:
        """Extrai temas principais dos comentários"""
        # Combinar todos os tokens
        all_tokens = []
        for tokens in self.comments_df['tokens']:
            all_tokens.extend(tokens)
