# Forecasting FDI Equity Inflows into India using Machine Learning

**Machine Learning Application Project | Project No. 72 | Problem No. 71**  
**Student:** Naman Bansal | **University Roll No.:** 24020570065  
**Domain:** Economy / Partnerships | **SDG 17: Partnerships for the Goals**  
**Related SDG:** SDG 8 – Decent Work and Economic Growth

> **Status: ANNUAL-FREQUENCY PILOT — NOT THE FINAL QUARTERLY EXPERIMENT.**  
> The assigned task requires quarterly FDI equity inflows and additional predictors such as exchange rates and policy indicators. The currently available data extract contains annual DPIIT equity-inflow observations. The supplied spreadsheet contains cumulative sector-wise totals, not quarterly observations. This repository labels the work accurately and does not manufacture quarterly values.

## 1. Project overview

This project studies whether classical regression models can forecast India's FDI equity inflows. The pilot compares Linear Regression, Polynomial Regression (degree 2 with Ridge regularisation), Ridge Regression and Lasso Regression against a persistence baseline.

The target is **FDI equity inflow in USD million**. The pilot uses the previous financial year's inflow (`lag1`) and a time index as predictors. A chronological split is used to avoid training on future observations.

## 2. Repository structure

```text
FDI_Equity_Inflows_India_ML_Project/
├── data/
│   ├── raw/
│   │   └── user_supplied_sector_cumulative_fdi.xls
│   └── processed/
│       └── fdi_annual_dataset.csv
├── docs/
│   └── DATA_SOURCES_AND_LIMITATIONS.md
├── notebooks/
│   └── 01_annual_pilot_overview.ipynb
├── reports/
│   ├── FDI_Project_71_Journal_Format_DRAFT.pdf
│   └── figures/
│       ├── fdi_annual_trend.png
│       └── fdi_model_comparison.png
├── results/
│   └── annual_pilot_model_metrics.csv
├── scripts/
│   └── reproduce_analysis.py
├── src/
│   └── __init__.py
├── .gitignore
├── PROBLEM.md
├── requirements.txt
└── README.md
```

## 3. Data sources

1. **DPIIT, Ministry of Commerce and Industry, Government of India** – Quarterly Fact Sheet on FDI Inflow, including financial-year-wise FDI equity inflow. The annual pilot series is transcribed from the fact sheet.
2. **Open Government Data Platform India** – FDI Equity Inflows catalogue: https://www.data.gov.in/catalog/foreign-direct-investment-fdi-equity-inflows
3. **RBI Database on Indian Economy** – source portal for exchange-rate and external-sector series: https://data.rbi.org.in/
4. **User-supplied sector spreadsheet** – cumulative sector-wise FDI equity totals from April 2000 to June 2023. It is supplementary only and is not a quarterly time series.

See [`docs/DATA_SOURCES_AND_LIMITATIONS.md`](docs/DATA_SOURCES_AND_LIMITATIONS.md).

## 4. Models and evaluation

- Linear Regression
- Polynomial Regression (degree 2) + Ridge regularisation
- Ridge Regression
- Lasso Regression
- Persistence baseline (predict next year as the previous year's value)

Metrics:
- RMSE (USD million)
- MAPE (%)
- R²

The annual dataset contains 25 full financial-year observations (FY 2000–01 to FY 2024–25). After creating the one-year lag, 24 samples remain. The first 18 are used for training and the final 6 for testing.

## 5. Current pilot results

The checked-in `results/annual_pilot_model_metrics.csv` contains the current run's metrics. In this six-observation test window, the persistence baseline performs better than the four regression models. This is reported transparently rather than selecting a worse model to make the results appear stronger.

**Do not interpret these numbers as quarterly forecast performance.** The quarterly target, RBI exchange-rate feature and dated policy indicators have not yet been incorporated.

## 6. How to reproduce

Python 3.10 or later is recommended.

### Windows (PowerShell)

```powershell
git clone https://github.com/YOUR-USERNAME/FDI-Equity-Inflows-India-ML-Project.git
cd FDI-Equity-Inflows-India-ML-Project
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/reproduce_analysis.py
```

### macOS / Linux

```bash
git clone https://github.com/YOUR-USERNAME/FDI-Equity-Inflows-India-ML-Project.git
cd FDI-Equity-Inflows-India-ML-Project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/reproduce_analysis.py
```

The script reads the included annual CSV and regenerates the metrics and figures.

## 7. Next steps to complete Problem 71

1. Retrieve the official quarterly DPIIT/OGD FDI equity-inflow observations, or monthly equity inflows that can be aggregated into quarters.
2. Retrieve a matching RBI USD/INR exchange-rate series.
3. Create dated policy-event indicators from documented official announcements.
4. Align all variables to the same quarter and document missing-value treatment.
5. Re-run chronological train/validation/test experiments using the assigned quarterly frequency.
6. Replace the annual-pilot tables and figures in the report with quarterly results.

## 8. Academic integrity and limitations

The repository intentionally distinguishes observed annual data from the required quarterly dataset. No annual total has been divided into four artificial quarters. No exchange rates or policy indicators have been fabricated. The attached PDF is a **draft pilot report**, not a final submission-ready quarterly paper.

## 9. Author

**Naman Bansal**  
B.Sc. (Hons.) Computer Science  
University of Delhi
