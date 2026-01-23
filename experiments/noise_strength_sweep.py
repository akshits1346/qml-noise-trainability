import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import csv
import numpy as np

from training.qnn import QuantumNeuralNetwork
from gradients.parameter_shift import parameter_shift_gradient
from gradients.statistics import gradient_statistics

NOISE_LEVELS = [0.0, 0.01, 0.02, 0.05, 0.1]
DEPTH = 8
N_QUBITS = 4
N_RUNS = 10
OUTPUT_FILE = "results/gradient_variance_noise_sweep.csv"

def run():
    rows = []
    for p in NOISE_LEVELS:
        variances = []
        for _ in range(N_RUNS):
            qnn = QuantumNeuralNetwork(
                n_qubits=N_QUBITS,
                depth=DEPTH,
                noise_strength=p
            )
            grads = parameter_shift_gradient(qnn)
            stats = gradient_statistics(grads)
            variances.append(stats["variance"])

        rows.append({
            "noise_strength": p,
            "mean_variance": float(np.mean(variances)),
            "std_variance": float(np.std(variances)),
        })

        print(f"Noise {p}: mean={rows[-1]['mean_variance']:.3e}")

    with open(OUTPUT_FILE, "w", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=["noise_strength", "mean_variance", "std_variance"]
        )
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    run()


