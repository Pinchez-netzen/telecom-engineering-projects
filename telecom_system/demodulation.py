def bpsk_demodulation(signal):
    """
    Convert noisy BPSK signal back to binary string
    """
    binary = ''

    for value in signal:
        if value > 0:
            binary += '1'
        else:
            binary += '0'

    return binary

def qpsk_demodulation(symbols):
    """
    Convert QPSK symbols back to binary
    """
    binary = ''

    for s in symbols:
        real = s.real
        imag = s.imag

        if real > 0 and imag > 0:
            binary += '00'
        elif real < 0 and imag > 0:
            binary += '01'
        elif real < 0 and imag < 0:
            binary += '11'
        elif real > 0 and imag < 0:
            binary += '10'

    return binary