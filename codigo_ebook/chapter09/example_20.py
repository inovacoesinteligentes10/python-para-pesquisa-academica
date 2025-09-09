# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Fundamentos dos Modelos ARIMA
Linha original no arquivo LaTeX: 361

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Teste de estacionariedade (Teste de Dickey-Fuller Aumentado)
def teste_estacionariedade(serie, titulo='Série'):
    """Realiza teste de estacionariedade e exibe resultados"""
    resultado = adfuller(serie.dropna())

    print(f'Teste de Estacionariedade - {titulo}:')
    print(f'Estatística ADF: {resultado[0]:.6f}')
    print(f'p-valor: {resultado[1]:.6f}')
    print(f'Valores críticos:')
    for chave, valor in resultado[4].items():
        print(f'chave: {valor:.3f}')

    if resultado[1] <= 0.05:
        print("Resultado: A série é estacionária (rejeita H0)")
    else:
        print("Resultado: A série não é estacionária (não rejeita H0)")
    print('-' * 50)
