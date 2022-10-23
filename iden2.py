import streamlit as st
import pandas as pd

st.title('Fly Species Identification Software')
st.warning('This software can identify CN, CM, CR, LC, HL, MD and PD')

st.subheader('Please upload sample_coordinate.csv' )

uploaded_files = st.file_uploader("Choose a CSV file", type='csv')

df = pd.read_csv(uploaded_files)
df = df.drop(columns=['landmark'])
lm_list = df.values.tolist()

def dist(la, lb):
    result = ((la[0]-lb[0])**2+(la[1]-lb[1])**2)**(1/2)
    return result
Da = dist(lm_list[0],lm_list[1])
sp = ''

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(Da)
