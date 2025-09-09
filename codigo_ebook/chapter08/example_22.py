# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Técnicas de Validação Cruzada
Linha original no arquivo LaTeX: 1163

Este código foi extraído automaticamente do arquivo chapter8.tex
"""

# Validação cruzada abrangente
cv_results = validator.comprehensive_cross_validation(model, X_df, y_series)
print("Resultados da Validação Cruzada:")
for metric, results in cv_results.items():
    print(f"{metric}: {results['mean']:.3f} +/- {results['std']:.3f}")

# Análise de curva de aprendizado
learning_results = validator.learning_curve_analysis(model, X_df, y_series)
validator.plot_learning_curves(learning_results)

# Bootstrap confidence interval
bootstrap_results = validator.bootstrap_confidence_interval(model, X_df, y_series)
print(f"\nIntervalo de Confiança (Bootstrap):")
print(f"Score médio: {bootstrap_results['mean_score']:.3f}")
print(f"95% CI: {bootstrap_results['confidence_interval']}")
