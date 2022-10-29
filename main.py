import streamlit as st

st.title('Fly Species Identification Software')
st.warning('This software can identify Chrysomya nigripes, Chrysomya megacephala, Chrysomya rufifacies, Lucilia cuprina, Hemipyrellia ligurriens, Musca domestica and Parasarcophaga dux')

st.subheader('Please input your sample morphological character' )

sp = ''

gena = st.radio( 'What is gena color?',('orange', 'white'))
body = st.radio('What is body color?', ('cuprous', 'grey','metalic green/blue'))
st.subheader('Please input the raw distance of your sample in micron unit')
st.image('https://drive.google.com/uc?id=16GofHejJvp7PULUZGMqrOaxkzSBOapuh')
Da = st.number_input('Enter distance a', min_value=100)
Db = st.number_input('Enter distance b', min_value=100)
Dc = st.number_input('Enter distance c', min_value=100)
Dd = st.number_input('Enter distance d', min_value=100)
De = st.number_input('Enter distance e', min_value=100)
Dg = st.number_input('Enter distance g', min_value=100)

raw_sum = Da+Db+Dc+Dd
ratio = 5000/raw_sum
Nda = Da*ratio
Ndb = Db*ratio
Ndc = Dc*ratio
Ndd = Dd*ratio
Nde = De*ratio
Ndg = Dg*ratio

if body == 'cuprous':
     sp = 'Lucilia cuprina'
elif body == 'grey':
     if Ndb > 738.44:
          sp = 'Parasarcophaga dux'
     else:
          sp = 'Musca domestica'
else:
     if gena == 'orange':
          sp = 'Chrysomya megacephala'
     else:
          if Nde > 1386.86:
               if Nda > 1409.28:
                    sp ='Chrysomya rufifacies'
               else:
                    sp ='Hemipyrellia ligurriens'
          else:
               if Ndg > 455.16:
                    sp = 'Hemipyrellia ligurriens'
               else:
                    if Nda >1564:
                         sp ='Chrysomya rufifacies'
                    else:
                         sp = 'Chrysomya nigripes'

if st.button('Identity'):
     st.write('Your sample is ...')
     st.subheader(sp)
