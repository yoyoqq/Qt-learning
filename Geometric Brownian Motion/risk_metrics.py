import numpy as np

def compute_var(returns, confidence=0.95):
    # 95% of time, losses are smaller than X 
    return np.percentile(returns, (1 - confidence) * 100)

def compute_cvar(returns, confidence=0.95):
    var = compute_var(returns, confidence)
    return returns[returns <= var].mean()
