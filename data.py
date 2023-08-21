import numpy as np
import pandas as pd
import streamlit as st 
import os 
st.set_page_config(
    page_title= 'Currency rate dashboard',
    layout= 'wide'
)
options = st.selectbox("Chose the Currency",('U.S Dollar','Euro','U.K Pound Sterling','Egyptian Pound'))

placeholder = st.empty()
extension = os.path.splitext("app.py")
