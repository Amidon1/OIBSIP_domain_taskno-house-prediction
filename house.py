import streamlit as st
import pickle
import joblib
import pandas as pd
import numpy as np

# Load model and feature list correctly
with open("House_model.sav", "rb") as file:
    model = pickle.load(file)

with open("features.pkl", "rb") as file:
    features = pickle.load(file)

st.title("🏡 House Price Prediction App")

# User input function
def user_input():
    area = st.number_input("Area (sqft)", 500, 10000, step=100)
    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3])
    stories = st.selectbox("Stories", [1, 2, 3, 4])
    mainroad = st.selectbox("Main Road Access", ['yes', 'no'])
    guestroom = st.selectbox("Guest Room", ['yes', 'no'])
    basement = st.selectbox("Basement", ['yes', 'no'])
    hotwaterheating = st.selectbox("Hot Water Heating", ['yes', 'no'])
    airconditioning = st.selectbox("Air Conditioning", ['yes', 'no'])
    parking = st.slider("Parking Spaces", 0, 4)
    prefarea = st.selectbox("Preferred Area", ['yes', 'no'])
    furnishingstatus = st.selectbox("Furnishing Status", ['furnished', 'semi-furnished', 'unfurnished'])

    data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'mainroad': mainroad,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotwaterheating,
        'airconditioning': airconditioning,
        'parking': parking,
        'prefarea': prefarea,
        'furnishingstatus': furnishingstatus
    }
    return pd.DataFrame([data])

# Get input
input_df = user_input()

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"🏷 Predicted House Price: ₦{int(prediction[0]):,}")

if __name__ == "__main__":
    st.write("House Price Prediction App is running!")