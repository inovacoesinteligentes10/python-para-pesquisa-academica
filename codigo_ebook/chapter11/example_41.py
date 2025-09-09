# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Sistema de Templates para Documentação Científica
Linha original no arquivo LaTeX: 1547

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Gerando artigo
artigo = templates.gerar_documento('artigo', dados_artigo)
templates.salvar_documento(artigo, 'artigo_cientifico.md')
