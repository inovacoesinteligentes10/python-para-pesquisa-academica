# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Limpeza e Normalização de Texto
Linha original no arquivo LaTeX: 65

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

class ContractionExpander:
    def __init__(self, language='en'):
        self.language = language
    
    def get_contractions(self):
        """Retorna dicionário de contrações"""
        if self.language == 'pt':
            return {
                "não": "nao", "é": "eh", "está": "esta"
            }
        else:  # English
            return {
                "can't": "cannot", "won't": "will not", "n't": " not",
                "'re": " are", "'ve": " have", "'ll": " will", "'d": " would",
                "'m": " am", "it's": "it is", "that's": "that is"
            }
