# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Limpeza e Transformação de Dados
Linha original no arquivo LaTeX: 367

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

# 4. Criar variáveis derivadas
dados_limpos['faixa_etaria'] = pd.cut(dados_limpos['idade'],
                                     bins=[0, 30, 50, 100],
                                     labels=['Jovem', 'Adulto', 'Idoso'])

dados_limpos['score_categoria'] = pd.cut(dados_limpos['score'],
                                        bins=[0, 60, 80, 100],
                                        labels=['Baixo', 'Médio', 'Alto'])

print(f"\nDados após limpeza:")
print(f"Valores ausentes: {dados_limpos.isnull().sum().sum()}")
print(f"Forma: {dados_limpos.shape}")
print(f"Registros removidos: {len(dados_sujos) - len(dados_limpos)}")

print(f"\nDistribuição por faixa etária:")
print(dados_limpos['faixa_etaria'].value_counts())

print(f"\nDistribuição por categoria de score:")
print(dados_limpos['score_categoria'].value_counts())
