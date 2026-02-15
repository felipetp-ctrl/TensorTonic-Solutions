import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    pass
    x = np.array(x)
    mean = float(np.mean(x))
    median = float(np.median(x))

    x_count = Counter(x)
    max_freq = max(x_count.values())
    mode = float(min(k for k,v in x_count.items() if v == max_freq))
    return print('mean=',mean,', median=', median,', mode=', mode)
    