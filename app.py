import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
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

hypertension = 1 if hypertension == 'yes' else 0
heart_disease = 1 if heart_disease == 'yes' else 0
Male = 1 if sex == 'Male' else 0
Female = 1 if Male == 0 else 0

fs, ns, s = 0,0,0
if smoking == 'formerly smoked':
  fs = 1
elif smoking == 'never smoked':
  ns = 1
elif smoking == 'smokes':
  s = 1
  
input_data = scaler.transform([[age, hypertension, heart_disease, avg_glucose, bmi, Male, Female, fs, ns, s]])
pred = model.predict(input_data)
if pred[0] == 1:
  st.subheader('Person has suffered stroke')
else:
  st.subheader('Person has not suffered stroke')
  
