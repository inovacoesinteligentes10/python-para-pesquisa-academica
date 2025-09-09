# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 960

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Teste de sazonalidade mais rigoroso
from statsmodels.stats.diagnostic import acorr_ljungbox

# Teste de Ljung-Box nos resíduos dessazonalizados
serie_dessazonalizada = df_academico['publicacoes'] - resultado_stl.seasonal
residuos_dessaz = serie_dessazonalizada - serie_dessazonalizada.rolling(12).mean()

ljung_box = acorr_ljungbox(residuos_dessaz.dropna(), lags=12, return_df=True)
print(f"\n5. TESTE DE LJUNG-BOX (Autocorrelação Residual):")
print(f"   p-valor mínimo: {ljung_box['lb_pvalue'].min():.6f}")

if ljung_box['lb_pvalue'].min() > 0.05:
    print("   Resultado: Não há autocorrelação significativa nos resíduos")
else:
    print("   Resultado: Ainda há autocorrelação nos resíduos")
