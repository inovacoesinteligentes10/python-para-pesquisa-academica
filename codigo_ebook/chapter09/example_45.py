# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 893

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise de concentração de publicações por período do ano
trimestre_concentracao = df_academico.groupby(['ano', 'trimestre'])['publicacoes'].sum().unstack()
trimestre_pct = trimestre_concentracao.div(trimestre_concentracao.sum(axis=1), axis=0) * 100

# Heatmap de concentração por trimestre
im = axes[1, 0].imshow(trimestre_pct.values, cmap='YlOrRd', aspect='auto')
axes[1, 0].set_title('Concentração de Publicações por Trimestre (%)')
axes[1, 0].set_xlabel('Trimestre')
axes[1, 0].set_ylabel('Ano')
axes[1, 0].set_xticks(range(4))
axes[1, 0].set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
axes[1, 0].set_yticks(range(len(trimestre_pct.index)))
axes[1, 0].set_yticklabels(trimestre_pct.index)

# Adicionando colorbar
cbar = plt.colorbar(im, ax=axes[1, 0])
cbar.set_label('Concentração (%)')
