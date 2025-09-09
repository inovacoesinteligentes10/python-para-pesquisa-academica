# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Operações de Agrupamento e Análise
Linha original no arquivo LaTeX: 236

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# Calcular melhoria (diferença pré-pós teste)
df['melhoria'] = df['pos_teste'] - df['pre_teste']

# Analise por grupo
analise_grupo = df.groupby('grupo').agg({
    'idade': ['mean', 'std', 'count'],
    'pre_teste': ['mean', 'std'],
    'pos_teste': ['mean', 'std'],
    'melhoria': ['mean', 'std'],
    'satisfacao': ['mean', 'std']
}).round(2)

print("Análise por grupo:")
print(analise_grupo)

# Análise mais detalhada com múltiplas variáveis
analise_detalhada = df.groupby(['grupo', 'genero']).agg({
    'melhoria': ['count', 'mean', 'std'],
    'satisfacao': 'mean'
}).round(2)

print(f"\nAnálise por grupo e gênero:")
print(analise_detalhada)
