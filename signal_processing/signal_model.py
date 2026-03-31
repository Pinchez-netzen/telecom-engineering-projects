import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, filtfilt

# -----------------------
# SETUP
# -----------------------

np.random.seed(42)  # Ensures consistent results every run
os.makedirs("results", exist_ok=True)

plt.style.use('seaborn-v0_8')  # Clean professional plots

# PARAMETERS
fs = 500
t = np.linspace(0, 1, fs)

# -----------------------
# SIGNAL GENERATION
# -----------------------

signal_main = np.sin(2 * np.pi * 5 * t)
signal_interference = 0.5 * np.sin(2 * np.pi * 20 * t)
signal = signal_main + signal_interference

# -----------------------
# NOISE MODEL (CONSISTENT)
# -----------------------

base_noise = np.random.normal(0, 1, signal.shape)

noise_std = 0.5
noisy_signal = signal + noise_std * base_noise

low_noise = signal + 0.2 * base_noise
high_noise = signal + 0.6 * base_noise

# -----------------------
# MOVING AVERAGE FILTER
# -----------------------

window_size = 10

filtered_signal = np.convolve(
    noisy_signal,
    np.ones(window_size) / window_size,
    mode='same'
)

# -----------------------
# BUTTERWORTH FILTER
# -----------------------

def butter_lowpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

cutoff = 10
butter_filtered = butter_lowpass_filter(noisy_signal, cutoff, fs)

# -----------------------
# METRICS
# -----------------------

def mse(original, processed):
    return np.mean((original - processed) ** 2)

def snr(original, noise):
    signal_power = np.mean(original ** 2)
    noise_power = np.mean(noise ** 2)
    return signal_power / noise_power

mse_noisy = mse(signal, noisy_signal)
mse_moving = mse(signal, filtered_signal)
mse_butter = mse(signal, butter_filtered)

snr_noisy = snr(signal, noisy_signal - signal)
snr_butter = snr(signal, butter_filtered - signal)

print("\n--- PERFORMANCE METRICS ---")
print("MSE Noisy:", mse_noisy)
print("MSE Moving Avg:", mse_moving)
print("MSE Butterworth:", mse_butter)

print("\nSNR Noisy:", snr_noisy)
print("SNR Butterworth:", snr_butter)

# -----------------------
# FFT FUNCTION
# -----------------------

def compute_fft(sig, fs):
    N = len(sig)
    fft_vals = np.fft.fft(sig)
    fft_vals = np.abs(fft_vals[:N // 2])

    freqs = np.fft.fftfreq(N, 1 / fs)
    freqs = freqs[:N // 2]

    return freqs, fft_vals

freqs, fft_clean = compute_fft(signal, fs)
_, fft_noisy = compute_fft(noisy_signal, fs)
_, fft_butter = compute_fft(butter_filtered, fs)

# -----------------------
# PLOTS
# -----------------------

# 1. Clean Signal
plt.figure()
plt.plot(t, signal, linewidth=2)
plt.title("Clean Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("results/clean_signal.png")
plt.close()

# 2. Noise Comparison
plt.figure()
plt.plot(t, signal, label="Clean", linewidth=2)
plt.plot(t, low_noise, label="Low Noise", alpha=0.7)
plt.plot(t, high_noise, label="High Noise", alpha=0.5)
plt.legend()
plt.title("Effect of Noise Levels")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("results/noise_comparison.png")
plt.close()

# 3. Filtering Result
plt.figure()
plt.plot(t, signal, label="Clean", linewidth=2)
plt.plot(t, noisy_signal, label="Noisy", alpha=0.5)
plt.plot(t, filtered_signal, label="Moving Avg", linewidth=1.5)
plt.legend()
plt.title("Filtering Result (Moving Average)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("results/filtering.png")
plt.close()

# 4. Filter Comparison
plt.figure()
plt.plot(t, signal, label="Clean", linewidth=2)
plt.plot(t, noisy_signal, label="Noisy", alpha=0.5)
plt.plot(t, filtered_signal, label="Moving Avg", alpha=0.7)
plt.plot(t, butter_filtered, label="Butterworth", linewidth=2)
plt.legend()
plt.title("Filter Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.savefig("results/filter_comparison.png")
plt.close()

# 5. FFT Analysis
plt.figure()
plt.plot(freqs, fft_clean, label="Clean", linewidth=2)
plt.plot(freqs, fft_noisy, label="Noisy", alpha=0.5)
plt.plot(freqs, fft_butter, label="Butterworth", linewidth=2)
plt.legend()
plt.title("Frequency Domain Analysis (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.savefig("results/fft_analysis.png")
plt.close()