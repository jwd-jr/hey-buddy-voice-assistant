import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from groq_summarizer import summarize_emails

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def fetch_emails():
    service = get_gmail_service()
    results = service.users().messages().list(
        userId='me', 
        labelIds=['UNREAD'], 
        maxResults=5
    ).execute()
    
    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        data = service.users().messages().get(
            userId='me', 
            id=msg['id'],
            format='metadata',
            metadataHeaders=['From', 'Subject']
        ).execute()

        headers = data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        snippet = data.get('snippet', '')

        emails.append({
            'sender': sender,
            'subject': subject,
            'snippet': snippet
        })
        
    return emails

if __name__ == "__main__":
    emails = fetch_emails()
    for i, email in enumerate(emails, 1):
        print(f"\nEmail {i}:")
        print(f"From: {email['sender']}")
        print(f"Subject: {email['subject']}")
        print(f"Preview: {email['snippet'][:100]}")



if __name__ == "__main__":
    emails = fetch_emails()
    print("\n--- RAW EMAILS ---")
    for i, email in enumerate(emails, 1):
        print(f"\nEmail {i}:")
        print(f"From: {email['sender']}")
        print(f"Subject: {email['subject']}")

    print("\n--- GROQ SUMMARY ---")
    summary = summarize_emails(emails)
    print(summary)