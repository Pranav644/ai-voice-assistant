import speech_recognition as sr
import pyttsx3
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Could not request results.")
        speak("Could not request results.")
        return ""

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("AI Voice Assistant started. Say something!")
    speak("Hello! How can I help you?")
    while True:
        query = listen()
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        if query:
            answer = ask_gpt(query)
            print(f"Assistant: {answer}")
            speak(answer)