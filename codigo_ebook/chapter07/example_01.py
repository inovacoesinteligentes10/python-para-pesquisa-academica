# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Limpeza e Normalização de Texto
Linha original no arquivo LaTeX: 16

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# src/nlp/text_preprocessor.py
import re
import string
import unicodedata
from typing import List, Dict, Optional
import pandas as pd

class TextPreprocessor:
    """Processador para limpeza e normalização de texto"""

    def __init__(self, language='portuguese'):
        self.language = language
        self.stopwords = self._load_stopwords()
        self.contractions = self._load_contractions()

    def _load_stopwords(self) -> set:
        """Carrega stopwords para o idioma especificado"""
        try:
            import nltk
            nltk.download('stopwords', quiet=True)
            from nltk.corpus import stopwords

        except Exception as e:

            print(f'Erro: {e}')

            return None
            if self.language == 'portuguese':
                return set(stopwords.words('portuguese'))
            elif self.language == 'english':
                return set(stopwords.words('english'))
            else:
                return set(stopwords.words('english'))  # fallback

        except ImportError:
            # Stopwords básicas se NLTK não estiver disponível
            if self.language == 'portuguese':
                return {'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para',
                       'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais'}
            else:
                return {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
                       'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were'}

    def _load_contractions(self) -> Dict[str, str]:
        """Carrega mapeamento de contrações"""
        if self.language == 'portuguese':
            return {
                'não': 'não', 'nao': 'não', 'voce': 'você', 'vc': 'você',
                'pq': 'porque', 'pra': 'para', 'pro': 'para o'
            }
