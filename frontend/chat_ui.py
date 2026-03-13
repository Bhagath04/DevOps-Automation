import streamlit as st
import requests

st.title("DevSecOps AI Assistant")

question = st.text_input("Ask DevSecOps Question")

if st.button("Ask"):
    response = requests.post(
        "http://localhost:8000/ask",
        params={"question": question}
    )
    answer = response.json()["answer"]
    st.write(answer)
