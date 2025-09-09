# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1002

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import pandas as pd


# Análise de incerteza por período sazonal
incerteza_sazonal = []
for i, data_futura in enumerate(datas_futuras):
    mes = data_futura.month

    # Histórico de variabilidade para o mesmo mês
    dados_mes = df_academico[df_academico.index.month == mes]['publicacoes']
    variabilidade_historica = dados_mes.std()

    # Incerteza da previsão
    ic_amplitude = ic_futuro.iloc[i, 1] - ic_futuro.iloc[i, 0]

    incerteza_sazonal.append({
        'mes': mes,
        'data': data_futura,
        'previsao': previsao_futura.iloc[i],
        'ic_inferior': ic_futuro.iloc[i, 0],
        'ic_superior': ic_futuro.iloc[i, 1],
        'variabilidade_historica': variabilidade_historica,
        'amplitude_ic': ic_amplitude
    })

df_incerteza = pd.DataFrame(incerteza_sazonal)
