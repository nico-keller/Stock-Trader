import streamlit as st
from stock_trader import *

st.title("Stocks Watchlist")
st.subheader("Visualize the stocks you want")

stock_ticker = st.text_input('Enter a stock ticker to add a stock watchlist:')
if st.button('Add stock watchlist'):
    add_to_watchlist(stock_ticker)

if watchlist:
    df = get_tickers_data(watchlist)
    st.write(df)
    # Display the current watchlist
    st.subheader("Your Watchlist")
    st.write(watchlist)
else:
    st.write("No stocks in watchlist.")


