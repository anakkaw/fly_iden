import streamlit as st
import pandas as pd

st.title('Fly Species Identification Software')
st.warning('This software can identify CN, CM, CR, LC, HL, MD and PD')

st.subheader('Instruction:' )
st.write('1. Download sample_coordinate.csv')
link = '[download](https://drive.google.com/file/d/16XD8QlHhg6PC06p6sVSeiXCMa9WGajAi/view?usp=sharing)'
st.markdown(link, unsafe_allow_html=True)

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
    sp = 'MD'
else:
    if Ndb > 1026.04:
        if Nde > 1403.12:
            if Ndl > 530.82:
                if Ndf > 1393.64:
                    if Ndr > 2945.76:
                        sp = 'CR'
                    else:
                        sp = 'CM'
                else:
                    sp = 'CM'
            else:
                sp = 'CM'
        else:
            if Ndc > 1645.70:
                if Nda > 1571.80:
                    sp = 'CR'
                else:
                    if Ndh > 1990.58:
                        if Ndd > 588.76:
                            sp = 'CN'
                        else:
                            sp = 'CM'
                    else:
                        sp = 'CM'
            else:
                if Ndh > 2133.98:
                    sp = 'CN'
                else:
                    if Ndu > 682.00:
                        sp = 'CN'
                    else:
                        if Nde > 1386.68:
                            if Ndg > 428.72:
                                sp = 'CM'
                            else:
                                sp = 'CR'
                        else:
                            sp = 'CM'
        
    else:
        if Ndg > 393.34:
            if Ndc > 1656.34:
                if Nde > 1432.80:
                    sp = 'PD'
                else:
                    if Ndd > 653.36:
                        if Ndg > 650.70:
                            sp = 'PD'
                        else:
                            if Nds > 1335.14:
                                sp = 'HL'
                            else:
                                sp = 'LC'
                    else:
                        sp = 'PD'
            else:
                sp = 'CM'
        else:
            sp = 'CN'

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(sp)
