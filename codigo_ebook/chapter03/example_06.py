# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Indexação Avançada e Máscaras Booleanas
Linha original no arquivo LaTeX: 160

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


# Aalise por grupo usando máscaras
mascara_controle = grupos_validos == 'controle'
mascara_experimental = grupos_validos == 'experimental'

print(f"):")
print(f"  Tempo reacao medio: {np.mean(tempos_validos[mascara_controle]):.1f} ms")
print(f"  Acuracia media: {np.mean(acuracia_valida[mascara_controle])*100:.1f}%")

print(f"):")
print(f"  Tempo reacao medio: {np.mean(tempos_validos[mascara_experimental]):.1f} ms")
print(f"  Acuracia media: {np.mean(acuracia_valida[mascara_experimental])*100:.1f}%")

# Analise por faixa etária
jovens = idades_validas < 30
adultos = (idades_validas >= 30) & (idades_validas < 50)
idosos = idades_validas >= 50

print(f"\nPor faixa etaria:")
for nome, mascara in [('Jovens', jovens), ('Adultos', adultos), ('Idosos', idosos)]:
    if np.sum(mascara) > 0:
        print(f"  {nome}: TR = {np.mean(tempos_validos[mascara]):.1f} ms")
