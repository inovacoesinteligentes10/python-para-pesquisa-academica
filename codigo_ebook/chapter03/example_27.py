# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Dicas de Performance e Otimização
Linha original no arquivo LaTeX: 880

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

import time

# Demonstração de diferenças de performance
def comparar_performance():
    """Compara diferentes abordagens para operações comuns"""

    # Dados de teste
    n = 1000000
    dados = pd.DataFrame({
        'grupo': np.random.choice(['A', 'B'], n),
        'valor': np.random.randn(n)
    })

    print("COMPARAÇÃO DE PERFORMANCE")
    print("="*40)

    # 1. Loop vs Vetorização
    print("1. Calcular quadrado dos valores")

    # Método lento: loop Python
    inicio = time.time()
    resultado_loop = []
    for valor in dados['valor']:
        resultado_loop.append(valor ** 2)
    tempo_loop = time.time() - inicio

    # Método rápido: vetorização NumPy
    inicio = time.time()
    resultado_numpy = dados['valor'] ** 2
    tempo_numpy = time.time() - inicio

    print(f"   Loop Python: {tempo_loop:.3f}s")
    print(f"   NumPy: {tempo_numpy:.3f}s")
    print(f"   Speedup: {tempo_loop/tempo_numpy:.1f}x")

    return dados, n
