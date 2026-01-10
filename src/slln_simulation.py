import numpy as np
import matplotlib.pyplot as plt
import os

def simulate_slln(n=10000):
    """
    Simulates the Strong Law of Large Numbers (SLLN).
    
    This function generates i.i.d. Uniform(0,1) random variables and computes 
    the cumulative sample mean. It demonstrates that the sample mean converges 
    almost surely to the theoretical mean (mu = 0.5) as n increases.

    Parameters:
    -----------
    n : int, optional
        The total number of observations in a single sample path. Default is 10000.

    Returns:
    --------
    None
        Displays the convergence plot and saves it to '../results/figures/slln_convergence.png'.
    """
    
    # Generate n independent and identically distributed (i.i.d.) variables from Uniform(0,1)
    # The theoretical mean (mu) for this distribution is 0.5.
    x = np.random.uniform(0, 1, n)
    
    # Compute the cumulative sample mean: (X1 + X2 + ... + Xn) / n
    # np.cumsum provides the prefix sums, and we divide by the index [1, 2, ..., n]
    cumulative_mean = np.cumsum(x) / np.arange(1, n + 1)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(cumulative_mean, label="Cumulative Sample Mean")
    
    # Add a horizontal dashed line at the theoretical mean mu = 0.5
    plt.axhline(y=0.5, color='r', linestyle='--', label="Theoretical Mean (μ = 0.5)")
    
    plt.xlabel("Number of observations (n)")
    plt.ylabel("Sample Mean")
    plt.title("Strong Law of Large Numbers (SLLN) Convergence")
    plt.legend()
    plt.grid(True)

    # Ensure the output directory exists and save the figure
    output_path = '../results/figures/slln_convergence.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path)
    plt.show()

# --- Execution Block ---
if __name__ == "__main__":
    # Execute the simulation with 10,000 observations
    simulate_slln(n=10000)
