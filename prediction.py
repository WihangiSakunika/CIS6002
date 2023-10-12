import streamlit as st
import pickle

import firebase_admin
from firebase_admin import credentials, firestore
import test
import numpy as np

db = firestore.client()

def generate_pdf(details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=details)
    return pdf.output(dest='S').encode('latin1')

def app():
    # Loading the saved model
    diabetes_model = pickle.load(open('Model/dia_model.pkl', 'rb'))

    # Page title
    st.title('Sri Lanka Diabetes Prediction')
    if st.session_state.username:

        # Getting the input data from the user
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

        # Code for the prediction
        Diabetes_diagnosis = ''
        Diabetes_details = ''

        # Creating a button for prediction
        if st.button('Diabetes Test Result'):
            Diabetes_prediction = diabetes_model.predict(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if Diabetes_prediction[0] == 1:
                Diabetes_diagnosis = 'The Person has Diabetes'
                st.warning(Diabetes_diagnosis)  # Display a red warning alert
                if st.button('Print Prediction Result as PDF'):
                    pdf_data = generate_pdf(Diabetes_details)  # Generate the PDF content
                    st.download_button('Download PDF', pdf_data, key='download_pdf')

                # Convert the NumPy array to a Python list
                Diabetes_prediction_list = Diabetes_prediction.tolist()

                # Store input data and prediction details in Firestore
                input_data = {
                    'Pregnancies': Pregnancies,
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'SkinThickness': SkinThickness,
                    'Insulin': Insulin,
                    'BMI': BMI,
                    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                    'Age': Age,
                }

                # Store prediction details in Firestore
                prediction_data = {
                    'result': 'The Person has Diabetes',
                    'details': Diabetes_prediction_list,
                    'input_data': input_data
                }
                db.collection('predictions').add(prediction_data)

            elif Diabetes_prediction[0] == 0:
                Diabetes_diagnosis = 'The Person does not have Diabetes'
                st.success(Diabetes_diagnosis)  # Display a green success alert
                if st.button('Print Prediction Result as PDF'):
                    pdf_data = generate_pdf(Diabetes_details)  # Generate the PDF content
                    st.download_button('Download PDF', pdf_data, key='download_pdf')

                # Convert the NumPy array to a Python list
                Diabetes_prediction_list = Diabetes_prediction.tolist()
                input_data = {
                    'Pregnancies': Pregnancies,
                    'Glucose': Glucose,
                    'BloodPressure': BloodPressure,
                    'SkinThickness': SkinThickness,
                    'Insulin': Insulin,
                    'BMI': BMI,
                    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
                    'Age': Age,
                }

                # Store prediction details in Firestore
                prediction_data = {
                    'result': 'The Person does not have Diabetes',
                    'details': Diabetes_prediction_list,
                    'input_data': input_data
                }
                db.collection('predictions').add(prediction_data)



