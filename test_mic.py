import speech_recognition as sr

recognizer = sr.Recognizer()

print("Say something...")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand")
except sr.RequestError:
    print("Internet error")