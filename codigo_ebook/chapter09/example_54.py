# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1095

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Relatório de previsão
print("=" * 70)
print("RELATÓRIO DE PREVISÃO - PRÓXIMOS 12 MESES")
print("=" * 70)

print(f"\nPREVISÃO MENSAL:")
for _, row in df_incerteza.iterrows():
    mes_nome = meses_nomes[row['mes']-1]
    print(f"{row['data'].strftime('%Y-%m')} ({mes_nome}): "
          f"{row['previsao']:.0f} publicações "
          f"[{row['ic_inferior']:.0f} - {row['ic_superior']:.0f}]")

print(f"\nRESUMO ESTATÍSTICO:")
print(f"Total previsto (12 meses): {df_incerteza['previsao'].sum():.0f} publicações")
print(f"Média mensal: {df_incerteza['previsao'].mean():.1f} publicações")

max_idx = df_incerteza['previsao'].idxmax()
min_idx = df_incerteza['previsao'].idxmin()
print(f"Mês com maior previsão: {meses_nomes[df_incerteza.loc[max_idx, 'mes']-1]} "
      f"({df_incerteza['previsao'].max():.0f} publicações)")
print(f"Mês com menor previsão: {meses_nomes[df_incerteza.loc[min_idx, 'mes']-1]} "
      f"({df_incerteza['previsao'].min():.0f} publicações)")
