# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Coleta de Dados do Twitter/X
Linha original no arquivo LaTeX: 409

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

import pandas as pd
from typing import List

class TwitterAnalyzer:
    def __init__(self):
        pass
    
    def process_tweets(self, tweets_data):
        """Processa dados de tweets"""
        try:
            # Processar tweets
            return pd.DataFrame(tweets_data)
        except Exception as e:
            print(f"Erro ao coletar tweets: {e}")
            return pd.DataFrame(tweets_data)

    def analyze_sentiment_trends(self, tweets_df: pd.DataFrame) -> pd.DataFrame:
        """Analisa tendências de sentimento nos tweets coletados"""
        if tweets_df.empty:
            return pd.DataFrame()

        from textblob import TextBlob

        # Análise de sentimento
        tweets_df['sentiment'] = tweets_df['text'].apply(
            lambda x: TextBlob(x).sentiment.polarity
        )

        # Agregar por hora
        tweets_df['hour'] = tweets_df['created_at'].dt.floor('H')
        hourly_sentiment = tweets_df.groupby('hour').agg({
            'sentiment': 'mean',
            'like_count': 'mean',
            'id': 'count'
        }).rename(columns={'id': 'tweet_count'})

        return hourly_sentiment
