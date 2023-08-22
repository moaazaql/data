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
st.title(":bar_chart: Currency rate / live data dashboard")
st.markdown("##")

options = st.sidebar.selectbox("Chose the Currency",('U.S Dollar','Euro','U.K Pound Sterling','Egyptian Pound'))

placeholder = st.empty()

st.header(options)
if options == 'U.S Dollar':
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Euro €", value=round(usd_df.loc['rate']['eur']))
        kpi2.metric(label="Egyptian Pound E£", value=round(usd_df.loc['rate']['egp'] ))
        kpi3.metric(label="U.K. Pound Sterling  £", value=round(usd_df.loc['rate']['gbp']))


    st.markdown("""---""")
    
    st.write(st.dataframe(usd_df.head()))

if options == 'Euro':

    st.markdown("""---""")
    
    st.write(st.dataframe(euro_df.head()))

if options == 'Egyptian Pound':
    

    st.markdown("""---""")
    
    st.write(st.dataframe(uk_df.head()))

if options == 'U.S Dollar':

    st.markdown("""---""")
    
    st.write(st.dataframe(egy_df.head()))

