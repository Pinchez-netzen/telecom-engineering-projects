import numpy as np

def add_awgn(signal, noise_std=0.5):
    """
    Add Gaussian noise (AWGN) to the signal
    """
    noise = np.random.normal(0, noise_std, len(signal))
    noisy_signal = signal + noise
    return noisy_signal

def add_awgn_complex(signal, noise_std=0.5):
    noise_real = np.random.normal(0, noise_std, len(signal))
    noise_imag = np.random.normal(0, noise_std, len(signal))

    noise = noise_real + 1j * noise_imag

    return signal + noise