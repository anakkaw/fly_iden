import streamlit as st

st.title('Fly Species Identification Software')
st.warning('This software can identify CN, CM, CR, LC, HL, MD and PD')

st.subheader('Please input your sample morphological character' )

sp = ''

uploaded_files = st.file_uploader("Choose a CSV file", type='csv')

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(sp)
