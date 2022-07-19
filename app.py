import streamlit as st
import joblib
model = joblib.load('Logistic regression model')
st.title('LOGISTIC REGRESSION MODEL FOR STROKE')
if st.button('Print accuracy score'):
  result = model.score(y_pred,y_test)*100
  print(result)  
