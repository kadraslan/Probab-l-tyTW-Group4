import numpy as np
from clt_slln_utils import slln_plot, clt_analysis

def generate(n):
    return np.random.exponential(1, n)

if __name__ == "__main__":
    n = 10000
    samples = generate(n)

    mu = 1
    sigma = 1

    slln_plot(
        samples,
        mu,
        "Exponential(1) - SLLN",
        "../results/exponential/slln.png"
    )

    clt_analysis(
        generate,
        mu,
        sigma,
        "Exponential(1)",
        "../results/exponential"
    )
