from groq import Groq
from dotenv import load_dotenv
load_dotenv()

import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_emails(emails):
    email_text = ""
    for i, email in enumerate(emails, 1):
        email_text += f"""
Email {i}:
From: {email['sender']}
Subject: {email['subject']}
Preview: {email['snippet']}
"""

    prompt = f"""
You are a helpful assistant. Read these emails and give a short summary.
For each email say: who sent it, what it is about, and if it is important.
Keep it short — speak like you are talking to someone.

{email_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content