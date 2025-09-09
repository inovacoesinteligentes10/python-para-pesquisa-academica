# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 915

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Padrão de crescimento anual
crescimento_anual = df_academico.groupby('ano')['publicacoes'].sum().pct_change() * 100
axes[1, 1].bar(crescimento_anual.index[1:], crescimento_anual.values[1:],
               color=['red' if x < 0 else 'green' for x in crescimento_anual.values[1:]],
               alpha=0.7)
axes[1, 1].axhline(y=0, color='black', linestyle='-', alpha=0.8)
axes[1, 1].set_title('Taxa de Crescimento Anual (%)')
axes[1, 1].set_xlabel('Ano')
axes[1, 1].set_ylabel('Crescimento (%)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
