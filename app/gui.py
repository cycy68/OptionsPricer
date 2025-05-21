import streamlit as st
from pricer.black_scholes import black_scholes_price
from pricer.greeks import compute_greeks
from pricer.american_option import barone_adesi_whaley_approx
from utils.plotter import plot_payoff

def launch_gui():
    st.set_page_config(page_title="Option Pricer", layout="centered")
    st.title("Option Pricer - Black-Scholes & American")

    option_type = st.selectbox("Option Type", ["call", "put"])
    style = st.selectbox("Style", ["European", "American"])
    S = st.number_input("Stock Price (S)", min_value=0.0, value=100.0)
    K = st.number_input("Strike Price (K)", min_value=0.0, value=100.0)
    T = st.number_input("Time to Maturity (T in years)", min_value=0.01, value=1.0)
    r = st.number_input("Risk-Free Rate (r)", min_value=0.0, value=0.05)
    sigma = st.number_input("Volatility (σ)", min_value=0.01, value=0.2)

    if st.button("Calculate"):
        if style == "European":
            price = black_scholes_price(S, K, T, r, sigma, option_type)
        else:
            price = barone_adesi_whaley_approx(S, K, T, r, sigma, option_type)

        greeks = compute_greeks(S, K, T, r, sigma, option_type)

        st.markdown(f"**{style} {option_type.capitalize()} Price**: `{price:.2f}`")
        st.markdown("**Greeks**:")
        st.text(f"Delta: {greeks['delta']:.4f}")
        st.text(f"Gamma: {greeks['gamma']:.4f}")
        st.text(f"Vega:  {greeks['vega']:.4f}")

        st.plotly_chart(plot_payoff(S, K, option_type), use_container_width=True)
