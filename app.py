import streamlit as st
import joblib
import pandas
model = joblib.load('Logistic regression model')
st.title('LOGISTIC REGRESSION MODEL FOR STROKE')
age = st.number_input("age", min_value=1, max_value=100)
hypertension = st.selectbox("hypertension",options=['yes', 'no'])
heart_disease = st.selectbox("heart disease",options=['yes', 'no'])
avg_glucose = st.number_input("average glucose level")
bmi = st.number_input("bmi")
sex = st.selectbox("Sex",options=['Male' , 'Female'])
smoking = st.selectbox("smoking status",options=['formerly smoked', 'never smoked', 'smokes'])
