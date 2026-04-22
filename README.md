# 🧠 AI Resume Screening System

An AI-powered Resume Screening System built using Generative AI and LangChain to automate candidate evaluation.

---

## 🚀 Project Overview

This project simulates how recruiters screen resumes by extracting key information and analyzing candidate profiles.

The system uses Large Language Models (LLMs) to:
- Extract important details from resumes
- Identify skills, experience, and tools
- Provide structured output for better decision-making

---

## ⚙️ Features

✅ Extracts:
- Skills  
- Experience  
- Tools  

✅ Uses LLM (Groq + Llama 3.1)  
✅ Modular pipeline using LangChain  
✅ Clean and structured output  
✅ Easy to extend (matching, scoring, etc.)

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain-Groq
- LLM (Llama 3.1 - Groq API)

---

## 📂 Project Structure

Ai-resume-screening/
│── main.py
│── chains/
│ └── extraction_chain.py
│── prompts/
│ └── extract_prompt.py


---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-screening.git
cd ai-resume-screening

2️⃣ Install Dependencies

pip install langchain langchain-groq
3️⃣ Set API Key

Option 1 (Temporary)
import os
os.environ["GROQ_API_KEY"] = "your_api_key"

4️⃣ Run Project
python main.py

📌 Example Output
Skills:
- Python
- Machine Learning
- TensorFlow

Experience:
- 2 years as Python Developer

Tools:
- Pandas
- SQL

