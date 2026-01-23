import numpy as np

def gradient_statistics(grads):
    """
    Compute summary statistics of parameter gradients.

    Args:
        grads: numpy array of gradients

    Returns:
        dict containing mean, variance, and L2 norm
    """
    flat_grads = grads.flatten()

    stats = {
        "mean": np.mean(flat_grads),
        "variance": np.var(flat_grads),
        "l2_norm": np.linalg.norm(flat_grads),
    }

    return stats

