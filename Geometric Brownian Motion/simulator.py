import numpy as np

def simulate_gbm(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    steps: int,
    n_simulations: int
):
    # how many steps (time step size)
    dt = T / steps
    
    # Random normal numbers, represent random market shock 
    Z = np.random.standard_normal((n_simulations, steps))
    
    # Price paths matrix
    prices = np.zeros((n_simulations, steps + 1))
    prices[:, 0] = S0   # start all with S0
    
    for t in range(1, steps + 1):
        # all at time t, GBM
        prices[:, t] = prices[:, t - 1] * np.exp(
            (mu - 0.5 * sigma**2) * dt              # deterministic part
            + sigma * np.sqrt(dt) * Z[:, t - 1]     # trend + shock 
        )
    
    return prices
