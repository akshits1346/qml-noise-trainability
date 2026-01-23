import pennylane as qml

def depolarizing_noise(wires, p):
    """
    Apply depolarizing noise to each wire.
    """
    for wire in wires:
        qml.DepolarizingChannel(p, wires=wire)


def amplitude_damping_noise(wires, gamma):
    """
    Apply amplitude damping noise to each wire.
    """
    for wire in wires:
        qml.AmplitudeDamping(gamma, wires=wire)


def phase_damping_noise(wires, gamma):
    """
    Apply phase damping noise to each wire.
    """
    for wire in wires:
        qml.PhaseDamping(gamma, wires=wire)

