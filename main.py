from pricer.black_scholes import black_scholes_price
from pricer.greeks import compute_greeks
from utils.plotter import plot_payoff

def main():
    # Option parameters
    S = 100      # current stock price
    K = 100      # strike price
    T = 1        # time to maturity (in years)
    r = 0.05     # risk-free rate
    sigma = 0.2  # volatility
    option_type = 'call'  # or 'put'

    # Compute price and greeks
    price = black_scholes_price(S, K, T, r, sigma, option_type)
    greeks = compute_greeks(S, K, T, r, sigma, option_type)

    # Print results
    print(f"{option_type.capitalize()} Option Price: {price:.2f}")
    print("Greeks:")
    for name, value in greeks.items():
        print(f"{name.capitalize()}: {value:.4f}")

    # Show interactive payoff
    plot_payoff(S, K, option_type)

if __name__ == "__main__":
    main()
