import streamlit as st
import joblib
import numpy as np
import pandas as pd
model = joblib.load("model/size_prediction_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")
st.title("Women's Clothing Size Prediction")
st.write("Enter your body measurements to predict the best clothing size.")
height = st.number_input("Height (cm)", 140, 200)
weight = st.number_input("Weight (kg)", 40, 120)
bust = st.number_input("Bust (cm)", 60, 120)
waist = st.number_input("Waist (cm)", 50, 110)
hips = st.number_input("Hip (cm)", 60, 130)
if st.button("Predict Size"):
    input_df = pd.DataFrame(
        [[height, weight, bust, waist, hips]],
        columns=["Height", "Weight", "Bust", "Waist", "Hip"]
    )
    scaled_data = scaler.transform(input_df)
    prediction = model.predict(scaled_data)
    size = label_encoder.inverse_transform(prediction)

    st.success(f"Recommended Size: **{size[0]}**")

#scaled_data = scaler.transform(input_df)