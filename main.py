import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
""")

#  2017 Ticker list from https://investexcel.net/all-yahoo-finance-stock-tickers/


@st.cache
def get_data():
    path = r'Yahoo Ticker Symbols - September 2017.csv'
    return pd.read_csv(path)


tickerList = get_data()
tickers = tickerList["Ticker"].drop_duplicates()
tickerSymbol = st.sidebar.selectbox('Select Ticker code ', tickers)
ticker_name = tickerList.loc[tickerList['Ticker'] == tickerSymbol]['Name'].values[0]

st.sidebar.header('Select start date and end date')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Stock price and volume for """ + ticker_name)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
