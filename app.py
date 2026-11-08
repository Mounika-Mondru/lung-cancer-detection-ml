import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("ML_Project.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Lung Cancer Detection", page_icon="🫁")

st.title("🫁 Lung Cancer Detection Using Machine Learning")
st.write("Enter the patient details below to predict whether Lung Cancer is likely or not.")

st.subheader("Patient Details")

# Input Fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)

smoking = st.selectbox("Smoking", [1, 2])
yellow_fingers = st.selectbox("Yellow Fingers", [1, 2])
anxiety = st.selectbox("Anxiety", [1, 2])
peer_pressure = st.selectbox("Peer Pressure", [1, 2])
chronic_disease = st.selectbox("Chronic Disease", [1, 2])
fatigue = st.selectbox("Fatigue", [1, 2])
allergy = st.selectbox("Allergy", [1, 2])
wheezing = st.selectbox("Wheezing", [1, 2])
alcohol = st.selectbox("Alcohol Consuming", [1, 2])
coughing = st.selectbox("Coughing", [1, 2])
shortness_breath = st.selectbox("Shortness of Breath", [1, 2])
swallowing = st.selectbox("Swallowing Difficulty", [1, 2])
chest_pain = st.selectbox("Chest Pain", [1, 2])

# Convert Gender
gender = 1 if gender == "Male" else 0

# Prediction Button
if st.button("Predict"):

    data = pd.DataFrame({
        'GENDER':[gender],
        'AGE':[age],
        'SMOKING':[smoking],
        'YELLOW_FINGERS':[yellow_fingers],
        'ANXIETY':[anxiety],
        'PEER_PRESSURE':[peer_pressure],
        'CHRONIC DISEASE':[chronic_disease],
        'FATIGUE ':[fatigue],
        'ALLERGY ':[allergy],
        'WHEEZING':[wheezing],
        'ALCOHOL CONSUMING':[alcohol],
        'COUGHING':[coughing],
        'SHORTNESS OF BREATH':[shortness_breath],
        'SWALLOWING DIFFICULTY':[swallowing],
        'CHEST PAIN':[chest_pain]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Prediction: Lung Cancer Detected")
    else:
        st.success("✅ Prediction: No Lung Cancer Detected")