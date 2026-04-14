import random
import numpy as np
import matplotlib.pyplot as plt

NUM_PACKETS = 200
MAX_DELAY = 100

loss_rates = [0.0, 0.1, 0.2, 0.3]

avg_delays = []
packet_losses = []

for LOSS_PROBABILITY in loss_rates:
    delays = []
    lost_packets = 0

    for i in range(NUM_PACKETS):
        if random.random() < LOSS_PROBABILITY:
            lost_packets += 1
            continue
        
        delay = random.randint(1, MAX_DELAY)
        delays.append(delay)

    avg_delay = np.mean(delays) if delays else 0
    loss_percent = lost_packets / NUM_PACKETS

    avg_delays.append(avg_delay)
    packet_losses.append(loss_percent)
    
    
# Results
received_packets = len(delays)
avg_delay = np.mean(delays) if delays else 0

print(f"Total packets sent: {NUM_PACKETS}")
print(f"Packets received: {received_packets}")
print(f"Packets lost: {lost_packets}")
print(f"Average delay: {avg_delay:.2f} ms")


# Plot results
plt.plot(loss_rates, avg_delays, marker='o')
plt.title("Loss Rate vs Average Delay")
plt.xlabel("Loss Probability")
plt.ylabel("Average Delay (ms)")
plt.show()

plt.plot(loss_rates, packet_losses, marker='o')
plt.title("Loss Rate vs Packet Loss")
plt.xlabel("Loss Probability")
plt.ylabel("Loss Percentage")
plt.show()