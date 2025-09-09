# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Fundamentos do Web Scraping Ético
Linha original no arquivo LaTeX: 147

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# Continuação: src/data_collection/news_scraper.py

import pandas as pd
from bs4 import BeautifulSoup
from typing import List
import logging

class NewsScraper:
    def __init__(self):
        self.articles = []
        self.logger = logging.getLogger(__name__)
    
    def respectful_request(self, url):
        """Método placeholder para requisições"""
        import requests
        try:
            response = requests.get(url)
            return response
        except:
            return None
    
    def extract_article_data(self, soup, url):
        """Extrai dados do artigo"""
        return {
            'title': soup.title.string if soup.title else '',
            'content': soup.get_text(),
            'url': url
        }

    def search_climate_articles(self, base_urls: List[str],
                               keywords: List[str],
                               max_articles: int = 100) -> pd.DataFrame:
        """Busca artigos sobre mudanças climáticas"""
        self.logger.info(f"Iniciando coleta de até {max_articles} artigos")

        for base_url in base_urls:
            self.logger.info(f"Processando {base_url}")

            # Buscar URLs de artigos
            article_urls = self._find_article_urls(base_url)

            for url in article_urls[:max_articles]:
                response = self.respectful_request(url)
                if response:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    article_data = self.extract_article_data(soup, url)

                    # Verificar se contém palavras-chave sobre clima
                    if self._contains_climate_keywords(article_data['content'], keywords):
                        self.articles.append(article_data)
                        self.logger.info(f"Artigo coletado: {article_data['title'][:50]}...")

                if len(self.articles) >= max_articles:
                    break

        return pd.DataFrame(self.articles)

    def _contains_climate_keywords(self, text: str, keywords: List[str]) -> bool:
        """Verifica se o texto contém palavras-chave relacionadas ao clima"""
        text_lower = text.lower()
        return any(keyword.lower() in text_lower for keyword in keywords)

    def _find_article_urls(self, base_url: str) -> List[str]:
        """Encontra URLs de artigos no site"""
        response = self.respectful_request(base_url)
        if not response:
            return []
