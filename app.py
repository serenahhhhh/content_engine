import streamlit as st
from chatbot_interface import ChatbotInterface  # Import your chatbot logic

# Initialize the chatbot interface
chatbot = ChatbotInterface()

# Streamlit UI settings
st.set_page_config(page_title="Chatbot Interface", layout="centered")

# Main application interface
st.title("Chatbot Messaging Interface")
st.write("Have a conversation with your bot below!")

# Session state to store the conversation
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"sender": "bot", "message": "Hi! How can I assist you today?"}
    ]

# Display the conversation
for chat in st.session_state["messages"]:
    if chat["sender"] == "bot":
        st.markdown(
            f"<div style='text-align: left; background-color: #f1f0f0; padding: 10px; border-radius: 10px;'>"
            f"<strong>Bot:</strong> {chat['message']}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='text-align: right; background-color: #e1f5fe; padding: 10px; border-radius: 10px;'>"
            f"<strong>You:</strong> {chat['message']}</div>",
            unsafe_allow_html=True,
        )

# Input for the user to send a message
user_input = st.text_input("Your message:", key="user_input")

# Handle the message when the user presses enter
if st.button("Send") and user_input.strip():
    # Add the user's message to the conversation
    st.session_state["messages"].append({"sender": "user", "message": user_input})
    
    # Get the bot's response
    bot_response = chatbot.query_engine.query(user_input)  # Replace with your logic
    st.session_state["messages"].append({"sender": "bot", "message": bot_response})

    # Clear the input box after sending
    st.experimental_rerun()
