import streamlit as st
import joblib
st.title('LOGISTIC REGRESSION MODEL FOR STROKE')
if st.button('Print accuracy score'):
  joblib.load('Logistic regression model')  
