# 🎯 Load environment variables
from dotenv import load_dotenv
load_dotenv()

# 📦 Import libraries
import os
import streamlit as st
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_community.tools.tavily_search import TavilySearchResults

# 🔐 Read API keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# 🎨 Streamlit page configuration
st.set_page_config(page_title="🤖 TufanBot", layout="centered")

# 🖼️ Optional: Add a banner or avatar image
st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80)
st.markdown("<h1 style='text-align: center;'>🤖 TufanBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your friendly AI assistant powered by Groq ✨</p>", unsafe_allow_html=True)
st.markdown("---")

# 🧠 Agent Personality
system_prompt = st.text_area(
    "🧠 Define your AI's Role (e.g., Doctor, Developer, Travel Buddy):",
    height=70,
    placeholder="Type the role or personality of your AI agent..."
)

# 🌐 Enable optional web search
allow_web_search = st.checkbox("🌐 Enable Web Search via Tavily")

# ✍️ User Query Input
user_query = st.text_area("💬 Ask Anything:", height=150, placeholder="Type your question here...")

# 🧠 Fixed model to Groq's llama-3.3-70b
selected_model = "llama-3.3-70b-versatile"

# 🚀 Trigger response
if st.button("🚀 Ask Tufan!"):
    if user_query.strip():
        try:
            status = st.empty()
            status.info("🤔 TufanBot is thinking...")

            # 💡 Initialize the Groq LLM
            llm = ChatGroq(model=selected_model)

            # 🔧 Use search tool if enabled
            tools = [TavilySearchResults(max_results=2)] if allow_web_search else []

            # 🤖 Create reactive agent
            agent = create_react_agent(
                model=llm,
                tools=tools,
                state_modifier=system_prompt
            )

            # 📨 Query the agent
            state = {"messages": user_query}
            result = agent.invoke(state)
            messages = result.get("messages", [])
            ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

            # ✅ Hide thinking message
            status.empty()

            # 📬 Show AI response
            if ai_messages:
                st.subheader("🧾 TufanBot says:")
                st.markdown(f"**{ai_messages[-1]}**")
            else:
                st.warning("⚠️ No response received.")

        except Exception as e:
            status.empty()
            st.error(f"💥 Error: {e}")
