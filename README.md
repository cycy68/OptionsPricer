README.md

# Black-Scholes Option Pricer (with Greeks & Interactive Payoff)

This Python project allows you to:

- Calculate the price of European call or put options using the Black-Scholes formula
- Display Greeks: Delta, Gamma, Vega  
-  Show an interactive payoff diagram using Plotly

---

## Project Structure

black_scholes_pricer/
├── main.py # Main script
├── pricer/
│ ├── black_scholes.py # Black-Scholes pricing
│ ├── greeks.py # Greek calculations
│ └── init.py
├── utils/
│ ├── plotter.py # Interactive payoff chart
│ └── init.py
├── requirements.txt # Project dependencies
└── README.md # Documentation


---

## How It Works

- Uses the Black-Scholes-Merton model to price European options.
- Computes Delta, Gamma, Vega (first and second-order sensitivities).
- Plots the payoff at expiration using an interactive chart.

---

## Installation and use

### 1. Clone the repo

```bash
git clone https://github.com/cycy68/black_scholes_pricer.git
cd black_scholes_pricer
```

### 2. Install the dependencies

pip install -r requirements.txt

### 3. Run the App

```bash
python main.py
```

This will display the option price and Greeks in the console and open an interactive Plotly graph showing the option’s payoff

Example Output:

Call Option Price: 10.45
Greeks:
Delta: 0.6368
Gamma: 0.0188
Vega: 37.5240

### 4. Change Option Parameters

Edit the main.py file to change:

S = 100         # Spot price
K = 100         # Strike price
T = 1           # Time to maturity (years)
r = 0.05        # Risk-free rate
sigma = 0.2     # Volatility
option_type = 'call'  # or 'put'

---

## Author

@cycy68