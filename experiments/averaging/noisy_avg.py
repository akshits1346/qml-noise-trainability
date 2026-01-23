import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import csv
import numpy as np

from models.qnn import QuantumNeuralNetwork
from gradients.parameter_shift import parameter_shift_gradient
from gradients.statistics import gradient_statistics

DEPTHS = [1, 2, 3, 5, 8, 12]
N_QUBITS = 4
N_RUNS = 10
NOISE_STRENGTH = 0.05
OUTPUT_FILE = "results/gradient_variance_noisy_avg.csv"

def run():
    rows = []
    for depth in DEPTHS:
        variances = []
        for _ in range(N_RUNS):
            qnn = QuantumNeuralNetwork(
                n_qubits=N_QUBITS, depth=depth, noise_strength=NOISE_STRENGTH
            )
            grads = parameter_shift_gradient(qnn)
            stats = gradient_statistics(grads)
            variances.append(stats["variance"])

        rows.append({
            "depth": depth,
            "mean_variance": float(np.mean(variances)),
            "std_variance": float(np.std(variances)),
        })

        print(f"Noisy depth {depth}: mean={rows[-1]['mean_variance']:.3e}")

    with open(OUTPUT_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["depth", "mean_variance", "std_variance"])
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    run()

