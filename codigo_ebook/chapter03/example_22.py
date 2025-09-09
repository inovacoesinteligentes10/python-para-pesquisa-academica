# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 689

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


def pipeline_limpeza_analise(dados_brutos):
    # 2. LIMPEZA DE DADOS
    print("2. Limpando dados...")

    # Remover outliers extremos no tempo de reação (> 3 DP)
    tr_mean = dados_brutos['tempo_reacao'].mean()
    tr_std = dados_brutos['tempo_reacao'].std()
    mask_tr_valido = np.abs(dados_brutos['tempo_reacao'] - tr_mean) <= 3 * tr_std

    dados_limpos = dados_brutos[mask_tr_valido].copy()
    print(f"   Outliers removidos: {len(dados_brutos) - len(dados_limpos)}")

    # 3. ANALISE ESTATISTICA
    print("3. Realizando análises...")

    # Calcular melhoria
    dados_limpos['melhoria'] = dados_limpos['pos_teste'] - dados_limpos['pre_teste']

    # Analise por grupo
    resultados_grupo = dados_limpos.groupby('grupo')['melhoria'].agg(['count', 'mean', 'std'])
    print(f"   Resultados por grupo:")
    print(resultados_grupo)

    return dados_limpos, resultados_grupo
