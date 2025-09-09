# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 9
Seção: Análise de Ciclos Acadêmicos
Linha original no arquivo LaTeX: 801

Este código foi extraído automaticamente do arquivo chapter9.tex
"""

# Análise de ciclos específicos da área acadêmica
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

# Análise espectral para identificar periodicidades
def analise_espectral(serie, freq_amostragem=12):
    """
    Realiza análise espectral para identificar periodicidades dominantes
    """
    # Removendo tendência (detrending)
    serie_detrend = serie - np.polyval(np.polyfit(range(len(serie)),
                                                  serie, 1), range(len(serie)))

    # Transformada de Fourier
    fft_valores = fft(serie_detrend)
    frequencias = fftfreq(len(serie_detrend), 1/freq_amostragem)

    # Magnitude do espectro (apenas frequências positivas)
    n = len(frequencias) // 2
    magnitude = np.abs(fft_valores[:n])
    freq_positivas = frequencias[:n]

    # Convertendo frequências para períodos
    periodos = 1 / freq_positivas[1:]  # Excluindo frequência zero
    magnitude = magnitude[1:]

    return periodos, magnitude
