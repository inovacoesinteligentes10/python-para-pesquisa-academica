# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Identificação de Padrões Sazonais
Linha original no arquivo LaTeX: 618

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Padrão trimestral
quarterly_pattern = df_academico.groupby('trimestre')['publicacoes'].agg(['mean', 'std'])
axes[0, 1].bar(quarterly_pattern.index, quarterly_pattern['mean'],
               yerr=quarterly_pattern['std'], capsize=5, alpha=0.7, color='lightgreen')
axes[0, 1].set_title('Padrão Sazonal Trimestral')
axes[0, 1].set_xlabel('Trimestre')
axes[0, 1].set_ylabel('Publicações Médias')
axes[0, 1].grid(True, alpha=0.3)

# Heatmap sazonal
pivot_sazonal = df_academico.pivot_table(values='publicacoes',
                                         index=df_academico.index.year,
                                         columns=df_academico.index.month,
                                         aggfunc='mean')

sns.heatmap(pivot_sazonal, annot=True, fmt='.0f', cmap='YlOrRd',
            ax=axes[1, 0], cbar_kws={'label': 'Publicações'})
axes[1, 0].set_title('Heatmap Sazonal (Ano x Mês)')
axes[1, 0].set_xlabel('Mês')
axes[1, 0].set_ylabel('Ano')
