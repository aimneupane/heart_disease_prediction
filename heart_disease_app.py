import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the pickle file
with open("best_logistic_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit App Configuration
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #C51104;
        }
        .main {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #2c3e50, #4ca1af);
            border-radius: 15px;
            padding: 1.5rem;
            color: white;
        }
        .stButton>button {
            background-color: #ff4757;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 14px 30px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #c0392b;
            transform: scale(1.1);
        }
        h1 {
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            font-size: 2.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown("<h1 style='text-align: center; color: white;'>💖 Heart Disease Prediction 💖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ecf0f1; font-size: 1.2rem;'>Enter patient details to predict the likelihood of heart disease.</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🩺 Patient Information")
st.sidebar.markdown("<p style='color: white; font-size: 1.1rem;'>Please enter the details below:</p>", unsafe_allow_html=True)

# Create Form Fields in Sidebar
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.sidebar.radio("Sex", ["Male", "Female"])
cp = st.sidebar.selectbox("Chest Pain Type", ["0: Typical Angina", "1: Atypical Angina", "2: Non-Anginal", "3: Asymptomatic"])
trestbps = st.sidebar.number_input("Resting BP (mm Hg)", min_value=60, max_value=200, value=120)
chol = st.sidebar.number_input("Cholesterol (mg/dL)", min_value=0, max_value=600, value=200)
fbs = st.sidebar.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
restecg = st.sidebar.selectbox("Resting ECG", ["0: Normal", "1: ST-T Abnormality", "2: Probable LVH"])
thalach = st.sidebar.number_input("Max Heart Rate", min_value=0, max_value=250, value=150)
exang = st.sidebar.radio("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.sidebar.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=10.0, value=1.0)
slope = st.sidebar.selectbox("Slope", ["0: Upsloping", "1: Flat", "2: Downsloping"])
ca = st.sidebar.slider("Number of Major Vessels", min_value=0, max_value=4, value=0)
thal = st.sidebar.selectbox("Thalassemia", ["0: Normal", "1: Fixed Defect", "2: Reversible Defect"])

# Convert inputs to numerical format
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0
cp = int(cp.split(":")[0])
restecg = int(restecg.split(":")[0])
slope = int(slope.split(":")[0])
thal = int(thal.split(":")[0])

# Create DataFrame for user input
input_data = pd.DataFrame({
    'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
    'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach],
    'exang': [exang], 'oldpeak': [oldpeak], 'slope': [slope],
    'ca': [ca], 'thal': [thal]
})

# Predict heart disease
if st.sidebar.button("🔮 Predict Now"):
    prediction = model.predict(input_data)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if prediction[0] == 1:
            st.markdown(
                """
                <div style="background-color: #ff4757; padding: 25px; border-radius: 15px; text-align: center;">
                    <h2 style="color: white; font-size: 1.5rem;">🔴 The patient is likely to have heart disease.</h2>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="background-color: #2ecc71; padding: 25px; border-radius: 15px; text-align: center;">
                    <h2 style="color: white; font-size: 1.5rem;">🟢 The patient is not likely to have heart disease.</h2>
                </div>
                """, unsafe_allow_html=True
            )
