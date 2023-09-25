# Import necessary libraries
import streamlit as st
from firebase_admin import credentials, firestore, auth

db = firestore.client()

def app():
    st.title('Prediction History')

    if st.session_state.username:
        user_id = st.session_state.username
        user = auth.get_user(user_id)
        st.write(f'Welcome {user.email} for your prediction history')

        # Fetch prediction history from Firestore
        predictions_ref = db.collection('predictions').where('user_id', '==', user_id).stream()
        prediction_data = [prediction.to_dict() for prediction in predictions_ref]

        if prediction_data:
            st.write('Prediction History:')
            st.table(prediction_data)
        else:
            st.write('No prediction history available.')

        if st.button('Logout'):
            auth.logout()
            st.session_state.clear()
            st.experimental_rerun()
    else:
        st.warning('You must log in to view your prediction history.')
