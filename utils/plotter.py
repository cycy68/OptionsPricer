import numpy as np
import plotly.graph_objects as go

def plot_payoff(S, K, option_type='call'):
    """
    Plots the payoff diagram at expiration for a call or put option.
    """
    S_range = np.linspace(0.5 * K, 1.5 * K, 100)

    if option_type == 'call':
        payoff = np.maximum(S_range - K, 0)
    else:
        payoff = np.maximum(K - S_range, 0)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=payoff, mode='lines', name=f'{option_type.capitalize()} Payoff'))
    fig.update_layout(title=f'{option_type.capitalize()} Option Payoff',
                      xaxis_title='Stock Price at Expiration',
                      yaxis_title='Payoff',
                      template='plotly_dark')
    fig.show()
