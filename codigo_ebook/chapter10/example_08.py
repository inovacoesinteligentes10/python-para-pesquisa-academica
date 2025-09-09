# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Animações e Séries Temporais
Linha original no arquivo LaTeX: 276

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Gráfico animado mostrando evolução temporal
fig_animado = px.scatter(
    df_temporal,
    x='bem_estar_medio',
    y='produtividade_media',
    color='area',
    animation_frame='ano',
    animation_group='area',
    size_max=20,
    range_x=[5, 8],
    range_y=[60, 85],
    title='Evolução Temporal: Bem-estar vs Produtividade por Área',
    labels={
        'bem_estar_medio': 'Bem-estar Médio',
        'produtividade_media': 'Produtividade Média',
        'area': 'Área de Atuação'
    }
)

fig_animado.update_layout(
    width=800,
    height=600,
    font=dict(size=12)
)

fig_animado.show()
