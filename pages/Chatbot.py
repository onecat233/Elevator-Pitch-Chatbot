import streamlit as st
from openai import OpenAI
from langchain.prompts import PromptTemplate

# -----------------------------------------------------------------------------
# Configuration: Replace with your own API key
# -----------------------------------------------------------------------------
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


# -----------------------------------------------------------------------------
# App Title and Description
# -----------------------------------------------------------------------------
st.title("💬 Elevator Pitch Chatbot")
st.write(
    """
    Welcome to Pitch Like a Pro! Simply type in your product idea into the chat box,
    and our agent will automatically generate an engaging, concise elevator pitch for you.
    """
)

# -----------------------------------------------------------------------------
# Initialize Chat Session State
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -----------------------------------------------------------------------------
# Chat Input: All user input is treated as a product idea
# -----------------------------------------------------------------------------
user_input = st.chat_input("Type your product idea here:")

if user_input:
    if not openai_api_key:
        st.info("🚨 Please enter your OpenAI API key in the sidebar to continue.")
        st.stop()
    client = OpenAI(api_key=openai_api_key)

    # Append and display the user’s message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Define the elevator pitch prompt template
    template = (
        "You are a creative and persuasive copywriter and the audience are experts and participates of Hackathon. Now you have the markdown format introduction of your project." 
        "Generate an elevator pitch under 50 seconds for the following product idea: {product_idea}. "
        "The pitch should be engaging, concise, professonal, and the contents should include: inspiration of this project, functions and competitive edges, crucial skills invloved, conclusion and calling on actions."
        "Attention: Do not occur words such as 'Introducing' and just output what can be read in the video."
    )
    pitch_template = PromptTemplate(input_variables=["product_idea"], template=template)
    formatted_prompt = pitch_template.format(product_idea=user_input)

    # Call the OpenAI API with the formatted prompt to get the pitch
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": formatted_prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    pitch = response.choices[0].message.content.strip()

    # Append and display the generated elevator pitch
    st.session_state.messages.append({"role": "assistant", "content": pitch})
    st.chat_message("assistant").write(pitch)
