# Housing Price Prediction

This repository contains a machine learning application that predicts house prices based on various features. The application uses a trained model to make predictions and provides a user-friendly web interface built with Streamlit.

## Project Overview

This project analyzes housing data and builds a predictive model to estimate median house values. The application allows users to input various housing characteristics and receive a predicted house price based on those inputs.

## Dataset

The application uses a housing dataset that includes the following features:

- **MedInc**: Median income in the block group
- **HouseAge**: Median house age in the block group
- **AveRooms**: Average number of rooms per household
- **AveBedrms**: Average number of bedrooms per household
- **Population**: Block group population
- **AveOccup**: Average number of household members
- **Latitude**: Block group latitude
- **Longitude**: Block group longitude

The target variable is the median house value for districts in the dataset.

## Model

The machine learning model was developed using scikit-learn. The model pipeline includes:

1. **Feature Engineering**: Creating derived features to improve model performance
   - Population Density: Population / Average Occupancy
   - Log of Median Income: Natural logarithm of Median Income
   - Rooms Per Household: Average Rooms / Average Occupancy
   - Bedroom Ratio: Average Bedrooms / Average Rooms

2. **Model Training**: The model was trained on historical housing data

## Streamlit Application

The Streamlit application provides an intuitive interface for users to interact with the model:

1. Users can input values for all required features
2. The application performs the necessary feature engineering
3. The model predicts the house price based on the input features
4. The predicted price is displayed to the user

### How to Use the App

1. Enter values for all the required fields:
   - Median Income
   - House Age
   - Average Rooms
   - Average Bedrooms
   - Population
   - Average Occupancy
   - Latitude
   - Longitude

2. Click the "Predict Price" button
3. View the predicted house price

## Installation and Setup

To run this application locally:

1. Clone this repository
```
git clone https://github.com/Chaitu123432/Housing-Price-Prediction.git
cd Housing-Price-Prediction
```

2. Install the required dependencies
```
pip install -r requirements.txt
```

3. Run the Streamlit app
```
streamlit run app.py
```

## Files in the Repository

- `app.py`: The Streamlit application code
- `house_price_model.pkl`: The trained machine learning model
- `requirements.txt`: List of required Python packages
- `README.md`: This file
- `.gitignore`: Specifies intentionally untracked files to ignore

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Future Improvements

- Add data visualization to show housing trends
- Implement model explanation using SHAP or LIME
- Add a map visualization for location-based predictions
- Expand the model to include more recent housing data
- Adapt the model for different housing markets

## License

This project is open source and available under the [MIT License](LICENSE).
