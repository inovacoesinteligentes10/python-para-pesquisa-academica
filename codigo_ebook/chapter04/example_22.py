# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Testes de Permutação
Linha original no arquivo LaTeX: 853

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def permutacao_distribuicao_nula(stat_observada, dados_combinados, n1, n2, estatistica_func, n_perm=10000):
    """Gera distribuicao nula e calcula p-valor"""
    # Gerar distribuicao nula por permutacao
    stats_permutacao = []

    for i in range(n_perm):
        # Permutacao aleatoria
        dados_permutados = np.random.permutation(dados_combinados)

        # Dividir novamente nos grupos originais
        perm_g1 = dados_permutados[:n1]
        perm_g2 = dados_permutados[n1:]

        # Calcular estatistica para esta permutacao
        stat_perm = estatistica_func(perm_g1, perm_g2)
        stats_permutacao.append(stat_perm)

    stats_permutacao = np.array(stats_permutacao)

    # Calcular p-valor
    # Para teste bilateral
    p_valor = np.mean(np.abs(stats_permutacao) >= np.abs(stat_observada))

    print(f"P-valor (bilateral): {p_valor:.4f}")

    return stats_permutacao, p_valor
