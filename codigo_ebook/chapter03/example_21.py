# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 654

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import pandas as pd


# Simulação de pipeline completo de pesquisa
def pipeline_completo_pesquisa():
    """
    Demonstra workflow típico: dados -> limpeza -> análise -> visualização
    """
    print("PIPELINE COMPLETO DE ANÁLISE DE PESQUISA")
    print("="*50)

    # 1. COLETA DE DADOS (simulada)
    print("1. Coletando dados...")
    np.random.seed(42)

    dados_brutos = pd.DataFrame({
        'participante': range(1, 301),
        'grupo': np.random.choice(['controle', 'experimental'], 300),
        'pre_teste': np.random.normal(50, 10, 300),
        'pos_teste': np.random.normal(55, 12, 300),
        'idade': np.random.randint(18, 65, 300),
        'genero': np.random.choice(['M', 'F'], 300),
        'tempo_reacao': np.random.lognormal(6, 0.3, 300)  # Distribuição realista
    })

    # Introduzir efeito realista do tratamento
    mask_experimental = dados_brutos['grupo'] == 'experimental'
    dados_brutos.loc[mask_experimental, 'pos_teste'] += np.random.normal(8, 3, mask_experimental.sum())

    print(f"   Dados coletados: {len(dados_brutos)} participantes")
    return dados_brutos
