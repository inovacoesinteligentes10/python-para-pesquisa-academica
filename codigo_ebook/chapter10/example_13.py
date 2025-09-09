# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 10
Seção: Introdução ao Dash
Linha original no arquivo LaTeX: 463

Este código foi extraído automaticamente do arquivo chapter10.tex
"""

import dash
from dash import dcc, html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
