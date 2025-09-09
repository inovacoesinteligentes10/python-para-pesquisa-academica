# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Cliente Genérico para APIs REST
Linha original no arquivo LaTeX: 285

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/world_bank_api.py
from api_client import APIClient
import pandas as pd
from typing import List

class WorldBankAPI(APIClient):
    """Cliente especializado para API do Banco Mundial"""

    def __init__(self):
        super().__init__("http://api.worldbank.org/v2", rate_limit=0.5)

    def get_indicators(self, country_codes: List[str],
                      indicator_codes: List[str],
                      start_year: int = 2000,
                      end_year: int = 2023) -> pd.DataFrame:
        """Obtém indicadores econômicos para países específicos"""
        all_data = []

        for country in country_codes:
            for indicator in indicator_codes:
                endpoint = f"countries/{country}/indicators/{indicator}"
                params = {
                    'format': 'json',
                    'date': f'{start_year}:{end_year}',
                    'per_page': 100
                }

                data = self.get(endpoint, params)

                if len(data) > 1 and data[1]:
                    for record in data[1]:
                        if record['value'] is not None:
                            all_data.append({
                                'country_code': country,
                                'indicator_code': indicator,
                                'year': int(record['date']),
                                'value': float(record['value']),
                                'country_name': record['country']['value'],
                                'indicator_name': record['indicator']['value']
                            })

        return pd.DataFrame(all_data)
