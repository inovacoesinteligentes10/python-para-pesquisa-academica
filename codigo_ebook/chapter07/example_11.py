# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 7
Seção: Reconhecimento de Entidades Nomeadas (NER)
Linha original no arquivo LaTeX: 371

Este código foi extraído automaticamente do arquivo chapter7.tex
"""

# src/nlp/entity_extractor.py
import re
import pandas as pd
from typing import List, Dict
from collections import defaultdict

class EntityExtractor:
    """Extrator de entidades nomeadas de texto"""

    def __init__(self, language='portuguese'):
        self.language = language
        self.patterns = self._load_patterns()

    def _load_patterns(self) -> Dict[str, str]:
        """Carrega padrões regex para diferentes tipos de entidades"""
        return {
            'email': r'\b',
            'phone_br': r'\b(?:\(2\)\s?)?4,5[-\s]?4\b',
            'cpf': r'\b3\.?3\.?3[-.]?2\b',
            'date_br': r'\b1,2[\/\-\.]1,2[\/\-\.]2,4\b',
            'money_br': r'R$\s*1,3(?:\.3)*(?:,2)?',
            'hashtag': r'#\w+',
            'mention': r'@\w+',
        }
