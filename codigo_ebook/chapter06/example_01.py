# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Fundamentos do Web Scraping Ético
Linha original no arquivo LaTeX: 29

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/ethical_scraper.py
import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.robotparser import RobotFileParser
import logging
from typing import List, Dict, Optional

class EthicalScraper:
    """Scraper que segue princípios éticos de coleta"""

    def __init__(self, user_agent="Research Bot", contact_email="researcher@university.edu"):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'{user_agent} ({contact_email})',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        self.logger = logging.getLogger(__name__)
        self.delay_range = (1, 3)  # Segundos entre requisições

    def can_fetch(self, url: str) -> bool:
        """Verifica se é permitido fazer scraping da URL"""
        try:
            rp = RobotFileParser()
            rp.set_url(f"{url.split('/')[0]}//{url.split('/')[2]}/robots.txt")
            rp.read()
            return rp.can_fetch(self.session.headers['User-Agent'], url)
        except Exception as e:
            # Se não conseguir acessar robots.txt, assume que é permitido
            self.logger.warning(f"Erro ao verificar robots.txt: {e}")
            return True
    def respectful_request(self, url: str, **kwargs) -> Optional[requests.Response]:
        """Faz requisição respeitando delays e robots.txt"""
        if not self.can_fetch(url):
            self.logger.warning(f"Robots.txt proíbe acesso a {url}")
            return None
