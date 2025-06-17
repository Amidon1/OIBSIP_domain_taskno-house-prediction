🏠 House Price Prediction App

This project is a machine learning web app that predicts the price of a house based on user inputs like area, number of bedrooms, bathrooms, parking, and other home features.

It was built using Python, trained on real housing data, and deployed with Streamlit to make it interactive and user-friendly.

🚀 Features

    Predict house prices based on 12 key features

    Built with a machine learning regression model

    Interactive web app using Streamlit

    Clean and simple user interface

    Easy to use for non-technical users

🛠️ Tools Used

    Python 🐍

    pandas & NumPy

    scikit-learn (for model building)

    Streamlit (for frontend app)

    Jupyter Notebook (for model training & testing)

📦 Project Files

    house.py – the main Streamlit app

    model.pkl – the trained machine learning model

    dataset.csv – cleaned housing data used for training

    notebook.ipynb – model development and EDA

💻 How to Run Locally

    Clone the repo

git clone https://github.com/Amidon1/OIBSIP_domain_taskno-house-prediction

    Install dependencies

pip install -r requirements.txt

    Run the app

streamlit run house.py

🔍 Input Features

Here are the 12 features used in the prediction:

    Area

    Bedrooms

    Bathrooms

    Stories

    Main Road (0 = No, 1 = Yes)

    Guest Room (0 = No, 1 = Yes)

    Basement (0 = No, 1 = Yes)

    Hot Water Heating (0 = No, 1 = Yes)

    Air Conditioning (0 = No, 1 = Yes)

    Parking (numeric: e.g., 1, 2, 3)

    Prefarea (0 = No, 1 = Yes)

    Furnishing Status (0 = Unfurnished, 1 = Semi-Furnished or Fully-Furnished).
