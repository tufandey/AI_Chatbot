# Load environment variables if not using pipenv
from dotenv import load_dotenv
load_dotenv()

# Step 1: Setup UI with Streamlit
import streamlit as st

st.set_page_config(page_title="Hey Tufan!", layout="centered")
st.title("🤖 TufanBot - Your Friendly AI Chat Companion")
st.write("💬 Chat, Chill, and Ask Me Anything!")

# System prompt setup
system_prompt = st.text_area(
    "🧠 Define your AI Agent (e.g., Financial Analyst, Doctor, Teacher):",
    height=70,
    placeholder="Type your system prompt here..."
)

# Groq models only
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
provider = "Groq"  # Fixed provider

selected_model = st.selectbox("🦙 Select Groq Model:", MODEL_NAMES_GROQ)

# Web search toggle
allow_web_search = st.checkbox("🌐 Allow Web Search")

# Query input
user_query = st.text_area("✍️ Enter your query:", height=150, placeholder="Ask Anything!")

# API endpoint (FastAPI)
API_URL = "http://127.0.0.1:9999/chat"

# Button to send query
if st.button("Ask Tufan!"):
    if user_query.strip():
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(f"🚫 {response_data['error']}")
                else:
                    st.subheader("🤖 TufanBot says:")
                    st.markdown(f"**{response_data}**")
            else:
                st.error("❌ Failed to get a valid response from the backend.")
        except Exception as e:
            st.error(f"💥 Error connecting to backend: {e}")
