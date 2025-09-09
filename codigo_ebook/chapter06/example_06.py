# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Cliente Genérico para APIs REST
Linha original no arquivo LaTeX: 217

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/api_client.py
import requests
import pandas as pd
from typing import Dict, List, Optional
import time
from datetime import datetime

class APIClient:
    """Cliente genérico para APIs REST"""

    def __init__(self, base_url: str, api_key: Optional[str] = None,
                 rate_limit: float = 1.0):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.rate_limit = rate_limit
        self.session = requests.Session()

        # Headers padrão
        self.session.headers.update({
            'User-Agent': 'Research-Python-Client/1.0',
            'Accept': 'application/json',
        })

        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })

        self.last_request_time = 0

    def _respect_rate_limit(self):
        """Respeita limite de taxa da API"""
        now = time.time()
        time_since_last = now - self.last_request_time

        if time_since_last < self.rate_limit:
            time.sleep(self.rate_limit - time_since_last)

        self.last_request_time = time.time()
