# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Decomposição de Séries Temporais
Linha original no arquivo LaTeX: 234

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Sazonalidade
axes[2].plot(df_academico.index, decomposicao.seasonal,
             color='blue', linewidth=1.5)
axes[2].set_title('Componente Sazonal', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Sazonalidade')
axes[2].grid(True, alpha=0.3)

# Resíduo
axes[3].plot(df_academico.index, decomposicao.resid,
             color='green', linewidth=1)
axes[3].set_title('Resíduo (Ruído)', fontsize=12, fontweight='bold')
axes[3].set_ylabel('Resíduo')
axes[3].set_xlabel('Data')
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
