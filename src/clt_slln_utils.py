import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def slln_plot(samples, true_mean, title, save_path):
    n = len(samples)
    cum_mean = np.cumsum(samples) / np.arange(1, n + 1)

    plt.figure()
    plt.plot(cum_mean, label="Cumulative Mean")
    if true_mean is not None:
        plt.axhline(true_mean, linestyle="--", label="True Mean")
    plt.xlabel("n")
    plt.ylabel("Cumulative Mean")
    plt.title(title)
    plt.legend()
    plt.savefig(save_path)
    plt.close()


def clt_analysis(generator, mu, sigma, dist_name, save_dir):
    n_values = [2, 5, 10, 30, 50, 100]
    m = 1000

    for n in n_values:
        sums = []

        for _ in range(m):
            X = generator(n)
            X_bar = np.mean(X)
            sums.append(X_bar)

        sums = np.array(sums)

        # Standartlaştırma (μ ve σ varsa)
        if mu is not None and sigma is not None:
            Z = (sums - mu) / (sigma / np.sqrt(n))
        else:
            Z = sums  # bilerek bozuk (raporda açıklanacak)

        # Histogram
        plt.figure()
        plt.hist(Z, bins=30, density=True)
        plt.title(f"{dist_name} - CLT Histogram (n={n})")
        plt.savefig(f"{save_dir}/hist_n{n}.png")
        plt.close()

        # Q-Q Plot
        plt.figure()
        stats.probplot(Z, dist="norm", plot=plt)
        plt.title(f"{dist_name} - Q-Q Plot (n={n})")
        plt.savefig(f"{save_dir}/qq_n{n}.png")
        plt.close()
