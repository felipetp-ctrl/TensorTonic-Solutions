import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    pass

    mean_x = np.mean(x)

    num = np.sum(((x - mean_x) ** 2))
    denom = (len(x) - 1)
    var = (num / denom)
    std = np.sqrt(var)
    return var, std