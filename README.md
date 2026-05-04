# Celerates Virtual Travel Assistant

**Conversational AI | LangChain | Streamlit | Google Gemini**

## Overview
A specialized AI chatbot designed for "Celerates Tour Agency" to automate customer service. It handles inquiries regarding tour packages, calculates total travel costs, and collects reservation data using natural language processing.

## Core Features
1. **Dynamic Pricing Engine:** Calculates real-time quotes based on package prices, airline selection, and number of travelers.
2. **Contextual Memory:** Retains conversation flow to handle follow-up questions seamlessly.
3. **Domain Guardrails:** Strictly constrained to travel services, professionally declining irrelevant or out-of-scope queries.
4. **Interactive UI:** A user-friendly chat interface built with Streamlit for easy deployment.

## Tech Stack
* **LLM:** Google Gemini 2.0 Flash
* **Framework:** LangChain Core
* **Deployment:** Streamlit
* **Language:** Python

## Installation
1. Clone the repo: `git clone https://github.com/yourusername/travel-chatbot.git`
2. Install requirements: `pip install streamlit langchain-google-genai`
3. Run the app: `streamlit run app.py`
