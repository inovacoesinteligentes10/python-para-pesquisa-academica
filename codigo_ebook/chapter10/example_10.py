# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Fundamentos do Streamlit
Linha original no arquivo LaTeX: 331

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

# app_pesquisa.py - Aplicação Streamlit para Análise de Dados de Pesquisa

def main():
    st.set_page_config(
        page_title="Dashboard de Pesquisa",
        page_icon="��",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("�� Dashboard Interativo de Análise de Pesquisa")
    st.markdown("---")

    # Sidebar para controles
    st.sidebar.header("�� Controles de Análise")

    # Upload de dados ou usar dados de exemplo
    opcao_dados = st.sidebar.radio(
        "Fonte de Dados:",
        ["Usar dados de exemplo", "Upload de arquivo CSV"]
    )

    if opcao_dados == "Upload de arquivo CSV":
        uploaded_file = st.sidebar.file_uploader(
            "Escolha um arquivo CSV",
            type="csv"
        )

        if uploaded_file is not None:
            dados = pd.read_csv(uploaded_file)
            st.sidebar.success("Arquivo carregado com sucesso!")
        else:
            st.warning("Por favor, faça upload de um arquivo CSV.")
            return
    else:
        # Usando dados de exemplo (mesmo dataset anterior)
        dados = carregar_dados_exemplo()

    # Exibindo informações básicas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total de Participantes", len(dados))
    with col2:
        st.metric("Bem-estar Médio", f"{dados['bem_estar'].mean():.1f}")
    with col3:
        st.metric("Produtividade Média", f"{dados['produtividade'].mean():.1f}")
    with col4:
        st.metric("Satisfação Média", f"{dados['satisfacao_trabalho'].mean():.1f}")

    st.markdown("---")

if __name__ == "__main__":
    main()
