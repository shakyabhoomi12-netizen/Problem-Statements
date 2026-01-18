Capital Pulse – Task 1

Predictive Core: Static Time-Series Forecasting

Overview:
This task implements a simple, explainable time-series forecasting system for stock prices using historical market data.
The goal is to forecast short-term price movement while explicitly modeling uncertainty, not just producing a single prediction line.

The solution prioritizes:

clarity of logic

correctness of methodology

explainability over complexity

Data Source

Source: Yahoo Finance (via yfinance)

Stock Used: Apple Inc. (AAPL)

Time Period: January 2021 – January 2026

Frequency: Daily (business days)

Feature Used: Closing Price

No CSV files are stored. Data is fetched dynamically at runtime.

Methodology:
A classical ARIMA (1,1,1) model is used for time-series forecasting.

The dataset is split into:
80% training data,
20% testing data (for evaluation),
Model performance is evaluated on past unseen data.
A 7-day future forecast is generated.
Confidence intervals are included to represent uncertainty and volatility.
This approach provides a clean and interpretable baseline suitable for financial forecasting tasks.

Output (Single Consolidated Graph)

The program produces one final graph that combines:
Historical stock price trend.
Forecasted prices for the next 7 days.
Confidence interval (upper and lower bounds)
All outputs are intentionally visualized in a single graph to avoid clutter and ensure interpretability.

Evaluation Metric:
Mean Absolute Error (MAE),
Calculated on past unseen (test) data,
Printed in the console after model execution.
MAE measures the average prediction error and serves as a basic validation of the forecasting pipeline.

Note on Warnings:
During execution, some library-level warnings from statsmodels may appear related to date indexing and frequency.

These warnings:
Do not affect model correctness.
Do not affect forecasts or plots.
Are common when working with real-world financial time-series data.
The forecasting logic and results remain valid.

Technologies Used:
Python,
yfinance,
pandas,
matplotlib,
statsmodels,
scikit-learn.

How to Run:

Install dependencies:
pip install yfinance pandas matplotlib statsmodels scikit-learn.

Run the script:
cd PS1/Task1, and then python task1.py.

Conclusion:
This task demonstrates a clean and interpretable predictive core for financial time-series forecasting.
By combining historical trends, future projections, uncertainty bounds, and evaluation metrics into a single coherent pipeline, the solution fulfills all Task-1 requirements in a simple and explainable manner.

