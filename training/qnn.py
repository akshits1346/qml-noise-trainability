import pennylane as qml
import numpy as np

from circuits.ansatz import build_ansatz
from noise.channels import depolarizing_noise


class QuantumNeuralNetwork:
    def __init__(self, n_qubits, depth, noise_strength=0.0, observable=None):
        self.n_qubits = n_qubits
        self.depth = depth
        self.noise_strength = noise_strength
        self.wires = list(range(n_qubits))

        self.dev = qml.device("default.mixed", wires=n_qubits)

        if observable is None:
            self.observable = qml.PauliZ(0)
        else:
            self.observable = observable

        self.params = np.random.uniform(
            low=0.0, high=2 * np.pi,
            size=(depth, n_qubits, 3)
        )

        self.qnode = qml.QNode(self._circuit, self.dev)

    def _circuit(self, params):
        for d in range(self.depth):
            build_ansatz(params[d:d+1], self.wires)

            if self.noise_strength > 0.0:
                depolarizing_noise(self.wires, self.noise_strength)

        return qml.expval(self.observable)

    def forward(self):
        return self.qnode(self.params)

