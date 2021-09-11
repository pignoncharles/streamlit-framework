import streamlit as st


import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
# import time

# import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# import altair as alt


import requests

import os


from boto.s3.connection import S3Connection
key = (os.environ['ALPHA_ADVANTAGE_API'])

st.title('Pignon 2021 Data Incubator Interactive Stock Ticker')
st.write("Display Google stock daily closing price for a user-selected month & year:")

user_input_stock_name = st.sidebar.text_input("Select a stock (e.g. GOOG, TSLA)", 'GOOG')


ts = TimeSeries(key, output_format='pandas')
# data, meta = ts.get_intraday('TSLA', interval='1min', outputsize='full')
# data, meta = ts.get_daily('GOOG', outputsize='full')
data, meta = ts.get_daily(user_input_stock_name, outputsize='full')

st.write("Stock ticker metadata:")
st.write(meta)

# st.write("Stock dataset info:")
# st.write(data.info())

# st.write("Stock dataset head:")
# st.write(data.head())

#extract year month
data['year'] = data.index.year
data['month'] = data.index.month

#year and month selection
sorted_years=list(set(data['year']))
sorted_years.sort()
year_option = st.sidebar.selectbox(
    'Select a year',
     # set(data['year']))
     sorted_years)

sorted_months=list(set(data['month']))
sorted_months.sort()
month_option = st.sidebar.selectbox(
    'Select a month',
     # set(data['month']))
     sorted_months)

'You selected: ', month_option, year_option

data=data[data.index.year == year_option]
data=data[data.index.month == month_option]

#keep only closing data
data=data[['4. close']]



# plot the graph
chart = st.line_chart(data)


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
