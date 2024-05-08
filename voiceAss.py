import speech_recognition as sr
import pyttsx3
import datetime
import os

r=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"you said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("soory, i don't undestand what you said.")
    except sr.RequestError:
        print("sorry my speech recognition service currently down.")      

def get_time():
    now = datetime.datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    am_pm = now.strftime("%p")
    speak(f"The time is {hour}:{minute} {am_pm}.")

def get_name():
    speak("My name is Aadhya.")

def create_note():
    speak("what should i write in the note?")
    note_text = listen()
    filename = datetime.datetime.now().strftime("%Y.%m.%d_%04.%M.%s")+".text"
    with open(filename,"w") as f:
        f.write(nnote_text)
    speak("note saved.")

def main():
    speak("Hello! what can i do for you today?")

    while True:
        command = listen()
        if "hello" in command:
            speak("hi there")
        elif " how are you "  in command:
            speak("i am doing well, thank you.")
        elif " how are you "  in command:
            speak("i am doing well, thank you.")
        elif " what's your name"  in command:
           get_name()
        elif " time "  in command:
            get_time()
        elif " create a note"  in command:
            create_note()
        elif "goodbye" in command:
            speak("goodbye!")
            break
        else:
            speak("i am sorry i don't understand what you said.")    
