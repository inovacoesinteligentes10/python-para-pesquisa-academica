# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Slides Interativos com Dados
Linha original no arquivo LaTeX: 840

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Slide com resultados estatísticos
def criar_slide_estatisticas(dados):
    """Cria slide com resultados estatísticos"""
    from scipy import stats

    # Realizando testes
    controle = dados[dados['grupo'] == 'Controle']
    experimental = dados[dados['grupo'] == 'Experimental']

    # Teste t
    t_stat, p_valor = stats.ttest_ind(experimental['pos_teste'], controle['pos_teste'])

    # Cohen's d
    pooled_std = np.sqrt(((len(controle)-1)*controle['pos_teste'].std()**2 +
                         (len(experimental)-1)*experimental['pos_teste'].std()**2) /
                        (len(controle)+len(experimental)-2))
    cohens_d = (experimental['pos_teste'].mean() - controle['pos_teste'].mean()) / pooled_std

    # Interpretação do tamanho do efeito
    if abs(cohens_d) < 0.2:
        interpretacao_d = "Pequeno"
    elif abs(cohens_d) < 0.5:
        interpretacao_d = "Médio"
    elif abs(cohens_d) < 0.8:
        interpretacao_d = "Grande"
    else:
        interpretacao_d = "Muito Grande"

    conteudo_stats = f"""
    <div style="text-align: center;">
#         <h3>Teste t para Amostras Independentes</h3>
        <div style="background-color: #ecf0f1; padding: 30px; border-radius: 10px; margin: 20px 0;">
            <p style="font-size: 24px; margin: 10px 0;"><strong>t({len(dados)-2}) = {t_stat:.3f}</strong></p>
            <p style="font-size: 24px; margin: 10px 0; color: {'#e74c3c' if p_valor < 0.05 else '#95a5a6'};"><strong>p = {p_valor:.4f}</strong></p>
            <p style="font-size: 20px; margin: 10px 0;"><strong>Cohen's d = {cohens_d:.3f}</strong> <em>({interpretacao_d})</em></p>
#         </div>

        <h3 style="margin-top: 40px;">Conclusão:</h3>
        <p style="font-size: 20px; color: {'#27ae60' if p_valor < 0.05 else '#e74c3c'};">
            {'✓ Diferença estatisticamente significativa' if p_valor < 0.05 else '✗ Diferença não significativa'}
#         </p>

"""