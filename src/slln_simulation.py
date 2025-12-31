IE221 – Probability and Statistics
Team Work 3

Strong Law of Large Numbers (SLLN) Simulation

This script experimentally verifies the Strong Law of Large Numbers.
Independent and identically distributed random variables are generated
from a Uniform(0,1) distribution. The cumulative sample mean is computed
and shown to converge almost surely to the expected value μ = 0.5.

import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.random.uniform(0, 1, n)
cumulative_mean = np.cumsum(x) / np.arange(1, n + 1)

# Grafik çizimi [cite: 55]
plt.figure(figsize=(10, 5))
plt.plot(cumulative_mean, label="Cumulative Mean")
plt.axhline(y=0.5, color='r', linestyle='--', label="Target Mean (0.5)")
plt.xlabel("Number of observations (n)")
plt.ylabel("Mean")
plt.title("SLLN Convergence")
plt.legend()
plt.grid()

plt.savefig('../results/figures/slln_convergence.png')
plt.show()
