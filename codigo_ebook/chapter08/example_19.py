# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 8
Seção: Técnicas de Validação Cruzada
Linha original no arquivo LaTeX: 1043

Este código foi extraído automaticamente do arquivo chapter8.tex
"""
import matplotlib.pyplot as plt


def plot_learning_curves(self, learning_results: Dict,
                            title: str = "Curvas de Aprendizado"):
        """Visualiza curvas de aprendizado"""
        plt.figure(figsize=(10, 6))

        train_sizes = learning_results['train_sizes']
        train_mean = learning_results['train_scores_mean']
        train_std = learning_results['train_scores_std']
        val_mean = learning_results['val_scores_mean']
        val_std = learning_results['val_scores_std']

        # Curvas de treino
        plt.plot(train_sizes, train_mean, 'o-', color='blue', label='Score de Treino')
        plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std,
                        alpha=0.2, color='blue')

        # Curvas de validação
        plt.plot(train_sizes, val_mean, 'o-', color='red', label='Score de Validação')
        plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std,
                        alpha=0.2, color='red')

        plt.xlabel('Tamanho do Conjunto de Treino')
        plt.ylabel('Score')
        plt.title(title)
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
