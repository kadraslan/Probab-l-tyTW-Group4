import numpy as np
from clt_slln_utils import slln_plot, clt_analysis

def generate(n):
    return (np.random.pareto(3, n) + 1)

if __name__ == "__main__":
    n = 10000
    samples = generate(n)

    mu = 3 / 2
    sigma = np.sqrt(3 / 4)

    slln_plot(
        samples,
        mu,
        "Pareto(α=3) - SLLN",
        "../results/pareto_3/slln.png"
    )

    clt_analysis(
        generate,
        mu,
        sigma,
        "Pareto(α=3)",
        "../results/pareto_3"
    )
