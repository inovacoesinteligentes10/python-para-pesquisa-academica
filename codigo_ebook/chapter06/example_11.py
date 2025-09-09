# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Agendamento de Coletas
Linha original no arquivo LaTeX: 447

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

# src/data_collection/scheduled_collector.py
import schedule
import time
import logging
from datetime import datetime
from typing import Callable, Dict

class ScheduledDataCollector:
    """Sistema para coleta automatizada e agendada de dados"""

    def __init__(self, base_config: Dict):
        self.config = base_config
        self.collectors = {}
        self.logger = logging.getLogger(__name__)

    def register_collector(self, name: str, collector_func: Callable,
                          schedule_config: Dict):
        """Registra um coletor com sua configuração de agendamento"""
        self.collectors[name] = {
            'function': collector_func,
            'schedule': schedule_config,
            'last_run': None,
            'total_runs': 0
        }

        # Configurar agendamento
        if schedule_config['type'] == 'interval':
            if schedule_config['unit'] == 'hours':
                schedule.every(schedule_config['value']).hours.do(
                    self._run_collector, name, collector_func
                )
            elif schedule_config['unit'] == 'days':
                schedule.every(schedule_config['value']).days.do(
                    self._run_collector, name, collector_func
                )

    def _run_collector(self, name: str, func: Callable):
        """Executa um coletor específico"""
        try:
            self.logger.info(f"Iniciando coleta: {name}")
            result = func()

        except Exception as e:

            print(f'Erro: {e}')

            return None
            self.collectors[name]['last_run'] = datetime.now()
            self.collectors[name]['total_runs'] += 1
            
            self.logger.info(f"Coleta {name} finalizada com sucesso")
            return result
            
        except Exception as e:
            self.logger.error(f"Erro na coleta {name}: {e}")
            return None
    
    def start_scheduler(self):
        """Inicia o agendador de coletas"""
        self.logger.info("Iniciando agendador de coletas")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Verifica a cada minuto
