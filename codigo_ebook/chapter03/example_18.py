# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Visualizações Avançadas para Pesquisa
Linha original no arquivo LaTeX: 566

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Criar visualização complexa
fig = plt.figure(figsize=(16, 12))

# 1. Heatmap de correlações
ax1 = plt.subplot(2, 3, 1)
correlacoes = dados_pesquisa.corr()
mask = np.triu(np.ones_like(correlacoes, dtype=bool))
sns.heatmap(correlacoes, mask=mask, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .8})
plt.title('Matriz de Correlações')

# 2. Distribuição de idades por quartis de satisfação
ax2 = plt.subplot(2, 3, 2)
dados_pesquisa['quartil_satisfacao'] = pd.qcut(dados_pesquisa['satisfacao_vida'],
                                              4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
dados_pesquisa.boxplot(column='idade', by='quartil_satisfacao', ax=ax2)
plt.title('Idade por Quartil de Satisfação')
plt.suptitle('')  # Remove título automático do pandas

# 3. Scatter plot matriz
ax3 = plt.subplot(2, 3, 3)
scatter = ax3.scatter(dados_pesquisa['stress_percebido'],
                     dados_pesquisa['qualidade_sono'],
                     c=dados_pesquisa['horas_exercicio'],
                     s=dados_pesquisa['idade'],
                     alpha=0.6, cmap='viridis')
ax3.set_xlabel('Stress Percebido')
ax3.set_ylabel('Qualidade do Sono')
ax3.set_title('Stress vs Sono (cor=exercício, tamanho=idade)')
cbar = plt.colorbar(scatter, ax=ax3)
cbar.set_label('Horas de Exercício')
