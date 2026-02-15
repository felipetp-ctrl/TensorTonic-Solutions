import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    pass

    x = np.array(x)
    y = np.array(y)

    sum = np.sum(((x - y) ** 2))
    sqrt = np.sqrt(sum)
    return sqrt