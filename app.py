# app.py - Flood Prediction App
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("flood_model.pkl")

st.title("🌊 Flood Probability Prediction")
st.write("Enter the environmental parameters to predict the flood probability.")

# Collect inputs from user
monsoon_intensity = st.number_input("Monsoon Intensity", min_value=0.0, step=0.1)
urbanization = st.number_input("Urbanization (%)", min_value=0.0, max_value=100.0, step=0.1)
deforestation = st.number_input("Deforestation (%)", min_value=0.0, max_value=100.0, step=0.1)
wetland_loss = st.number_input("Wetland Loss (%)", min_value=0.0, max_value=100.0, step=0.1)
drainage = st.number_input("Drainage Capacity", min_value=0.0, step=0.1)

# Convert to dataframe (make sure column names match training data)
input_data = pd.DataFrame({
    "MonsoonIntensity": [monsoon_intensity],
    "Urbanization": [urbanization],
    "Deforestation": [deforestation],
    "WetlandLoss": [wetland_loss],
    "Drainage": [drainage]
})

if st.button("Predict Flood Probability"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Flood Probability: {prediction:.2f}")
    
    if prediction > 0.7:
        st.error("⚠️ High Risk of Flood!")
    elif prediction > 0.4:
        st.warning("⚠️ Moderate Risk of Flood.")
    else:
        st.info("✅ Low Risk of Flood.")
