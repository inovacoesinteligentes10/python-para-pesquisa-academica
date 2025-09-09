# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Jupyter como Ferramenta de Apresentação
Linha original no arquivo LaTeX: 633

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

# Instalação das dependências para apresentações
# !pip install RISE
# !pip install jupyter_contrib_nbextensions
# !jupyter contrib nbextension install --user
# !jupyter nbextension enable rise --py

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML, display, Markdown
import warnings
warnings.filterwarnings('ignore')
