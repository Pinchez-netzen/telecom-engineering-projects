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
drops_over_time = []
delay_over_time = []

dropped_packets = 0
processed_packets = 0

for t in range(TIME_STEPS):
    
    dropped_this_step = 0
    delays_this_step = []
    
    # Packet arrivals
    for i in range(PACKET_ARRIVAL_RATE):
        if len(queue) < MAX_QUEUE_SIZE:
            queue.append(t)
        else:
            dropped_packets += 1
            dropped_this_step += 1
    
    # Process packets
    packets_to_process = min(len(queue), BANDWIDTH)
    
    for i in range(packets_to_process):
        arrival_time = queue.pop(0)
        waiting_time = t - arrival_time
        transmission_delay = random.randint(1, MAX_DELAY)
        
        total_delay = waiting_time + transmission_delay
        delays.append(total_delay)
        delays_this_step.append(total_delay)
        processed_packets += 1
    
    # Track metrics
    queue_sizes.append(len(queue))
    drops_over_time.append(dropped_this_step)
    
    avg_step_delay = np.mean(delays_this_step) if delays_this_step else 0
    delay_over_time.append(avg_step_delay)

# Final stats
avg_delay = np.mean(delays) if delays else 0
drop_rate = dropped_packets / (TIME_STEPS * PACKET_ARRIVAL_RATE)

print(f"Average delay: {avg_delay:.2f} ms")
print(f"Drop rate: {drop_rate:.2f}")

# --------- PLOTS ---------

# 1. Queue size
plt.figure()
plt.plot(queue_sizes)
plt.title("Queue Size Over Time")
plt.xlabel("Time Step")
plt.ylabel("Queue Size")
plt.show()

# 2. Delay over time
plt.figure()
plt.plot(delay_over_time)
plt.title("Average Delay Per Time Step")
plt.xlabel("Time Step")
plt.ylabel("Delay (ms)")
plt.show()

# 3. Packet drops over time
plt.figure()
plt.plot(drops_over_time)
plt.title("Packet Drops Per Time Step")
plt.xlabel("Time Step")
plt.ylabel("Dropped Packets")
plt.show()