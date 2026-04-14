📡 Network Performance Simulation

 📌 Overview

This project models and analyzes network performance under different conditions using Python-based simulations. It explores how data packets behave in communication systems, focusing on congestion, delay, packet loss, and multi-node transmission.

The simulations progressively build from basic packet transmission to more advanced scenarios such as queueing systems and multi-node network behavior.

---

 🎯 Objectives

* Understand how network congestion occurs
* Analyze the impact of bandwidth limitations
* Model queueing behavior in communication systems
* Study packet delay and packet loss
* Simulate real-world multi-node network environments


 🚀 Features

 🔹 Basic Simulation

* Models packet transmission under simple conditions

 🔹 Packet Loss Analysis

* Compares different network conditions and loss behavior

 🔹 Bandwidth Limitation

* Simulates constrained network capacity
* Demonstrates how limited bandwidth affects performance

 🔹 Queueing System (Core Concept)

* Implements a finite buffer (queue)
* Models packet waiting time and congestion
* Simulates packet drops due to overflow

 🔹 Performance Visualization

* Graphs queue size, delay, and packet drops over time
* Enables analysis of network behavior

 🔹 Multi-Node Network (Advanced)

* Simulates packet flow across multiple routers
* Demonstrates bottlenecks and congestion propagation


 📊 Key Insights

* When traffic exceeds bandwidth → congestion occurs
* Queue buildup increases packet delay
* Limited buffer size leads to packet loss
* Bottlenecks in one node affect the entire network
* Multi-node systems introduce cumulative delays

 🛠 Technologies Used

* Python
* NumPy
* Matplotlib

 ⚡ Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

 ▶️ How to Run

Example:

```bash
python simulations/04_queue_simulation.py
```

You can run any simulation file depending on the level of complexity you want to explore.

 📈 Sample Outputs

The simulations generate graphs such as:

* Queue size over time
* Packet delay trends
* Packet drop rates

These are saved in the `results/` directory.

 🧠 Learning Outcomes

This project demonstrates:

* Network performance modeling
* Queueing theory fundamentals
* Congestion analysis
* System-level thinking in telecommunications


 🔮 Future Improvements

* Add real-time visualization dashboard
* Implement adaptive routing algorithms
* Extend to larger-scale network topologies
* Integrate machine learning for traffic prediction

 👤 Author

PETERSON KIBOI WAIRIMU

 📬 Contact

Feel free to connect or reach out for collaboration or discussion on network systems and telecommunications.

Email: petersonkiboi634@gmail.com
