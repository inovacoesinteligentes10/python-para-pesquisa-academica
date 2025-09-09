# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Gráficos Básicos para Publicação
Linha original no arquivo LaTeX: 464

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# 2. Boxplot
dados_boxplot = [
    np.random.normal(72.5, 8, 50),  # Controle
    np.random.normal(81.3, 9, 50),  # Tratamento A
    np.random.normal(85.7, 7, 50)   # Tratamento B
]

bp = ax2.boxplot(dados_boxplot, labels=grupos, patch_artist=True)
ax2.set_ylabel('Score')
ax2.set_title('Distribuição dos Scores por Grupo')

# Colorir boxplots
cores = ['lightblue', 'lightgreen', 'lightcoral']
for patch, cor in zip(bp['boxes'], cores):
    patch.set_facecolor(cor)

# 3. Gráfico de linha temporal
tempos = np.arange(0, 11)  # 0 a 10 semanas
grupo_controle = 72 + 0.2 * tempos + np.random.normal(0, 1, len(tempos))
grupo_trat = 72 + 1.5 * tempos + np.random.normal(0, 1.5, len(tempos))

ax3.plot(tempos, grupo_controle, 'o-', label='Controle', linewidth=2, markersize=6)
ax3.plot(tempos, grupo_trat, 's-', label='Tratamento', linewidth=2, markersize=6)
ax3.set_xlabel('Semanas')
ax3.set_ylabel('Score')
ax3.set_title('Evolução Temporal')
ax3.legend()
ax3.grid(True, alpha=0.3)
