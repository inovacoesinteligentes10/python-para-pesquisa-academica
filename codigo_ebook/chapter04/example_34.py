# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Controle de Erro Tipo I em Múltiplas Comparações
Linha original no arquivo LaTeX: 1303

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
from scipy import stats


# Simular exemplo com multiplas comparacoes
np.random.seed(123)

# Simular 15 testes: 3 com efeito real, 12 sem efeito
p_valores_exemplo = []

# 3 testes com efeito real (p-valores baixos)
for _ in range(3):
    # Simular dados com diferenca real
    grupo1 = np.random.normal(50, 10, 30)
    grupo2 = np.random.normal(58, 10, 30)  # Diferenca real
    _, p = stats.ttest_ind(grupo1, grupo2)
    p_valores_exemplo.append(p)

# 12 testes sem efeito (apenas ruido)
for _ in range(12):
    # Simular dados sem diferenca
    grupo1 = np.random.normal(50, 10, 30)
    grupo2 = np.random.normal(50, 10, 30)  # Sem diferenca
    _, p = stats.ttest_ind(grupo1, grupo2)
    p_valores_exemplo.append(p)

print("EXEMPLO: 15 TESTES (3 com efeito real, 12 sem efeito)")
print("=" * 55)

# Executar correcoes
p_valores, n_testes = correcao_multiplas_comparacoes(p_valores_exemplo)
resultados = aplicar_correcoes(p_valores, ['bonferroni', 'holm', 'fdr_bh'])
resultado_final = visualizar_correcoes(p_valores, resultados, ['bonferroni', 'holm', 'fdr_bh'])
