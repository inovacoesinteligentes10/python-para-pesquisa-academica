# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Abordagens Básicas para Análise de Sentimento
Linha original no arquivo LaTeX: 221

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# src/nlp/sentiment_analyzer.py
import pandas as pd
from typing import Dict, List, Union
import numpy as np

class SentimentAnalyzer:
    """Analisador de sentimento com múltiplas abordagens"""

    def __init__(self, language='portuguese'):
        self.language = language
        self.lexicon = self._load_sentiment_lexicon()

    def _load_sentiment_lexicon(self) -> Dict[str, float]:
        """Carrega léxico de sentimento para o idioma"""
        if self.language == 'portuguese':
            # Léxico básico em português
            positive_words = {
                'bom': 1.0, 'ótimo': 2.0, 'excelente': 2.0, 'maravilhoso': 2.0,
                'legal': 1.0, 'bacana': 1.0, 'perfeito': 2.0, 'incrível': 2.0,
                'positivo': 1.0, 'feliz': 1.5, 'alegre': 1.5, 'satisfeito': 1.0,
                'aprovado': 1.0, 'concordo': 1.0, 'apoio': 1.5, 'gosto': 1.0
            }

            negative_words = {
                'ruim': -1.0, 'péssimo': -2.0, 'terrível': -2.0, 'horrível': -2.0,
                'negativo': -1.0, 'triste': -1.5, 'raiva': -1.5, 'ódio': -2.0,
                'contra': -1.0, 'discordo': -1.0, 'odeio': -2.0, 'detesto': -2.0,
                'reprovado': -1.0, 'rejeitado': -1.5, 'problema': -1.0
            }

            lexicon = {**positive_words, **negative_words}

        else:  # English fallback
            lexicon = {
                'good': 1.0, 'great': 2.0, 'excellent': 2.0, 'amazing': 2.0,
                'bad': -1.0, 'terrible': -2.0, 'awful': -2.0, 'horrible': -2.0,
                'love': 2.0, 'like': 1.0, 'hate': -2.0, 'dislike': -1.0
            }

        return lexicon
