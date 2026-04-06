import streamlit as st
import pandas as pd
import joblib as jb
st.write("App strat ho gya hai ")
try:
    model=jb.load("LogisticRegression_heart.pkl")
    Scaler=jb.load("Scaler.pkl")
    Expected_colums=jb.load('Columns.pkl')
    st.success("model loaded ✅")
except Exception as e:
    st.error(f"Error aa rha hai : {e}")    

st.title("Heart Stroke Prediction by Ankit ❤️ ")
st.markdown("Provide the following details")

Age=st.slider("Age",18,100,40)
sex=st.selectbox("SEX",['Male','Female'])
chest_pain=st.selectbox("Chest pain Type",["ATA","NAP","TA","ASY"])
resting_bp=st.number_input("Resting BP(mm Hg)",80,200,120)
cholestrol =st.number_input("Cholesterol(mg/dL)",100,600,200)
FastingBS=st.selectbox("Fasting BS> 120 mg/dL",[0,1])
RestingECG=st.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr =st.slider("MAX Heart Rate ",60,220,150)
ExerciseAngina = st.selectbox("Exercise Angina",["y","N"])
oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)
ST_Slope = st.selectbox("ST Slope",["Up","Flat","Down"])

if st.button("Predict"):
    raw_input ={
        'Age':Age,
        'RestingBP':resting_bp,
        "Cholesterol":cholestrol,
        'FastingBS':FastingBS,
        'MaxHR':max_hr,
        'Sex_'+sex:1,
        'ChestPainType_' + chest_pain :1,
        'RestingECG_'+RestingECG:1,
        'ExerciseAngina_' + ExerciseAngina.upper():1,
        'ST_Slope_' + ST_Slope:1
    }
    input_df =pd.DataFrame([raw_input])
    input_df = input_df.reindex(columns=Expected_colums, fill_value=0)

    for col in Expected_colums:
        if col not in input_df.columns:
            input_df[col]=0

    input_df = input_df[Expected_colums]   

    Scaled_input =Scaler.transform(input_df)  
    
    prediction = model.predict(Scaled_input)[0]

    if prediction ==1:
        st.error("⚠️ High Risk of Heart Disease") 
    else:
        st.success("✅ Low Risk of Heart Disease")