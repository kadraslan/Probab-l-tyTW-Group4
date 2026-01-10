import numpy as np
import matplotlib.pyplot as plt
import os

def estimate_pi_monte_carlo(n=10000):
    """
    Estimates the value of pi using the Monte Carlo method.
    
    This function generates random points in a unit square [0,1]x[0,1] and 
    calculates the ratio of points falling inside the unit quarter-circle. 
    By SLLN, this ratio multiplied by 4 converges to pi as n increases.

    Parameters:
    -----------
    n : int, optional
        The total number of random points to generate. Default is 10000.

    Returns:
    --------
    None
        Displays a convergence plot and saves it to '../results/figures/pi_estimation.png'.
    """
    
    # Generate random x and y coordinates from a Uniform(0,1) distribution
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    # Check if points fall inside the quarter-circle (x^2 + y^2 <= 1)
    inside_circle = (x**2 + y**2) <= 1
    
    # Calculate the running estimate of pi: 
    # (Cumulative sum of points inside / Number of points processed) * 4
    pi_estimates = 4 * np.cumsum(inside_circle) / np.arange(1, n + 1)

    # Visualization of the estimation process
    plt.figure(figsize=(10, 6))
    plt.plot(pi_estimates, label='Monte Carlo Estimate')
    
    # Theoretical value of pi for comparison
    plt.axhline(y=np.pi, color='r', linestyle='--', label=f'True Pi ({np.pi:.5f})')
    
    plt.xlabel('Number of Points (n)')
    plt.ylabel('Estimated Value of Pi')
    plt.title('Monte Carlo Estimation of Pi Convergence')
    plt.legend()
    plt.grid(True)

    # Ensure the output directory exists and save the figure
    output_path = '../results/figures/pi_estimation.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path)
    plt.show()

# --- Execution Block ---
if __name__ == "__main__":
    # Perform the estimation with 10,000 points
    estimate_pi_monte_carlo(n=10000)
