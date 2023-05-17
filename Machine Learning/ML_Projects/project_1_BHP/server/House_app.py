import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json

result = None

# loading the saved model
__model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))

# loading the column json file
__data_columns = json.load(open("columns.json", "r"))['data_columns']
__locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

# creating a function for Prediction
def get_predicted_price(location, sqft, bathroom, BHK):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bathroom
    x[2] = BHK

    if loc_index >= 0:
        x[loc_index] = 1

    price = round(__model.predict([x])[0],2)
    strp = ' lakhs'

    return str(price) + strp

def main():
    global result
    
    # giving a title
    st.title('Bangalore House Price Predictor')
    
    
    # getting the input data from the user
    total_sqft = st.text_input("Total_sqft")
    bathroom = st.number_input("Number of Bathrooms",1,21)
    BHK = st.number_input("BHK",1,18)
    location = st.selectbox("Location", __locations)

    # creating a button for Prediction
    if st.button("Predict"):
        result = get_predicted_price(location, total_sqft, bathroom, BHK)

    st.success(f"Price = {result}")

if __name__ == "__main__":
    main()