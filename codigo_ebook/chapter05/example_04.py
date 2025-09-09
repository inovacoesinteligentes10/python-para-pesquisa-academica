# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 5
Seção: Controle de Versões para Pesquisa
Linha original no arquivo LaTeX: 212

Este código foi extraído automaticamente do arquivo chapter5.tex
"""

# src/utils/reproducibility.py
import random
import numpy as np
import pandas as pd
import torch
from datetime import datetime
import hashlib
import os

class ReproducibilityManager:
    """Gerencia reprodutibilidade de experimentos"""

    def __init__(self, seed=42):
        self.seed = seed
        self.experiment_log = []

    def set_seeds(self):
        """Define seeds para todos os geradores de números aleatórios"""
        random.seed(self.seed)
        np.random.seed(self.seed)
        torch.manual_seed(self.seed)
        torch.cuda.manual_seed_all(self.seed)
        os.environ['PYTHONHASHSEED'] = str(self.seed)

        # Para reprodutibilidade completa no PyTorch
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    def log_experiment(self, experiment_name, parameters):
        """Registra parâmetros de um experimento"""
        experiment_record = {
            'timestamp': datetime.now().isoformat(),
            'experiment': experiment_name,
            'seed': self.seed,
            'parameters': parameters,
            'hash': self._calculate_hash(parameters)
        }
        self.experiment_log.append(experiment_record)
