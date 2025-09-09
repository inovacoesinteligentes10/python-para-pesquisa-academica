# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Verificação de Pressupostos
Linha original no arquivo LaTeX: 132

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def diagnosticos_visuais(dados, grupo_col, variavel_dependente):
    """Cria diagnosticos visuais"""
    print(f"\n3. DIAGNOSTICOS VISUAIS")
    print("-" * 20)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Q-Q plot para normalidade
    stats.probplot(dados[variavel_dependente], dist="norm", plot=axes[0,0])
    axes[0,0].set_title('Q-Q Plot (Normalidade)')
    axes[0,0].grid(True, alpha=0.3)

    # Histograma com curva normal
    axes[0,1].hist(dados[variavel_dependente], bins=20, density=True, alpha=0.7)
    mu, sigma = dados[variavel_dependente].mean(), dados[variavel_dependente].std()
    x = np.linspace(dados[variavel_dependente].min(), dados[variavel_dependente].max(), 100)
    axes[0,1].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, label='Normal teorica')
    axes[0,1].set_title('Histograma vs Normal')
    axes[0,1].legend()

    # Boxplot por grupo (se aplicavel)
    if grupo_col:
        dados.boxplot(column=variavel_dependente, by=grupo_col, ax=axes[1,0])
        axes[1,0].set_title('Boxplot por Grupo')
    else:
        axes[1,0].boxplot(dados[variavel_dependente])
        axes[1,0].set_title('Boxplot Geral')

    return axes
