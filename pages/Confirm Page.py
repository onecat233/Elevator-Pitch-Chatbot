import streamlit as st

def main():
    st.set_page_config(page_title="Elevator Pitch Confirm Page", page_icon="🚀")
    
    st.title("Elevator Pitch Confirm Page")
    
    st.write(
        """Are you an engineer with a great idea but struggle to pitch it confidently due to shyness or language barriers?"
        Introducing our solution - a website where you can input your idea details and receive a professionally crafted elevator pitch or even a pitch video advertisement with voiceover!
        With our tool, you can effectively communicate your ideas to potential investors or judges at hackathons, increasing your chances of success.
        Don't let nervousness or language barriers hold you back from achieving your goals. Try our platform today and start pitching with confidence!"""
    )

if __name__ == "__main__":
    main()
