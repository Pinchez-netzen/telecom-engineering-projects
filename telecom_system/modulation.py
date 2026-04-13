import numpy as np

def bpsk_modulation(binary):
    return np.array([1 if bit == '1' else -1 for bit in binary])

def qpsk_modulation(binary):
    """
    Convert binary string into QPSK symbols
    2 bits per symbol
    """
    symbols = []

    # Ensure even number of bits
    if len(binary) % 2 != 0:
        binary += '0'

    for i in range(0, len(binary), 2):
        bits = binary[i:i+2]

        if bits == '00':
            symbols.append(1 + 1j)
        elif bits == '01':
            symbols.append(-1 + 1j)
        elif bits == '11':
            symbols.append(-1 - 1j)
        elif bits == '10':
            symbols.append(1 - 1j)

    return np.array(symbols)