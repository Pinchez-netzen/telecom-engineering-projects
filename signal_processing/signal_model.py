import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS

fs = 500  # sampling frequency (samples per second)
t = np.linspace(0, 1, fs)


# SIGNAL COMPONENTS

# Main signal (low frequency)
signal_main = np.sin(2 * np.pi * 5 * t)

# Interference signal (higher frequency)
signal_interference = 0.5 * np.sin(2 * np.pi * 20 * t)

# Combined signal
signal = signal_main + signal_interference

# -----------------------
# PLOT SIGNAL
# -----------------------

plt.figure()
plt.plot(t, signal_main, label="Main Signal (5 Hz)")
plt.plot(t, signal_interference, label="Interference (20 Hz)")
plt.plot(t, signal, label="Combined Signal", linestyle='--')

plt.title("Signal Model (Clean)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.savefig("signal_processing/results/signal_clean.png")
plt.show()