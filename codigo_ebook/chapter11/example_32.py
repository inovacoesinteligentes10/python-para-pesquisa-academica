# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Padrões de Qualidade para Publicação
Linha original no arquivo LaTeX: 1167

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Scatter plot pré vs pós
criar_grafico_publicacao(
    dados_estudo,
    tipo='scatter',
    titulo='Relação entre Pré-teste e Pós-teste por Grupo',
    xlabel='Pontuação Pré-teste',
    ylabel='Pontuação Pós-teste',
    filename='figura3_correlacao_pre_pos.png'
)
