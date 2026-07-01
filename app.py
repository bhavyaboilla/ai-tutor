

import streamlit as st
import google.generativeai as genai

# Load API key safely
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🎓 AI Learning Buddy boilla bhavya")

topic = st.text_input("Enter a topic")

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating..."):
            response = model.generate_content(topic)
            st.write(response.text)
