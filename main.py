import speech_recognition as sr
from speaker import speak
from gmail_checker import fetch_emails
from groq_summarizer import summarize_emails
from app_opener import open_app
from system_controls import system_control

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=12)
            return recognizer.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry")
            return ""
        except sr.RequestError:
            speak("Internet problem")
            return ""

def handle_command(command):
    if not command:
        speak("I didn't get any command. Try again!")
        return
    if "email" in command or "gmail" in command:
        speak("Sure! Let me check your emails!")
        emails = fetch_emails()
        summary = summarize_emails(emails)
        speak(summary)
    elif "open" in command:
        result = open_app(command)
        speak(result)
    elif "shutdown" in command or "sleep" in command or "restart" in command:
        system_control(command)
    else:
        speak("Sorry")

# Main loop
speak(" Jaidie")

while True:
    print("Waiting for wake word...")
    text = listen()

    if "galaxy" in text:
        command = text.replace("galaxy", "").strip()

        if command:
            print("Command:", command)
            speak("Jaidie!")
            handle_command(command)
        else:
            speak("Yes! Jaidie I am here")
            command = listen()
            print("Command:", command)
            handle_command(command)