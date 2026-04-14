import random
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
NUM_PACKETS = 100
LOSS_PROBABILITY = 0.1   # 10% packet loss
MAX_DELAY = 100          # max delay in ms

delays = []
lost_packets = 0

for i in range(NUM_PACKETS):
    # Check if packet is lost
    if random.random() < LOSS_PROBABILITY:
        lost_packets += 1
        continue
    
    # Simulate delay
    delay = random.randint(1, MAX_DELAY)
    delays.append(delay)

# Results
received_packets = len(delays)
avg_delay = np.mean(delays) if delays else 0

print(f"Total packets sent: {NUM_PACKETS}")
print(f"Packets received: {received_packets}")
print(f"Packets lost: {lost_packets}")
print(f"Average delay: {avg_delay:.2f} ms")

# Plot delay distribution
plt.hist(delays, bins=10)
plt.title("Packet Delay Distribution")
plt.xlabel("Delay (ms)")
plt.ylabel("Frequency")
plt.show()