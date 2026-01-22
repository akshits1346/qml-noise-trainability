import numpy as np

SHIFT = np.pi / 2

def parameter_shift_gradient(qnn):
    """
    Compute gradients of the QNN output with respect to all parameters
    using the parameter-shift rule.
    
    Returns:
        grads: numpy array with same shape as qnn.params
    """
    params = qnn.params
    grads = np.zeros_like(params)

    for d in range(params.shape[0]):
        for q in range(params.shape[1]):
            for r in range(params.shape[2]):
                original = params[d, q, r]

                # Forward shift
                params[d, q, r] = original + SHIFT
                forward = qnn.forward()

                # Backward shift
                params[d, q, r] = original - SHIFT
                backward = qnn.forward()

                # Parameter-shift gradient
                grads[d, q, r] = 0.5 * (forward - backward)

                # Restore original value
                params[d, q, r] = original

    return grads

