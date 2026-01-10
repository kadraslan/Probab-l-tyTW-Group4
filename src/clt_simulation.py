import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

def simulate_clt(n_values, m=1000):
    """
    Simulates the Central Limit Theorem (CLT) and visualizes the results.
    
    This function demonstrates how the standardized sum of i.i.d. random variables 
    from a Uniform(0,1) distribution converges to a Standard Normal Distribution 
    as the sample size n increases.

    Parameters:
    -----------
    n_values : list
        A list of integers representing the sample sizes to be simulated (e.g., [2, 5, 10, 30]).
    m : int, optional
        The number of replications (simulations) for each n value. Default is 1000.

    Returns:
    --------
    None
        Displays the plots and saves the figure to '../results/figures/clt_histograms.png'.
    """
    
    # Theoretical mean (mu) and standard deviation (sigma) for Uniform(0,1)
    mu, sigma = 0.5, np.sqrt(1/12)

    plt.figure(figsize=(15, 10))
    
    for i, n in enumerate(n_values):
        # Generate an (m x n) matrix of Uniform(0,1) random variables
        samples = np.random.uniform(0, 1, (m, n))
        
        # Calculate the standardized sums for each replication:
        # Z = (Sum(X) - n*mu) / (sigma * sqrt(n))
        # According to CLT, this should converge in distribution to N(0,1).
        standardized_sums = (np.sum(samples, axis=1) - n*mu) / (sigma * np.sqrt(n))
        
        # Create a subplot for each sample size n
        plt.subplot(2, 3, i+1)
        
        # Plot the histogram of the experimental standardized sums
        plt.hist(standardized_sums, bins=30, density=True, alpha=0.6, color='g', label='Simulation')
        
        # Overlay the theoretical Standard Normal Distribution (PDF) for comparison
        x = np.linspace(-4, 4, 100)
        plt.plot(x, stats.norm.pdf(x, 0, 1), 'r', lw=2, label='N(0,1)')
        
        plt.title(f'Sample Size n = {n}')
        plt.legend()

    plt.tight_layout()
    
    # Ensure the output directory exists and save the figure
    output_path = '../results/figures/clt_histograms.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()

# --- Execution Block ---
if __name__ == "__main__":
    # Define n values to observe the rate of convergence to normality [cite: 41]
    test_n_values = [2, 5, 10, 30, 50]
    simulate_clt(test_n_values)
