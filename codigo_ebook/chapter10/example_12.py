# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Fundamentos dos Jupyter Widgets
Linha original no arquivo LaTeX: 406

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Widget básico para exploração de dados
def explorar_distribuicoes(dados):
    """Cria widgets para explorar distribuições de variáveis"""

    # Definindo opções
    variaveis = ['bem_estar', 'produtividade', 'satisfacao_trabalho', 'idade', 'experiencia']
    areas = ['Todas'] + list(dados['area'].unique())
    tipos_grafico = ['Histograma', 'Box Plot', 'Density Plot']

    # Criando widgets
    widget_variavel = widgets.Dropdown(
        options=variaveis,
        value='bem_estar',
        description='Variável:'
    )

    widget_area = widgets.Dropdown(
        options=areas,
        value='Todas',
        description='Área:'
    )

    widget_tipo = widgets.Dropdown(
        options=tipos_grafico,
        value='Histograma',
        description='Tipo:'
    )

    widget_bins = widgets.IntSlider(
        value=20,
        min=5,
        max=50,
        step=5,
        description='Bins:'
    )

    # Interface interativa
    interface = interactive(
        plotar_distribuicao,
        variavel=widget_variavel,
        area=widget_area,
        tipo_grafico=widget_tipo,
        bins=widget_bins
    )

    return interface
