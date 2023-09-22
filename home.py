import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


def app ():


    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("styles/style.css")

    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    img_contact_form = Image.open("images/diabties.jpg")
    img_lottie_animation = Image.open("images/diabtic 2.jpg")
    img_dia = Image.open("images/foods.png")

    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Welcome to Diapredict! 🌟 :wave:")
        st.title("A prediction expert in Sri Lanka ")
        st.write(
            "At Diapredict, we're on a mission to empower individuals with diabetes to live their healthiest, happiest lives. 🌱💪"
        )
        st.write("[Learn More >](https://pythonandvba.com)")

    # ---- WHAT I DO ----
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("👁️‍🗨️ What We Do")
            st.write("##")
            st.write(
                """
                📈 Diabetes Prediction Using ML: Our cutting-edge machine learning technology analyzes your health data to predict your diabetes risk, helping you take proactive steps towards prevention.
                - 🍏 Maintain a Healthy Lifestyle: Discover a treasure trove of lifestyle tips, from nutritious recipes to exercise routines, specially tailored to support your journey to a healthier you
                - 🤝 Community and Support: Connect with a supportive community of individuals who understand your challenges and triumphs. Share your experiences, ask questions, and find inspiration.
                -  Welcome to a world where managing diabetes is not just a task, but a fulfilling lifestyle. 🌍
                -  Let's emark on this journey together! 🚀💙
                -    Remember, with Diapredict, your health is in your hands. 🤗
                """
            )
            st.write("[YouTube Channel >](https://youtube.com/playlist?list=PLwKZdOHmwfHGSl9h21oM_B3OCP-7lGqCw&si=63hA5xtcIUkQ5H7J)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    with st.container():
        st.write("---")
        st.header("Our Service ")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("📚 Educational Resources:")
            st.write(
                """
                 Dive into a wealth of educational content, including articles, videos, and expert advice, all aimed at helping you better understand diabetes and how to manage it effectively.
                """
            )
            st.markdown("[Watch Video...](https://youtube.com/playlist?list=PLwKZdOHmwfHGSl9h21oM_B3OCP-7lGqCw&si=63hA5xtcIUkQ5H7J)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("🔔 Personalized Insights: ")
            st.write(
                """
                Receive personalized recommendations based on your unique health profile, making it easier than ever to make informed choices for your well-being..
                """
            )
            st.markdown("[Watch Video...](https://youtube.com/playlist?list=PLwKZdOHmwfHGSl9h21oM_B3OCP-7lGqCw&si=63hA5xtcIUkQ5H7J)")
#projec
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_dia)
        with text_column:
            st.subheader("🌟 Stay Inspired: ")
            st.write(
                """
                Our success stories and motivational content will keep you inspired and motivated on your journey to better health.
                """
            )
            st.markdown("[Watch Video...](https://youtube.com/playlist?list=PLwKZdOHmwfHGSl9h21oM_B3OCP-7lGqCw&si=63hA5xtcIUkQ5H7J)")


    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/yongofficialvs@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()