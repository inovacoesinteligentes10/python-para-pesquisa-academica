# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Slides Interativos com Dados
Linha original no arquivo LaTeX: 767

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Slide com gráfico interativo
def criar_slide_com_grafico(titulo, dados, tipo_grafico="bar"):
    """Cria slide com gráfico incorporado"""

    if tipo_grafico == "bar":
        # Gráfico de barras comparativo
        stats_grupos = dados.groupby('grupo').agg({
            'pre_teste': ['mean', 'std'],
            'pos_teste': ['mean', 'std'],
            'ganho_aprendizado': ['mean', 'std']
        }).round(2)

        fig = go.Figure()

        grupos = stats_grupos.index
        fig.add_trace(go.Bar(
            name='Pré-teste',
            x=grupos,
            y=stats_grupos['pre_teste']['mean'],
            error_y=dict(type='data', array=stats_grupos['pre_teste']['std']),
            marker_color='lightblue'
        ))

        fig.add_trace(go.Bar(
            name='Pós-teste',
            x=grupos,
            y=stats_grupos['pos_teste']['mean'],
            error_y=dict(type='data', array=stats_grupos['pos_teste']['std']),
            marker_color='darkblue'
        ))

        fig.update_layout(
            title=f'{titulo}',
            xaxis_title='Grupo',
            yaxis_title='Pontuação',
            barmode='group',
            font=dict(size=16),
            height=500,
            template='plotly_white'
        )
