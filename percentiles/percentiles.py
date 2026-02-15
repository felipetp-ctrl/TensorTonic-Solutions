import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    pass
    
    percentile = np.array(np.percentile(x, q, method="linear"))
    return percentile