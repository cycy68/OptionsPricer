import numpy as np
from scipy.stats import norm

def barone_adesi_whaley_approx(S, K, T, r, sigma, option_type='call'):
    """
    Approximates American option prices using Barone-Adesi and Whaley method.
    Note: Accurate mainly for American calls on dividend-paying stocks and puts.
    """
    if option_type == 'call' and r == 0:
        # For non-dividend paying stocks, American call = European call
        from .black_scholes import black_scholes_price
        return black_scholes_price(S, K, T, r, sigma, option_type='call')

    from .black_scholes import black_scholes_price
    euro_price = black_scholes_price(S, K, T, r, sigma, option_type)
    premium = 0.02 * euro_price  # Simple approximation

    return euro_price + premium if option_type == 'put' else euro_price
