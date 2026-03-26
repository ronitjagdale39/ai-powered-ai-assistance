import pyttsx3

engine = pyttsx3.init('nsss')  # Mac engine

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()