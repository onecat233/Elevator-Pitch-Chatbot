import io
import requests
import streamlit as st
from openai import OpenAI
from elevenlabs.client import ElevenLabs

# -----------------------------------------------------------------------------
# Configuration: Replace with your own keys and settings
# -----------------------------------------------------------------------------
openai_api_key = "YOUR_OPENAI_API"
elevenlabs_api_key = "YOUR_EVEVENLABS_API"
vadoo_api_key = "YOUR_VADOO_API"
tts_voice_id = "JBFqnCBsd6RMkjVDRZzb"       # Replace with your ElevenLabs voice ID
tts_model_id = "eleven_multilingual_v2" 

# Initialize OpenAI and ElevenLabs clients
client = OpenAI(api_key=openai_api_key)
tts_client = ElevenLabs(api_key=elevenlabs_api_key)

# -----------------------------------------------------------------------------
# Streamlit App Title and Description
# -----------------------------------------------------------------------------
st.title("💬 Elevator Pitch Chatbot with Pitch Video and Human-like Speech!")
st.write(
    """
    Welcome to Pitch Like a Pro! Simply type your product idea into the chat box,
    and our agent will generate an engaging, concise elevator pitch for you – 
    then convert it to PITCH VIDEO with human-like SPEECH!
    """
)

# -----------------------------------------------------------------------------
# Chat Session State Initialization
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -----------------------------------------------------------------------------
# Chat Input: Process each input as a product idea
# -----------------------------------------------------------------------------
user_input = st.chat_input("Enter your product idea:")

if user_input:
    # Append and display the user’s message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Generate the Elevator Pitch Text using OpenAI
    template = (
        "You are a creative and persuasive copywriter and the audience are experts in Computer Science. Now you have the markdown format introduction of your project." 
        "Generate an elevator pitch under 50 seconds for the following product idea: {product_idea}. "
        "The pitch should be engaging, concise, professonal, and the contents should include: inspiration of this project, functions and competitive edges, crucial skills invloved, conclusion and calling on actions."
        "Attention: Avoid incomplete sentences."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": template.format(product_idea=user_input)}],
        max_tokens=150,
        temperature=0.7,
    )
    pitch = response.choices[0].message.content.strip()

    st.session_state.messages.append({"role": "assistant", "content": pitch})
    st.chat_message("assistant").write(pitch)

    # Convert the Pitch Text to Audio Using ElevenLabs TTS API
    try:
        # Convert text to audio stream
        audio_stream = tts_client.text_to_speech.convert_as_stream(
            text=pitch,
            voice_id=tts_voice_id,
            model_id=tts_model_id,
        )

        # Concatenate audio chunks
        audio_bytes = b""
        for chunk in audio_stream:
            if isinstance(chunk, bytes):
                audio_bytes += chunk

        # Save the audio file for the video generation
        audio_file_path = "output.mp3"
        with open(audio_file_path, "wb") as f:
            f.write(audio_bytes)

        # Check if audio is valid
        if audio_bytes:
            # Use BytesIO to pass audio bytes
            st.audio(io.BytesIO(audio_bytes), format="audio/mp3")

            # Generate Video Using Vadoo API
            try:
                vadoo_url = "https://viralapi.vadoo.tv/api/generate_video"
                headers = {
                    "X-API-KEY": vadoo_api_key
                }
                data = {
                    "topic": "Custom",
                    "script": user_input, 
                    "voice": "Charlie voice",
                    "theme": "Hormozi_1",
                    "style": "None",
                    "language": "English",
                    "duration": "30-60",
                    "aspect_ratio": "9:16",
                    "use_ai": "0",
                    "url": "https://webhook.site/d3e18fde-60b2-4f7e-9ef3-c19317bab145"
                }
                files = {"audio": open(audio_file_path, "rb")}

                response = requests.post(vadoo_url, headers=headers, data=data, files=files)

                if response.status_code == 200:
                    st.success("Your request has been submitted successfully!")
                    st.write(
                       
                        """
                        The video generation process will take approximately **5 minutes**.  
                        **Step 1**: Click the link below, then click "View in Webhook.site".  
                        **Step 2**: Find your ticket based on the submission time (usually the first one at the top).  
                        **Step 3**: Once the POST request appears, find the URL in the response and open it to enjoy your video!  
                        """
                    )
                    st.markdown(
                        "[Go to the Webhook Page to View Your Video](https://webhook.site/d3e18fde-60b2-4f7e-9ef3-c19317bab145)",
                        unsafe_allow_html=True,
                    )
                else:
                    st.error(f"Failed to generate video. Status Code: {response.status_code}")
                    st.error(f"Response: {response.text}")

            except Exception as e:
                st.error(f"Error generating video: {str(e)}")

        else:
            st.error("Failed to generate audio. Please try again.")

    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")
