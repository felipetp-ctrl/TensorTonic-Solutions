import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pass

    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    sum = np.sum((y_pred - y_true) ** 2)
    division = sum / len(y_pred)
    return division
