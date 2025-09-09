# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 720

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


def pipeline_testes_estatisticos(dados_limpos):
    # Teste t
    from scipy import stats
    controle = dados_limpos[dados_limpos['grupo'] == 'controle']['melhoria']
    experimental = dados_limpos[dados_limpos['grupo'] == 'experimental']['melhoria']

    t_stat, p_valor = stats.ttest_ind(experimental, controle)

    # Tamanho do efeito
    def cohen_d(grupo1, grupo2):
        n1, n2 = len(grupo1), len(grupo2)
        s_pooled = np.sqrt(((n1-1)*grupo1.var() + (n2-1)*grupo2.var()) / (n1+n2-2))
        return (grupo1.mean() - grupo2.mean()) / s_pooled

    d = cohen_d(experimental, controle)

    print(f"   Teste t: t = {t_stat:.3f}, p = {p_valor:.3f}")
    print(f"   Cohen's d = {d:.3f}")

    return controle, experimental, t_stat, p_valor, d
