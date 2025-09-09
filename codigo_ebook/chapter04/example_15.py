# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Regressão Robusta
Linha original no arquivo LaTeX: 574

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np


def regressao_robusta_interpretacao(modelo, X, y, preditores, p_norm, bp_p, white_p, dw_stat, outliers_residuos):
    """Executa regressao robusta e interpretacao final"""
    print(f"\n4. REGRESSAO ROBUSTA (Huber)")
    print("-" * 27)
    huber = HuberRegressor(epsilon=1.35, max_iter=1000)
    huber.fit(X, y)
    y_pred_huber = huber.predict(X)
    r2_huber = r2_score(y, y_pred_huber)
    print(f"R2 da regressao robusta: {r2_huber:.3f}")
    print(f"R2 da regressao classica: {modelo.rsquared:.3f}")
    print(f"\nCoeficientes:")
    print(f"{'Variavel':<15} {'OLS':<12} {'Huber':<12} {'Diferenca'}")
    print("-" * 45)
    print(f"{'Intercepto':<15} {modelo.params[0]:<12.3f} {huber.intercept_:<12.3f} {abs(modelo.params[0] - huber.intercept_):<12.3f}")
    for i, pred in enumerate(preditores):
        diff = abs(modelo.params[i+1] - huber.coef_[i])
        print(f"{pred:<15} {modelo.params[i+1]:<12.3f} {huber.coef_[i]:<12.3f} {diff:<12.3f}")
    print(f"\n5. INTERPRETACAO E RECOMENDACOES")
    print("-" * 32)
    pressupostos_ok = True
    if p_norm < 0.05:
        print("AVISO: Residuos nao seguem distribuicao normal")
        pressupostos_ok = False
    if bp_p < 0.05 or white_p < 0.05:
        print("AVISO: Heterocedasticidade detectada")
        pressupostos_ok = False
    if dw_stat < 1.5 or dw_stat > 2.5:
        print("AVISO: Possivel autocorrelacao nos residuos")
        pressupostos_ok = False
    if len(outliers_residuos) > 0:
        print(f"AVISO: {len(outliers_residuos)} outliers detectados")
        pressupostos_ok = False
    if pressupostos_ok:
        print("- Todos os pressupostos da regressao satisfeitos")
        print("- Resultados da regressao OLS sao confiaveis")
    else:
        print("\nRECOMENDACOES:")
        print("- Considere transformacao de variaveis")
        print("- Use regressao robusta (Huber mostrada acima)")
        print("- Investigue e possivelmente remova outliers")
        print("- Considere modelos nao-lineares")
    return huber, pressupostos_ok
np.random.seed(42)
n = 100
