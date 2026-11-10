"""Reproduce annual-frequency FDI equity inflow pilot results.

IMPORTANT: This is an annual pilot, not the assigned quarterly experiment.
Run from the repository root:
    python src/run_analysis.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import (
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "fdi_annual_dataset.csv"
RESULTS = ROOT / "results"
FIGURES = ROOT / "report" / "figures"
RESULTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.read_csv(DATA)
    df["year_index"] = range(len(df))
    df["lag1"] = df["fdi_equity_inflow_usd_million"].shift(1)
    data = df.dropna().copy()

    features = ["lag1", "year_index"]
    train, test = data.iloc[:18], data.iloc[18:]
    y_true = test["fdi_equity_inflow_usd_million"].to_numpy()

    models = {
        "Linear regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LinearRegression()),
        ]),
        "Polynomial (degree 2)": Pipeline([
            ("poly", PolynomialFeatures(degree=2, include_bias=False)),
            ("scale", StandardScaler()),
            ("model", Ridge(alpha=1.0)),
        ]),
        "Ridge regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", Ridge(alpha=10.0)),
        ]),
        "Lasso regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", Lasso(alpha=0.05, max_iter=10000)),
        ]),
    }

    metric_rows = []
    predictions = {}
    for name, model in models.items():
        model.fit(train[features], train["fdi_equity_inflow_usd_million"])
        y_pred = model.predict(test[features])
        predictions[name] = y_pred
        metric_rows.append({
            "Model": name,
            "RMSE_USD_mn": mean_squared_error(y_true, y_pred) ** 0.5,
            "MAPE_percent": mean_absolute_percentage_error(y_true, y_pred) * 100,
            "R2": r2_score(y_true, y_pred),
        })

    # Naive persistence baseline: forecast each test year with the previous year.
    baseline = test["lag1"].to_numpy()
    metric_rows.append({
        "Model": "Persistence (last year)",
        "RMSE_USD_mn": mean_squared_error(y_true, baseline) ** 0.5,
        "MAPE_percent": mean_absolute_percentage_error(y_true, baseline) * 100,
        "R2": r2_score(y_true, baseline),
    })
    metrics = pd.DataFrame(metric_rows)
    metrics.to_csv(RESULTS / "annual_pilot_model_metrics.csv", index=False)

    plt.figure(figsize=(9, 4))
    plt.plot(df["financial_year"], df["fdi_equity_inflow_usd_million"], marker="o")
    plt.xticks(
        range(0, len(df), 2),
        df["financial_year"].iloc[::2],
        rotation=35,
        ha="right",
    )
    plt.ylabel("USD million")
    plt.xlabel("Financial year")
    plt.title("India: annual FDI equity inflows (DPIIT)")
    plt.tight_layout()
    plt.savefig(FIGURES / "fdi_annual_trend.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9, 4))
    plt.plot(test["financial_year"], y_true, marker="o", label="Observed")
    for name, values in predictions.items():
        plt.plot(test["financial_year"], values, marker="x", label=name)
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("USD million")
    plt.xlabel("Financial year")
    plt.title("Annual pilot: hold-out comparison")
    plt.legend(fontsize=7, ncol=2)
    plt.tight_layout()
    plt.savefig(FIGURES / "fdi_model_comparison.png", dpi=180)
    plt.close()

    print("Annual pilot complete. These are NOT quarterly forecasting results.")
    print(metrics.to_string(index=False))


if __name__ == "__main__":
    main()
