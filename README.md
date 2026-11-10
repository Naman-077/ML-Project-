# Forecasting FDI Equity Inflows into India using Machine Learning

**Project No.: 72 | Problem No.: 71**  
**Student:** Naman Bansal | **University Roll No.:** 24020570065  
**Domain:** Economy / Partnerships  
**SDG 17:** Partnerships for the Goals  
**Related SDG 8:** Decent Work and Economic Growth

> **Status: ANNUAL-FREQUENCY PILOT — NOT THE FINAL QUARTERLY EXPERIMENT.** The assigned problem requires quarterly FDI equity inflows and supporting predictors. This repository currently contains an annual-frequency pilot because quarterly observations and matching predictor series still need to be retrieved and validated. Do not describe these annual metrics as quarterly forecasting results.

## Research objectives
1. Describe the movement in India's FDI equity inflows.
2. Compare syllabus-level regression models using lagged inflows.
3. Evaluate predictions using RMSE, MAPE and R² with chronological train/test splitting.
4. Extend the study to quarterly frequency after obtaining official quarterly/monthly target observations and matching RBI predictors.

## Repository structure
```
ML-Project-/
├── data/
│   ├── fdi_annual_dataset.csv
│   └── user_supplied_sector_cumulative_fdi.xls  # upload this binary source workbook
├── docs/
│   └── DATA_SOURCES_AND_LIMITATIONS.md
├── notebooks/
│   └── 01_annual_pilot_overview.ipynb
├── report/
│   ├── FDI_Project_71_Journal_Format_DRAFT.pdf   # upload from ZIP
│   └── figures/
│       ├── fdi_annual_trend.png
│       └── fdi_model_comparison.png
├── results/
│   └── annual_pilot_model_metrics.csv
├── src/
│   └── run_analysis.py
├── .gitignore
├── PROBLEM.md
├── STATUS.md
├── requirements.txt
└── README.md
```

## Data
- `data/fdi_annual_dataset.csv`: DPIIT annual FDI equity inflow observations for FY 2000–01 to FY 2024–25, in USD million.
- `data/user_supplied_sector_cumulative_fdi.xls`: original supplied workbook of cumulative sector-wise FDI totals. This is supplementary context, not a quarterly time series.

Official source portals:
- DPIIT, Ministry of Commerce and Industry: https://www.dpiit.gov.in/
- Open Government Data FDI equity inflow catalogue: https://www.data.gov.in/catalog/foreign-direct-investment-fdi-equity-inflows
- RBI Database on Indian Economy: https://data.rbi.org.in/

See [data source and limitation notes](docs/DATA_SOURCES_AND_LIMITATIONS.md).

## Models
- Linear Regression
- Polynomial Regression (degree 2) with Ridge regularisation
- Ridge Regression
- Lasso Regression
- Persistence baseline (next annual value equals the previous year's value)

Metrics: RMSE (USD million), MAPE (%) and R². The annual series contains 25 full financial-year observations; after constructing a one-year lag, the first 18 usable observations form the training set and the final 6 form the hold-out test set.

## Current annual-pilot result
The checked-in metrics show the persistence baseline outperforms the four regression models in this small six-observation hold-out window. This is reported transparently. The test window is too small for strong claims about generalisation.

**These values are not quarterly forecast metrics.** No quarterly target, RBI exchange-rate predictor or policy-event feature has yet been incorporated.

## Reproduce the annual pilot
Python 3.10+ recommended.

### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python src/run_analysis.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_analysis.py
```

The script regenerates the model metrics and figures in `results/` and `report/figures/`.

## Remaining work for Problem 71
1. Retrieve official quarterly FDI equity observations, or monthly observations that can be consistently aggregated into quarters.
2. Retrieve matching RBI USD/INR exchange-rate observations.
3. Encode dated and sourced policy-event indicators.
4. Align all variables by quarter and build chronological train/validation/test splits.
5. Re-run the model comparison and replace the annual pilot PDF, graphs and metrics with genuine quarterly results.

No annual inflow total has been divided into artificial quarters. No exchange-rate or policy-event values have been fabricated.

## Academic integrity
The PDF in `report/` is an annual-pilot draft, not the final quarterly report. Verify all source figures and follow the course's AI-use disclosure policy before submission.

## Author
**Naman Bansal**  
B.Sc. (Hons.) Computer Science, University of Delhi
