import pennylane as qml
import numpy as np

from circuits.ansatz import build_ansatz

class QuantumNeuralNetwork:
    def __init__(self, n_qubits, depth, observable=None):
        self.n_qubits = n_qubits
        self.depth = depth
        self.wires = list(range(n_qubits))

        self.dev = qml.device("default.qubit", wires=n_qubits)

        if observable is None:
            self.observable = qml.PauliZ(0)
        else:
            self.observable = observable

        # Parameter tensor: (depth, n_qubits, 3)
        self.params = np.random.uniform(
            low=0.0, high=2 * np.pi,
            size=(depth, n_qubits, 3)
        )

        self.qnode = qml.QNode(self._circuit, self.dev)

    def _circuit(self, params):
        build_ansatz(params, self.wires)
        return qml.expval(self.observable)

    def forward(self):
        return self.qnode(self.params)

