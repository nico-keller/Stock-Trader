import yfinance as yf
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

watchlist = []


def add_to_watchlist(stock_symbol):
    if stock_symbol not in watchlist:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

        # Check if the ticker is valid by verifying if 'shortName' exists in stock_info
        if 'shortName' in stock_info:
            watchlist.append(stock_symbol)
            st.success(f"Added {stock_symbol} to watchlist.")
        else:
            st.error(f"Ticker '{stock_symbol}' not found.")
    else:
        st.warning(f"{stock_symbol} is already in the watchlist.")

def get_tickers_data(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            stock_info = stock.info
            if 'shortName' in stock_info:  # Check if the ticker is valid
                data.append({
                    'Short Name': stock_info.get('shortName', 'N/A'),
                    'Symbol': stock_info.get('symbol', 'N/A'),
                    'Sector': stock_info.get('sector', 'N/A'),
                    'Industry': stock_info.get('industry', 'N/A'),
                    'Country': stock_info.get('country', 'N/A'),
                })
            else:
                st.error(f"Ticker '{ticker}' not found.")
        except Exception as e:
            st.error(f"An error occurred with ticker '{ticker}': {str(e)}")

    df = pd.DataFrame(data)
    return df


def visualize_stocks(tickers):
    plt.figure(figsize=(10, 6))
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            plt.plot(hist.index, hist['Close'], label=ticker)
        except Exception as e:
            st.error(f"An error occurred while fetching data for {ticker}: {str(e)}")

    plt.title('Stock Prices Over Last Year')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    st.pyplot(plt)