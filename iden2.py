import streamlit as st
import pandas as pd

st.title('Fly Species Identification Software')
st.warning('This software can identify CN, CM, CR, LC, HL, MD and PD')

st.subheader('Please upload sample_coordinate.csv' )

uploaded_files = st.file_uploader("Choose a CSV file", type='csv')

df = pd.read_csv(uploaded_files)
lm_list = df.values.tolist()

sp = ''

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(lm_list)
