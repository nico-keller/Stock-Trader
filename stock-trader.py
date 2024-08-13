import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def search_stock(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    return stock

watchlist = []

def add_to_watchlist(stock_symbol):
    stock = search_stock(stock_symbol)
    if stock_symbol not in [s.ticker for s in watchlist]:
        watchlist.append(stock)

def fetch_watchlist_data():
    data = {}
    for stock in watchlist:
        # Fetch historical data for the last year
        data[stock.ticker] = stock.history(period='1y')  # Fetching 1 year of data
    return data

def plot_stocks():
    plt.figure(figsize=(10, 6))

    # Fetch data and plot each stock
    for stock in watchlist:
        data = stock.history(period='1y')  # Adjust the period as needed
        monthly_data = data['Close'].resample('ME').mean()  # Resampling by month and taking the mean price
        plt.plot(monthly_data.index.strftime('%Y-%m'), monthly_data, label=stock.ticker)

    plt.title("Stock Prices for Watchlist (Monthly over Last Year)")
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def run():
    while True:
        stock_symbol = input("Enter stock symbol to add to watchlist (or 'exit' to finish): ").upper()
        if stock_symbol == 'EXIT':
            break
        add_to_watchlist(stock_symbol)

    if watchlist:
        plot_stocks()
    else:
        print("No stocks were added to the watchlist.")

# Run the program
run()
