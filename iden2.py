import streamlit as st
import pandas as pd

st.title('Fly Species Identification (without Characteristic Feature)')
st.warning('This software can identify Chrysomya nigripes, Chrysomya megacephala, Chrysomya rufifacies, Lucilia cuprina, Hemipyrellia ligurriens, Musca domestica and Parasarcophaga dux')

st.subheader('Instruction:' )
st.write('1. Download sample_coordinate.csv')
link = '[download](https://drive.google.com/file/d/16XD8QlHhg6PC06p6sVSeiXCMa9WGajAi/view?usp=sharing)'
st.markdown(link, unsafe_allow_html=True)
st.write('2. Input the coordinate of all landmarks of your sample in the csv file')
st.write('3. Upload the csv file below and then click identify')

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

if Ndb < 737.62:
    sp = 'Musca domestica'
else:
    if Ndb > 1026.04:
        if Nde > 1403.12:
            if Ndl > 530.82:
                if Ndf > 1393.64:
                    if Ndr > 2945.76:
                        sp = 'Chrysomya rufifacies'
                    else:
                        sp = 'Chrysomya megacephala'
                else:
                    sp = 'Chrysomya megacephala'
            else:
                sp = 'Chrysomya megacephala'
        else:
            if Ndc > 1645.70:
                if Nda > 1571.80:
                    sp = 'Chrysomya rufifacies'
                else:
                    if Ndh > 1990.58:
                        if Ndd > 588.76:
                            sp = 'Chrysomya nigripes'
                        else:
                            sp = 'Chrysomya megacephala'
                    else:
                        sp = 'Chrysomya megacephala'
            else:
                if Ndh > 2133.98:
                    sp = 'Chrysomya nigripes'
                else:
                    if Ndu > 682.00:
                        sp = 'Chrysomya nigripes'
                    else:
                        if Nde > 1386.68:
                            if Ndg > 428.72:
                                sp = 'Chrysomya megacephala'
                            else:
                                sp = 'Chrysomya rufifacies'
                        else:
                            sp = 'Chrysomya megacephala'
        
    else:
        if Ndg > 393.34:
            if Ndc > 1656.34:
                if Nde > 1432.80:
                    sp = 'Parasarcophaga dux'
                else:
                    if Ndd > 653.36:
                        if Ndg > 650.70:
                            sp = 'Parasarcophaga dux'
                        else:
                            if Nds > 1335.14:
                                sp = 'Hemipyrellia ligurriens'
                            else:
                                sp = 'Lucilia cuprina'
                    else:
                        sp = 'Parasarcophaga dux'
            else:
                sp = 'Chrysomya megacephala'
        else:
            sp = 'Chrysomya nigripes'

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(sp)
