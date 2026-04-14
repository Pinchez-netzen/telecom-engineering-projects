import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
TIME_STEPS = 50
PACKET_ARRIVAL_RATE = 3   # packets arriving per time step
BANDWIDTH = 5             # packets processed per time step
MAX_DELAY = 100

queue = []
delays = []
queue_sizes = []

time = 0

for t in range(TIME_STEPS):
    
    # Step 1: New packets arrive
    for i in range(PACKET_ARRIVAL_RATE):
        queue.append(t)  # store arrival time
    
    # Step 2: Process packets (limited by bandwidth)
    packets_to_process = min(len(queue), BANDWIDTH)
    
    for i in range(packets_to_process):
        arrival_time = queue.pop(0)
        delay = t - arrival_time + random.randint(1, MAX_DELAY)
        delays.append(delay)
    
    # Track queue size
    queue_sizes.append(len(queue))

# Results
avg_delay = np.mean(delays)

print(f"Average delay: {avg_delay:.2f} ms")
print(f"Final queue size: {len(queue)}")

# Plot queue growth
plt.plot(queue_sizes)
plt.title("Queue Size Over Time (Bandwidth Limited)")
plt.xlabel("Time Step")
plt.ylabel("Queue Size")
plt.show()