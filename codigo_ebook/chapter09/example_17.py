# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Detecção de Mudanças Estruturais
Linha original no arquivo LaTeX: 301

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Visualizando os pontos de mudança
plt.figure(figsize=(15, 6))
plt.plot(df_academico.index, df_academico['publicacoes'],
         linewidth=1.5, color='steelblue', label='Série Original')

# Marcando os pontos de mudança
for data in datas_mudanca:
    plt.axvline(x=data, color='red', linestyle='--', alpha=0.8)

plt.title('Detecção de Mudanças Estruturais na Série',
          fontsize=14, fontweight='bold')
plt.xlabel('Data')
plt.ylabel('Número de Publicações')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
