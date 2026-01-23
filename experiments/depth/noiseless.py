import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import csv
from models.qnn import QuantumNeuralNetwork
from gradients.parameter_shift import parameter_shift_gradient
from gradients.statistics import gradient_statistics

DEPTHS = [1, 2, 3, 5, 8, 12]
N_QUBITS = 4
OUTPUT_FILE = "results/gradient_variance_noiseless.csv"

def run_depth_sweep():
    results = []

    for depth in DEPTHS:
        qnn = QuantumNeuralNetwork(n_qubits=N_QUBITS, depth=depth)
        grads = parameter_shift_gradient(qnn)
        stats = gradient_statistics(grads)

        results.append({
            "depth": depth,
            "variance": stats["variance"],
            "l2_norm": stats["l2_norm"],
        })

        print(
            f"Depth {depth}: "
            f"variance={stats['variance']:.6e}, "
            f"l2_norm={stats['l2_norm']:.6e}"
        )

    return results

def save_results(results):
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["depth", "variance", "l2_norm"]
        )
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    results = run_depth_sweep()
    save_results(results)

