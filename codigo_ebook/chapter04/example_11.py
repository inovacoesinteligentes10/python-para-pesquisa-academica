# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Comparação de Grupos: Paramétrico vs Não-paramétrico
Linha original no arquivo LaTeX: 406

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
import pandas as pd


def anova_efeito_posthoc(dados, grupo_col, variavel_dep, grupos_dados, p_anova):
   """Calcula tamanho de efeito e testes post-hoc"""
   print(f"\nTAMANHO DE EFEITO:")
   print("-" * 17)
   ss_between = sum(len(g) * (g.mean() - dados[variavel_dep].mean())**2
                   for g in grupos_dados)
   ss_total = sum((dados[variavel_dep] - dados[variavel_dep].mean())**2)
   eta_squared = ss_between / ss_total
   print(f"Eta-squared = {eta_squared:.3f}")
   if eta_squared < 0.01:
       interpretacao = "trivial"
   elif eta_squared < 0.06:
       interpretacao = "pequeno"
   elif eta_squared < 0.14:
       interpretacao = "medio"
   else:
       interpretacao = "grande"
   print(f"Interpretacao: efeito {interpretacao}")
   if p_anova < 0.05:
       print(f"\nTESTES POST-HOC:")
       print("-" * 15)
       posthoc = pg.pairwise_tukey(data=dados, dv=variavel_dep, between=grupo_col)
       print("Tukey HSD:")
       for _, row in posthoc.iterrows():
           print(f"   {row['A']} vs {row['B']}: p = {row['p-tukey']:.3f}")
np.random.seed(123)
dados_multi = pd.DataFrame({
   'grupo': np.repeat(['controle', 'trat1', 'trat2'], 30),
   'score': np.concatenate([
       np.random.normal(50, 8, 30),
       np.random.normal(55, 9, 30),
       np.random.normal(62, 10, 30)
   ])
})
grupo1, grupo2, grupos = bateria_testes_comparacao(dados_multi, 'grupo', 'score')
if grupo1 is not None:
   t_stat = testes_independentes(grupo1, grupo2)
   cohens_d = calcular_tamanhos_efeito(grupo1, grupo2, t_stat)
else:
   grupos_dados, p_anova, dados_long = testes_multiplos_grupos(dados_multi, 'grupo', 'score')
   anova_efeito_posthoc(dados_multi, 'grupo', 'score', grupos_dados, p_anova)
