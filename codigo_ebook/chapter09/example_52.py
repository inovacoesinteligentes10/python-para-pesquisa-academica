# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Previsão com Incerteza Sazonal
Linha original no arquivo LaTeX: 1049

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Destacando períodos de maior incerteza
alta_incerteza = df_incerteza['amplitude_ic'] > df_incerteza['amplitude_ic'].median()
axes[0].scatter(df_incerteza[alta_incerteza]['data'],
                df_incerteza[alta_incerteza]['previsao'],
                s=100, color='orange', marker='*',
                label='Alta Incerteza', zorder=5)

axes[0].set_title('Previsão com Análise de Incerteza Sazonal',
                  fontsize=14, fontweight='bold')
axes[0].set_ylabel('Número de Publicações')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].tick_params(axis='x', rotation=45)
