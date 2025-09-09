# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Jupyter como Ferramenta de Apresentação
Linha original no arquivo LaTeX: 651

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Configuração para apresentações
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 14
sns.set_style("whitegrid")
sns.set_palette("husl")

# Função para criar slides com markdown
def criar_slide_titulo(titulo, subtitulo="", autor=""):
    """Cria slide de título para apresentação"""
    html_content = f"""
    <div style="text-align: center; padding: 100px 0;">
        <h1 style="font-size: 48px; color: #2c3e50; margin-bottom: 30px;">{titulo}</h1>
        {f'<h2 style="font-size: 32px; color: #7f8c8d; margin-bottom: 20px;">{subtitulo}</h2>' if subtitulo else ''}
        {f'<h3 style="font-size: 24px; color: #95a5a6;">{autor}</h3>' if autor else ''}
        <p style="font-size: 18px; color: #bdc3c7; margin-top: 40px;">{datetime.now().strftime('%d de %B de %Y')}</p>
#     </div>
    """
    return HTML(html_content)

# Função para slides de conteúdo
def criar_slide_conteudo(titulo, conteudo, layout="single"):
    """Cria slide de conteúdo"""
    if layout == "single":
        html_content = f"""
        <div style="padding: 20px;">
            <h2 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 30px;">{titulo}</h2>
            <div style="font-size: 18px; line-height: 1.6;">
                {conteudo}
#             </div>
#         </div>
        """
    elif layout == "two-column":
        conteudo_esq, conteudo_dir = conteudo
        html_content = f"""
        <div style="padding: 20px;">
            <h2 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 30px;">{titulo}</h2>
            <div style="display: flex; gap: 40px;">
                <div style="flex: 1; font-size: 16px; line-height: 1.6;">
                    {conteudo_esq}
#                 </div>
                <div style="flex: 1; font-size: 16px; line-height: 1.6;">
                    {conteudo_dir}
#                 </div>
#             </div>
#         </div>
        """
