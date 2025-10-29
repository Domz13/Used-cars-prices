import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your trained pipeline (replace with your .pkl file path if saved)
# Example: rf_pipeline = joblib.load("rf_pipeline.pkl")
from sklearn.pipeline import Pipeline
from category_encoders import TargetEncoder
from sklearn.ensemble import RandomForestRegressor

# If model is already in memory, comment out the joblib.load line below
rf_pipeline = joblib.load("final_rf_model.pkl")

st.set_page_config(page_title="Used Car Price Predictor", layout="centered")

st.title("Used Car Price Prediction App")
st.markdown("Enter car details below to estimate its price.")

# Define inputs
mileage = st.number_input("Mileage (in km):", min_value=0, max_value=2_000_000, value=50000, step=1000)
auto = st.selectbox("Automatic Transmission:", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
ac = st.selectbox("Air Conditioner:", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
ps = st.selectbox("Power Steering:", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
remote = st.selectbox("Remote Control:", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
brand_model = st.text_input("Brand and Model (e.g., Toyota Corolla):")

# When user clicks predict
if st.button("Predict Price"):
    # Make DataFrame
    input_data = pd.DataFrame([{
        'Mileage': mileage,
        'Automatic Transmission': auto,
        'Air Conditioner': ac,
        'Power Steering': ps,
        'Remote Control': remote,
        'brand_model': brand_model
    }])

    # Predict using your trained pipeline
    try:
        prediction = rf_pipeline.predict(input_data)[0]
        # If trained on log-transformed prices, reverse it
        # prediction = np.expm1(prediction)

        st.success(f"**Estimated Price:** {prediction:,.0f} EGP")

    except Exception as e:
        st.error(f"Error during prediction: {e}")