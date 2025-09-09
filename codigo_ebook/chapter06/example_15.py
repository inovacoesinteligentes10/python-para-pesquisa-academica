# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Framework Ético para Coleta
Linha original no arquivo LaTeX: 611

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/ethical_framework.py
import hashlib
import pandas as pd
import re
from typing import List

class EthicalDataProcessor:
    """Processador que aplica princípios éticos na coleta de dados"""

    def __init__(self, research_purpose: str, institution: str):
        self.research_purpose = research_purpose
        self.institution = institution

    def anonymize_identifiers(self, data: pd.DataFrame,
                             identifier_columns: List[str]) -> pd.DataFrame:
        """Remove ou anonimiza identificadores pessoais"""
        anonymized_data = data.copy()

        for col in identifier_columns:
            if col in anonymized_data.columns:
                # Criar hash irreversível para IDs únicos
                anonymized_data[f"{col}_hash"] = anonymized_data[col].apply(
                    lambda x: hashlib.sha256(str(x).encode()).hexdigest()[:12]
                )
                # Remover coluna original
                anonymized_data = anonymized_data.drop(columns=[col])

        return anonymized_data

    def remove_sensitive_content(self, text_series: pd.Series) -> pd.Series:
        """Remove conteúdo potencialmente sensível de textos"""
        cleaned_text = text_series.copy()

        # Padrões para remoção
        patterns = {
            'email': r'\b',
            'phone': r'\b2,3[-.\s]?4,5[-.\s]?4\b',
            'cpf': r'\b3\.?3\.?3[-.]?2\b'
        }

        for pattern_type, pattern in patterns.items():
            cleaned_text = cleaned_text.str.replace(
                pattern, f'[{pattern_type.upper()}_REMOVED]', regex=True
            )

        return cleaned_text
