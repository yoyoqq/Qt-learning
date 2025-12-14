import matplotlib.pyplot as plt

def plot_price_paths(prices, n_paths=10):
    for i in range(n_paths):
        plt.plot(prices[i])
    plt.title("Monte Carlo Stock Price Paths")
    plt.xlabel("Time Steps")
    plt.ylabel("Price")
    plt.show()

def plot_distribution(final_prices):
    plt.hist(final_prices, bins=50)
    plt.title("Distribution of Final Stock Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()
