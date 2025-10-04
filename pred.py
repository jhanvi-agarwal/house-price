import pandas as pd
import pickle as pk
import streamlit as st
import os

# File paths
MODEL_PATH = 'c:/Users/MEHAK/bangalore house price/miniproject/House_prediction_model.pkl'
DATA_PATH = 'c:/Users/MEHAK/bangalore house price/miniproject/Cleanedd_data.csv'

# Load the model
if os.path.exists(MODEL_PATH):
    model = pk.load(open(MODEL_PATH, 'rb'))
else:
    st.error("Model file not found!")

# Load the data
if os.path.exists(DATA_PATH):
    data = pd.read_csv(DATA_PATH)
else:
    st.error("Cleaned data file not found!")

# Streamlit UI
st.header('Banglore House Prices Predictor')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter total sqft', min_value=100)
beds = st.number_input('Enter number of bedrooms', min_value=1)
bath = st.number_input('Enter number of bathrooms', min_value=1)
balc = st.number_input('Enter number of balconies', min_value=0)

# Prepare input for prediction
input_df = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                        columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

# Predict button
if st.button("Predict Price"):
    try:
        output = model.predict(input_df)
        st.success('Price of the House is ₹' + str(int(output[0] * 100000)))
    except Exception as e:
        st.error("Prediction failed: " + str(e))
