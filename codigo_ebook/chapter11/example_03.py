# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Classe para Geração de Relatórios
Linha original no arquivo LaTeX: 87

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

class GeradorRelatorio:
    """Classe para automatizar a geração de relatórios científicos"""

    def __init__(self, dados, titulo="Relatório de Pesquisa", autor="Pesquisador"):
        self.dados = dados
        self.titulo = titulo
        self.autor = autor
        self.data_relatorio = datetime.now()
        self.figuras = []
        self.estatisticas = {}

    def calcular_estatisticas_descritivas(self):
        """Calcula estatísticas descritivas básicas"""
        stats = {}

        # Estatísticas por grupo
        for grupo in self.dados['grupo'].unique():
            dados_grupo = self.dados[self.dados['grupo'] == grupo]
            stats[grupo] = {
                'n': len(dados_grupo),
                'pre_teste_media': dados_grupo['pre_teste'].mean(),
                'pre_teste_dp': dados_grupo['pre_teste'].std(),
                'pos_teste_media': dados_grupo['pos_teste'].mean(),
                'pos_teste_dp': dados_grupo['pos_teste'].std(),
                'ganho_media': dados_grupo['ganho_aprendizado'].mean(),
                'ganho_dp': dados_grupo['ganho_aprendizado'].std(),
                'satisfacao_media': dados_grupo['satisfacao'].mean(),
                'satisfacao_dp': dados_grupo['satisfacao'].std()
            }

        # Estatísticas gerais
        stats['geral'] = {
            'total_participantes': len(self.dados),
            'idade_media': self.dados['idade'].mean(),
            'idade_dp': self.dados['idade'].std(),
            'periodo_coleta': f"{self.dados['data_coleta'].min().strftime('%d/%m/%Y')} a {self.dados['data_coleta'].max().strftime('%d/%m/%Y')}"
        }

        self.estatisticas = stats
        return stats
