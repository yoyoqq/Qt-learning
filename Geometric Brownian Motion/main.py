"""

Create a stochastic process using MC 

From a random sampling, get different outcomes 


"""

import numpy as np
from simulator import simulate_gbm
from risk_metrics import compute_var, compute_cvar
from plots import plot_price_paths, plot_distribution

# Parameters
S0 = 100        # price start at 
mu = 0.08       # expected annual return (drift)
sigma = 0.2     # volatity 
T = 1           # total time years 
steps = 252     # time discretization (days)
n_simulations = 10000   

prices = simulate_gbm(S0, mu, sigma, T, steps, n_simulations)

final_prices = prices[:, -1]        # take all rows, take last col
returns = (final_prices - S0) / S0  # get the return of each simulation 

var_95 = compute_var(returns, 0.95)     # loss threshold given a confidence level, losses are smaller than X, does not capture how bad it goes  
cvar_95 = compute_cvar(returns, 0.95)   # if go bad, avg loss is X. does not capture tail risk 

print(f"VaR (95%): {var_95:.2%}")
print(f"CVaR (95%): {cvar_95:.2%}")

plot_price_paths(prices)
plot_distribution(final_prices)
