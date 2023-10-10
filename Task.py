# Import necessary libraries
import streamlit as st
from firebase_admin import credentials, firestore, auth

# Initialize Firestore client
db = firestore.client()

def app():
    st.title('To-Do List App')

    # Check if the user is logged in
    if st.session_state.username:
        user_id = st.session_state.username
        user = auth.get_user(user_id)
        st.write(f'Welcome, {user.email}!')
        # Create a form to add tasks
        task = st.text_input('Add a new task:')
        if st.button('Add Task') and task:
            # Add the task to Firestore
            task_data = {'user_id': user_id, 'task': task}
            db.collection('tasks').add(task_data)
            st.success('Task added successfully!')

        # Fetch tasks from Firestore
        tasks_ref = db.collection('tasks').where('user_id', '==', user_id).stream()
        task_data = [task.to_dict() for task in tasks_ref]

        if task_data:
            st.write('Your To-Do List:')
            # Display tasks in a table with edit and delete buttons
            table_data = []
            for task_item in task_data:
                task_text = task_item['task']
                edit_button = st.button(f'Edit ({task_text})')
                delete_button = st.button(f'Delete ({task_text})')

                if edit_button:
                    # Implement the edit functionality here (e.g., open an input field for editing)
                    edited_task = st.text_input(f'Edit task: {task_text}', task_text)
                    if st.button('Save'):
                        db.collection('tasks').document(task_text).update({'task': edited_task})
                        st.success('Task edited successfully!')

                if delete_button:
                    db.collection('tasks').document(task_text).delete()
                    st.success('Task deleted successfully!')

                table_data.append([task_text])


            # Create a table with the task, edit, and delete columns
            st.table(table_data)
        else:
            st.write('No tasks in your To-Do List.')
    else:
        st.warning('You must log in to use the To-Do List.')


