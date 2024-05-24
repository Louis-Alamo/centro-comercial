import random


import numpy as np
from scipy.stats import kstest


# Generador Congruencial Mixto
def lcg(a, c, m, seed, n):
    x = seed
    result = []
    for _ in range(n):
        x = (a * x + c) % m
        result.append(x)
    return result


# Prueba de Kolmogorov-Smirnov
def ks_test(sequence):
    ks_stat, p_value = kstest(sequence, 'uniform')
    return p_value


# Prueba de Correlación Autocorrelada
def autocorrelation_test(sequence, lag=1):
    n = len(sequence)
    mean = np.mean(sequence)
    autocov = np.sum((sequence[:n - lag] - mean) * (sequence[lag:] - mean))
    autocorr = autocov / np.sum((sequence - mean) ** 2)
    return abs(autocorr)


# Prueba de la Transformada Discreta de Fourier (DFT)
def dft_test(sequence, threshold=0.95):
    N = len(sequence)
    fft_values = np.fft.fft(sequence)
    power_spectrum = np.abs(fft_values) ** 2
    cutoff = int(threshold * N / 2)
    dft_pass = np.sum(power_spectrum[1:cutoff]) / np.sum(power_spectrum[cutoff:])
    return dft_pass


# Generar números aleatorios y verificar su calidad
def generar_numeros_aleatorios(cantidad):
    # Parámetros del LCG
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    seed_max = 2 ** 31 - 1

    while True:
        seed = np.random.randint(0, seed_max)
        random_numbers = lcg(a, c, m, seed, cantidad)
        normalized_numbers = [x / m for x in random_numbers]

        # Realizar pruebas
        p_value_ks = ks_test(normalized_numbers)
        autocorr = autocorrelation_test(normalized_numbers)
        dft_pass = dft_test(normalized_numbers)

        # Verificar si los números pasan las pruebas
        pruebas_aprobadas = 0
        if p_value_ks > 0.05:
            pruebas_aprobadas += 1
        if autocorr < 0.05:
            pruebas_aprobadas += 1
        if dft_pass < 1:  # Ajuste según el umbral especificado
            pruebas_aprobadas += 1

        if pruebas_aprobadas >= 2:
            return normalized_numbers




def generar_aleatorio():
    return generar_numeros_aleatorios(10)[0]