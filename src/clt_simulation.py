IE221 – Probability and Statistics
Team Work 3

Central Limit Theorem (CLT) Simulation

This script illustrates the Central Limit Theorem using sums of i.i.d.
Uniform(0,1) random variables. For increasing sample sizes, the
standardized sums are shown to converge in distribution to N(0,1)
using histograms and Normal Q-Q plots.
    
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# CLT Simülasyonu: n arttıkça toplamların dağılımı normale yaklaşır
n_values = [2, 5, 10, 30, 50]
m = 1000
mu, sigma = 0.5, np.sqrt(1/12)

plt.figure(figsize=(15, 10))
for i, n in enumerate(n_values):
    samples = np.random.uniform(0, 1, (m, n))
    standardized_sums = (np.sum(samples, axis=1) - n*mu) / (sigma*np.sqrt(n))
    
    plt.subplot(2, 3, i+1)
    plt.hist(standardized_sums, bins=30, density=True, alpha=0.6, color='g')
    x = np.linspace(-4, 4, 100)
    plt.plot(x, stats.norm.pdf(x, 0, 1), 'r', lw=2)
    plt.title(f'n = {n}')

plt.tight_layout()
plt.savefig('../results/figures/clt_histograms.png') # Grafiği figures klasörüne kaydeder
plt.show()
