from statsmodels.tsa.stattools import adfuller
import numpy as np

def adf_test(series):
   
    series = series.dropna()

    if len(series) < 20:
        raise ValueError("Time series too short for ADF test.")

    result = adfuller(series)
    return {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Is Stationary (5%)": result[1] < 0.05
    }
