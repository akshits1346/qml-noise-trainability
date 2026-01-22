import pennylane as qml
import numpy as np

def variational_layer(params, wires):
    """
    One layer of parameterized single-qubit rotations.
    """
    for i, wire in enumerate(wires):
        qml.RX(params[i, 0], wires=wire)
        qml.RY(params[i, 1], wires=wire)
        qml.RZ(params[i, 2], wires=wire)


def entangling_layer(wires):
    """
    Simple nearest-neighbor entanglement.
    """
    for i in range(len(wires) - 1):
        qml.CNOT(wires=[wires[i], wires[i + 1]])


def build_ansatz(params, wires):
    """
    Full variational circuit composed of alternating
    rotation and entangling layers.
    """
    depth = params.shape[0]

    for d in range(depth):
        variational_layer(params[d], wires)
        entangling_layer(wires)

