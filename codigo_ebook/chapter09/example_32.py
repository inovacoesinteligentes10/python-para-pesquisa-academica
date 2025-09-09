# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Identificação de Padrões Sazonais
Linha original no arquivo LaTeX: 601

Este código foi extraído automaticamente do arquivo chapter9.tex
"""
import matplotlib.pyplot as plt


# Análise de sazonalidade por diferentes períodos
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Padrão mensal
monthly_pattern = df_academico.groupby(df_academico.index.month)['publicacoes'].agg(['mean', 'std'])
axes[0, 0].bar(monthly_pattern.index, monthly_pattern['mean'],
               yerr=monthly_pattern['std'], capsize=5, alpha=0.7, color='skyblue')
axes[0, 0].set_title('Padrão Sazonal Mensal')
axes[0, 0].set_xlabel('Mês')
axes[0, 0].set_ylabel('Publicações Médias')
axes[0, 0].set_xticks(range(1, 13))
axes[0, 0].grid(True, alpha=0.3)
