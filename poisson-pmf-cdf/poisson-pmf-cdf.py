import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pass

    pmf_num = (lam ** k) * (np.e ** -lam)
    pmf_denom = math.factorial(k)
    pmf = pmf_num / pmf_denom

    cdf = []

    for x in range(k + 1):
        cdf_num = (np.e ** -lam) * (lam ** x)
        cdf_denom = math.factorial(x)
        cdf.append(np.sum(cdf_num / cdf_denom))
    
    return pmf, np.sum(cdf)