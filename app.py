import streamlit as st
import pandas as pd

st.title("Dynamic BMI Calculator :")

height = st.slider("Enter your height (in meter) : ",1.0,2.5,1.5)
weight = st.slider("Enter your weight (in kg) : ",30,120,45)

bmi = weight/(height**2)

st.write(f'Your BMI is \"{bmi:.2f}\"')
if bmi < 18.5:
    st.write(f'Your BMI Category is in \'underweight\'.')
elif 18.5 < bmi < 24.9:
    st.write('Your BMI Category is in \'Normal weight\'.')
elif 24.9 < bmi <29.9:
    st.write('Your BMI Category is in \'Overweight\'.')
elif bmi >= 30:
    st.write('Your BMI Category is in \'Obesity\'.')


st.write("### BMI Categories ###")
st.write("-Underweight : BMI less than 18.5")
st.write("-Normal weight : BMI greater than 18.5 and less than 24.9")
st.write("-Underweight : BMI greater than 24.9 and less than 29.9")
st.write("-Obesity : BMI greater than or equal to 30.0")