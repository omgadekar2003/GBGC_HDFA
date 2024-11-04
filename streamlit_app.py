
# #----------------------------------------------------------------------------
# #----------------------------------------------------------------------------
# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd
# from PIL import Image
# import os

# # MongoDB Connection
# mongo_uri = st.secrets["MONGO_URI"]
# client = MongoClient(mongo_uri)
# db = client["GestureGameControl"]  # Database name
# feedback_collection = db["feedback"]  # Collection name

# # Set page configuration and sidebar
# st.set_page_config(page_title="Gesture Based Game Control", page_icon="🎮", layout="wide")
# st.sidebar.title("Gesture Based Game Control")
# st.sidebar.image("IMG-20241020-WA0001.jpg", use_column_width=True)  # Add a logo at the top of the sidebar

# # Use radio buttons for page selection
# page = st.sidebar.radio(
#     "Navigate",
#     ["Home", "Install Manual & Download Code", "Feedback", "About Us"],
#     index=0,
# )

# # Home Page
# if page == "Home":
#     st.title("🎮 Gesture Based Game Control")
#     st.subheader("Effortlessly control games with just your hand gestures!")
#     st.markdown(
#         """
#         This project allows you to control popular games using hand gestures detected by your camera.
#         Enjoy a hands-free gaming experience with Python, OpenCV, and MediaPipe.
#         """
#     )

#     # # YouTube Video
#      st.write("---")
#     # st.video("https://youtu.be/QMc6YheYKl0?si=iRq3qXVLEVgQTnPe")
#     # st.write("---")
# # Page separator
#    #st.write("---")

# # HTML iframe for YouTube video with autoplay enabled
#      video_html = """
#         <iframe width="560" height="315" 
#         src="https://www.youtube.com/embed/QMc6YheYKl0?autoplay=1&mute=1&controls=1&loop=1" 
#         frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
#        """

# # Display the HTML with autoplay in Streamlit
#      st.markdown(video_html, unsafe_allow_html=True)

# # Page separator
# #st.write("---")

# # Install Manual & Download Code Page
# elif page == "Install Manual & Download Code":
#     st.title("📥 Install Manual & Download Code")
#     st.markdown("### Follow these instructions to set up Gesture Based Game Control:")
#     instructions = [
#         "1. Install Python",
#         "2. Install OpenCV: `pip install opencv-python`",
#         "3. Install MediaPipe: `pip install mediapipe`",
#         "4. Install PyAutoGUI: `pip install pyautogui`",
#         "5. Install ctypes (pre-installed with Python)"
#     ]
#     for step in instructions:
#         st.write(step)

#     # Load and provide the zip file for download
#     with open("GBGC.zip", "rb") as file:
#         data = file.read()

#     st.download_button(
#         label="📥 Download Code",
#         data=data,
#         file_name="GBGC.zip",
#         mime="application/zip",
#         help="Download the source code in a zip file."
#     )
#     st.write("---")

# # Feedback Page
# elif page == "Feedback":
#     st.title("📝 Feedback")
#     st.write("We value your feedback on the Gesture Based Game Control application.")

#     # Feedback form
#     with st.form("feedback_form"):
#         email = st.text_input("📧 Email")
#         rating = st.slider("⭐ Rate Us", 1, 5, 3)
#         like_it = st.checkbox("👍 I like this app!")
#         suggestions = st.text_area("💡 Suggestions (max 60 words)", max_chars=60)
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

#     # Displaying feedback from MongoDB
#     st.write("---")
#     st.write("### User Feedback")
#     feedback_docs = feedback_collection.find()
#     feedback_list = [{"Email": doc["email"], "Rating": doc["rating"], "Liked": doc["like_it"], "Suggestions": doc["suggestions"]} for doc in feedback_docs]
#     feedback_df = pd.DataFrame(feedback_list)
#     st.dataframe(feedback_df)

# # About Us Page
# elif page == "About Us":
#     st.title("👥 About Us")

#     st.write("## Meet the Developers")

#     col1, col2 = st.columns(2)

#     # Developer 1
#     with col1:
#         st.write("### Om Gadekar")
#         om_image = Image.open("1000017801_11zon.jpg").resize((150, 150))  # Adjust image size
#         st.image(om_image, use_column_width=False, width=150, caption="Om Gadekar", output_format="PNG", clamp=True)

#     # Developer 2
#     with col2:
#         st.write("### Aniket Chopde")
#         aniket_image = Image.open("IMG_20241103_143437.jpg").resize((150, 150))  # Adjust image size
#         st.image(aniket_image, use_column_width=False, width=150, caption="Aniket Chopde", output_format="PNG", clamp=True)

#     st.write("---")

#     # Guide and College Information
#     st.write("## Guide")
#     st.write("🎓 Prof. P. A. Bhalekar")

#     st.write("## College")
#     st.write("🏫 Deogiri Institute of Engineering and Management Studies (DIEMS)")
#     college_image = Image.open("deogiri.png").resize((150, 150))
#     st.image(college_image, use_column_width=False, width=150, output_format="PNG", clamp=True)

# # Footer
# st.sidebar.write("---")
# st.sidebar.write("© 2024 Gesture Based Game Control Project")



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
st.sidebar.image("IMG-20241020-WA0001.jpg", use_column_width=True)  # Add a logo at the top of the sidebar

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
        "4. Install PyAutoGUI: `pip install pyautogui`",
        "5. Install ctypes (pre-installed with Python)",
        "6. See Game Playing Video to understand Gestures"
    ]
    for step in instructions:
        st.write(step)

    # Load and provide the zip file for download
    with open("GBGC.zip", "rb") as file:
        data = file.read()

    st.download_button(
        label="📥 Download Code 📥",
        data=data,
        file_name="GBGC.zip",
        mime="application/zip",
        help="Download the source code in a zip file."
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
        st.image(om_image, use_column_width=False, width=150, caption="Om Gadekar", output_format="PNG", clamp=True)
        

    # Developer 2
    with col2:
        st.write("### Aniket Chopde")
        aniket_image = Image.open("IMG_20241103_143437.jpg").resize((150, 150))  # Adjust image size
        st.image(aniket_image, use_column_width=False, width=150, caption="Aniket Chopde", output_format="PNG", clamp=True)

    st.write("---")

    # Guide and College Information
    st.write("## Guide")
    st.write("🎓 Prof. P. A. Bhalekar")

    st.write("## College")
    st.write("🏫 Deogiri Institute of Engineering and Management Studies (DIEMS)")
    college_image = Image.open("deogiri.png").resize((150, 150))
    st.image(college_image, use_column_width=False, width=150, output_format="PNG", clamp=True)

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2024 Gesture Based Game Control Project")


