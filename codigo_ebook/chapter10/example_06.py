# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Visualizações Multidimensionais
Linha original no arquivo LaTeX: 175

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Gráfico de coordenadas paralelas
fig_parallel = go.Figure(data=go.Parcoords(
    line=dict(
        color=dados_estudo['bem_estar'],
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title="Bem-estar")
    ),
    dimensions=[
        dict(
            range=[dados_estudo['idade'].min(), dados_estudo['idade'].max()],
            label='Idade',
            values=dados_estudo['idade']
        ),
        dict(
            range=[dados_estudo['experiencia'].min(), dados_estudo['experiencia'].max()],
            label='Experiência',
            values=dados_estudo['experiencia']
        ),
        dict(
            range=[dados_estudo['horas_trabalho'].min(), dados_estudo['horas_trabalho'].max()],
            label='Horas Trabalho',
            values=dados_estudo['horas_trabalho']
        ),
        dict(
            range=[dados_estudo['bem_estar'].min(), dados_estudo['bem_estar'].max()],
            label='Bem-estar',
            values=dados_estudo['bem_estar']
        ),
        dict(
            range=[dados_estudo['produtividade'].min(), dados_estudo['produtividade'].max()],
            label='Produtividade',
            values=dados_estudo['produtividade']
        ),
        dict(
            range=[dados_estudo['satisfacao_trabalho'].min(), dados_estudo['satisfacao_trabalho'].max()],
            label='Satisfação',
            values=dados_estudo['satisfacao_trabalho']
        )
    ]
))

fig_parallel.update_layout(
    title='Coordenadas Paralelas - Análise Multivariada',
    font=dict(size=12)
)

fig_parallel.show()
