

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error



# 1. Fetch stock data (2021–2026)

df = yf.download(
    "AAPL",
    start="2021-01-01",
    end="2026-01-01",
    progress=False
)

close_price = df["Close"].dropna()


# 2. Train-Test split (for accuracy)

split = int(len(close_price) * 0.8)
train = close_price[:split]
test = close_price[split:]


# 3. Train ARIMA on train data

eval_model = ARIMA(train, order=(1, 1, 1))
eval_fit = eval_model.fit()


# 4. Past data prediction (accuracy)

past_pred = eval_fit.forecast(steps=len(test))
mae = mean_absolute_error(test, past_pred)


# 5. Train final model on full data

final_model = ARIMA(close_price, order=(1, 1, 1))
final_fit = final_model.fit()


# 6. Forecast next 7 days

forecast = final_fit.get_forecast(steps=7)
future_price = forecast.predicted_mean
future_ci = forecast.conf_int()


# 7. Create future dates (business days)

last_date = close_price.index[-1]
future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=7,
    freq="B"
)

future_price.index = future_dates
future_ci.index = future_dates

# 8. SINGLE FINAL GRAPH (ONLY ONE)

fig = plt.figure(figsize=(12, 6))

plt.plot(close_price, label="Historical Price", color="blue")
plt.plot(future_price, label="Next 7 Days Forecast", color="green")

plt.fill_between(
    future_ci.index,
    future_ci.iloc[:, 0],
    future_ci.iloc[:, 1],
    alpha=0.3,
    label="Confidence Interval"
)

plt.title("AAPL Stock Price Forecast using ARIMA (2021–2026)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
plt.close(fig)

print("MAE:", round(mae, 2))







