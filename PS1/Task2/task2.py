import yfinance as yf


# 1. Ticker mapping

TICKERS = {
    "apple": "AAPL",
    "aapl": "AAPL",
    "microsoft": "MSFT",
    "msft": "MSFT",
    "tesla": "TSLA"
}


# 2. Extract ticker

def get_ticker(query):
    query = query.lower()
    for name in TICKERS:
        if name in query:
            return TICKERS[name]
    return None


# 3. Get price trend

def get_trend(ticker):
    data = yf.download(ticker, period="14d", progress=False)
    close = data["Close"]

    if len(close) < 2:
        return "stable"

    change = (close.iloc[-1] - close.iloc[0]).item()

    if change > 0:
        return "up"
    elif change < 0:
        return "down"
    else:
        return "stable"


# 4. Get one safe news title

def get_news(ticker):
    stock = yf.Ticker(ticker)
    news = stock.news

    if not news:
        return "No major recent news."

    item = news[0]

    # SAFE access
    return (
        item.get("title")
        or item.get("headline")
        or "Recent news available, but headline not provided."
    )


# 5. Answer user query

def answer_query(query):
    ticker = get_ticker(query)

    if not ticker:
        return "Sorry, I could not identify the stock."

    trend = get_trend(ticker)
    news = get_news(ticker)

    response = f"Stock: {ticker}\n"
    response += f"Recent price trend: {trend}\n"
    response += f"Related news: {news}\n"
    response += (
        "The recent movement may be influenced by this news "
        "and overall market sentiment."
    )

    return response


# 6. Chat loop

print("Capital Pulse Task 2 (Minimum Final)")
print("Type 'exit' to quit\n")

while True:
    q = input("Ask a question: ")
    if q.lower() == "exit":
        break

    print("\n" + answer_query(q) + "\n")







