# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Detecção de Mudanças Estruturais
Linha original no arquivo LaTeX: 290

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Convertendo índices para datas
datas_mudanca = [df_academico.index[i] for i in pontos_mudanca]

print("Pontos de mudança detectados:")
for i, data in enumerate(datas_mudanca):
    print(f"Mudança {i+1}: {data.strftime('%Y-%m')}")
