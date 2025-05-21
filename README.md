README.md

# Option Pricer - Black-Scholes, Greeks & American Approximation

This project allows you to price European and American-style options using the Black-Scholes formula (and approximations), with interactive visualization and a GUI.

## Features

- European Call/Put pricing (Black-Scholes formula)
- Approximate American option pricing (Barone-Adesi & Whaley style)
- Greeks calculation (Delta, Gamma, Vega)
- Interactive Streamlit interface
- Payoff diagram (Plotly)

---

## Project Structure

black_scholes_pricer/  
├── app/  
│   ├── __init__.py  
│   └── gui.py  
├── pricer/  
│   ├── __init__.py  
│   ├── black_scholes.py  
│   ├── greeks.py  
│   └── american_option.py  
├── utils/  
│   ├── __init__.py  
│   └── plotter.py  
├── main.py  
├── requirements.txt  
└── README.md  

---

## How It Works

- Uses the Black-Scholes-Merton model to price European call and put options.
- Calculates the key Greeks: Delta, Gamma, and Vega to measure sensitivities of the option price to underlying parameters.
- Supports approximate pricing of American options using a commonly used heuristic (e.g., Barone-Adesi and Whaley approximation).
- Provides an interactive payoff chart at expiration, rendered with Plotly and embedded in a Streamlit web interface for easy user interaction.
- Allows users to input parameters such as underlying price, strike price, volatility, risk-free rate, time to maturity, and option type through a simple GUI.

---

## Installation and use

### 1. Clone the repo

```bash
git clone https://github.com/cycy68/OptionsPricer.git
cd OptionsPricer
```

### 2. Install the dependencies

pip install -r requirements.txt

### 3. Run the App

```bash
streamlit run main.py
```
---

## Author

@cycy68