from groq import Groq 
import os 
from dotenv import load_dotenv 

load_dotenv() 

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_insights(summary):
    prompt = f"""
    You are a professional data analyst.

    A user uploaded a dataset.

    Your job:
    1. Understand what this dataset is about
    2. Identify important columns
    3. Find patterns, trends, and anomalies
    4. Give useful business insights

    Be specific to THIS dataset.
    Do NOT give generic answers.

    DATA:
    {summary}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content