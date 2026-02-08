import pandas as pd

def load_price_data(csv_path):
    """
    Load and preprocess Brent oil price data.
    """
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {csv_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading CSV: {e}")

    if 'Date' not in df.columns or 'Price' not in df.columns:
        raise ValueError("CSV must contain 'Date' and 'Price' columns.")

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date', 'Price'])
    df = df.sort_values('Date').set_index('Date')

    return df
