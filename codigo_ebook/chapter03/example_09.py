# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Operações de Agrupamento e Análise
Linha original no arquivo LaTeX: 266

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# Calcular tamanho do efeito simples
def cohen_d(grupo1, grupo2):
    """Calcula Cohen's d entre dois grupos"""
    n1, n2 = len(grupo1), len(grupo2)
    s1, s2 = grupo1.std(), grupo2.std()

    # Pooled standard deviation
    s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))

    return (grupo1.mean() - grupo2.mean()) / s_pooled

controle = df[df['grupo'] == 'controle']['melhoria']
tratamento = df[df['grupo'] == 'tratamento']['melhoria']

d = cohen_d(tratamento, controle)
print(f"")

# Interpretacao
if abs(d) < 0.2:
    interpretacao = "trivial"
elif abs(d) < 0.5:
    interpretacao = "pequeno"
elif abs(d) < 0.8:
    interpretacao = "médio"
else:
    interpretacao = "grande"

print(f"Interpretação: efeito {interpretacao}")
