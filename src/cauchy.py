import numpy as np
from clt_slln_utils import slln_plot, clt_analysis

def generate(n):
    return np.random.standard_cauchy(n)

if __name__ == "__main__":
    n = 10000
    samples = generate(n)

    mu = None
    sigma = None

    slln_plot(
        samples,
        mu,
        "Cauchy(0,1) - SLLN",
        "../results/cauchy/slln.png"
    )

    clt_analysis(
        generate,
        mu,
        sigma,
        "Cauchy(0,1)",
        "../results/cauchy"
    )
