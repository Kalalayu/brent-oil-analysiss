import numpy as np
import pandas as pd
import pymc as pm
import arviz as az


def prepare_log_returns(df: pd.DataFrame, price_col: str = "Price") -> np.ndarray:
    """
    Compute log returns from a price series.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing price data
    price_col : str
        Column name for prices

    Returns
    -------
    np.ndarray
        Log return series
    """
    log_returns = np.log(df[price_col]).diff().dropna().values
    return log_returns


def fit_bayesian_change_point(
    returns: np.ndarray,
    draws: int = 2000,
    tune: int = 1000,
    target_accept: float = 0.9,
):
    """
    Fit a Bayesian single change point model to a time series.

    Parameters
    ----------
    returns : np.ndarray
        Stationary time series (e.g., log returns)
    draws : int
        Number of MCMC samples
    tune : int
        Number of tuning steps
    target_accept : float
        Target acceptance rate for NUTS

    Returns
    -------
    model : pm.Model
        PyMC model object
    trace : arviz.InferenceData
        Posterior samples
    """
    n = len(returns)
    time_idx = np.arange(n)

    with pm.Model() as model:

        # Change point prior
        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n - 1
        )

        # Mean before and after the change
        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        # Shared volatility
        sigma = pm.Exponential("sigma", 1)

        # Switch function
        mu = pm.math.switch(time_idx < tau, mu_1, mu_2)

        # Likelihood
        pm.Normal(
            "obs",
            mu=mu,
            sigma=sigma,
            observed=returns
        )

        # Sampling
        trace = pm.sample(
            draws=draws,
            tune=tune,
            target_accept=target_accept,
            return_inferencedata=True,
            progressbar=True
        )

    return model, trace


def summarize_change_point(trace: az.InferenceData) -> dict:
    """
    Extract key summary statistics from the posterior.

    Parameters
    ----------
    trace : arviz.InferenceData

    Returns
    -------
    dict
        Summary containing tau, mu_1, mu_2
    """
    summary = {
        "tau_mean": int(trace.posterior["tau"].mean().values),
        "mu_1_mean": trace.posterior["mu_1"].mean().item(),
        "mu_2_mean": trace.posterior["mu_2"].mean().item(),
        "sigma_mean": trace.posterior["sigma"].mean().item(),
    }
    return summary


def quantify_impact(mu_1: float, mu_2: float) -> float:
    """
    Compute percentage change between regimes.

    Parameters
    ----------
    mu_1 : float
        Mean before change
    mu_2 : float
        Mean after change

    Returns
    -------
    float
        Percentage change
    """
    if mu_1 == 0:
        return np.nan
    return (mu_2 - mu_1) / abs(mu_1) * 100
