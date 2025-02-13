'''
Day 69: Statistical analysis
Perform statistical analysis on a dataset.
'''

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

data = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')

data['Date'] = pd.to_datetime(data["Date"])
data = data.sort_values('Date')
data['Month'] = data['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))

month = st.sidebar.selectbox('Month', data['Month'].unique())
data_filtered = data[data['Month'] == month]
city_total = data_filtered.groupby("City")[["Total"]].sum().reset_index()
rating = data_filtered.groupby("City")[["Rating"]].mean().reset_index()



col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(data_filtered, x='Date', y='Total', color='City',title = 'billing per day')
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(data_filtered, x='Date', y='Product line', color='City', title='billing by product type', orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True)

fig_city = px.bar(data_filtered, x='City', y='Total', title = 'billing per branch')
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(data_filtered, values='Total', names='Payment', title= 'billing by payment type')
col4.plotly_chart(fig_kind, use_container_width=True)

fig_rating = px.bar(data_filtered, x='City', y='Rating', title='Rating')
col5.plotly_chart(fig_rating, use_container_width=True)



