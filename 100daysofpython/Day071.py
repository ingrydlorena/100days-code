'''
Day 71: Interactive data visualizations
Create interactive data visualizations with Plotly or Bokeh
'''
import plotly.express as px
import pandas as pd
import streamlit as st

data = pd.read_csv("top_100_tiktok.csv", sep = ',')
top_5_followers = data.sort_values(by='Followers', ascending=False).head()
top_5_likes = data.sort_values(by='Likes', ascending=False).head()
col1, col2 = st.columns(2)
col3,col4 = st.columns(2)


fig_data1 = px.pie(top_5_followers, values = 'Followers', names = 'Username', title='The five tiktokers with more Followers')
col1.plotly_chart(fig_data1, use_container_width=True)

fig_data2 = px.bar(top_5_likes, x='Username', y='Likes', color='Username', title='Tiktokers with more Likes')
col2.plotly_chart(fig_data2, use_container_width=True)


top_5_followers = data.sort_values(by='Followers', ascending=True).head()
fig_data3 = px.pie(top_5_followers, values='Followers',names='Username', title='Tiktoker with less Followers')
col3.plotly_chart(fig_data3, use_container_width=True)

top_5_likes = data.sort_values(by='Likes', ascending=True).head()
fig_data4 = px.bar(top_5_likes, x='Username', y='Likes', color='Username', title='Tiktokers with less Likes')
col4.plotly_chart(fig_data4, use_container_width=True)