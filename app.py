import streamlit as st
from ctransformers import AutoModelForCausalLM

# Load the Llama-2 model
@st.cache_resource
def load_model():
    return AutoModelForCausalLM.from_pretrained(
        "model",
        model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        config={"max_new_tokens": 512, "temperature": 0.7}
    )

model = load_model()

# Streamlit UI
st.title("🗺️ Roadmap Generator – Llama2 Powered Tool")
st.subheader("Enter a skill you want to learn:")

user_input = st.text_input("Skill", placeholder="e.g. Machine Learning")

if st.button("Generate Roadmap"):
    if user_input:
        with st.spinner("Generating roadmap..."):
            prompt = f"Generate a step-by-step learning roadmap for mastering {user_input}. Include free resources."
            output = model(prompt)
            st.markdown("### 📚 Personalized Roadmap")
            st.markdown(output)
    else:
        st.warning("Please enter a skill.")