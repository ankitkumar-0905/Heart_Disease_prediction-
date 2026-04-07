import streamlit as st
import numpy as np
import joblib

# Load files
model = joblib.load("LogisticRegression_heart.pkl")
scaler = joblib.load("Scaler.pkl")
columns = joblib.load("Columns.pkl")

st.set_page_config(page_title="Heart Disease Predictor")

st.title("❤️ Heart Disease Predictor")

st.write("Enter patient details below:")


# Inputs
age = st.slider("Age", 1, 120)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain", ["ATA", "NAP", "TA", "ASY"])
bp = st.number_input("Resting BP",80,200,120)
chol = st.number_input("Cholesterol",80,600,200)
fbs = st.selectbox("Fasting BS > 120", [0,1])
maxhr = st.slider("Max Heart Rate")
oldpeak = st.slider("Oldpeak",0.0,6.0,1.0)
restecg = st.selectbox("Rest ECG", ["Normal","ST","LVH"])
exang = st.selectbox("Exercise Angina", ["Y","N"])
slope = st.selectbox("ST Slope", ["Up","Flat","Down"])

# Create input dataframe (all 0)
input_data = np.zeros(len(columns))

# Fill numeric values
input_data[columns.index("Age")] = age
input_data[columns.index("RestingBP")] = bp
input_data[columns.index("Cholesterol")] = chol
input_data[columns.index("FastingBS")] = fbs
input_data[columns.index("MaxHR")] = maxhr
input_data[columns.index("Oldpeak")] = oldpeak

# One-hot encoding
if sex == "Male":
    input_data[columns.index("Sex_M")] = 1

if cp != "ASY":
    input_data[columns.index(f"ChestPainType_{cp}")] = 1

if restecg != "LVH":
    input_data[columns.index(f"RestingECG_{restecg}")] = 1

if exang == "Y":
    input_data[columns.index("ExerciseAngina_Y")] = 1

if slope != "Down":
    input_data[columns.index(f"ST_Slope_{slope}")] = 1

# Convert to 2D
input_data = input_data.reshape(1, -1)

# 🔥 Apply scaler only on correct columns
scale_indices = [
    columns.index("Age"),
    columns.index("RestingBP"),
    columns.index("Cholesterol"),
    columns.index("MaxHR"),
    columns.index("Oldpeak")
]

input_data[:, scale_indices] = scaler.transform(input_data[:, scale_indices])

# Prediction
if st.button("Predict"):
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
    Scaled_input =Scaler.transform(input_df)  
    
    prediction = model.predict(Scaled_input)[0]

    if prediction ==1:
        st.error("⚠️ High Risk of Heart Disease") 
    else:
        st.success("✅ Low Risk of Heart Disease")
