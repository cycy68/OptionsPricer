import numpy as np
import plotly.graph_objects as go

def plot_payoff(S, K, option_type):
    x = list(range(0, int(2 * K) + 1))
    if option_type.lower() == 'call':
        y = [max(spot - K, 0) for spot in x]
    elif option_type.lower() == 'put':
        y = [max(K - spot, 0) for spot in x]
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Payoff'))
    fig.update_layout(title="Option Payoff", xaxis_title="Stock Price", yaxis_title="Payoff")
    return fig