import streamlit as st
import joblib
st.title("spam-ham Classifier")
st.write("enter message")
test_model=joblib.load("spam-ham")
ip=st.text_input("Enter the message")
op=test_model.predict([ip])
if st.button('predict'):
  st.title(op[0])