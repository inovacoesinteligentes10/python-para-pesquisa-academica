# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Dicas de Performance e Otimização
Linha original no arquivo LaTeX: 923

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

def comparar_performance_continuacao(dados):
    # 2. Agrupamento eficiente
    print("\n2. Calcular média por grupo")

    # Método lento: loop manual
    inicio = time.time()
    resultado_manual = {}
    for grupo in ['A', 'B']:
        mask = dados['grupo'] == grupo
        resultado_manual[grupo] = dados.loc[mask, 'valor'].mean()
    tempo_manual = time.time() - inicio

    # Método rápido: groupby
    inicio = time.time()
    resultado_groupby = dados.groupby('grupo')['valor'].mean()
    tempo_groupby = time.time() - inicio

    print(f"   Loop manual: {tempo_manual:.3f}s")
    print(f"   GroupBy: {tempo_groupby:.3f}s")
    print(f"   Speedup: {tempo_manual/tempo_groupby:.1f}x")

    return resultado_manual, resultado_groupby
