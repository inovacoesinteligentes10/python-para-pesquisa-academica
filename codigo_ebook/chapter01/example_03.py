# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 1
Seção: Reproducibilidade e Transparência
Linha original no arquivo LaTeX: 106

Este código foi extraído automaticamente do arquivo chapter1.tex
"""

# Exemplo de análise reproduzível
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Configurar seed para reprodutibilidade
np.random.seed(42)

# Simular dados de experimento
control_group = np.random.normal(100, 15, 50)
treatment_group = np.random.normal(110, 15, 50)

# Teste estatístico
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

# Visualização
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Histogramas
ax1.hist(control_group, alpha=0.7, label='Controle', bins=15)
ax1.hist(treatment_group, alpha=0.7, label='Tratamento', bins=15)
ax1.legend()
ax1.set_title('Distribuição dos Grupos')

# Box plot
data_combined = pd.DataFrame({
    'Grupo': ['Controle']*50 + ['Tratamento']*50,
    'Valor': np.concatenate([control_group, treatment_group])
})
sns.boxplot(data=data_combined, x='Grupo', y='Valor', ax=ax2)
ax2.set_title('Comparação entre Grupos')

plt.tight_layout()
plt.savefig('results_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Resultados
print(f"Estatística t: {t_stat:.3f}")
print(f"Valor p: {p_value:.3f}")
print(f"Diferença significativa: {'Sim' if p_value < 0.05 else 'Não'}")
