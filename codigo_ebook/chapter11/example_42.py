# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Gerador de Documentação de Código
Linha original no arquivo LaTeX: 1557

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

class GeradorDocumentacao:
    """Gera documentação automática para projetos científicos"""

    def __init__(self, nome_projeto, versao="1.0.0"):
        self.nome_projeto = nome_projeto
        self.versao = versao
        self.secoes = []

    def adicionar_secao(self, titulo, conteudo):
        """Adiciona seção à documentação"""
        self.secoes.append({'titulo': titulo, 'conteudo': conteudo})

    def documentar_funcao(self, funcao):
        """Extrai documentação de uma função"""
        import inspect

        doc = {
            'nome': funcao.__name__,
            'docstring': inspect.getdoc(funcao) or 'Sem documentação',
            'assinatura': str(inspect.signature(funcao)),
            'codigo': inspect.getsource(funcao) if hasattr(funcao, '__code__') else 'N/A'
        }
        return doc

    def documentar_dataset(self, df, nome="Dataset"):
        """Documenta estrutura de um dataset"""
        doc = f"""
### {nome}

**Dimensões:** {df.shape[0]} linhas × {df.shape[1]} colunas

**Colunas:**
"""
        for col in df.columns:
            dtype = str(df[col].dtype)
            nulls = df[col].isnull().sum()
            unique = df[col].nunique()
            doc += f"** ({dtype}): {unique} valores únicos, {nulls} valores nulos"

        doc += f"\n\n**Estatísticas Básicas:**\n```df.describe().to_string()\n```"

        return doc

    def gerar_readme(self):
        """Gera arquivo README.md"""
        readme = f"""# {self.nome_projeto}

"""