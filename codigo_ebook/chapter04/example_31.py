# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Controle de Erro Tipo I em Múltiplas Comparações
Linha original no arquivo LaTeX: 1183

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
from scipy import stats


from statsmodels.stats.multitest import multipletests

def correcao_multiplas_comparacoes(p_valores, metodos=['bonferroni', 'holm', 'fdr_bh']):
    """
    Aplica diferentes metodos de correcao para multiplas comparacoes

    Parametros:
    -----------
    p_valores : array-like
        Lista de p-valores nao corrigidos
    metodos : list
        Metodos de correcao a aplicar
    """

    print("CORRECAO PARA MULTIPLAS COMPARACOES")
    print("=" * 40)

    p_valores = np.array(p_valores)
    n_testes = len(p_valores)

    print(f"Numero de testes: {n_testes}")
    print(f"P-valores originais: {p_valores}")
    print(f"Significativos sem correcao (alpha=0.05): {np.sum(p_valores < 0.05)}")

    # Calcular inflacao do erro Tipo I
    erro_familywise = 1 - (1 - 0.05)**n_testes
    print(f"Erro Tipo I familywise sem correcao: {erro_familywise:.3f}")

    print(f"\nCORRECOES APLICADAS:")
    print("-" * 20)

    return p_valores, n_testes
