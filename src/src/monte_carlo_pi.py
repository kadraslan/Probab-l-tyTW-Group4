IE221 – Probability and Statistics
Team Work 3

Monte Carlo Estimation of Pi

This script estimates the value of π using the Monte Carlo method.
Random points are generated inside the unit square [0,1]×[0,1].
The proportion of points falling inside the unit quarter-circle
converges to π/4 by the Strong Law of Large Numbers.
  
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Pi Tahmini [cite: 73, 80]
n = 10000
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

inside_circle = (x**2 + y**2) <= 1
pi_estimates = 4 * np.cumsum(inside_circle) / np.arange(1, n + 1)

plt.figure(figsize=(10, 6))
plt.plot(pi_estimates, label='Estimated Pi')
plt.axhline(y=np.pi, color='r', linestyle='--', label='True Pi (3.14159)')
plt.xlabel('Number of Points (n)')
plt.ylabel('Pi Value')
plt.legend()
plt.grid(True)
plt.savefig('../results/figures/pi_estimation.png') # [cite: 35, 91]
plt.show()
