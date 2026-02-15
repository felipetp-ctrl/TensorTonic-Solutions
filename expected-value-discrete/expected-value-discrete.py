import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    pass

    x = np.array(x)
    p = np.array(p)

    val_probas = np.allclose(1, sum(p))

    if val_probas == True:
        exp_value = np.sum(x * p)
    else:
        raise ValueError("The probabilities do not sum to 1.")    
    return exp_value
