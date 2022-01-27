import streamlit as st
import pandas as pd
from PIL import Image
import pickle
st.write("""
# Income Classification App
""")

#Load the Pickle file
irisclassifier = open('sdecision_tree.pkl', 'rb')
classifier = pickle.load(irisclassifier)

# Text Input
													
Age = st.text_input("Enter the Age",)
Workclass = st.text_input("Enter the SWorkclass",)
Fnlwgt = st.text_input("Enter the Fnlwgt",)
Education = st.text_input("Enter the Education",)
Education_num = st.text_input("Enter the Education_num",)
Marital_status = st.text_input("Enter the Marital_status",)
Occupation = st.text_input("Enter the Occupation",)
Relationship = st.text_input("Enter the Relationship",)
Race = st.text_input("Enter the Race",)
Sex = st.text_input("Enter the Sex",)
Capital_gain = st.text_input("Enter the Capital_gain",)
Capital_loss = st.text_input("Enter the Capital_loss",)
Hours_per_week = st.text_input("Enter the Hours_per_week",)
Native_country = st.text_input("Enter the Native_country",)
submit = st.button('Classify')

if submit:
    with st.spinner("Classifying.."):
        result = classifier.predict([[Age,Workclass,Fnlwgt,Education,Education_num,Marital_status,Occupation,Relationship,Race,Sex,Capital_gain,Capital_loss,Hours_per_week,Native_country]])
        if(result[0]==0):
          st.write("The income is low")
        else:
           st.write("The income is high")
