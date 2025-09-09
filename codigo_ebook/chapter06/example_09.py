# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Coleta de Dados do Twitter/X
Linha original no arquivo LaTeX: 360

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/twitter_collector.py
import tweepy
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict

class TwitterDataCollector:
    """Coletor de dados do Twitter usando API v2"""

    def __init__(self, bearer_token: str):
        self.client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    def search_tweets(self, query: str, max_results: int = 100,
                     days_back: int = 7) -> pd.DataFrame:
        """Busca tweets recentes baseado em query"""
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=days_back)

        tweets_data = []

        # Configurar campos para coletar
        tweet_fields = ['created_at', 'author_id', 'public_metrics', 'lang']

        try:
            tweets = tweepy.Paginator(
                self.client.search_recent_tweets,
                query=query,
                tweet_fields=tweet_fields,
                start_time=start_time,
                end_time=end_time,
                max_results=min(100, max_results)
            ).flatten(limit=max_results)


        except Exception as e:


            print(f'Erro: {e}')


            return None
            for tweet in tweets:
                tweet_data = {
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'author_id': tweet.author_id,
                    'retweet_count': tweet.public_metrics['retweet_count'],
                    'like_count': tweet.public_metrics['like_count'],
                    'lang': tweet.lang if hasattr(tweet, 'lang') else None
                }
                tweets_data.append(tweet_data)
        
        except Exception as e:
            print(f"Erro ao coletar tweets: {e}")
            return pd.DataFrame()
        
        return pd.DataFrame(tweets_data)
