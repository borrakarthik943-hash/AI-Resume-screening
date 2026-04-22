from langchain_groq import ChatGroq
from prompts.extract_prompt import extract_prompt   # ✅ VERY IMPORTANT

llm = ChatGroq(model="llama-3.1-8b-instant")

chain = extract_prompt | llm

def extract_data(resume):
    return chain.invoke({"resume": resume})
