# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Sistema de Templates para Documentação Científica
Linha original no arquivo LaTeX: 1354

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

class TemplatesCientificos:
    """Sistema de templates para documentação científica"""

    def __init__(self):
        self.templates = {}
        self.carregar_templates()

    def carregar_templates(self):
        """Carrega templates predefinidos"""

        # Template de artigo científico
        self.templates['artigo'] = """
# {{ titulo }}

**{{ autores }}**
*{{ afiliacao }}*

## Resumo
{{ resumo }}

**Palavras-chave:** {{ palavras_chave }}

## 1. Introdução
{{ introducao }}

## 2. Metodologia

### 2.1 Participantes
{{ participantes }}

### 2.2 Procedimentos
{{ procedimentos }}

### 2.3 Análise de Dados
{{ analise_dados }}

## 3. Resultados
{{ resultados }}

## 4. Discussão
{{ discussao }}

"""