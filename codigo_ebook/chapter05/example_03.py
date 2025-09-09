# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 5
Seção: Configuração e Parametrização
Linha original no arquivo LaTeX: 171

Este código foi extraído automaticamente do arquivo chapter5.tex
"""

# src/config/config_loader.py
import yaml
from pathlib import Path

def load_config(config_path="config/research_config.yaml"):
    """Carrega configurações do projeto"""
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

def validate_config(config):
    """Valida configurações obrigatórias"""
    required_keys = ['project', 'data', 'analysis']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Configuração '{key}' obrigatória não encontrada")
    return True

def get_analysis_params(config):
    """Extrai parâmetros para análise"""
    return {
        'alpha': config['analysis']['significance_level'],
        'min_effect_size': config['analysis']['minimum_effect_size'],
        'bootstrap_n': config['analysis']['bootstrap_samples']
    }

# Exemplo de uso
config = load_config()
validate_config(config)
analysis_params = get_analysis_params(config)
