Task 1: Predictive Core (Static Analysis)
Objective

To analyze historical stock price data and predict short-term future prices.

Approach

Stock selected: Apple Inc. (AAPL)

Historical data (last 5 years) is fetched using yfinance

Closing prices are used for modeling

An ARIMA(1,1,1) model is trained on the data

The next 7 business days are forecasted

Forecasted values are visualized along with confidence intervals

Output

The output is a graph showing:

Historical closing prices

7-day price forecast

Confidence interval representing prediction uncertainty

Task 2: Analytical Chatbot (Contextual Explanation)

Objective

To build a natural language chatbot that explains stock market movements using contextual information.

Example Queries

Why did Apple stock drop?

When did Microsoft go up?

Explain Apple stock movement

How It Works

The user enters a natural language query

The system identifies the company name and maps it to a stock ticker

Relevant stock-related news is retrieved

The chatbot generates an explanation using the retrieved context

RAG-Based Explanation

The chatbot follows a lightweight Retrieval-Augmented Generation (RAG) approach:

Retrieval: Fetches recent financial news for the identified stock

Generation: Produces an explanation based on the retrieved information

If no major news is found, the system explains the movement using market sentiment, which reflects real-world trading behavior.

How to Run
Install Dependencies
pip install yfinance pandas matplotlib statsmodels

Run Task 1

cd PS1/Task1

python task1.py

Run Task 2

cd PS1/Task2

python task2.py

Type exit to stop the chatbot.
