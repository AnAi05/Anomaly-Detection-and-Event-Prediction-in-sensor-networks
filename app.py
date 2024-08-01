import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
df = pd.read_csv("data.csv")

# Split the data into features and target variable
X = df.drop('Number of Barriers', axis=1)
y = df['Number of Barriers']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = GradientBoostingRegressor()
model.fit(x_train, y_train)

# Save the trained model
joblib.dump(model, 'gbm_model.joblib')

import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('gbm_model.joblib')

# Create a Streamlit app
st.title("Anomaly Detection")

# Input fields for feature values on the main screen
st.header("Data for Checking Barrier")

area = st.number_input("Area", min_value=5000, max_value=50000)
sensing_range = st.number_input("Sensing Range", min_value=15, max_value=40)
transmission_range = st.number_input("Transmission Range", min_value=30, max_value=80)
n_sensor_node = st.number_input("Number of Sensor nodes", min_value=100, max_value=400)

# Make a prediction using the model
if st.button("Predict"):
    input_data = np.array([[area, sensing_range, transmission_range, n_sensor_node]])
    prediction = model.predict(input_data)

    # Display the prediction result on the main screen
    st.write("Number Of Barriers =", prediction[0])
