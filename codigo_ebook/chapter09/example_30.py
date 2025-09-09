# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão e Validação
Linha original no arquivo LaTeX: 561

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Q-Q plot
from scipy import stats
stats.probplot(residuos.dropna(), dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot dos Resíduos')

# ACF dos resíduos
plot_acf(residuos.dropna(), ax=axes[1, 1], lags=20)
axes[1, 1].set_title('ACF dos Resíduos')

plt.tight_layout()
plt.show()
