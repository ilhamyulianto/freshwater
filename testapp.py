import streamlit as st
import pandas as pd
import joblib
import json
import xgboost as xgb

# Load model and column structure
xgb_model = joblib.load('notebook/xgb_modeljson.pkl')
with open('notebook/xgb_columns.json') as f:
    model_columns = json.load(f)

st.title("Fresh Water Consumption Predictor")

# Example user input
distances_input = st.text_input("Enter distances (comma-separated)", "333, 450, 600")

if st.button("Predict"):
    try:
        # Convert input to list of floats
        distances = [float(d.strip()) for d in distances_input.split(",")]

        # Create base test DataFrame
        test_df = pd.DataFrame({'DISTANCE': distances})

        # Add missing one-hot columns with 0
        for col in model_columns:
            if col != 'DISTANCE':
                test_df[col] = 0

        # Reorder columns to match training
        test_df = test_df[model_columns]

        # Predict
        dmatrix_test = xgb.DMatrix(test_df)
        predictions = xgb_model.predict(dmatrix_test)

        # Show results
        for dist, pred in zip(distances, predictions):
            st.write(f"Distance: {dist} km — Predicted Fresh Water Consumption: {pred:.2f} liters")

    except Exception as e:
        st.error(f"Error: {e}")
