import csv
import matplotlib.pyplot as plt

def load(path):
    d, m, s = [], [], []
    with open(path) as f:
        r = csv.DictReader(f)
        for row in r:
            d.append(int(row["depth"]))
            m.append(float(row["mean_variance"]))
            s.append(float(row["std_variance"]))
    return d, m, s

d1, m1, s1 = load("results/gradient_variance_noiseless_avg.csv")
d2, m2, s2 = load("results/gradient_variance_noisy_avg.csv")

plt.figure(figsize=(6,4))
plt.errorbar(d1, m1, yerr=s1, marker="o", label="Noiseless")
plt.errorbar(d2, m2, yerr=s2, marker="o", label="Noisy (p=0.05)")
plt.yscale("log")
plt.xlabel("Circuit depth")
plt.ylabel("Gradient variance (log scale)")
plt.title("Noise accelerates gradient collapse")
plt.legend()
plt.tight_layout()
plt.savefig("results/gradient_variance_comparison.png", dpi=200)
plt.show()

