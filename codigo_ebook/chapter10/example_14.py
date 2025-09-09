# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Introdução ao Dash
Linha original no arquivo LaTeX: 479

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# dashboard_pesquisa.py - Dashboard completo com Dash

# Configuração da aplicação
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard de Pesquisa Acadêmica"

# Carregando dados (mesmo dataset anterior)
def carregar_dados():
    np.random.seed(42)
    n_participantes = 1000

    dados = pd.DataFrame({
        'participante_id': range(1, n_participantes + 1),
        'idade': np.random.normal(35, 12, n_participantes).astype(int),
        'bem_estar': np.random.normal(7, 1.5, n_participantes),
        'produtividade': np.random.normal(75, 15, n_participantes),
        'horas_trabalho': np.random.normal(8, 2, n_participantes),
        'satisfacao_trabalho': np.random.normal(6.5, 1.8, n_participantes),
        'area': np.random.choice(['Tecnologia', 'Educação', 'Saúde', 'Finanças'], n_participantes),
        'experiencia': np.random.randint(1, 20, n_participantes),
        'data_coleta': pd.date_range(start='2023-01-01', periods=n_participantes, freq='H')
    })

    # Correlações realistas
    dados['produtividade'] += dados['bem_estar'] * 3 + np.random.normal(0, 5, n_participantes)
    dados['satisfacao_trabalho'] += dados['bem_estar'] * 0.3 + np.random.normal(0, 0.5, n_participantes)

    # Limitando valores
    dados['bem_estar'] = np.clip(dados['bem_estar'], 1, 10)
    dados['satisfacao_trabalho'] = np.clip(dados['satisfacao_trabalho'], 1, 10)
    dados['produtividade'] = np.clip(dados['produtividade'], 30, 100)
    dados['horas_trabalho'] = np.clip(dados['horas_trabalho'], 4, 12)

    return dados

dados_globais = carregar_dados()
