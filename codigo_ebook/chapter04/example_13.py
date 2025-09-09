# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Regressão Robusta
Linha original no arquivo LaTeX: 492

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
from scipy import stats


def diagnosticos_residuos(modelo, X_const):
    """Executa diagnosticos completos dos residuos"""
    # 2. DIAGNOSTICOS DE RESIDUOS
    print(f"\n2. DIAGNOSTICOS DE RESIDUOS")
    print("-" * 27)

    residuos = modelo.resid
    valores_preditos = modelo.fittedvalues
    residuos_estudentizados = modelo.get_influence().resid_studentized_external

    # Teste de normalidade dos residuos
    stat_norm, p_norm = stats.shapiro(residuos)
    print(f"Normalidade dos residuos (Shapiro): p = {p_norm:.3f}")

    # Teste de homocedasticidade
    bp_stat, bp_p, _, _ = het_breuschpagan(residuos, X_const)
    print(f"Homocedasticidade (Breusch-Pagan): p = {bp_p:.3f}")

    white_stat, white_p, _, _ = het_white(residuos, X_const)
    print(f"Homocedasticidade (White): p = {white_p:.3f}")

    # Teste de independencia (Durbin-Watson)
    dw_stat = durbin_watson(residuos)
    print(f"Independencia (Durbin-Watson): {dw_stat:.3f}")
    print(f"  (Valores entre 1.5-2.5 indicam independencia)")

    # Deteccao de outliers
    outliers_residuos = np.where(np.abs(residuos_estudentizados) > 3)[0]
    print(f"Outliers detectados (|resid| > 3): {len(outliers_residuos)}")

    return residuos, valores_preditos, residuos_estudentizados, p_norm, bp_p, white_p, dw_stat, outliers_residuos
