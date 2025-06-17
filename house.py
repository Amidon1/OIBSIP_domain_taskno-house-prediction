# Import  libraries
import streamlit as st
import pickle
import numpy as np

#  Loading the model
loaded_model = pickle.load(open('House_model.sav','rb'))


def predict_house_price(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_array)
    return prediction[0]

def main():
    st.title("🏠 House Price Prediction App")

    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.number_input("Area (sqft)", min_value=100, value=3000)
        bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
        bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
        stories = st.number_input("Stories", min_value=1, value=2)

    with col2:
        mainroad = st.selectbox("Main Road Access (1 = Yes, 0 = No)", [1, 0])
        guestroom = st.selectbox("Guest Room (1 = Yes, 0 = No)", [1, 0])
        basement = st.selectbox("Basement (1 = Yes, 0 = No)", [1, 0])
        hotwaterheating = st.selectbox("Hot Water Heating (1 = Yes, 0 = No)", [1, 0])

    with col3:
        airconditioning = st.selectbox("Air Conditioning (1 = Yes, 0 = No)", [1, 0])
        parking = st.selectbox("Parking Spaces", [0, 1, 2, 3])
        prefarea = st.selectbox("Preferred Area (1 = Yes, 0 = No)", [1, 0])
        furnishingstatus = st.selectbox("Furnishing Status (0 = Unfurnished, 1 = Semi, 2 = Furnished)", [0, 1, 2])

    if st.button("Predict House Price"):
        input_data = [
            area, bedrooms, bathrooms, stories,
            mainroad, guestroom, basement, hotwaterheating,
            airconditioning, parking, prefarea, furnishingstatus
        ]
        result = predict_house_price(input_data)
        st.success(f"Estimated House Price: ₦{result:,.2f}")


# Run the main function
if __name__ == "__main__":  # Corrected the __name__ check
    main()