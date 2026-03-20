import streamlit as st

# Initialize session state to keep track of conversation history
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Chatbot Interface")

user_input = st.text_input("You:", "")

if user_input:
    # Simulate a bot response (replace with actual bot function)
    response = f"Bot: Responding to '{user_input}'"
    # Save both user input and bot response to history
    st.session_state.history.append((user_input, response))

# Display conversation history
if st.session_state.history:
    st.subheader("Conversation History:")
    for user_msg, bot_msg in st.session_state.history:
        st.write(f"You: {user_msg}")
        st.write(f"{bot_msg}")
