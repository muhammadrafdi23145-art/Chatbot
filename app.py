import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Page Configuration
st.set_page_config(page_title="Celerates AI Assistant", layout="centered")

# Sidebar for API Key
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter Google AI API Key", type="password")
    st.info("Get your key at aistudio.google.com")

# System Prompt Translation to English
system_prompt = """
You are an AI assistant for "Celerates Tour Agency".
Your task is to assist customers with booking or tour package information.

Available Packages:
- England Tour: IDR 25,000,000 per person
- Japan Tour: IDR 24,000,000 per person
- Singapore Tour: IDR 20,000,000 per person
* All packages are 5 days and include accommodation + 2 destinations.
* Flight tickets are excluded.

Flight Options:
- Etihad Airways: IDR 5,000,000 per person
- Emirates Airways: IDR 6,000,000 per person
- Garuda Indonesia: IDR 4,500,000 per person

Guidelines:
- Greet customers warmly and professionally.
- Help select packages and calculate total costs (Package + Flight) * Number of People.
- Politely decline non-travel topics (politics, science, etc.) and refocus on Celerates services.
"""

st.title("Celerates Tour Agency Chatbot")
st.write("Plan your dream vacation with our AI-powered travel consultant.")

# Session State for History
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=system_prompt)]

# Display History
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Input Chat
if prompt := st.chat_input("How can I help you?"):
    if not api_key:
        st.error("Please provide an API Key in the sidebar to start.")
    else:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
            with st.chat_message("assistant"):
                response = llm.invoke(st.session_state.messages)
                st.markdown(response.content)
            st.session_state.messages.append(AIMessage(content=response.content))
        except Exception as e:
            st.error(f"Error: {e}")
