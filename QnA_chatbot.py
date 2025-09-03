from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Chat-Bot")
st.header("Chat-Bot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display chat messages from history on app rerun
for role, text in st.session_state['chat_history']:
    with st.chat_message(role):
        st.write(text)

# Handle user input and get a new response
if "input" not in st.session_state:
    st.session_state.input = ""

if st.session_state.input:
    user_input = st.session_state.input
    
    # Append user message to chat history and display it
    st.session_state['chat_history'].append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get bot response and stream it
    response = get_gemini_response(user_input)
    
    # Create a message placeholder for the bot's response
    with st.chat_message("assistant"):
        full_response = ""
        placeholder = st.empty()
        for chunk in response:
            full_response += chunk.text
            placeholder.write(full_response + "▌")  # Add blinking cursor effect
        placeholder.write(full_response)
        
    # Append bot's full response to chat history
    st.session_state['chat_history'].append(("assistant", full_response))
    st.session_state.input = "" # Clear the input box after submission

# Display the input box and button at the end
# Use st.form to group the input and button and process them together
with st.form(key='my_form', clear_on_submit=True):
    user_input = st.text_input("Input: ", key="input", label_visibility="collapsed")
    submit = st.form_submit_button("Ask the question")