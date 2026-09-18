import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model = joblib.load("insurance_model.pkl")


# Page title
st.title("🏥 Medical Insurance Cost Prediction")

st.write(
    "Enter the patient's information below "
    "to estimate medical insurance charges."
)


# Age
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30,
    step=1
)


# Sex
sex = st.selectbox(
    "Sex",
    ["male", "female"]
)


# BMI
bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0,
    step=0.1
)


# Number of children
children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)


# Smoking status
smoker = st.selectbox(
    "Smoker",
    ["no", "yes"]
)


# Region
region = st.selectbox(
    "Region",
    [
        "northeast",
        "northwest",
        "southeast",
        "southwest"
    ]
)


# Prediction button
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Medical Insurance Cost: "
        f"${prediction[0]:,.2f}"
    )
