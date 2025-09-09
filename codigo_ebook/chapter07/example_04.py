# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Limpeza e Normalização de Texto
Linha original no arquivo LaTeX: 132

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

def tokenize(self, text: str, remove_stopwords: bool = True) -> List[str]:
        """Tokeniza texto em palavras"""
        # Limpeza básica
        cleaned_text = self.clean_text(text)

        # Tokenização simples por espaços
        tokens = cleaned_text.split()

        # Remover stopwords
        if remove_stopwords:
            tokens = [token for token in tokens if token not in self.stopwords]

        # Filtrar tokens muito curtos
        tokens = [token for token in tokens if len(token) > 2]

        return tokens
