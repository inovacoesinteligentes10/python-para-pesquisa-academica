# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Importação e Preparação de Dados Temporais
Linha original no arquivo LaTeX: 84

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import numpy as np


# Simulando impacto da pandemia (2020-2021)
pandemia_inicio = ((datas_pub >= '2020-03-01') &
                   (datas_pub <= '2020-12-31'))
pandemia_recup = ((datas_pub >= '2021-01-01') &
                  (datas_pub <= '2021-12-31'))

eventos_esp[pandemia_inicio] = -20
eventos_esp[pandemia_recup] = 10

ruido = np.random.normal(0, 8, len(datas_pub))
