# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Slides Interativos com Dados
Linha original no arquivo LaTeX: 740

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Slide com metodologia
conteudo_metodologia = f"""
# <h3>Desenho do Estudo:</h3>
<p style="font-size: 18px;">Experimento controlado randomizado com pré e pós-teste</p>

# <h3>Participantes:</h3>
<ul style="font-size: 18px; line-height: 1.8;">
#     <li><strong>N =</strong> {len(dados_estudo)} participantes</li>
    <li><strong>Grupo Controle:</strong> {len(dados_estudo[dados_estudo['grupo'] == 'Controle'])} participantes</li>
    <li><strong>Grupo Experimental:</strong> {len(dados_estudo[dados_estudo['grupo'] == 'Experimental'])} participantes</li>
    <li><strong>Idade média:</strong> {dados_estudo['idade'].mean():.1f} anos (DP = {dados_estudo['idade'].std():.1f})</li>
# </ul>

# <h3>Instrumentos:</h3>
<ul style="font-size: 18px; line-height: 1.8;">
#     <li>Teste de conhecimento (0-100 pontos)</li>
#     <li>Escala de satisfação (1-10 pontos)</li>
#     <li>Questionário sociodemográfico</li>
# </ul>
"""

display(criar_slide_conteudo("Metodologia", conteudo_metodologia))
