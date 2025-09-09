# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Framework de Validação
Linha original no arquivo LaTeX: 526

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/data_validator.py
import pandas as pd
from datetime import datetime
from typing import Dict, Callable

class DataQualityValidator:
    """Sistema de validação de qualidade de dados coletados"""

    def __init__(self):
        self.validation_rules = {}

    def add_validation_rule(self, rule_name: str, validator_func: Callable):
        """Adiciona regra de validação personalizada"""
        self.validation_rules[rule_name] = validator_func

    def validate_dataset(self, data: pd.DataFrame, dataset_name: str = "unnamed") -> Dict:
        """Executa todas as validações em um dataset"""
        report = {
            'dataset_name': dataset_name,
            'timestamp': datetime.now(),
            'total_rows': len(data),
            'total_columns': len(data.columns),
            'issues': [],
            'quality_score': 100.0
        }

        # Validações básicas
        missing_data = data.isnull().sum()
        duplicates = data.duplicated().sum()

        # Penalizar qualidade por problemas
        missing_penalty = (missing_data.sum() / (len(data) * len(data.columns))) * 50
        duplicate_penalty = (duplicates / len(data)) * 30

        report['quality_score'] -= (missing_penalty + duplicate_penalty)
