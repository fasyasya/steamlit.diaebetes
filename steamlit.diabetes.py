import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav' , 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    pregnancies = st.text_input ('input nilai pregnancies')

with col2 :
    Glucose = st.text_input ('input nilai Glucose')

with col1 :
    Bloodpressure = st.text_input ('input nilai Blood Pressure')

with col2 :
    skinThickness = st.text_input ('input nilai Skin Thickness')

with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    