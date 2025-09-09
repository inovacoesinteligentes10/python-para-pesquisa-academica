# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Identificação de Padrões Sazonais
Linha original no arquivo LaTeX: 643

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Boxplot por mês
df_academico.boxplot(column='publicacoes', by=df_academico.index.month,
                     ax=axes[1, 1])
axes[1, 1].set_title('Distribuição por Mês')
axes[1, 1].set_xlabel('Mês')
axes[1, 1].set_ylabel('Publicações')

plt.tight_layout()
plt.show()
