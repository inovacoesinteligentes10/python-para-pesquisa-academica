# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Dicas de Performance e Otimização
Linha original no arquivo LaTeX: 952

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import pandas as pd


def otimizacao_memoria(n):
    # 3. Otimização de tipos
    print("\n3. Otimização de memória")

    # DataFrame com tipos não otimizados
    df_original = pd.DataFrame({
        'int_col': np.random.randint(0, 100, n),  # int64 por padrão
        'float_col': np.random.randn(n),  # float64 por padrão
        'cat_col': np.random.choice(['A', 'B', 'C'], n)  # object por padrão
    })

    # DataFrame com tipos otimizados
    df_otimizado = pd.DataFrame({
        'int_col': np.random.randint(0, 100, n).astype('int8'),  # Suficiente para 0-100
        'float_col': np.random.randn(n).astype('float32'),  # Precisão suficiente
        'cat_col': pd.Categorical(np.random.choice(['A', 'B', 'C'], n))  # Categórico
    })

    memoria_original = df_original.memory_usage(deep=True).sum() / 1024**2
    memoria_otimizada = df_otimizado.memory_usage(deep=True).sum() / 1024**2

    print(f"   Memória original: {memoria_original:.1f} MB")
    print(f"   Memória otimizada: {memoria_otimizada:.1f} MB")
    print(f"   Economia: {(1 - memoria_otimizada/memoria_original)*100:.1f}%")

# Executar comparação completa
dados, n = comparar_performance()
resultado_manual, resultado_groupby = comparar_performance_continuacao(dados)
otimizacao_memoria(n)
