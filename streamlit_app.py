# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd

# # MongoDB Connection
# mongo_uri = st.secrets["MONGO_URI"]
# client = MongoClient(mongo_uri)
# db = client["GestureGameControl"]  # Database name
# feedback_collection = db["feedback"]  # Collection name

# # Main App Title
# st.set_page_config(page_title="GESTURE BASED GAME CONTROL", page_icon="🎮")
# st.sidebar.title("GESTURE BASED GAME CONTROL")
# page = st.sidebar.selectbox("Choose a page", ["Home", "Install Manual/Download Code", "Feedback", "About Us"])

# # Home Page
# if page == "Home":
#     st.title("Gesture Based Game Control")
#     st.subheader("Control games effortlessly with just hand gestures!")
#     st.write("This project allows you to control popular games using hand gestures detected by your camera.")
#     st.write("With this app, you can enjoy hands-free gaming experience using Python, OpenCV, and MediaPipe.")

#     # Embed YouTube Video
#     video_url = "https://youtu.be/QMc6YheYKl0?si=iRq3qXVLEVgQTnPe"
#     st.video(video_url, start_time=0)

# # Install Manual / Download Code Page
# elif page == "Install Manual/Download Code":
#     st.title("Install Manual & Download Code")
#     st.write("### Installation Instructions:")
#     st.write("1. Install Python")
#     st.write("2. Install OpenCV: `pip install opencv-python`")
#     st.write("3. Install MediaPipe: `pip install mediapipe`")
#     st.write("4. Install PyAutoGUI: `pip install pyautogui`")
#     st.write("5. Install ctypes (comes pre-installed with Python)")

#     # Download button
#     download_url = "https://github.com/yourusername/yourrepo/archive/main.zip"
#     st.markdown(f"[Download Code](https://github.com/yourusername/yourrepo/archive/main.zip)", unsafe_allow_html=True)

# # Feedback Page
# elif page == "Feedback":
#     st.title("Feedback")
#     st.write("Please provide your feedback on the Gesture Based Game Control application.")

#     # Feedback Form
#     with st.form("feedback_form"):
#         email = st.text_input("Email")
#         rating = st.slider("Rate Us", 1, 5, 3)
#         like_it = st.checkbox("I like this app!")
#         suggestions = st.text_area("Suggestions (max 60 words)", max_chars=60)
#         submitted = st.form_submit_button("Submit")

#         if submitted:
#             feedback = {
#                 "email": email,
#                 "rating": rating,
#                 "like_it": like_it,
#                 "suggestions": suggestions
#             }
#             feedback_collection.insert_one(feedback)
#             st.success("Thank you for your feedback!")

#     # Displaying Feedback from MongoDB
#     st.write("### User Feedback")
#     feedback_docs = feedback_collection.find()
#     feedback_list = [{"Email": doc["email"], "Rating": doc["rating"], "Liked": doc["like_it"], "Suggestions": doc["suggestions"]} for doc in feedback_docs]
#     feedback_df = pd.DataFrame(feedback_list)
#     st.write(feedback_df)

# # About Us Page
# elif page == "About Us":
#     st.title("About Us")
#     st.write("## Developers")
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write("### OM GADEKAR (B.Tech CSE)")
#         st.image("path/to/om_image.jpg")
#     with col2:
#         st.write("### ANIKET CHOPDE (B.Tech CSE)")
#         st.image("path/to/aniket_image.jpg")

#     st.write("## Guide")
#     st.write("Prof. P. A. Bhalekar")

#     st.write("## College")
#     st.write("DIEMS")
#     st.image("path/to/college_logo.jpg")

#----------------------------------------------------------------------------
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os

# MongoDB Connection
mongo_uri = st.secrets["MONGO_URI"]
client = MongoClient(mongo_uri)
db = client["GestureGameControl"]  # Database name
feedback_collection = db["feedback"]  # Collection name

# Main App Title
st.set_page_config(page_title="GESTURE BASED GAME CONTROL", page_icon="🎮")
st.sidebar.title("GESTURE BASED GAME CONTROL")
page = st.sidebar.selectbox("Choose a page", ["Home", "Install Manual/Download Code", "Feedback", "About Us"])

# Home Page
if page == "Home":
    st.title("Gesture Based Game Control")
    st.subheader("Control games effortlessly with just hand gestures!")
    st.write("This project allows you to control popular games using hand gestures detected by your camera.")
    st.write("With this app, you can enjoy a hands-free gaming experience using Python, OpenCV, and MediaPipe.")

    # Embed YouTube Video
    video_url = "https://youtu.be/QMc6YheYKl0?si=iRq3qXVLEVgQTnPe"
    st.video(video_url, start_time=0)

# Install Manual / Download Code Page
elif page == "Install Manual/Download Code":
    st.title("Install Manual & Download Code")
    st.write("### Installation Instructions:")
    st.write("1. Install Python")
    st.write("2. Install OpenCV: `pip install opencv-python`")
    st.write("3. Install MediaPipe: `pip install mediapipe`")
    st.write("4. Install PyAutoGUI: `pip install pyautogui`")
    st.write("5. Install ctypes (comes pre-installed with Python)")

    # Download button for code
    download_file_path = "path/to/your_code.zip"  # Replace with the actual path to your compressed code file
    if os.path.exists(download_file_path):  # Check if the file exists
        with open(download_file_path, "rb") as f:
            st.download_button(
                label="Download Code",
                data=f,
                file_name="GBGC.zip",  # The name for the downloaded file
                mime="application/zip"
            )
    else:
        st.error("Code download file not found. Please check the path.")

# Feedback Page
elif page == "Feedback":
    st.title("Feedback")
    st.write("Please provide your feedback on the Gesture Based Game Control application.")

    # Feedback Form
    with st.form("feedback_form"):
        email = st.text_input("Email")
        rating = st.slider("Rate Us", 1, 5, 3)
        like_it = st.checkbox("I like this app!")
        suggestions = st.text_area("Suggestions (max 60 words)", max_chars=60)
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

    # Displaying Feedback from MongoDB
    st.write("### User Feedback")
    feedback_docs = feedback_collection.find()
    feedback_list = [{"Email": doc["email"], "Rating": doc["rating"], "Liked": doc["like_it"], "Suggestions": doc["suggestions"]} for doc in feedback_docs]
    feedback_df = pd.DataFrame(feedback_list)
    st.write(feedback_df)

# About Us Page
elif page == "About Us":
    st.title("About Us")
    st.write("## Developers")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### OM GADEKAR (B.Tech CSE)")
        st.image("1000017801_111zon.jpg.jpg")  # Ensure this path is correct
    with col2:
        st.write("### ANIKET CHOPDE (B.Tech CSE)")
        st.image("IMG_20241103_143437.jpg")  # Ensure this path is correct

    st.write("## Guide")
    st.write("Prof. P. A. Bhalekar")

    st.write("## College")
    st.write("DIEMS")
    st.image("path/to/college_logo.jpg")  # Ensure this path is correct


