# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Controle de Erro Tipo I em Múltiplas Comparações
Linha original no arquivo LaTeX: 1222

Este código foi extraído automaticamente do arquivo chapter4.tex
"""

def aplicar_correcoes(p_valores, metodos):
    """Aplica diferentes metodos de correcao"""
    resultados = {}

    for metodo in metodos:
        reject, p_corrigidos, alpha_sidak, alpha_bonf = multipletests(
            p_valores, alpha=0.05, method=metodo, returnsorted=False)

        n_significativos = np.sum(reject)

        print(f"metodo.upper():")
        print(f"  P-valores corrigidos: {p_corrigidos.round(4)}")
        print(f"  Significativos apos correcao: {n_significativos}")
        print(f"  Indices significativos: {np.where(reject)[0]}")

        resultados[metodo] = {
            'p_corrigidos': p_corrigidos,
            'significativos': reject,
            'n_significativos': n_significativos
        }

    return resultados
