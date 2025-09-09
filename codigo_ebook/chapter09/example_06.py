# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Importação e Preparação de Dados Temporais
Linha original no arquivo LaTeX: 99

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

publicacoes = (base_pub + crescimento + sazon_acad +
               eventos_esp + ruido).astype(int)
publicacoes = np.maximum(publicacoes, 10)  # Mínimo de 10 publicações

# Criando DataFrame principal
df_academico = pd.DataFrame({
    'data': datas_pub,
    'publicacoes': publicacoes,
    'ano': datas_pub.year,
    'mes': datas_pub.month,
    'trimestre': datas_pub.quarter
})

# Configurando índice temporal
df_academico.set_index('data', inplace=True)
