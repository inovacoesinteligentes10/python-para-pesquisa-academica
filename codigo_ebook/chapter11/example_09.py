# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Classe para Geração de Relatórios
Linha original no arquivo LaTeX: 355

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Template HTML continuação
template_continuation = """
#                     <tr>
#                         <td>Pré-teste (M +/- DP)</td>
#                         <td>{{ pre_controle | round(2) }} +/- {{ pre_controle_dp | round(2) }}</td>
#                         <td>{{ pre_experimental | round(2) }} +/- {{ pre_experimental_dp | round(2) }}</td>
#                     </tr>
                    <tr class="highlight">
#                         <td>Pós-teste (M +/- DP)</td>
#                         <td>{{ pos_controle | round(2) }} +/- {{ pos_controle_dp | round(2) }}</td>
#                         <td>{{ pos_experimental | round(2) }} +/- {{ pos_experimental_dp | round(2) }}</td>
#                     </tr>
                    <tr class="highlight">
#                         <td>Ganho de Aprendizado</td>
#                         <td>{{ ganho_controle | round(2) }} +/- {{ ganho_controle_dp | round(2) }}</td>
#                         <td>{{ ganho_experimental | round(2) }} +/- {{ ganho_experimental_dp | round(2) }}</td>
#                     </tr>
#                     <tr>
#                         <td>Satisfação</td>
#                         <td>{{ sat_controle | round(2) }} +/- {{ sat_controle_dp | round(2) }}</td>
#                         <td>{{ sat_experimental | round(2) }} +/- {{ sat_experimental_dp | round(2) }}</td>
#                     </tr>
#                 </table>
#             </div>

            <div class="section">
#                 <h2>4. Análises Estatísticas</h2>
#                 <h3>Teste t para Amostras Independentes (Pós-teste)</h3>
#                 <ul>
#                     <li>t({{ graus_liberdade }}) = {{ t_statistic | round(3) }}</li>
#                     <li>p = {{ p_valor | round(4) }}</li>
                    <li>Cohen's d = {{ cohens_d | round(3) }}</li>
#                     <li><strong>Interpretação:</strong> {{ interpretacao_resultado }}</li>
#                 </ul>
#             </div>
"""

# Dados de exemplo para o template
dados_template = {
    'pre_controle': 75.5,
    'pre_controle_dp': 8.2,
    'pre_experimental': 76.1,
    'pre_experimental_dp': 7.9,
    'pos_controle': 78.3,
    'pos_controle_dp': 8.5,
    'pos_experimental': 85.7,
    'pos_experimental_dp': 6.8,
    'ganho_controle': 2.8,
    'ganho_controle_dp': 3.1,
    'ganho_experimental': 9.6,
    'ganho_experimental_dp': 4.2,
    'sat_controle': 6.2,
    'sat_controle_dp': 1.8,
    'sat_experimental': 8.1,
    'sat_experimental_dp': 1.3,
    'graus_liberdade': 98,
    't_statistic': 4.82,
    'p_valor': 0.0001,
    'cohens_d': 0.96,
    'interpretacao_resultado': 'Diferença estatisticamente significativa com efeito grande'
}
