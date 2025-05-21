import numpy as np
from scipy.stats import norm

def compute_greeks(S, K, T, r, sigma, option_type='call'):
    """
    Computes the main Greeks: Delta, Gamma, Vega.

    Returns:
        dict: { 'delta': ..., 'gamma': ..., 'vega': ... }
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    delta = norm.cdf(d1) if option_type == 'call' else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)

    return {
        'delta': delta,
        'gamma': gamma,
        'vega': vega
    }
