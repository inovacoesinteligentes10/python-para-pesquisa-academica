# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Introdução ao Dash
Linha original no arquivo LaTeX: 520

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# Layout básico do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Pesquisa Acadêmica"),
    dcc.Graph(id="exemplo-grafico"),
    html.P("Dashboard funcional com Dash")
])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
