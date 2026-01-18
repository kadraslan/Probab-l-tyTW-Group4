import numpy as np
from clt_slln_utils import slln_plot, clt_analysis

def generate(n):
    return np.random.uniform(0, 1, n)

if __name__ == "__main__":
    n = 10000
    samples = generate(n)

    mu = 0.5
    sigma = np.sqrt(1/12)

    slln_plot(
        samples,
        mu,
        "Uniform(0,1) - SLLN",
        "../results/uniform/slln.png"
    )

    clt_analysis(
        generate,
        mu,
        sigma,
        "Uniform(0,1)",
        "../results/uniform"
    )
