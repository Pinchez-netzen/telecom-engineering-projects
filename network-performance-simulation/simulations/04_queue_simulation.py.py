import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
TIME_STEPS = 50
PACKET_ARRIVAL_RATE = 6
BANDWIDTH = 3
MAX_QUEUE_SIZE = 20
MAX_DELAY = 50

queue = []
delays = []
queue_sizes = []
dropped_packets = 0
processed_packets = 0

for t in range(TIME_STEPS):
    
    # Step 1: Packet arrivals
    for i in range(PACKET_ARRIVAL_RATE):
        if len(queue) < MAX_QUEUE_SIZE:
            queue.append(t)  # store arrival time
        else:
            dropped_packets += 1
    
    # Step 2: Process packets
    packets_to_process = min(len(queue), BANDWIDTH)
    
    for i in range(packets_to_process):
        arrival_time = queue.pop(0)
        waiting_time = t - arrival_time
        transmission_delay = random.randint(1, MAX_DELAY)
        
        total_delay = waiting_time + transmission_delay
        delays.append(total_delay)
        processed_packets += 1
    
    # Track queue size
    queue_sizes.append(len(queue))

# Results
avg_delay = np.mean(delays) if delays else 0
drop_rate = dropped_packets / (TIME_STEPS * PACKET_ARRIVAL_RATE)

print(f"Processed packets: {processed_packets}")
print(f"Dropped packets: {dropped_packets}")
print(f"Drop rate: {drop_rate:.2f}")
print(f"Average delay: {avg_delay:.2f} ms")

# Plot queue size
plt.plot(queue_sizes)
plt.title("Queue Size Over Time")
plt.xlabel("Time Step")
plt.ylabel("Queue Size")
plt.show()