# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Indexação Avançada e Máscaras Booleanas
Linha original no arquivo LaTeX: 131

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# Dados de um experimento: tempo de reacao e acuracia
n_participantes = 1000
np.random.seed(123)

tempos_reacao = np.random.normal(500, 100, n_participantes)  # ms
acuracia = np.random.beta(8, 2, n_participantes)  # proporção entre 0-1
idades = np.random.randint(18, 65, n_participantes)
grupos = np.random.choice(['controle', 'experimental'], n_participantes)

# Criar mascara booleana para participantes validos
# (tempo de reacao entre 200-1000ms e acuracia > 50%)
mascara_validos = (tempos_reacao >= 200) & (tempos_reacao <= 1000) & (acuracia > 0.5)

print(f"Participantes totais: {n_participantes}")
print(f"Participantes validos: {np.sum(mascara_validos)}")
print(f"Taxa de exclusao: {(1 - np.mean(mascara_validos))*100:.1f}%")

# Aplicar filtros
tempos_validos = tempos_reacao[mascara_validos]
acuracia_valida = acuracia[mascara_validos]
idades_validas = idades[mascara_validos]
grupos_validos = grupos[mascara_validos]
