# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Limpeza e Transformação de Dados
Linha original no arquivo LaTeX: 339

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# Pipeline de limpeza
dados_limpos = dados_sujos.copy()

# 1. Filtrar idades válidas (18-65)
mask_idade_valida = (dados_limpos['idade'] >= 18) & (dados_limpos['idade'] <= 65)
dados_limpos = dados_limpos[mask_idade_valida]

# 2. Remover outliers extremos do score (fora de 3 desvios padrão)
mean_score = dados_limpos['score'].mean()
std_score = dados_limpos['score'].std()
limite_inferior = mean_score - 3 * std_score
limite_superior = mean_score + 3 * std_score

mask_score_valido = (dados_limpos['score'] >= limite_inferior) & \
                   (dados_limpos['score'] <= limite_superior)
dados_limpos = dados_limpos[mask_score_valido | dados_limpos['score'].isnull()]

# 3. Tratar valores ausentes - Imputar pela média do grupo
dados_limpos['score'] = dados_limpos.groupby('grupo')['score'].transform(
    lambda x: x.fillna(x.mean())
)
