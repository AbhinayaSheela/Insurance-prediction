import streamlit as st
import sys
import os

# add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from prediction import Insurance_Prediction

st.title("Insurance Prediction")

st.write("This app predicts insurance premium based on age, income, policy term and sum assured.")

Age = st.number_input("Age")
Annual_Income_LPA = st.number_input("Annual Income (LPA)")
Policy_Term_Years = st.number_input("Policy Term (Years)")
Sum_Assured_Lakhs = st.number_input("Sum Assured (Lakhs)")

if st.button("Predict"):
    model = Insurance_Prediction()
    result = model.prediction(Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs)
    st.success(f"Predicted Premium: {result}")