import numpy as np
import matplotlib.pyplot as plt

# GENERATE SYNTHETIC DATA 
def generate_linear_data(T=100, dt=1.0, q=0.1, r=1.0):
    """
    Constant velocity model
    """
    F = np.array([[1, dt],
                  [0, 1]])
    H = np.array([[1, 0]])

    Q = q * np.eye(2)
    R = np.array([[r]])

    x = np.zeros((T, 2))
    y = np.zeros(T)

    x[0] = np.array([0.0, 1.0])  # initial position, velocity

    for t in range(1, T):
        process_noise = np.random.multivariate_normal(mean=[0, 0], cov=Q)
        x[t] = F @ x[t-1] + process_noise

        obs_noise = np.random.normal(0, np.sqrt(r))
        y[t] = H @ x[t] + obs_noise

    return x, y, F, H, Q, R


# KF FROM SCRATCH 
class KalmanFilter:
    def __init__(self, F, H, Q, R, x0, P0):
        self.F = F
        self.H = H
        self.Q = Q
        self.R = R

        self.x = x0
        self.P = P0

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, y):
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        innovation = y - self.H @ self.x
        self.x = self.x + K.flatten() * innovation
        self.P = (np.eye(len(self.x)) - K @ self.H) @ self.P

    def step(self, y):
        self.predict()
        self.update(y)
        return self.x.copy()


# RUN THE FILTER
# Generate data
T = 100
x_true, y_obs, F, H, Q, R = generate_linear_data(T)

# Initialize filter
kf = KalmanFilter(
    F=F,
    H=H,
    Q=Q,
    R=R,
    x0=np.array([0.0, 0.0]),
    P0=np.eye(2)
)

# Run
estimates = np.zeros((T, 2))
for t in range(T):
    estimates[t] = kf.step(y_obs[t])


# VS DIAGONOSIS
plt.figure(figsize=(10,5))
plt.plot(x_true[:,0], label="True Position")
plt.plot(y_obs, '.', alpha=0.4, label="Observed")
plt.plot(estimates[:,0], label="KF Estimate")
plt.legend()
plt.title("Kalman Filter: Position Tracking")
plt.show()


# RMSE METRIC
rmse = np.sqrt(np.mean((estimates[:,0] - x_true[:,0])**2))
print("RMSE:", rmse)
