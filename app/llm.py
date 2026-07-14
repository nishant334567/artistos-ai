from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Shared Groq client for all agents (reads GROQ_API_KEY from env)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
