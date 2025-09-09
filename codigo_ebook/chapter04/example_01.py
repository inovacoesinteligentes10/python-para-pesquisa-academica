# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Verificação de Pressupostos
Linha original no arquivo LaTeX: 20

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.diagnostic import lilliefors

def verificar_pressupostos(dados, grupo_col=None, variavel_dependente=None):
    """
    Verifica pressupostos estatisticos fundamentais

    Parametros:
    -----------
    dados : DataFrame
        Dados para analise
    grupo_col : str, optional
        Nome da coluna com grupos (para teste de homogeneidade)
    variavel_dependente : str
        Nome da variavel dependente a ser testada
    """

    print("VERIFICACAO DE PRESSUPOSTOS ESTATISTICOS")
    print("="*50)

    return dados, grupo_col, variavel_dependente
