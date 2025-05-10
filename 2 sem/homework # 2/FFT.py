import numpy as np
from math import pi, log2


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