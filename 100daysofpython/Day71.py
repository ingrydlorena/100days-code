'''
Day 71: Interactive data visualizations
Create interactive data visualizations with Plotly or Bokeh
'''
import plotly.express as px
import pandas as pd
import streamlit as st

data = pd.read_csv("br_rf_arrecadacao_uf.csv", sep = ',', decimal = '.')

# year = st.sidebar.selectbox('Year', data['ano'].unique())
# data_filtered = data[data['ano'] == year]
# city_total = data_filtered.groupby("Estado")[["imposto"]].sum().reset_index()

col1, col2 = st.column(2)
col3, col4 = st.column(2)

fig_data1 = px.bar(data, x='ano', y='imposto_importacao', color='sigla_uf', title='tax per year')