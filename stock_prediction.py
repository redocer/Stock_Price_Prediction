# Import python libraries
import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import pickle
import re

import matplotlib.pyplot as plt

m = st.markdown("""
<style>
div.stButton > button:first-child {
    width:44em;
}
</style>""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>STOCK PREDICTION</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green;'>XYZ Stock</h2>", unsafe_allow_html=True)

input_number = st.number_input("Enter Nifty Open price:")

run_model = st.button('Make Prediction')

filename = 'N:\\PROJECTS\\NEW_NOTEBOOKS\\Streamlit\\model.sav'

if run_model:
    model = pickle.load(open(filename, 'rb'))
    output_value = model.predict([[input_number]]) #run model on input data

    #st.text("Predicted Stock Price:")
    st.markdown("<h4 style='text-align: center; color: green;'>Predicted Stock Price:</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 5.9])
    with col2:
        st.text("{:.1f}".format(output_value[0]))
else:
    #st.text("Predicted Stock Price:")
    st.markdown("<h4 style='text-align: center; color: green;'>Predicted Stock Price:</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 5.8])
    with col2:
        st.text(0.0)
