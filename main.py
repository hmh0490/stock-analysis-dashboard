import streamlit as st
import yfinance as yf
import plotly as pl
import cufflinks as cf
import pandas as pd
import datetime

# Sidebar
st.sidebar.subheader("Query Parameters")
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2023, 1, 1))

interval = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
default_interval = interval.index("1d")
# range = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
optionInterval = st.sidebar.selectbox("Interval", interval, index=default_interval)
# optionRange = st.sidebar.selectbox("Range", range)

# Retrieve ticker data
tickers_list = ["AAPL", "AMZN", "EBAY", "META", "MSFT", "NDAQ", "NFLX", "SPX",
		   "TSLA", "UBER", "ZM"]
ticker = st.sidebar.selectbox("Ticker", tickers_list)
data = yf.Ticker(ticker)
history = data.history(interval=optionInterval, start=start_date, end=end_date)

# Ticker information
string_name = data.info['longName']
st.header('%s' % string_name)
price = data.info['currentPrice']
currency = data.info['currency']
st.header('%s' % currency + " " + str(price))


string_summary = data.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('Price data')
st.write(history)

# Bollinger bands
st.header('Bollinger Bands')
qf=cf.QuantFig(history,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

# st.write(data.info)

