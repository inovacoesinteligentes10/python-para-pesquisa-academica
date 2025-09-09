# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Modelagem de Tópicos
Linha original no arquivo LaTeX: 592

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

results = modeler.analyze_corpus_topics(sample_documents, n_topics=2)

print("Tópicos encontrados:")
for i, words in enumerate(results['topic_words']):
    print(f"Tópico {i}: {', '.join(words[:5])}")
