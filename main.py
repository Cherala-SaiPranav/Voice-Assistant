import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os

speech = pyttsx3.init('sapi5')
voices = speech.getProperty('voices')
speech.setProperty('voice', voices[1].id)

def speak(text):
    speech.say(text)
    speech.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 20 or hour < 4:
        speak("Good Night!")
    elif hour >=4 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour <16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How may i help you?")

def recieveCommand():
    voiceRecog = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        voiceRecog.pause_threshold = 1
        voiceRecog.adjust_for_ambient_noise(source)
        try:
            audio = voiceRecog.listen(source)
            query = voiceRecog.recognize_google(audio, language='en-in')
            print(query)
            return query
        except Exception as e:
            speak("Say that again please.")
            return "None"

if __name__=="__main__":
    greetings()
    while True:
        query = recieveCommand().lower()
        if 'open vs code' in query or 'open code' in query or 'open visual studio' in query:
            codePath = "Replace with vs code exe file path"
            os.startfile(codePath)
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            print(f"Time is {time}")
            speak(f"Time is {time}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye")
            break
        else:
            speak("Insufficient clearence level")