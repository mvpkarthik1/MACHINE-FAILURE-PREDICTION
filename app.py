import streamlit as st
import pandas as pd
import pickle
#---------------------------------#

pickle_in = open("RF_model.pkl","rb")
RF_model = pickle.load(pickle_in)

#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='MACHINE FAILURE PREDICTION',
    layout='wide')
#---------------------------------#
st.header("""MACHINE FAILURE PREDICTION 
Enter the values in the input boxes and check the machine failure prediction""")

#---------------------------------#
st.markdown('**ENTER THE VALUES**')
Type = st.number_input("enter Type here")


Air_temp = st.number_input("enter Air_temp here")

Process_temp = st.number_input("enter Process_temp here")
Rot_speed = st.number_input("enter Rot_speed here")
Torque = st.number_input("enter Torque here")
Tool_wear = st.number_input("enter Tool_wear here")

X = pd.DataFrame(columns=list('ABCDEF'))

X.loc[0] = [Type,Air_temp,Process_temp,Rot_speed,Torque,Tool_wear]


if st.button('PREDICT MACHINE FAILURE'):
    predict = RF_model.predict(X)

    array = predict[0]
    TWF = array[0]
    HDF = array[1]
    PWF = array[2]
    OSF = array[3]
    RNF = array[4]
    Mach_failure = array[5]
    
    if TWF==1 :
        st.write("Tool Wear Failure Occured")
    else :
        st.write("Tool Wear Failure  didnt Occur")

    if HDF==1 :
        st.write("Heat Dissipation Failure Occured")
    else :
        st.write("Heat Dissipation Failure  didnt Occur")
    if PWF==1 :
        st.write("Power Failure Occured")
    else :
        st.write("Power Failure  didnt Occur")
    if OSF==1 :
        st.write("Overstrain Failure Occured")
    else :
        st.write("Overstrain Failure  didnt Occur")
    if RNF==1 :
        st.write("Random Failure Occured")
    else :
        st.write("Random Failure  didnt Occur")
    if Mach_failure==1 :
        st.write("Machine Failure Occured")
    else :
        st.write("Machine Failure  didnt Occur")
