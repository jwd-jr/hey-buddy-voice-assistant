from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_emails(emails):
    if not emails:
        return "You have no unread emails in the last 24 hours!"

    email_text = ""
    for i, email in enumerate(emails, 1):
        email_text += f"""
Email {i}:
From: {email['sender']}
Subject: {email['subject']}
Preview: {email['snippet']}
"""

    prompt = f"""
You are Jadi, a personal voice assistant for Jaidie.
You have received {len(emails)} unread emails from the last 24 hours.

First say: "You have {len(emails)} new emails in the last 24 hours."

Then read all emails carefully and rank them from MOST IMPORTANT to LEAST IMPORTANT.

For each email say it like this:
"The most important email is from [sender], they are saying [what it is about]."
"The next one is from [sender], they are saying [what it is about]."
"Then there is one from [sender], about [what it is about]."
...and so on until all emails are covered.

At the end say one closing line like:
"That is all your emails for today Jaidie."

Rules:
- Speak naturally like talking to a person
- No bullet points, no numbering
- Most important email first, least important last
- Keep each email description to one sentence
- Do not miss any email

{email_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content