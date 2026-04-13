from encoder import text_to_binary
from decoder import binary_to_text
from modulation import bpsk_modulation, qpsk_modulation
from channel import add_awgn, add_awgn_complex
from demodulation import bpsk_demodulation, qpsk_demodulation
from error_correction import hamming_encode, hamming_decode
from metrics import calculate_ber

import matplotlib.pyplot as plt
import numpy as np
import os

# -----------------------
# SETUP
# -----------------------

np.random.seed(42)
os.makedirs("results", exist_ok=True)

# -----------------------
# INPUT MESSAGE
# -----------------------

message = "HELLO WORLD"

# -----------------------
# ENCODING
# -----------------------

binary = text_to_binary(message)
decoded_message = binary_to_text(binary)

# -----------------------
# MODULATION (BASE SIGNALS)
# -----------------------

mod_bpsk = bpsk_modulation(binary)

encoded_bits = hamming_encode(binary)
mod_hamming = bpsk_modulation(encoded_bits)

qpsk_signal = qpsk_modulation(binary)

# -----------------------
# CLEAR SIGNAL vs NOISE VISUALIZATION
# -----------------------

# Generate multiple noise levels from SAME base signal
noise_low = add_awgn(mod_bpsk, noise_std=0.2)
noise_medium = add_awgn(mod_bpsk, noise_std=0.5)
noise_high = add_awgn(mod_bpsk, noise_std=1.0)

plt.figure()

plt.plot(mod_bpsk[:100], label="Clean Signal", linewidth=2)
plt.plot(noise_low[:100], label="Low Noise", alpha=0.7)
plt.plot(noise_medium[:100], label="Medium Noise", alpha=0.6)
plt.plot(noise_high[:100], label="High Noise", alpha=0.5)

plt.axhline(0, linestyle='--', color='red', label="Decision Boundary")

plt.title("Signal Degradation Under Noise")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.legend()
plt.grid()

plt.savefig("results/signal_noise_effect.png")
plt.show()

# -----------------------
# SINGLE TEST (example noise)
# -----------------------

noise_std = 0.5

noisy_signal = add_awgn(mod_bpsk, noise_std=noise_std)
received_binary = bpsk_demodulation(noisy_signal)

received_message = binary_to_text(received_binary)

ber, errors = calculate_ber(binary, received_binary)

# QPSK test
noisy_qpsk = add_awgn_complex(qpsk_signal, noise_std=noise_std)
received_qpsk_binary = qpsk_demodulation(noisy_qpsk)
ber_qpsk, _ = calculate_ber(binary, received_qpsk_binary[:len(binary)])

# Hamming test
noisy_hamming = add_awgn(mod_hamming, noise_std=noise_std)
rec_hamming = bpsk_demodulation(noisy_hamming)
corrected_bits = hamming_decode(rec_hamming)
corrected_bits = corrected_bits[:len(binary)]

ber_hamming_test, _ = calculate_ber(binary, corrected_bits)

# -----------------------
# PRINT RESULTS
# -----------------------

print("\n--- BASIC SYSTEM ---")
print("Original Message:", message)
print("Decoded Message:", decoded_message)

print("\n--- BPSK ---")
print("BER:", ber)

print("\n--- QPSK ---")
print("BER:", ber_qpsk)

print("\n--- HAMMING (Error Correction) ---")
print("BER:", ber_hamming_test)

# -----------------------
# COMPARISON (BER vs NOISE)
# -----------------------

noise_levels = [0.1, 0.3, 0.5, 0.7, 1.0]

ber_bpsk = []
ber_hamming = []
ber_qpsk = []

for noise in noise_levels:

    # BPSK
    noisy_bpsk = add_awgn(mod_bpsk, noise_std=noise)
    rec_bpsk = bpsk_demodulation(noisy_bpsk)
    ber_val, _ = calculate_ber(binary, rec_bpsk[:len(binary)])
    ber_bpsk.append(ber_val)

    # BPSK + Hamming
    noisy_hamming = add_awgn(mod_hamming, noise_std=noise)
    rec_hamming = bpsk_demodulation(noisy_hamming)
    corrected = hamming_decode(rec_hamming)
    corrected = corrected[:len(binary)]

    ber_val, _ = calculate_ber(binary, corrected)
    ber_hamming.append(ber_val)

    # QPSK
    noisy_qpsk = add_awgn_complex(qpsk_signal, noise_std=noise)
    rec_qpsk = qpsk_demodulation(noisy_qpsk)
    rec_qpsk = rec_qpsk[:len(binary)]

    ber_val, _ = calculate_ber(binary, rec_qpsk)
    ber_qpsk.append(ber_val)

# -----------------------
# PLOTS
# -----------------------

# 1. Signal Visualization
plt.figure()
plt.plot(mod_bpsk[:100], label="Clean")
plt.plot(noisy_signal[:100], label="Noisy", alpha=0.7)
plt.axhline(0, linestyle='--', color='red', label="Decision Boundary")

plt.title("BPSK Signal with Noise")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.savefig("results/bpsk_signal.png")
plt.show()

# 2. QPSK Constellation
plt.figure()
plt.scatter(noisy_qpsk.real, noisy_qpsk.imag, alpha=0.5)

plt.title("QPSK Constellation (Noisy)")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.axhline(0)
plt.axvline(0)
plt.grid()

plt.savefig("results/qpsk_constellation.png")
plt.show()

# 3. BER vs Noise (Single System)
plt.figure()
plt.plot(noise_levels, ber_bpsk, marker='o')

plt.title("BER vs Noise (BPSK)")
plt.xlabel("Noise Standard Deviation")
plt.ylabel("BER")
plt.grid()

plt.savefig("results/ber_bpsk.png")
plt.show()

# 4. FINAL COMPARISON
plt.figure()

plt.plot(noise_levels, ber_bpsk, marker='o', label="BPSK")
plt.plot(noise_levels, ber_hamming, marker='s', label="BPSK + Hamming")
plt.plot(noise_levels, ber_qpsk, marker='^', label="QPSK")

plt.title("BER Comparison of Communication Systems")
plt.xlabel("Noise Standard Deviation")
plt.ylabel("Bit Error Rate (BER)")

plt.legend()
plt.grid()

plt.savefig("results/system_comparison.png")
plt.show()