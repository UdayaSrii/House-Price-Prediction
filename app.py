import streamlit as st
import pickle
import os
import time
# ---------------------------------------
# Caching Example
# ---------------------------------------
@st.cache_resource
def load_model():
    if not os.path.exists('house_price_model.pkl'):
       raise FileNotFoundError("Model file not found.")
    with open('house_price_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
if 'prediction' not in st.session_state:
    st.session_state.prediction_count = 0
st.title("House Price Prediction")
# ----------------------------------------
# Load Model
# -----------------------------------------
try:
    model = load_model()
except Exception as e:
    st.error(e)
    st.stop()
# -----------------------------------------
# Input Fields
# -----------------------------------------
area = st.number_input("Area ( sq ft)", 1000, 50000, 1500)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
age = st.slider("House Age", 0, 30, 5)
# -----------------------------------------         
# Prediction 
# -----------------------------------------
if st.button("Predict Price"):
    try:
        prediction = model.predict([[area, bedrooms, age]])
        st.success(f"Estimated Price: {prediction[0]:,.0f}")
        st.session_state.prediction_count += 1
    except Exception as e:
        st.error("Prediction Failed")
        st.exception(e)
# -----------------------------------------
# Session State Demo
# -----------------------------------------
st.info(f"Predictions Made : {st.session_state.prediction_count}")
# -----------------------------------------
# Reset Session 
# -----------------------------------------
if st.button("Reset Counter"):
    st.session_state.prediction_count = 0
    st.success("Counter Reset")