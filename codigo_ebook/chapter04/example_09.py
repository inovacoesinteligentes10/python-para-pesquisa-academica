# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 323

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np


def calcular_tamanhos_efeito(grupo1, grupo2, t_stat):
    """Calcula diferentes tamanhos de efeito"""
    # TAMANHOS DE EFEITO
    print(f"\nTAMANHOS DE EFEITO:")
    print("-" * 18)

    # Cohen's d
    pooled_std = np.sqrt(((len(grupo1)-1)*grupo1.var() +
                         (len(grupo2)-1)*grupo2.var()) /
                        (len(grupo1)+len(grupo2)-2))
    cohens_d = (grupo1.mean() - grupo2.mean()) / pooled_std
    print(f"Cohen's d = {cohens_d:.3f}")

    # Glass's delta (usa DP do grupo controle)
    glass_delta = (grupo1.mean() - grupo2.mean()) / grupo2.std()
    print(f"Glass's delta = {glass_delta:.3f}")

    # r de Pearson (a partir do teste t)
    r_pearson = t_stat / np.sqrt(t_stat**2 + (len(grupo1) + len(grupo2) - 2))
    print(f"r de Pearson = {r_pearson:.3f}")

    # Interpretacao do tamanho do efeito
    if abs(cohens_d) < 0.2:
        interpretacao = "trivial"
    elif abs(cohens_d) < 0.5:
        interpretacao = "pequeno"
    elif abs(cohens_d) < 0.8:
        interpretacao = "medio"
    else:
        interpretacao = "grande"

    print(f"Interpretacao: efeito {interpretacao}")

    return cohens_d
