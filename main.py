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

def search_exe_files(search_name, search_path="C:\\"):
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower() == f"{search_name}.exe".lower():
                return os.path.join(root, file)
    return None

def processQuery(query):
    if 'run' in query:
        file = query.replace('open', '').strip().lower()
        appPath = search_exe_files(file)
        if appPath:
            os.startfile(appPath)
        else:
            speak("App not found.")
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M")
        print(f"Time is {time}")
        speak(f"Time is {time}")
    elif 'open' in query:
        website = query.replace('open', '').strip().replace(' ', '')
        if '.' not in website:
            website+='.com'
        webbrowser.open(f"https://{website}")
    elif 'search' in query:
        search = query.replace('search', '').strip()
        if search:
            webbrowser.open(f"https://www.google.com/search?q={search}")
        else:
            speak("Please specify.")
    elif 'exit' in query:
        speak("Goodbye")
        return False
    else:
        speak("Insufficient clearence level")
    return True

if __name__=="__main__":
    greetings()
    while True:
        query = recieveCommand().lower()
        if not processQuery(query):
            break