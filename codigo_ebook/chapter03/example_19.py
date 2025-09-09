# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Visualizações Avançadas para Pesquisa
Linha original no arquivo LaTeX: 604

Este código foi extraído automaticamente do arquivo chapter3.tex
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 4. Histograma de distribuições
ax4 = plt.subplot(2, 3, 4)
dados_pesquisa[['stress_percebido', 'satisfacao_vida', 'qualidade_sono']].hist(
    bins=10, alpha=0.7, ax=ax4)
plt.title('Distribuições das Variáveis Principais')

# 5. Gráfico de violin
ax5 = plt.subplot(2, 3, 5)
# Categorizar exercício em grupos
dados_pesquisa['grupo_exercicio'] = pd.cut(dados_pesquisa['horas_exercicio'],
                                          bins=3, labels=['Baixo', 'Médio', 'Alto'])
sns.violinplot(data=dados_pesquisa, x='grupo_exercicio', y='satisfacao_vida', ax=ax5)
plt.title('Satisfação por Nível de Exercício')

# 6. Regressão linear
ax6 = plt.subplot(2, 3, 6)
sns.regplot(data=dados_pesquisa, x='educacao_anos', y='renda', ax=ax6, scatter_kws={'alpha':0.6})
plt.title('Educação vs Renda')

plt.tight_layout()
plt.savefig('analise_multivariada.png', dpi=300, bbox_inches='tight')
plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
