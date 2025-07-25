import streamlit as st
import requests
import os

# Set your Hugging Face API token (use secrets for real deployments)
API_TOKEN = st.secrets["HUGGINGFACE_API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI
st.title("🗺️ Roadmap Generator – Hugging Face Powered Tool")
st.subheader("Enter a skill you want to learn:")

user_input = st.text_input("Skill", placeholder="e.g. Natural Language Processing")

if st.button("Generate Roadmap"):
    if user_input:
        with st.spinner("Generating roadmap..."):
            prompt = f"Create a personalized step-by-step roadmap to master the skill '{user_input}'. Include free learning resources."
            response = query({"inputs": prompt})
            output = response[0]["generated_text"] if isinstance(response, list) else str(response)
            st.markdown("### 📚 Personalized Roadmap")
            st.markdown(output)
    else:
        st.warning("Please enter a skill.")
