# Makefile para Python para Pesquisa Acadêmica
# Utiliza uv para gerenciamento de pacotes

.PHONY: help install test fix clean run-example run-chapter jupyter lint

help: ## Mostrar ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instalar dependências usando uv
	@echo "📦 Instalando dependências com uv..."
	uv sync
	@echo "✅ Dependências instaladas!"

install-dev: ## Instalar dependências de desenvolvimento
	@echo "📦 Instalando dependências de desenvolvimento..."
	uv add --dev pytest black isort ruff mypy
	@echo "✅ Dependências de desenvolvimento instaladas!"

test: ## Testar sintaxe de todos os exemplos
	@echo "🔍 Testando sintaxe de todos os exemplos..."
	uv run python test_examples.py

fix: ## Aplicar correções automáticas aos exemplos
	@echo "🔧 Aplicando correções automáticas..."
	python fix_examples.py
	@echo "✅ Correções aplicadas!"

test-fix: fix test ## Aplicar correções e testar
	@echo "🔄 Correções aplicadas e testes executados!"

clean: ## Limpar arquivos temporários
	@echo "🧹 Limpando arquivos temporários..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✅ Limpeza concluída!"

run-example: ## Executar exemplo específico (uso: make run-example EXAMPLE=chapter03/example_01.py)
ifndef EXAMPLE
	@echo "❌ Especifique o exemplo: make run-example EXAMPLE=chapter03/example_01.py"
else
	@echo "🚀 Executando $(EXAMPLE)..."
	uv run python codigo_ebook/$(EXAMPLE)
endif

run-chapter: ## Executar todos exemplos de um capítulo (uso: make run-chapter CHAPTER=03)
ifndef CHAPTER
	@echo "❌ Especifique o capítulo: make run-chapter CHAPTER=03"
else
	@echo "🚀 Executando todos exemplos do capítulo $(CHAPTER)..."
	@for file in codigo_ebook/chapter$(CHAPTER)/*.py; do \
		echo "📄 Executando $$file"; \
		uv run python "$$file" || echo "❌ Erro em $$file"; \
	done
endif

jupyter: ## Iniciar Jupyter Notebook
	@echo "📓 Iniciando Jupyter Notebook..."
	uv run jupyter notebook --port=8888

jupyter-lab: ## Iniciar Jupyter Lab
	@echo "🔬 Iniciando Jupyter Lab..."
	uv run jupyter lab --port=8888

lint: ## Verificar qualidade do código
	@echo "🔍 Verificando qualidade do código..."
	uv run ruff check .
	uv run black --check .

format: ## Formatar código
	@echo "🎨 Formatando código..."
	uv run black .
	uv run isort .

check-env: ## Verificar ambiente e dependências
	@echo "🔍 Verificando ambiente..."
	@python -c "import sys; print(f'Python: {sys.version}')"
	@python -c "import uv; print('✅ uv instalado')" 2>/dev/null || echo "❌ uv não encontrado"
	@python -c "import numpy, pandas, matplotlib, sklearn; print('✅ Bibliotecas principais OK')" 2>/dev/null || echo "❌ Algumas bibliotecas não encontradas"

stats: ## Mostrar estatísticas do projeto
	@echo "📊 Estatísticas do projeto:"
	@echo "Total de arquivos Python: $$(find codigo_ebook -name "*.py" | wc -l)"
	@echo "Linhas de código: $$(find codigo_ebook -name "*.py" -exec wc -l {} + | tail -1 | awk '{print $$1}')"
	@echo "Capítulos: $$(find codigo_ebook -type d -name "chapter*" | wc -l)"

setup: install test ## Configuração inicial completa
	@echo "🎉 Configuração inicial concluída!"
	@echo "💡 Use 'make help' para ver todos os comandos disponíveis"

# Comandos para desenvolvimento
dev-install: install-dev ## Instalar tudo para desenvolvimento
	@echo "🛠️  Ambiente de desenvolvimento configurado!"

dev-test: test lint ## Executar todos os testes de desenvolvimento
	@echo "✅ Testes de desenvolvimento concluídos!"

# Comandos para exemplos específicos
chapter01: ## Executar exemplos do Capítulo 1 - Introdução
	@make run-chapter CHAPTER=01

chapter03: ## Executar exemplos do Capítulo 3 - NumPy, Pandas, Matplotlib
	@make run-chapter CHAPTER=03

chapter04: ## Executar exemplos do Capítulo 4 - Análise Estatística
	@make run-chapter CHAPTER=04

chapter05: ## Executar exemplos do Capítulo 5 - Metodologia
	@make run-chapter CHAPTER=05

chapter09: ## Executar exemplos do Capítulo 9 - Séries Temporais
	@make run-chapter CHAPTER=09

chapter10: ## Executar exemplos do Capítulo 10 - Visualizações
	@make run-chapter CHAPTER=10