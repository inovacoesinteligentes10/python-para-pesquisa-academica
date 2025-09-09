# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Gráficos Básicos para Publicação
Linha original no arquivo LaTeX: 430

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np


# 1. Gráfico de barras com barras de erro
x_pos = np.arange(len(grupos))
largura = 0.35

barras1 = ax1.bar(x_pos - largura/2, pre_teste, largura,
                  yerr=erros_pre, label='Pré-teste', alpha=0.8)
barras2 = ax1.bar(x_pos + largura/2, pos_teste, largura,
                  yerr=erros_pos, label='Pós-teste', alpha=0.8)

ax1.set_xlabel('Grupos')
ax1.set_ylabel('Score Médio')
ax1.set_title('Comparação Pré vs Pós-teste')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(grupos)
ax1.legend()
ax1.set_ylim(65, 90)

# Adicionar valores nas barras
for barra in barras1:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 1,
             f'{altura:.1f}', ha='center', va='bottom')

for barra in barras2:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 1,
             f'{altura:.1f}', ha='center', va='bottom')
