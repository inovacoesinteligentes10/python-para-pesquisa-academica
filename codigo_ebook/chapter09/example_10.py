# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Visualização Inicial dos Dados
Linha original no arquivo LaTeX: 170

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Tendência anual
publicacoes_por_ano = df_academico.groupby('ano')['publicacoes'].sum()
axes[1, 0].plot(publicacoes_por_ano.index, publicacoes_por_ano.values,
                marker='o', linewidth=2, markersize=6, color='darkgreen')
axes[1, 0].set_title('Tendência Anual: Total de Publicações',
                     fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Ano')
axes[1, 0].set_ylabel('Total de Publicações')
axes[1, 0].grid(True, alpha=0.3)

# Distribuição dos valores
axes[1, 1].hist(df_academico['publicacoes'], bins=20,
                color='orange', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('Distribuição dos Valores',
                     fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Número de Publicações')
axes[1, 1].set_ylabel('Frequência')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
