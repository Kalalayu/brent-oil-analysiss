import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def plot_price(df, save_path=None):
    if 'Price' not in df.columns:
        raise ValueError("DataFrame must contain 'Price' column.")

    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['Price'])
    plt.title("Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)

    plt.show()


def add_log_returns(df):
    if 'Price' not in df.columns:
        raise ValueError("Cannot compute log returns without 'Price' column.")

    df = df.copy()
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
    return df
