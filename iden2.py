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
Db = dist(lm_list[1],lm_list[2])
Dc = dist(lm_list[2],lm_list[3])
Dd = dist(lm_list[3],lm_list[4])
De = dist(lm_list[5],lm_list[6])
Df = dist(lm_list[6],lm_list[9])
Dg = dist(lm_list[8],lm_list[9])
Dh = dist(lm_list[8],lm_list[14])
Dl = dist(lm_list[12],lm_list[16])
Dr = dist(lm_list[4],lm_list[11])
Ds = dist(lm_list[10],lm_list[13])
Du = dist(lm_list[6],lm_list[7])

raw_sum = Da+Db+Dc+Dd
ratio = 5000/raw_sum
Nda = Da*ratio
Ndb = Db*ratio
Ndc = Dc*ratio
Ndd = Dd*ratio
Nde = De*ratio
Ndf = Df*ratio
Ndg = Dg*ratio
Ndh = Dh*ratio
Ndl = Dl*ratio
Ndr = Dr*ratio
Nds = Ds*ratio
Ndu = Du*ratio


sp = ''

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(Ndu)
