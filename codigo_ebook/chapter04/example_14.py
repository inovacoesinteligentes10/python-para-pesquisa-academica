# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Análise de Regressão Robusta
Linha original no arquivo LaTeX: 530

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def visualizacoes_diagnosticas(residuos, valores_preditos, residuos_estudentizados, dados, preditores):
    """Cria visualizacoes diagnosticas"""
    # 3. VISUALIZACOES DIAGNOSTICAS
    print(f"\n3. DIAGNOSTICOS VISUAIS")
    print("-" * 20)

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # Residuos vs valores preditos
    axes[0,0].scatter(valores_preditos, residuos, alpha=0.7)
    axes[0,0].axhline(y=0, color='r', linestyle='--')
    axes[0,0].set_xlabel('Valores Preditos')
    axes[0,0].set_ylabel('Residuos')
    axes[0,0].set_title('Residuos vs Preditos')

    # Q-Q plot dos residuos
    stats.probplot(residuos, dist="norm", plot=axes[0,1])
    axes[0,1].set_title('Q-Q Plot dos Residuos')

    # Scale-Location plot
    residuos_padronizados = np.sqrt(np.abs(residuos_estudentizados))
    axes[0,2].scatter(valores_preditos, residuos_padronizados, alpha=0.7)
    axes[0,2].set_xlabel('Valores Preditos')
    axes[0,2].set_ylabel('Residuos Padronizados')
    axes[0,2].set_title('Scale-Location Plot')

    # Residuos vs cada preditor
    for i, pred in enumerate(preditores[:3]):  # Maximo 3 preditores
        if i < len(preditores):
            axes[1,i].scatter(dados[pred], residuos, alpha=0.7)
            axes[1,i].axhline(y=0, color='r', linestyle='--')
            axes[1,i].set_xlabel(pred)
            axes[1,i].set_ylabel('Residuos')
            axes[1,i].set_title(f'Residuos vs {pred}')

    plt.tight_layout()
    plt.show()
