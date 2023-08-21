import numpy as np
import pandas as pd
import streamlit as st 
import os 

usd_df = pd.read_json("https://www.floatrates.com/daily/usd.json")
euro_df = pd.read_json("https://www.floatrates.com/daily/eur.json")
uk_df = pd.read_json("https://www.floatrates.com/daily/gbp.json")
egy_df = pd.read_json("https://www.floatrates.com/daily/egp.json")

st.set_page_config(
    page_title= 'Currency rate dashboard',
    layout= 'wide'
)
st.title("Currency rate / live data dashboard")
options = st.sidebar.selectbox("Chose the Currency",('U.S Dollar','Euro','U.K Pound Sterling','Egyptian Pound'))

placeholder = st.empty()

st.header(options)

if options == 'U.S Dollar':
    usd_df.head()
    

