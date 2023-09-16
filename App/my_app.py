
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Exchange rate Euro to custom currency, 1999-2022')

@st.cache_data
def load_data():
    data = pd.read_csv("euro-daily-hist_1999_2022.csv")
    data.rename(columns={'Period\\Unit:': 'Time'}, inplace=True)

    data['Time'] = pd.to_datetime(data['Time'])
    data.sort_values('Time', inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Data ready!")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Currency exchange rate plot
country = option = st.selectbox(
    'Choose your currency :',
     data.columns[1:])
st.subheader(f'Plot of exchange rate over time, Euro to {country}')

current_exch = data[['Time', country]]
current_exch = current_exch[current_exch[country] != '-']
current_exch[country] = current_exch[country].astype(float)

current_exch['rolling_mean'] = current_exch[country].rolling(30).mean()
fig = plt.figure()
plt.plot(current_exch['Time'], current_exch['rolling_mean']) 

st.pyplot(fig)
