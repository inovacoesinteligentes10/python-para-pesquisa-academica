# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Abordagens Básicas para Análise de Sentimento
Linha original no arquivo LaTeX: 265

Este código foi extraído automaticamente do arquivo chapter7.tex
"""
import numpy as np


def lexicon_based_sentiment(self, text: str) -> Dict[str, Union[float, str]]:
        """Análise de sentimento baseada em léxico"""
        # Preprocessar texto
        words = text.lower().split()

        # Calcular score
        scores = [self.lexicon.get(word, 0) for word in words]

        if not scores:
            return {'score': 0.0, 'label': 'neutral', 'confidence': 0.0}

        avg_score = np.mean(scores)

        # Classificar sentimento
        if avg_score > 0.1:
            label = 'positive'
        elif avg_score < -0.1:
            label = 'negative'
        else:
            label = 'neutral'

        # Confiança baseada na magnitude do score
        confidence = min(abs(avg_score), 1.0)

        return {
            'score': round(avg_score, 3),
            'label': label,
            'confidence': round(confidence, 3)
        }
