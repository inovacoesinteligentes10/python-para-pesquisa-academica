# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Regressão Robusta
Linha original no arquivo LaTeX: 625

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

dados_reg = pd.DataFrame({
    'idade': np.random.randint(20, 60, n),
    'educacao': np.random.randint(8, 20, n),
    'experiencia': np.random.randint(0, 30, n)
})
dados_reg['salario'] = (dados_reg['idade'] * 500 +
                       dados_reg['educacao'] * 2000 +
                       dados_reg['experiencia'] * 800 +
                       np.random.normal(0, 5000, n))
dados_reg.loc[5, 'salario'] = 150000  # outlier alto
dados_reg.loc[25, 'salario'] = 10000   # outlier baixo
modelo, X, y, X_const = regressao_completa(dados_reg, 'salario', ['idade', 'educacao', 'experiencia'])
residuos, valores_preditos, residuos_estudentizados, p_norm, bp_p, white_p, dw_stat, outliers_residuos = diagnosticos_residuos(modelo, X_const)
visualizacoes_diagnosticas(residuos, valores_preditos, residuos_estudentizados, dados_reg, ['idade', 'educacao', 'experiencia'])
huber, pressupostos_ok = regressao_robusta_interpretacao(modelo, X, y, ['idade', 'educacao', 'experiencia'], p_norm, bp_p, white_p, dw_stat, outliers_residuos)
