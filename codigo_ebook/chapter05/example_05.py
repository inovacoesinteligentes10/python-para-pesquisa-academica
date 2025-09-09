# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 5
Seção: Controle de Versões para Pesquisa
Linha original no arquivo LaTeX: 257

Este código foi extraído automaticamente do arquivo chapter5.tex
"""

# Continuação: src/utils/reproducibility.py

import hashlib

class ReproducibilityManager:
    def __init__(self, seed=42):
        self.seed = seed
        self.experiment_log = {}
    
    def set_seeds(self):
        """Define seeds para reprodutibilidade"""
        import random
        import numpy as np
        random.seed(self.seed)
        np.random.seed(self.seed)
    
    def log_experiment(self, name, params):
        """Registra experimento no log"""
        self.experiment_log[name] = {
            'params': params,
            'timestamp': str(__import__('datetime').datetime.now()),
            'hash': self._calculate_hash(params)
        }
    
    def _calculate_hash(self, parameters):
        """Calcula hash dos parâmetros para identificação única"""
        param_str = str(sorted(parameters.items()))
        return hashlib.md5(param_str.encode()).hexdigest()[:8]

    def save_experiment_log(self, filepath="results/experiment_log.json"):
        """Salva log de experimentos"""
        import json
        with open(filepath, 'w') as f:
            json.dump(self.experiment_log, f, indent=2)

# Exemplo de uso
repro = ReproducibilityManager(seed=42)
repro.set_seeds()

# Log do experimento
experiment_params = {
    'model_type': 'random_forest',
    'n_estimators': 100,
    'max_depth': 10,
    'feature_selection': 'mutual_info'
}
repro.log_experiment('cognitive_prediction_v1', experiment_params)
