# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 1
Seção: Casos de Sucesso na Academia
Linha original no arquivo LaTeX: 70

Este código foi extraído automaticamente do arquivo chapter1.tex
"""

import networkx as nx
import pandas as pd
from textblob import TextBlob
import re

def extract_mentions(text):
    """Extrai menções (@usuario) de um texto"""
    return re.findall(r'@(\w+)', text)

# Carregar dados de tweets
tweets_df = pd.read_csv('political_tweets.csv')

# Análise de sentimento
tweets_df['sentiment'] = tweets_df['text'].apply(
    lambda x: TextBlob(x).sentiment.polarity
)

# Criar rede de menções
G = nx.DiGraph()
for _, tweet in tweets_df.iterrows():
    mentions = extract_mentions(tweet['text'])
    for mention in mentions:
        G.add_edge(tweet['user'], mention, sentiment=tweet['sentiment'])

# Métricas de rede
print(f"Usuários mais influentes:")
centrality = nx.betweenness_centrality(G)
top_users = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]
for user, score in top_users:
    print(f"{user}: {score:.3f}")
