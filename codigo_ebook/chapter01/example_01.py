# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 1
Seção: Por que Python Conquistou a Academia?
Linha original no arquivo LaTeX: 16

Este código foi extraído automaticamente do arquivo chapter1.tex
"""

from Bio import SeqIO
import pandas as pd

# Carregar e analisar sequências de DNA
sequences = []
for record in SeqIO.parse("sequences.fasta", "fasta"):
    gc_content = (record.seq.count("G") + record.seq.count("C")) / len(record.seq)
    sequences.append({
        "id": record.id,
        "length": len(record.seq),
        "gc_content": gc_content
    })

df = pd.DataFrame(sequences)
print(f"GC médio: {df['gc_content'].mean():.2%}")
