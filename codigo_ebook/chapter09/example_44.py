# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 868

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise por semestre acadêmico (assumindo início em março e setembro)
df_academico['semestre'] = np.where(df_academico.index.month.isin([3,4,5,6,7,8]), 1, 2)
semestre_stats = df_academico.groupby(['ano', 'semestre'])['publicacoes'].agg(['mean', 'sum', 'std'])

# Visualizando padrões semestrais
sem1_values = semestre_stats[semestre_stats.index.get_level_values(1) == 1]['mean'].values
sem2_values = semestre_stats[semestre_stats.index.get_level_values(1) == 2]['mean'].values

anos = semestre_stats.index.get_level_values(0).unique()
x = np.arange(len(anos))

axes[0, 1].bar(x - 0.2, sem1_values, 0.4, label='1º Semestre', alpha=0.7, color='lightblue')
axes[0, 1].bar(x + 0.2, sem2_values, 0.4, label='2º Semestre', alpha=0.7, color='orange')
axes[0, 1].set_title('Publicações Médias por Semestre Acadêmico')
axes[0, 1].set_xlabel('Ano')
axes[0, 1].set_ylabel('Publicações Médias')
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(anos, rotation=45)
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
