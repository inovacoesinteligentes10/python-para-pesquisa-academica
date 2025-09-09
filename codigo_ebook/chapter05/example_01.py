# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 5
Seção: Estrutura de Diretórios para Projetos de Pesquisa
Linha original no arquivo LaTeX: 53

Este código foi extraído automaticamente do arquivo chapter5.tex
"""

# src/data/longitudinal_processor.py
import pandas as pd
import numpy as np
from datetime import datetime
import logging

class LongitudinalDataProcessor:
    """Processador para dados longitudinais de desenvolvimento cognitivo"""

    def __init__(self, config):
        self.config = config
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(
            filename=f'logs/processing_{datetime.now().strftime("%Y%m%d")}.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)

    def load_raw_data(self, wave):
        """Carrega dados de uma onda específica do estudo"""
        try:
            filepath = f"data/raw/wave_{wave}_cognitive_tests.csv"
            data = pd.read_csv(filepath)
            self.logger.info(f"Carregados {len(data)} registros da onda {wave}")
            return data
        except FileNotFoundError:
            self.logger.error(f"Arquivo da onda {wave} não encontrado")
            raise

        except Exception as e:

            print(f'Erro: {e}')

            return None
