import streamlit as st
import pickle

def app():
    # loading the saved model
    diabetes_model = pickle.load(open('Model/dia_model.pkl', 'rb'))

    # diabetes form
    # page title
    st.title('Sri Lanka Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        try:
            Pregnancies = float(st.text_input('Number of your pregnancies'))
        except ValueError:
            st.error('Invalid input for Pregnancies. Please enter a valid number.')
            return

    with col2:
        try:
            Glucose = float(st.text_input('Your Glucose Level'))
        except ValueError:
            st.error('Invalid input for Glucose. Please enter a valid number.')
            return

    with col3:
        try:
            BloodPressure = float(st.text_input('Your Blood Pressure Value'))
        except ValueError:
            st.error('Invalid input for Blood Pressure. Please enter a valid number.')
            return

    with col1:
        try:
            SkinThickness = float(st.text_input('Your Skin Thickness'))
        except ValueError:
            st.error('Invalid input for Skin Thickness. Please enter a valid number.')
            return

    with col2:
        try:
            Insulin = float(st.text_input('Your Insulin Level'))
        except ValueError:
            st.error('Invalid input for Insulin. Please enter a valid number.')
            return

    with col3:
        try:
            BMI = float(st.text_input('Your BMI'))
        except ValueError:
            st.error('Invalid input for BMI. Please enter a valid number.')
            return

    with col1:
        try:
            DiabetesPedigreeFunction = float(st.text_input('Diabetes Pedigree Function'))
        except ValueError:
            st.error('Invalid input for Diabetes Pedigree Function. Please enter a valid number.')
            return

    with col2:
        try:
            Age = float(st.text_input('Your Age'))
        except ValueError:
            st.error('Invalid input for Age. Please enter a valid number.')
            return

    # code for the prediction
    Diabetes_diagnosis = ''

    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        Diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if Diabetes_prediction[0] == 1:
            Diabetes_diagnosis = 'The Person has Diabetes'
            st.warning(Diabetes_diagnosis)
        elif Diabetes_prediction[0] == 0:
            Diabetes_diagnosis = 'The Person does not have Diabetes'
            st.success(Diabetes_diagnosis)
        else:
            Diabetes_diagnosis = 'Invalid prediction value'
            st.info(Diabetes_diagnosis)



