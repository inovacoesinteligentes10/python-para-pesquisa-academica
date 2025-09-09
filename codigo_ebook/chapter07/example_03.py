# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Limpeza e Normalização de Texto
Linha original no arquivo LaTeX: 79

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# Continuação: src/nlp/text_preprocessor.py

import re
import string
import unicodedata

class TextPreprocessor:
    def __init__(self):
        self.contractions = {
            "can't": "cannot", "won't": "will not", "n't": " not"
        }

    def clean_text(self, text: str,
                   remove_urls: bool = True,
                   remove_mentions: bool = True,
                   remove_hashtags: bool = False,
                   remove_numbers: bool = False,
                   remove_punctuation: bool = True,
                   lowercase: bool = True) -> str:
        """Aplica limpeza básica ao texto"""

        if not isinstance(text, str):
            return ""

        # Normalizar unicode
        text = unicodedata.normalize('NFKD', text)

        # Remover URLs
        if remove_urls:
            text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

        # Remover menções (@usuario)
        if remove_mentions:
            text = re.sub(r'@\w+', '', text)

        # Remover hashtags (mas manter o texto)
        if remove_hashtags:
            text = re.sub(r'#(\w+)', r'\1', text)

        # Remover números
        if remove_numbers:
            text = re.sub(r'\d+', '', text)

        # Expandir contrações
        for contraction, expansion in self.contractions.items():
            text = re.sub(r'\b' + contraction + r'\b', expansion, text, flags=re.IGNORECASE)

        # Converter para minúsculas
        if lowercase:
            text = text.lower()

        # Remover pontuação
        if remove_punctuation:
            text = text.translate(str.maketrans('', '', string.punctuation))

        # Remover espaços extras
        text = re.sub(r'\s+', ' ', text).strip()

        return text
