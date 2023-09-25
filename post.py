import streamlit as st
from firebase_admin import firestore


def app():
    st.subheader("🤩 Send us your warm message about your life style ")
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db = firestore.client()
    st.session_state.db = db

    ph = ''
    if st.session_state.username == '':
        ph = 'Login to be able to post!!'
    else:
        ph = 'Post your thought'

    post = st.text_area(label=' :orange[+ New Post]', placeholder=ph, height=None, max_chars=500)

    if st.button('Post', use_container_width=20):
        if post != '':
            username = st.session_state.username

            # Check if the user has already posted
            user_doc = db.collection('Posts').document(username).get()
            if user_doc.exists:
                user_data = user_doc.to_dict()
                if 'Content' in user_data.keys():
                    # User has already posted, update the content
                    updated_content = user_data['Content'] + [post]
                    db.collection('Posts').document(username).update({'Content': updated_content})
                else:
                    # User has posted for the first time
                    data = {"Content": [post], 'Username': username}
                    db.collection('Posts').document(username).set(data)
            else:
                # User has posted for the first time
                data = {"Content": [post], 'Username': username}
                db.collection('Posts').document(username).set(data)

            st.success('Post uploaded!!')

    st.header(' :violet[Latest Posts] ')

    docs = db.collection('Posts').get()

    for doc in docs:
        d = doc.to_dict()
        try:
            # Allow users to edit their own posts
            if st.session_state.username == d['Username']:
                edited_post = st.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']),
                                           value=d['Content'][-1], height=20)
                if st.button(f'Update Post by {d["Username"]}'):
                    updated_content = d['Content'][:-1] + [edited_post]
                    db.collection('Posts').document(d['Username']).update({'Content': updated_content})
                    st.success('Post updated!!')
                else:
                    st.write("You can edit your post above.")
            else:
                st.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']),
                             value=d['Content'][-1], height=20)
        except:
            pass
