# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Arrays Multidimensionais para Dados Complexos
Linha original no arquivo LaTeX: 86

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


# Simular dados de EEG: 64 eletrodos, 1000 pontos temporais, 100 trials
n_eletrodos = 64
n_tempos = 1000
n_trials = 100

# Criar dados simulados (normalmente carregados de arquivo)
np.random.seed(42)
dados_eeg = np.random.randn(n_eletrodos, n_tempos, n_trials)

print(f"Forma dos dados: {dados_eeg.shape}")
print(f"Memoria ocupada: {dados_eeg.nbytes / 1024**2:.1f} MB")

# Calcular media por eletrodo atraves dos trials
media_eletrodos = np.mean(dados_eeg, axis=2)  # media na dimensao trials
print(f"Forma da media: {media_eletrodos.shape}")

# Encontrar eletrodo com maior atividade media
atividade_media = np.mean(np.abs(media_eletrodos), axis=1)
eletrodo_max = np.argmax(atividade_media)
print(f"Eletrodo mais ativo: {eletrodo_max} (atividade: {atividade_media[eletrodo_max]:.3f})")
