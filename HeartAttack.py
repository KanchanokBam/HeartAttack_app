import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
import pickle

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)



Menu = st.sidebar.selectbox("Menu",("Home", "Creator"))

if Menu == 'Home':
    page_bg_img = """
    <style>
        [data-testid="stAppViewContainer"] {
        background-image: url("https://images.pexels.com/photos/4436355/pexels-photo-4436355.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
        background-size: cover;
        }

        [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
        }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    image = Image.open('Logo.png')
    st.image(image)
    #st.title('HEART ATTACK')
    name = st.text_input("Your Name:")
    Age = st.number_input("Your Age:")
    sex = st.selectbox('Your Sex:', ('-','Female', 'Male'))
    if sex == "Female" :
        sex =0
    if sex == "Male" :
        sex =1
    Chest = st.number_input("Chest Pain type:")
    Blood = st.slider("Blood pressure: (mm/Hg)",  min_value=0, max_value=500)
    Clo = st.slider("Cholestoral: (mg/dl)" , min_value=0, max_value=500)
    HR = st.slider("Heart rate:" , min_value=0, max_value=500)
    BS = st.radio("Blood sugar:",('Yes', 'No'))
    if BS == "Yes" :
        BS = 1
    if BS == 'No':
        BS = 0
    subbs= st.caption("Do you have a blood sugar value greater than 120mm/dl?")

    submit = st.button("Submit")
    if submit:
        prediction = classifier.predict([[Age,sex,Chest,Blood,Clo,HR,BS]])
        if prediction == 0:
            st.success(str(name) + "You aren't at risk of developing this disease.")
        else:
            st.error("Oh"+str(name)+"You aren't at risk of developing this disease.")

if Menu == 'Creator':
    page_bg_img = """
    <style>
        [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #83deff, rgba(255,144,168,1))
        }

        [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
        }
    </style>
    """

    col1, col2, = st.columns(2)
    with col1:
        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.title('INFORMATION')

        image = Image.open('Pro.jpg')
        st.image(image)

        st.title('Hello, *World!* :sunglasses:')
        st.subheader("Kanchanok Kamernthong")
        st.write("")
        st.header("Education")
        st.text("""
        Data Science and Software Innovation 
        Ubonratchathani University
        2022-present.
        Science Math
        Kantharalak Witthaya school
        2016-2022.""")

        st.subheader("Contact")
        st.text("""
        FB:Kanchanok Khamernthong
        Line:bam025boo
        Tel.0923472280""")
