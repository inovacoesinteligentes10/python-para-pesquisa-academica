# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Classe para Geração de Relatórios
Linha original no arquivo LaTeX: 181

Este código foi extraído automaticamente do arquivo chapter11.tex
"""
import numpy as np
import matplotlib.pyplot as plt


def gerar_graficos(self, salvar=True):
        """Gera gráficos para o relatório"""

        # Configuração de figura
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))

        # Gráfico 1: Comparação pré vs pós por grupo
        grupos = self.dados['grupo'].unique()
        x = np.arange(len(grupos))
        width = 0.35

        pre_medias = [self.dados[self.dados['grupo'] == g]['pre_teste'].mean() for g in grupos]
        pos_medias = [self.dados[self.dados['grupo'] == g]['pos_teste'].mean() for g in grupos]
        pre_erros = [self.dados[self.dados['grupo'] == g]['pre_teste'].std() for g in grupos]
        pos_erros = [self.dados[self.dados['grupo'] == g]['pos_teste'].std() for g in grupos]

        axes[0, 0].bar(x - width/2, pre_medias, width, label='Pré-teste',
                       yerr=pre_erros, capsize=5, alpha=0.8)
        axes[0, 0].bar(x + width/2, pos_medias, width, label='Pós-teste',
                       yerr=pos_erros, capsize=5, alpha=0.8)
        axes[0, 0].set_xlabel('Grupo')
        axes[0, 0].set_ylabel('Pontuação')
        axes[0, 0].set_title('Comparação Pré vs Pós-teste por Grupo')
        axes[0, 0].set_xticks(x)
        axes[0, 0].set_xticklabels(grupos)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Gráfico 2: Distribuição dos ganhos de aprendizado
        self.dados.boxplot(column='ganho_aprendizado', by='grupo', ax=axes[0, 1])
        axes[0, 1].set_title('Distribuição dos Ganhos de Aprendizado')
        axes[0, 1].set_xlabel('Grupo')
        axes[0, 1].set_ylabel('Ganho (Pós - Pré)')

        # Gráfico 3: Correlação entre satisfação e ganho
        cores = {'Controle': 'blue', 'Experimental': 'red'}
        for grupo in grupos:
            dados_grupo = self.dados[self.dados['grupo'] == grupo]
            axes[1, 0].scatter(dados_grupo['satisfacao'], dados_grupo['ganho_aprendizado'],
                              c=cores[grupo], alpha=0.6, label=grupo)
