# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Características dos Dados Temporais
Linha original no arquivo LaTeX: 16

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuração para gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
