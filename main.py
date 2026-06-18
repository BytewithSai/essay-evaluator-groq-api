import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
# print(os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

with open("sample.txt", "r") as f:
    essay = f.read()

# print(essay)
prompt = f"""
You are an expert English teacher.

Evaluate the following essay based on:

1. Grammar
2. Clarity
3. Structure

Return the result in this format:

Grammar: X/10
Clarity: X/10
Structure: X/10
Overall: X/10

Feedback:
- Point 1
- Point 2
- Point 3
- Point 4

Essay:
{essay}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


print(response.choices[0].message.content)