import pyttsx3
import datetime

speech = pyttsx3.init('sapi5')
voices = speech.getProperty('voices')
speech.setProperty('voice', voices[1].id)

def speak(text):
    speech.say(text)
    speech.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 8 and hour < 4:
        speak("Good Night!")
    elif hour >=4 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 5:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How may i help you?")

if __name__=="__main__":
    greetings()