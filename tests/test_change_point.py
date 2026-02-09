import numpy as np
import pandas as pd
import pytest

from src.change_point import (
    prepare_log_returns,
    fit_bayesian_change_point,
    summarize_change_point,
    quantify_impact
)


def test_prepare_log_returns():
    """Log returns should be computed correctly and be shorter by 1."""
    df = pd.DataFrame({
        "Price": [100, 105, 110, 120]
    })

    returns = prepare_log_returns(df)

    assert isinstance(returns, np.ndarray)
    assert len(returns) == len(df) - 1
    assert not np.isnan(returns).any()


def test_quantify_impact():
    """Impact should be correctly computed."""
    mu_1 = 0.01
    mu_2 = 0.02

    impact = quantify_impact(mu_1, mu_2)

    assert isinstance(impact, float)
    assert impact > 0


def test_summarize_change_point_structure():
    """Summary output should contain required keys."""
    # Fake minimal trace-like object using ArviZ structure
    import arviz as az
    import xarray as xr

    fake_trace = az.from_dict(
        posterior={
            "tau": xr.DataArray([5]),
            "mu_1": xr.DataArray([0.01]),
            "mu_2": xr.DataArray([0.02]),
            "sigma": xr.DataArray([0.1]),
        }
    )

    summary = summarize_change_point(fake_trace)

    assert isinstance(summary, dict)
    assert "tau_mean" in summary
    assert "mu_1_mean" in summary
    assert "mu_2_mean" in summary
    assert "sigma_mean" in summary


@pytest.mark.slow
def test_fit_bayesian_change_point_runs():
    """
    Ensure the Bayesian model runs with a very small dataset.
    This test checks execution, not statistical quality.
    """
    np.random.seed(0)
    returns = np.random.normal(0, 0.01, 30)

    model, trace = fit_bayesian_change_point(
        returns,
        draws=200,
        tune=100
    )

    assert model is not None
    assert trace is not None
    assert "tau" in trace.posterior
