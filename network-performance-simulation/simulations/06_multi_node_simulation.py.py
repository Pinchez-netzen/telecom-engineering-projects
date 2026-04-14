import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
TIME_STEPS = 50
ARRIVAL_RATE = 5

BANDWIDTH_A = 3
BANDWIDTH_B = 2

MAX_QUEUE = 20
MAX_DELAY = 20

# Queues for nodes
queue_A = []
queue_B = []

delays = []
drops = 0

queue_A_sizes = []
queue_B_sizes = []

for t in range(TIME_STEPS):
    
    # Step 1: Packets arrive at Node A
    for i in range(ARRIVAL_RATE):
        if len(queue_A) < MAX_QUEUE:
            queue_A.append(t)
        else:
            drops += 1

    # Step 2: Process Node A → send to Node B
    processed_A = min(len(queue_A), BANDWIDTH_A)
    
    for i in range(processed_A):
        arrival_time = queue_A.pop(0)
        
        # Try to move to Node B
        if len(queue_B) < MAX_QUEUE:
            queue_B.append(arrival_time)
        else:
            drops += 1

    # Step 3: Process Node B → destination
    processed_B = min(len(queue_B), BANDWIDTH_B)
    
    for i in range(processed_B):
        arrival_time = queue_B.pop(0)
        
        total_delay = (t - arrival_time) + random.randint(1, MAX_DELAY)
        delays.append(total_delay)

    # Track queue sizes
    queue_A_sizes.append(len(queue_A))
    queue_B_sizes.append(len(queue_B))

# Results
avg_delay = np.mean(delays) if delays else 0

print(f"Average delay: {avg_delay:.2f}")
print(f"Total drops: {drops}")

# Plot queues
plt.figure()
plt.plot(queue_A_sizes, label="Queue A")
plt.plot(queue_B_sizes, label="Queue B")
plt.title("Queue Sizes Across Nodes")
plt.xlabel("Time Step")
plt.ylabel("Queue Size")
plt.legend()
plt.show()