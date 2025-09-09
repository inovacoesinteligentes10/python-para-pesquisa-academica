# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Regressão Robusta
Linha original no arquivo LaTeX: 458

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, het_white
from statsmodels.stats.stattools import durbin_watson
from sklearn.linear_model import HuberRegressor
from sklearn.metrics import r2_score

def regressao_completa(dados, variavel_dep, preditores):
    """
    Executa regressao linear completa com diagnosticos
    """

    print("ANALISE DE REGRESSAO COMPLETA")
    print("="*35)

    # Preparar dados
    X = dados[preditores]
    y = dados[variavel_dep]
    X_const = sm.add_constant(X)  # Adicionar intercepto

    # 1. REGRESSAO LINEAR CLASSICA
    print("1. REGRESSAO LINEAR CLASSICA")
    print("-" * 28)

    modelo = sm.OLS(y, X_const).fit()
    print(modelo.summary())

    return modelo, X, y, X_const
