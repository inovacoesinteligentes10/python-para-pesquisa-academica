# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Fundamentos da Geração Automatizada
Linha original no arquivo LaTeX: 36

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Configuração de estilo para gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Criando dados de exemplo para relatório de pesquisa
np.random.seed(42)
n_participantes = 200

# Simulando dados de um estudo longitudinal sobre aprendizado
dados_estudo = pd.DataFrame({
    'participante_id': range(1, n_participantes + 1),
    'grupo': np.random.choice(['Controle', 'Experimental'], n_participantes),
    'idade': np.random.normal(22, 3, n_participantes).astype(int),
    'genero': np.random.choice(['M', 'F', 'NB'], n_participantes, p=[0.45, 0.45, 0.1]),
    'pre_teste': np.random.normal(65, 15, n_participantes),
    'pos_teste': np.random.normal(70, 18, n_participantes),
    'satisfacao': np.random.normal(7.5, 1.8, n_participantes),
    'tempo_estudo': np.random.normal(4.5, 2, n_participantes),
    'data_coleta': pd.date_range(start='2024-01-15', periods=n_participantes, freq='D')
})

# Adicionando efeito realista do grupo experimental
mask_experimental = dados_estudo['grupo'] == 'Experimental'
dados_estudo.loc[mask_experimental, 'pos_teste'] += np.random.normal(8, 3, mask_experimental.sum())
dados_estudo.loc[mask_experimental, 'satisfacao'] += np.random.normal(0.8, 0.4, mask_experimental.sum())

# Limitando valores aos ranges apropriados
dados_estudo['pre_teste'] = np.clip(dados_estudo['pre_teste'], 0, 100)
dados_estudo['pos_teste'] = np.clip(dados_estudo['pos_teste'], 0, 100)
dados_estudo['satisfacao'] = np.clip(dados_estudo['satisfacao'], 1, 10)
dados_estudo['tempo_estudo'] = np.clip(dados_estudo['tempo_estudo'], 1, 10)

# Calculando variáveis derivadas
dados_estudo['ganho_aprendizado'] = dados_estudo['pos_teste'] - dados_estudo['pre_teste']
dados_estudo['ganho_percentual'] = (dados_estudo['ganho_aprendizado'] / dados_estudo['pre_teste']) * 100

print("Dataset para relatório criado:")
print(dados_estudo.head())
print(f"\nEstatísticas básicas:")
print(dados_estudo.groupby('grupo')[['pre_teste', 'pos_teste', 'ganho_aprendizado']].mean())
