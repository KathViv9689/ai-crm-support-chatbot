import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 CRM AI Support Bot")

# Load FAQ knowledge
def load_knowledge():
    try:
        with open("crm_faq.txt", "r") as f:
            return f.read()
    except:
        return ""

knowledge = load_knowledge()

# System prompt (IMPORTANT for interview)
system_prompt = f"""
You are a CRM support assistant.

Rules:
- Answer only CRM, pricing, and support-related questions
- Be professional and concise
- If unsure, say: "I will connect you to a human agent"

Knowledge Base:
{knowledge}
"""

# User input
user_input = st.text_input("Ask your question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
