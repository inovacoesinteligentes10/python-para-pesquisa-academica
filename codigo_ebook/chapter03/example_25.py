# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 3
Seção: Integração das Três Bibliotecas
Linha original no arquivo LaTeX: 775

Este código foi extraído automaticamente do arquivo chapter3.tex
"""

def pipeline_visualizacoes_3_4(dados_limpos, ax3, ax4):
    # Gráfico 3: Pré vs Pós por grupo
    grupos = ['Controle', 'Experimental']
    pre_medias = [dados_limpos[dados_limpos['grupo'] == g]['pre_teste'].mean()
                  for g in ['controle', 'experimental']]
    pos_medias = [dados_limpos[dados_limpos['grupo'] == g]['pos_teste'].mean()
                  for g in ['controle', 'experimental']]

    x = np.arange(len(grupos))
    largura = 0.35

    ax3.bar(x - largura/2, pre_medias, largura, label='Pré-teste', alpha=0.8)
    ax3.bar(x + largura/2, pos_medias, largura, label='Pós-teste', alpha=0.8)
    ax3.set_xlabel('Grupo')
    ax3.set_ylabel('Score Médio')
    ax3.set_title('Pré vs Pós-teste')
    ax3.set_xticks(x)
    ax3.set_xticklabels(grupos)
    ax3.legend()

    # Gráfico 4: Correlação idade vs melhoria
    ax4.scatter(dados_limpos['idade'], dados_limpos['melhoria'], alpha=0.6)

    # Linha de tendência
    z = np.polyfit(dados_limpos['idade'], dados_limpos['melhoria'], 1)
    p = np.poly1d(z)
    ax4.plot(dados_limpos['idade'], p(dados_limpos['idade']), "r--", alpha=0.8)

    # Correlação
    r = np.corrcoef(dados_limpos['idade'], dados_limpos['melhoria'])[0, 1]
    ax4.text(0.05, 0.95, f'r = {r:.3f}', transform=ax4.transAxes,
             bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.8))

    ax4.set_xlabel('Idade')
    ax4.set_ylabel('Melhoria')
    ax4.set_title('Idade vs Melhoria')

    plt.tight_layout()
    plt.savefig('pipeline_completo.png', dpi=300, bbox_inches='tight')
    plt.show()
