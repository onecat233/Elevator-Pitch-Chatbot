import streamlit as st

st.title("Elevator Pitch Confirm Page")

# Attempt to read the latest pitch from the shared file
try:
    with open("blog_content.txt", "r") as f:
        blog_content = f.read()
    st.write(blog_content)
except FileNotFoundError:
    st.write("No pitch generated yet. Submit a product idea on the main page!")
