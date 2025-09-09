# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Gráficos Interativos Básicos
Linha original no arquivo LaTeX: 72

Este código foi extraído automaticamente do arquivo chapter10.tex
"""
import numpy as np


# Gráfico de dispersão interativo
fig_scatter = px.scatter(
    dados_estudo,
    x='bem_estar',
    y='produtividade',
    color='area',
    size='experiencia',
    hover_data=['idade', 'horas_trabalho', 'satisfacao_trabalho'],
    title='Relação entre Bem-estar e Produtividade por Área de Atuação',
    labels={
        'bem_estar': 'Índice de Bem-estar (1-10)',
        'produtividade': 'Índice de Produtividade (30-100)',
        'area': 'Área de Atuação',
        'experiencia': 'Anos de Experiência'
    }
)

# Personalizando o layout
fig_scatter.update_layout(
    width=800,
    height=600,
    font=dict(size=12),
    hovermode='closest'
)

# Adicionando linha de tendência
fig_scatter.add_scatter(
    x=dados_estudo['bem_estar'],
    y=np.poly1d(np.polyfit(dados_estudo['bem_estar'], dados_estudo['produtividade'], 1))(dados_estudo['bem_estar']),
    mode='lines',
    name='Tendência Linear',
    line=dict(color='red', dash='dash')
)

fig_scatter.show()
