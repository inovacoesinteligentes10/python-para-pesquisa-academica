# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Fundamentos do Web Scraping Ético
Linha original no arquivo LaTeX: 192

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ArticleUrlFinder:
    def __init__(self):
        pass
    
    def find_article_urls(self, response, base_url):
        """Encontra URLs de artigos"""
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        article_urls = []
        for link in links:
            href = link['href']
            if href.startswith('/'):
                href = urljoin(base_url, href)

            # Filtrar apenas URLs que parecem ser artigos
            if '/article/' in href or '/news/' in href:
                article_urls.append(href)

        return list(set(article_urls))  # Remove duplicatas
