# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Slides de Conclusão e Recomendações
Linha original no arquivo LaTeX: 911

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Slide de conclusões
def criar_slide_conclusoes(dados):
    """Cria slide com conclusões do estudo"""

    # Calculando estatísticas finais
    experimental = dados[dados['grupo'] == 'Experimental']
    controle = dados[dados['grupo'] == 'Controle']

    ganho_experimental = experimental['ganho_aprendizado'].mean()
    ganho_controle = controle['ganho_aprendizado'].mean()
    diferenca_percentual = ((ganho_experimental - ganho_controle) / ganho_controle) * 100

    conteudo_conclusoes = f"""
#     <h3>Principais Achados:</h3>
    <div style="background-color: #e8f5e8; padding: 20px; border-left: 5px solid #27ae60; margin: 20px 0;">
        <ul style="font-size: 18px; line-height: 2;">
#             <li>O grupo experimental apresentou <strong>{diferenca_percentual:.1f}% mais ganho</strong> de aprendizado</li>
#             <li>Diferença estatisticamente significativa entre os grupos (p < 0.05)</li>
#             <li>Tamanho do efeito considerado <strong>médio a grande</strong></li>
#             <li>Alta satisfação no grupo experimental</li>
#         </ul>
#     </div>

#     <h3>Implicações Práticas:</h3>
    <ul style="font-size: 18px; line-height: 2;">
#         <li>A nova metodologia é <strong>eficaz</strong> para melhorar o aprendizado</li>
#         <li>Implementação recomendada em maior escala</li>
#         <li>Benefícios observados em diferentes perfis de estudantes</li>
#     </ul>

#     <h3>Limitações:</h3>
    <ul style="font-size: 16px; line-height: 1.8; color: #7f8c8d;">
#         <li>Estudo de curta duração</li>
#         <li>Amostra específica de uma instituição</li>
#         <li>Necessidade de replicação em outros contextos</li>
#     </ul>
    """
