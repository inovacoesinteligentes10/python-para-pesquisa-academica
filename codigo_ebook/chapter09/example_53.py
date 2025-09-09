# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1067

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Gráfico de incerteza por mês
meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

incerteza_por_mes = df_incerteza.groupby('mes')['amplitude_ic'].mean()
variabilidade_por_mes = df_incerteza.groupby('mes')['variabilidade_historica'].mean()

x = range(1, 13)
axes[1].bar([i-0.2 for i in x], [incerteza_por_mes.get(i, 0) for i in x],
            0.4, label='Incerteza da Previsão', alpha=0.7, color='red')
axes[1].bar([i+0.2 for i in x], [variabilidade_por_mes.get(i, 0) for i in x],
            0.4, label='Variabilidade Histórica', alpha=0.7, color='blue')

axes[1].set_title('Incerteza da Previsão vs Variabilidade Histórica por Mês')
axes[1].set_xlabel('Mês')
axes[1].set_ylabel('Amplitude da Incerteza')
axes[1].set_xticks(x)
axes[1].set_xticklabels(meses_nomes)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
