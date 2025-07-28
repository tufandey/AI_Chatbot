# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Step 1: Import libraries
import os
import streamlit as st
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_community.tools.tavily_search import TavilySearchResults

# Step 2: Read API keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Step 3: Streamlit UI Setup
st.set_page_config(page_title="🤖 TufanBot", layout="centered")
st.title("🤖 TufanBot - Your Friendly AI Chat Companion")
st.write("💬 Chat, Chill, and Ask Me Anything!")

# Fixed model (llama-3.3-70b-versatile only)
selected_model = "llama-3.3-70b-versatile"

# System prompt input
system_prompt = st.text_area(
    "🧠 Define your AI Agent (e.g., Financial Analyst, Doctor, Teacher):",
    height=70,
    placeholder="Type your system prompt here..."
)

# Optional web search
allow_web_search = st.checkbox("🌐 Allow Web Search")

# User query input
user_query = st.text_area("✍️ Enter your query:", height=150, placeholder="Ask anything!")

# Ask button logic
if st.button("Ask Tufan!"):
    if user_query.strip():
        try:
            status = st.empty()
            status.info("🔄 Thinking...")

            # Initialize LLM and tools
            llm = ChatGroq(model=selected_model)
            tools = [TavilySearchResults(max_results=2)] if allow_web_search else []

            # Create AI agent
            agent = create_react_agent(
                model=llm,
                tools=tools,
                state_modifier=system_prompt
            )

            # Send user query
            state = {"messages": user_query}
            result = agent.invoke(state)
            messages = result.get("messages", [])
            ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

            status.empty()  # Hide "Thinking..." message

            # Show result
            if ai_messages:
                st.subheader("🤖 TufanBot says:")
                st.markdown(f"**{ai_messages[-1]}**")
            else:
                st.warning("⚠️ No response received.")

        except Exception as e:
            status.empty()
            st.error(f"💥 Error: {e}")
