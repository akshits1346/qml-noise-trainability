import csv
import matplotlib.pyplot as plt

noise, mean, std = [], [], []

with open("results/gradient_variance_noise_sweep.csv") as f:
    r = csv.DictReader(f)
    for row in r:
        noise.append(float(row["noise_strength"]))
        mean.append(float(row["mean_variance"]))
        std.append(float(row["std_variance"]))

plt.figure(figsize=(6,4))
plt.errorbar(noise, mean, yerr=std, marker="o")
plt.yscale("log")
plt.xlabel("Depolarizing noise strength (p)")
plt.ylabel("Gradient variance (log scale)")
plt.title("Gradient collapse increases with noise strength")
plt.tight_layout()
plt.savefig("results/gradient_variance_noise_sweep.png", dpi=200)
plt.show()

