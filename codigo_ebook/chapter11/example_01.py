# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 11
Seção: Fundamentos da Geração Automatizada
Linha original no arquivo LaTeX: 18

Este código foi extraído automaticamente do arquivo chapter11.tex
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import jinja2
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import warnings
warnings.filterwarnings('ignore')
