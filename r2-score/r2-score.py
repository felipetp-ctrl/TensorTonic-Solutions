import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    pass

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    num = np.sum((y_true - y_pred) ** 2)
    denom = np.sum((y_true - np.mean(y_true)) ** 2)
    # Handle the constant-target edge case
    if denom == 0:
        return 1.0 if np.array_equal(y_true, y_pred) else 0.0
    result = 1 - (num / denom)
    return result