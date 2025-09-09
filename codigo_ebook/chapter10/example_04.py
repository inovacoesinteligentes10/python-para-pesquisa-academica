# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Gráficos Interativos Básicos
Linha original no arquivo LaTeX: 112

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Histograma interativo com seleção de variável
from ipywidgets import interact, Dropdown

def criar_histograma_interativo(variavel='bem_estar'):
    fig = px.histogram(
        dados_estudo,
        x=variavel,
        color='area',
        nbins=20,
        title=f'Distribuição de {variavel.replace("_", " ").title()}',
        barmode='overlay',
        opacity=0.7
    )

    fig.update_layout(
        width=700,
        height=500,
        bargap=0.1
    )

    return fig.show()

# Lista de variáveis disponíveis
variaveis_numericas = ['bem_estar', 'produtividade', 'horas_trabalho',
                      'satisfacao_trabalho', 'idade', 'experiencia']

print("Histograma Interativo - selecione uma variável:")
print("Disponível em ambiente Jupyter com widgets")
