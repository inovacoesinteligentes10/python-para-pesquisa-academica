# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Abordagens Básicas para Análise de Sentimento
Linha original no arquivo LaTeX: 355

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# Analisar sentimentos
results = analyzer.analyze_sentiment_dataset(sample_texts)
print("Análise de Sentimento:")
print(results[['text', 'score', 'label']].head())
