# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Fundamentos do Web Scraping Ético
Linha original no arquivo LaTeX: 75

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

import requests
import time
import random
import logging

class EthicalScraper:
    def __init__(self):
        self.session = requests.Session()
        self.delay_range = (1, 3)
        self.logger = logging.getLogger(__name__)
    
    def respectful_request(self, url, **kwargs):
        """Faz requisição com delay aleatório"""
        # Delay aleatório entre requisições
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)

        try:
            response = self.session.get(url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            self.logger.error(f"Erro ao acessar {url}: {e}")
            return None
