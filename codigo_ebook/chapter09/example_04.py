# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Importação e Preparação de Dados Temporais
Linha original no arquivo LaTeX: 68

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Simulando dados de um estudo sobre produtividade acadêmica
np.random.seed(123)

# Dados de publicações científicas por mês
datas_pub = pd.date_range(start='2015-01-01', end='2023-12-31', freq='M')

# Simulando padrões realistas de publicação
base_pub = 50
crescimento = np.linspace(0, 30, len(datas_pub))
sazon_acad = 15 * np.sin(2 * np.pi * np.arange(len(datas_pub)) / 12 + np.pi/2)
eventos_esp = np.zeros(len(datas_pub))
