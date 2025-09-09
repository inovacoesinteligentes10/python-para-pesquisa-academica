# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Testes de Permutação
Linha original no arquivo LaTeX: 817

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def teste_permutacao(grupo1, grupo2, estatistica_func=None, n_perm=10000):
    """
    Realiza teste de permutacao para comparar dois grupos

    Parametros:
    -----------
    grupo1, grupo2 : array-like
        Dados dos dois grupos
    estatistica_func : function
        Funcao para calcular estatistica (default: diferenca de medias)
    n_perm : int
        Numero de permutacoes
    """

    if estatistica_func is None:
        estatistica_func = lambda g1, g2: np.mean(g1) - np.mean(g2)

    print("TESTE DE PERMUTACAO")
    print("=" * 20)

    # Estatistica observada
    stat_observada = estatistica_func(grupo1, grupo2)
    print(f"Estatistica observada: {stat_observada:.4f}")

    # Combinar todos os dados
    dados_combinados = np.concatenate([grupo1, grupo2])
    n1, n2 = len(grupo1), len(grupo2)

    return stat_observada, dados_combinados, n1, n2
