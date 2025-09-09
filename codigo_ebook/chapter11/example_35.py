# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Gráficos com Anotações Estatísticas
Linha original no arquivo LaTeX: 1276

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

def criar_grafico_com_anotacoes(dados):
    """Cria gráfico com anotações estatísticas para publicação"""
    from scipy import stats as scipy_stats

    fig, ax = plt.subplots(figsize=(10, 8))

    # Preparando dados
    controle = dados[dados['grupo'] == 'Controle']['pos_teste']
    experimental = dados[dados['grupo'] == 'Experimental']['pos_teste']

    # Violin plot
    positions = [1, 2]
    vp = ax.violinplot([controle, experimental], positions=positions,
                       widths=0.5, showmeans=True, showmedians=True)

    # Personalizando cores
    for i, pc in enumerate(vp['bodies']):
        pc.set_facecolor(cores_publicacao[i])
        pc.set_alpha(0.7)

    # Teste estatístico
    t_stat, p_valor = scipy_stats.ttest_ind(controle, experimental)

    # Adicionando anotação de significância
    if p_valor < 0.001:
        sig_text = '***'
    elif p_valor < 0.01:
        sig_text = '**'
    elif p_valor < 0.05:
        sig_text = '*'
    else:
        sig_text = 'ns'

    # Linha conectando grupos
    y_max = max(controle.max(), experimental.max())
    y_line = y_max + 5
    ax.plot([1, 2], [y_line, y_line], 'k-', linewidth=1)
    ax.text(1.5, y_line + 1, sig_text, ha='center', fontsize=14)
    ax.text(1.5, y_line + 4, f'p = {p_valor:.4f}', ha='center', fontsize=10)

    # Adicionando médias como texto
    ax.text(1, controle.mean() - 5, f'M = {controle.mean():.1f}',
            ha='center', fontsize=10, fontweight='bold')
    ax.text(2, experimental.mean() - 5, f'M = {experimental.mean():.1f}',
            ha='center', fontsize=10, fontweight='bold')
