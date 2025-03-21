import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load('house_price_model.pkl')

# Function to create derived features
def create_features(X):
    # Create a copy to avoid modifying the original
    X_new = X.copy()
    
    # Create the missing derived features
    X_new['PopulationDensity'] = X['Population'] / X['AveOccup']
    X_new['LogMedInc'] = np.log(X['MedInc'])
    X_new['RoomsPerHousehold'] = X['AveRooms'] / X['AveOccup']
    X_new['BedroomRatio'] = X['AveBedrms'] / X['AveRooms']
    
    return X_new

# Set up the app
st.title('California House Price Prediction')
st.write('Enter the features of the house to predict its price')

# Create input fields
med_inc = st.number_input('Median Income', min_value=0.0, max_value=15.0, value=3.5)
house_age = st.number_input('House Age', min_value=1.0, max_value=52.0, value=29.0)
ave_rooms = st.number_input('Average Rooms', min_value=0.8, max_value=142.0, value=5.2)
ave_bedrms = st.number_input('Average Bedrooms', min_value=0.3, max_value=35.0, value=1.0)
population = st.number_input('Population', min_value=3, max_value=36000, value=1200)
ave_occup = st.number_input('Average Occupancy', min_value=0.6, max_value=1250.0, value=3.0)
latitude = st.number_input('Latitude', min_value=32.5, max_value=42.0, value=35.6)
longitude = st.number_input('Longitude', min_value=-124.4, max_value=-114.3, value=-119.6)

# Create a prediction button
if st.button('Predict Price'):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame([[med_inc, house_age, ave_rooms, ave_bedrms, 
                               population, ave_occup, latitude, longitude]], 
                             columns=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
                                     'Population', 'AveOccup', 'Latitude', 'Longitude'])
    
    # Apply feature engineering to input data
    input_data = create_features(input_data)
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display prediction
    st.success(f'The predicted house price is: ${prediction * 100000:.2f}')
