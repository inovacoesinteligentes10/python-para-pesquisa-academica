# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Relatórios em PDF com ReportLab
Linha original no arquivo LaTeX: 519

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

def gerar_relatorio_pdf(dados, titulo="Relatório de Pesquisa"):
    """Gera relatório profissional em PDF"""
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.lib.pagesizes import letter

    # Configuração do documento
    nome_arquivo = f"relatorio_pdf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)

    # Estilos
    styles = getSampleStyleSheet()
    titulo_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        alignment=1  # Centralizado
    )

    # Conteúdo do documento
    story = []

    # Título
    story.append(Paragraph(titulo, titulo_style))
    story.append(Spacer(1, 12))

    # Informações gerais
    info_geral = f"""
    <b>Data do Relatório:</b> {datetime.now().strftime('%d/%m/%Y')}<br/>
#     <b>Total de Participantes:</b> {len(dados)}<br/>
    <b>Período de Coleta:</b> {dados['data_coleta'].min().strftime('%d/%m/%Y')} a {dados['data_coleta'].max().strftime('%d/%m/%Y')}
    """
    story.append(Paragraph(info_geral, styles['Normal']))
    story.append(Spacer(1, 12))

    # Estatísticas por grupo
    story.append(Paragraph("<b>Estatísticas por Grupo</b>", styles['Heading2']))
