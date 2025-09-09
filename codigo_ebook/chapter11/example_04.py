# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Classe para Geração de Relatórios
Linha original no arquivo LaTeX: 134

Este código foi extraído automaticamente do arquivo chapter11.tex
"""
import numpy as np


def realizar_testes_estatisticos(self):
        """Realiza testes estatísticos principais"""
        from scipy import stats as scipy_stats

        # Separando grupos
        controle = self.dados[self.dados['grupo'] == 'Controle']
        experimental = self.dados[self.dados['grupo'] == 'Experimental']

        # Teste t para diferenças entre grupos no pós-teste
        t_stat, p_valor = scipy_stats.ttest_ind(
            controle['pos_teste'],
            experimental['pos_teste']
        )

        # Teste t pareado para ganho de aprendizado no grupo experimental
        t_stat_pareado, p_valor_pareado = scipy_stats.ttest_rel(
            experimental['pre_teste'],
            experimental['pos_teste']
        )

        # Tamanho do efeito (Cohen's d)
        pooled_std = np.sqrt(((len(controle)-1)*controle['pos_teste'].std()**2 +
                             (len(experimental)-1)*experimental['pos_teste'].std()**2) /
                            (len(controle)+len(experimental)-2))
        cohens_d = (experimental['pos_teste'].mean() - controle['pos_teste'].mean()) / pooled_std

        testes = {
            'teste_independente': {
                't_statistic': t_stat,
                'p_valor': p_valor,
                'cohens_d': cohens_d,
                'significativo': p_valor < 0.05
            },
            'teste_pareado_experimental': {
                't_statistic': t_stat_pareado,
                'p_valor': p_valor_pareado,
                'significativo': p_valor_pareado < 0.05
            }
        }

        self.testes_estatisticos = testes
        return testes
