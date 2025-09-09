# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Framework de Validação
Linha original no arquivo LaTeX: 567

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

import pandas as pd
from datetime import datetime

class DataQualityValidator:
    def __init__(self):
        self.validation_rules = {}
    
    def add_validation_rule(self, name, func):
        """Adiciona regra de validação"""
        self.validation_rules[name] = func
    
    def validate_data(self, data):
        """Executa validações nos dados"""
        report = {
            'issues': [],
            'quality_score': 100
        }
        
        # Executar validações customizadas
        for rule_name, rule_func in self.validation_rules.items():
            try:
                result = rule_func(data)
                if not result['passed']:
                    report['issues'].append({
                        'rule': rule_name,
                        'message': result['message']
                    })
                    report['quality_score'] -= 10
            except Exception as e:
                report['issues'].append({
                    'rule': rule_name,
                    'message': f"Erro na validação: {str(e)}"
                })
        
        return report

# Exemplo de uso
validator = DataQualityValidator()

def validate_date_range(data):
    """Valida se datas estão em range aceitável"""
    if 'created_at' not in data.columns:
        return {'passed': True, 'message': 'Sem coluna de data'}

    dates = pd.to_datetime(data['created_at'], errors='coerce')
    future_dates = (dates > datetime.now()).sum()

    if future_dates > 0:
        return {'passed': False, 'message': f'{future_dates} datas futuras encontradas'}

    return {'passed': True, 'message': 'Datas válidas'}

validator.add_validation_rule('date_range', validate_date_range)
