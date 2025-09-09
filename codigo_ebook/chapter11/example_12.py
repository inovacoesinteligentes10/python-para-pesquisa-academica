# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Classe para Geração de Relatórios
Linha original no arquivo LaTeX: 477

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

def gerar_relatorio_completo(self):
        """Gera relatório completo com todas as análises"""
        print("Gerando relatório completo...")
        print("=" * 50)

        # Passo 1: Calcular estatísticas
        print("1. Calculando estatísticas descritivas...")
        self.calcular_estatisticas_descritivas()

        # Passo 2: Realizar testes
        print("2. Realizando testes estatísticos...")
        self.realizar_testes_estatisticos()

        # Passo 3: Gerar gráficos
        print("3. Gerando gráficos...")
        self.gerar_graficos()

        # Passo 4: Gerar relatório HTML
        print("4. Gerando relatório HTML...")
        arquivo_html, _ = self.gerar_relatorio_html()

        print("=" * 50)
        print("Relatório completo gerado com sucesso!")
        print(f"Arquivo: {arquivo_html}")

        return arquivo_html

# Exemplo de uso
relatorio = GeradorRelatorio(
    dados_estudo,
    titulo="Eficácia de Nova Metodologia de Ensino",
    autor="Dr. João Silva"
)

arquivo_relatorio = relatorio.gerar_relatorio_completo()
