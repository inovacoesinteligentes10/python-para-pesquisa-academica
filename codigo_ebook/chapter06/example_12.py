# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Agendamento de Coletas
Linha original no arquivo LaTeX: 496

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

import schedule
import time
import logging
from datetime import datetime

class DataCollector:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def save_collection_data(self, name, result):
        """Salva dados da coleta"""
        try:
            # Salvar dados se especificado
            if 'output_path' in self.config:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_file = f"{self.config['output_path']}/{name}_{timestamp}.csv"
                if hasattr(result, 'to_csv'):
                    result.to_csv(output_file, index=False)

            self.logger.info(f"Coleta {name} concluída")

        except Exception as e:
            self.logger.error(f"Erro na coleta {name}: {e}")

    def start_monitoring(self):
        """Inicia monitoramento contínuo"""
        self.logger.info("Iniciando sistema de coleta automatizada")
        while True:
            schedule.run_pending()
            time.sleep(60)
