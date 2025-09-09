# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Animações e Séries Temporais
Linha original no arquivo LaTeX: 230

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Criando dados temporais para demonstrar animações
datas = pd.date_range(start='2020-01-01', end='2023-12-31', freq='M')
np.random.seed(42)

# Simulando evolução temporal de indicadores por área
dados_temporais = []
for area in dados_estudo['area'].unique():
    for data in datas:
        # Simulando tendências e sazonalidade
        base_bem_estar = 6 + np.sin(data.month * 2 * np.pi / 12) * 0.5
        base_produtividade = 70 + np.sin(data.month * 2 * np.pi / 12) * 5

        # Adicionando variação por área
        if area == 'Tecnologia':
            base_bem_estar += 0.5
            base_produtividade += 5
        elif area == 'Saúde':
            base_bem_estar += 0.3
            base_produtividade += 3
        elif area == 'Educação':
            base_bem_estar += 0.1
            base_produtividade -= 2

        # Adicionando ruído e tendência temporal
        tendencia = (data.year - 2020) * 0.1
        ruido_bem_estar = np.random.normal(0, 0.3)
        ruido_produtividade = np.random.normal(0, 3)

        dados_temporais.append({
            'data': data,
            'area': area,
            'bem_estar_medio': base_bem_estar + tendencia + ruido_bem_estar,
            'produtividade_media': base_produtividade + tendencia * 2 + ruido_produtividade,
            'ano': data.year,
            'mes': data.month
        })

df_temporal = pd.DataFrame(dados_temporais)

print("Dados temporais criados:")
print(df_temporal.head())
