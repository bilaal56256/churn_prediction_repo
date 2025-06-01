
import gzip
import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import streamlit as st
# Model, and Collumns

st.title("☎️ Telco Churn Customers Prediction App")
st.write("Enter customer information below to get Churn Prediction.")

# User input feilds
def user_input():
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Has Partner?", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

    input_dict = {
        'gender': [gender],
        'SeniorCitizen': [1 if senior == "Yes" else 0],
        'Partner': [1 if partner == "Yes" else 0],
        'Dependents': [1 if dependents == "Yes" else 0],
        'tenure': [tenure],
        'MonthlyCharges': [monthly],
        'TotalCharges': [total],
    }

    return pd.DataFrame(input_dict)

input_df = user_input()

# OneHotEncode
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

# Predicting Custumer Churn
if st.button("Predict Churn"):
    prediction = model.predict(input_encoded)[0]
    prob = model.predict_proba(input_encoded)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This customer is more likely to Churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ This customer is not likely to Churn (Probability: {prob:.2f})")
