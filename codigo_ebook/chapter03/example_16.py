# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Gráficos Básicos para Publicação
Linha original no arquivo LaTeX: 499

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import numpy as np
import matplotlib.pyplot as plt


# 4. Scatter plot com linha de tendência
np.random.seed(42)
idade = np.random.randint(20, 60, 100)
score = 60 + 0.5 * idade + np.random.normal(0, 5, 100)

ax4.scatter(idade, score, alpha=0.6, s=50)

# Adicionar linha de tendência
z = np.polyfit(idade, score, 1)
p = np.poly1d(z)
ax4.plot(idade, p(idade), "r--", alpha=0.8, linewidth=2)

# Calcular e mostrar correlação
correlacao = np.corrcoef(idade, score)[0, 1]
ax4.text(0.05, 0.95, f'r = {correlacao:.3f}', transform=ax4.transAxes,
         bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.8))

ax4.set_xlabel('Idade')
ax4.set_ylabel('Score')
ax4.set_title('Relação Idade vs Performance')

plt.tight_layout()
plt.savefig('analise_completa.png', dpi=300, bbox_inches='tight')
plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
