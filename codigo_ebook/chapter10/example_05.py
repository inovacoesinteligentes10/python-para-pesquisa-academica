# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Visualizações Multidimensionais
Linha original no arquivo LaTeX: 147

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Matriz de correlação interativa
correlacoes = dados_estudo[variaveis_numericas].corr()

fig_heatmap = go.Figure(data=go.Heatmap(
    z=correlacoes.values,
    x=correlacoes.columns,
    y=correlacoes.columns,
    colorscale='RdBu',
    zmid=0,
    text=correlacoes.round(2).values,
    texttemplate="%{text}",
    textfont={"size": 10},
    hoverongaps=False
))

fig_heatmap.update_layout(
    title='Matriz de Correlação Interativa - Variáveis do Estudo',
    width=600,
    height=600,
    font=dict(size=12)
)

fig_heatmap.show()
