# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Fundamentos do Web Scraping Ético
Linha original no arquivo LaTeX: 97

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/news_scraper.py
from ethical_scraper import EthicalScraper
import pandas as pd
from datetime import datetime
import re
from urllib.parse import urljoin

class NewsArticleScraper(EthicalScraper):
    """Coletor especializado para artigos de notícias"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.articles = []

    def extract_article_data(self, soup, url: str) -> Dict:
        """Extrai dados estruturados de um artigo"""
        article_data = {
            'url': url,
            'collected_at': datetime.now(),
            'title': '',
            'content': '',
            'author': '',
            'publish_date': ''
        }

        # Título do artigo
        title_selectors = ['h1', '.article-title', '.post-title', 'title']
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                article_data['title'] = title_elem.get_text().strip()
                break

        # Conteúdo principal
        content_selectors = ['.article-content', '.post-content', 'article']
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                # Remove scripts e estilos
                for script in content_elem(["script", "style"]):
                    script.decompose()
                article_data['content'] = content_elem.get_text().strip()
                break

        return article_data
