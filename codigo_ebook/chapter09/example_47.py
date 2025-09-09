# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 933

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Relatório de análise de sazonalidade
print("=" * 60)
print("RELATÓRIO DE ANÁLISE DE SAZONALIDADE")
print("=" * 60)

print(f"\n1. PERÍODOS DOMINANTES DETECTADOS:")
for i, pico in enumerate(picos[:3]):
    periodo = periodos[pico]
    print(f"   Período {i+1}: {periodo:.1f} meses")

print(f"\n2. ANÁLISE SEMESTRAL:")
print(f"   Média 1º Semestre: {np.mean(sem1_values):.1f} publicações")
print(f"   Média 2º Semestre: {np.mean(sem2_values):.1f} publicações")
diferenca_rel = ((np.mean(sem2_values) - np.mean(sem1_values))/np.mean(sem1_values)*100)
print(f"   Diferença relativa: {diferenca_rel:.1f}%")

print(f"\n3. CONCENTRAÇÃO TRIMESTRAL MÉDIA:")
concentracao_media = trimestre_pct.mean()
for i, trimestre in enumerate(['Q1', 'Q2', 'Q3', 'Q4']):
    print(f"   {trimestre}: {concentracao_media.iloc[i]:.1f}%")

print(f"%")
