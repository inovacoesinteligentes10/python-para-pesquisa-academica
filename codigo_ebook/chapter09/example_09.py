# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Visualização Inicial dos Dados
Linha original no arquivo LaTeX: 147

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Destacando período da pandemia
pandemia_mask = ((df_academico.index >= '2020-03-01') &
                 (df_academico.index <= '2021-12-31'))
axes[0, 0].fill_between(df_academico.index[pandemia_mask],
                        df_academico['publicacoes'][pandemia_mask],
                        alpha=0.3, color='red', label='Período Pandemia')
axes[0, 0].legend()

# Padrão sazonal por mês
publicacoes_por_mes = df_academico.groupby('mes')['publicacoes'].mean()
axes[0, 1].bar(range(1, 13), publicacoes_por_mes.values,
               color='lightcoral', alpha=0.7)
axes[0, 1].set_title('Padrão Sazonal Médio por Mês',
                     fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Mês')
axes[0, 1].set_ylabel('Publicações Médias')
axes[0, 1].set_xticks(range(1, 13))
axes[0, 1].grid(True, alpha=0.3)
