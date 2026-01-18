import numpy as np
from clt_slln_utils import slln_plot, clt_analysis

def generate(n):
    return (np.random.pareto(1.5, n) + 1)

if __name__ == "__main__":
    n = 10000
    samples = generate(n)

    mu = 1.5 / 0.5   # Var ama varyans yok
    sigma = None

    slln_plot(
        samples,
        mu,
        "Pareto(α=1.5) - SLLN",
        "../results/pareto_1_5/slln.png"
    )

    clt_analysis(
        generate,
        mu,
        sigma,
        "Pareto(α=1.5)",
        "../results/pareto_1_5"
    )
