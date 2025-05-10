from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from math import log2, pi


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def bit_reverse_inplace(P):
    n = len(P)
    j = 0
    for i in range(n):
        if i < j:
            swap(P, i, j)
        mask = n >> 1
        while j & mask:
            j &= ~mask
            mask >>= 1
        j |= mask
    return P


def FFT_inplace(P):
    n = len(P)
    k = 1
    while k < n:
        k *= 2
    P += [0] * (k - n)
    bit_reverse_inplace(P)
    bits = int(log2(k))
    for s in range(1, bits + 1):
        m = 2 ** s
        w = [np.exp(-2j * pi * i / m) for i in range(m // 2)]
        for i in range(0, k, m):
            for j in range(m // 2):
                P_0 = P[i + j]
                P_1 = P[i + j + m // 2]
                P[i + j] = P_0 + w[j] * P_1
                P[i + j + m // 2] = P_0 - w[j] * P_1
    return P


def IFFT_inplace(P):
    n = len(P)
    k = 1
    while k < n:
        k *= 2
    P += [0] * (k - n)
    bit_reverse_inplace(P)
    bits = int(log2(k))
    for s in range(1, bits + 1):
        m = 2 ** s
        w = [np.exp(2j * pi * i / m) for i in range(m // 2)]
        for i in range(0, k, m):
            for j in range(m // 2):
                P_0 = P[i + j]
                P_1 = P[i + j + m // 2]
                P[i + j] = P_0 + w[j] * P_1
                P[i + j + m // 2] = P_0 - w[j] * P_1
    P = [round((x / k).real) for x in P]
    return P


def apply_fft_filter(input_file, cutoff_freq, filter_type='low'):
    sample_rate, data = wavfile.read(input_file)
    original_dtype = data.dtype

    if len(data.shape) == 2:
        data = data.mean(axis=1)
    n_original = len(data)

    # Преобразование данных в комплексные числа
    complex_data = [complex(x, 0) for x in data]

    # Применение FFT_inplace
    spectrum = FFT_inplace(complex_data.copy())
    N = len(spectrum)

    # Генерация частот
    freqs = np.fft.fftfreq(N, d=1 / sample_rate)

    # Создание маски
    if filter_type == 'low':
        mask = np.abs(freqs) < cutoff_freq
    elif filter_type == 'high':
        mask = np.abs(freqs) > cutoff_freq
    else:
        raise ValueError("Filter type must be 'low' or 'high'")
    mask = mask.astype(float)  # Преобразование булевой маски в float

    # Применение маски к спектру
    filtered_spectrum = [s * m for s, m in zip(spectrum, mask)]

    # Применение IFFT_inplace
    filtered_signal = IFFT_inplace(filtered_spectrum.copy())
    filtered_signal = filtered_signal[:n_original]  # Обрезка до исходной длины

    # Преобразование в numpy массив исходного типа
    filtered_signal_np = np.array(filtered_signal, dtype=original_dtype)

    # Сохранение
    output_file = f'{filter_type}_pass_{input_file}'
    wavfile.write(output_file, sample_rate, filtered_signal_np)

    # Визуализация с использованием FFT_inplace
    plt.figure(figsize=(12, 8))

    # Исходный сигнал
    plt.subplot(3, 1, 1)
    plt.plot(data)
    plt.title('Original Signal')

    # Исходный спектр
    plt.subplot(3, 1, 2)
    N = len(spectrum)
    freqs_custom = np.fft.fftfreq(N, 1 / sample_rate)
    plt.plot(freqs_custom[:N // 2], np.abs(np.array(spectrum[:N // 2])))
    plt.title('Original Spectrum (Custom FFT)')

    # Фильтрованный спектр
    plt.subplot(3, 1, 3)
    plt.plot(freqs_custom[:N // 2], np.abs(np.array(filtered_spectrum[:N // 2])))
    plt.title('Filtered Spectrum (Custom FFT)')

    plt.tight_layout()
    plt.show()

    return filtered_signal_np


apply_fft_filter('welcome-to-Mars.wav', 1000, 'low')
apply_fft_filter('welcome-to-Mars.wav', 1000, 'high')