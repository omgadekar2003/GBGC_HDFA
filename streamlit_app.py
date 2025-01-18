
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
import streamlit as st
from pymongo import MongoClient
import pandas as pd
from PIL import Image
import os

# MongoDB Connection
mongo_uri = st.secrets["MONGO_URI"]
client = MongoClient(mongo_uri)
db = client["GestureGameControl"]  # Database name
feedback_collection = db["feedback"]  # Collection name

# Set page configuration and sidebar
st.set_page_config(page_title="Gesture Based Game Control", page_icon="🎮", layout="wide")
st.sidebar.title("Gesture Based Game Control")
st.sidebar.image("IMG-20241020-WA0001.jpg", use_container_width=True)  # Add a logo at the top of the sidebar

# Use radio buttons for page selection
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Install Manual & Download Code", "Feedback", "About Us"],
    index=0,
)

# Home Page
if page == "Home":
    st.title("🎮 Gesture Based Game Control 🎮")
    st.subheader("Effortlessly control games with just your hand gestures!")
    st.markdown(
        """
        This project allows you to control popular games using hand gestures detected by your camera.
        Enjoy a hands-free gaming experience with Python, OpenCV, and MediaPipe.
        """
    )

    # YouTube Video
    st.write("---")
    st.video("https://youtu.be/QMc6YheYKl0?si=iRq3qXVLEVgQTnPe")
    st.write("---")

# Install Manual & Download Code Page
elif page == "Install Manual & Download Code":
    st.title("📥 Install Manual & Download Code")
    st.markdown("### Follow these instructions to set up Gesture Based Game Control:")
    instructions = [
        "1. Install Python",
        "2. Install OpenCV: `pip install opencv-python`",
        "3. Install MediaPipe: `pip install mediapipe`",
        "4. Install Pynput for MAC OR LINUX only: `pip install pynput`",
        "5. Install ctypes (pre-installed with Python)",
        "6. See Game Playing Video to understand Gestures"
    ]
    for step in instructions:
        st.write(step)

    # Load and provide the zip files for download
    with open("GBGC.zip", "rb") as windows_file:
        windows_data = windows_file.read()
    
    with open("MAC code.zip", "rb") as mac_file:
        mac_data = mac_file.read()
    
    with open("Linux Code.zip", "rb") as linux_file:
        linux_data = linux_file.read()

    # Add download buttons for each platform
    st.markdown("#### Choose your platform to download the code:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(
            label="📥 Download Windows Code",
            data=windows_data,
            file_name="GBGC.zip",
            mime="application/zip",
            help="Download the source code for Windows."
        )
    
    with col2:
        st.download_button(
            label="📥 Download macOS Code",
            data=mac_data,
            file_name="MAC code.zip",
            mime="application/zip",
            help="Download the source code for macOS."
        )
    
    with col3:
        st.download_button(
            label="📥 Download Linux Code",
            data=linux_data,
            file_name="Linux Code.zip",
            mime="application/zip",
            help="Download the source code for Linux."
        )
    st.write("---")



# Feedback Page
elif page == "Feedback":
    st.title("📝 Feedback 📝")
    st.write("We value your feedback on the Gesture Based Game Control application.")

    # Feedback form
    with st.form("feedback_form"):
        email = st.text_input("📧 Email")
        rating = st.slider("⭐ Rate Us", 1, 5, 3)
        like_it = st.checkbox("👍 I like this app!")
        suggestions = st.text_area("💡 Suggestions/Your Experience (max 60 words)", max_chars=60)
        submitted = st.form_submit_button("Submit")

        if submitted:
            feedback = {
                "email": email,
                "rating": rating,
                "like_it": like_it,
                "suggestions": suggestions
            }
            feedback_collection.insert_one(feedback)
            st.success("Thank you for your feedback!")

    # Displaying feedback from MongoDB
    st.write("---")
    st.write("### User Feedback")
    feedback_docs = feedback_collection.find()
    feedback_list = [{"Email": doc["email"], "Rating": doc["rating"], "Liked": doc["like_it"], "Suggestions": doc["suggestions"]} for doc in feedback_docs]
    feedback_df = pd.DataFrame(feedback_list)
    st.dataframe(feedback_df)

# About Us Page
elif page == "About Us":
    st.title("👥 About Us")

    st.write("## Meet the Developers")

    col1, col2 = st.columns(2)

    # Developer 1
    with col1:
        st.write("### Om Gadekar")
        om_image = Image.open("1000017801_11zon.jpg").resize((150, 150))  # Adjust image size
        st.image(om_image, use_container_width=False, width=150, caption="Om Gadekar", output_format="PNG", clamp=True)
        

    # Developer 2
    with col2:
        st.write("### Aniket Chopde")
        aniket_image = Image.open("IMG-20241107-WA0001.jpg").resize((150, 150))  # Adjust image size
        st.image(aniket_image, use_container_width=False, width=150, caption="Aniket Chopde", output_format="PNG", clamp=True)

    st.write("---")

    # Guide and College Information
    st.write("## Guide")
    st.write("🎓 Prof. P. A. Bhalekar")

    st.write("## College")
    st.write("🏫 Deogiri Institute of Engineering and Management Studies (DIEMS)")
    college_image = Image.open("deogiri.png").resize((150, 150))
    st.image(college_image, use_container_width=False, width=150, output_format="PNG", clamp=True)

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2024 Gesture Based Game Control Project")


