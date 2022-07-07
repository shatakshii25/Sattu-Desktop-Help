import pyttsx3
import speech_recognition as s
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
# print(voices[1].id)
# print(voices[2].id)
# print(voices[3].id)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Shatakshi!")

    elif hour>=12 and hour<18:
        speak("Good afternoond Shatakshi! Done with your lunch?")

    else:
        speak("Good evening Shatakshi, don't forget to workout today! and have dinner at time")
    
    speak("I am Sattu, your Desktop help. Please tell me how may I help you?")

def takeInstructions():

    r = s.Recognizer()
    with s.Microphone() as source:
       print('Hearing you...')
       r.pause_threshold = 1
       audio = r.listen(source)

    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say that again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login('shatakshishree25@gmail.com', 'enfeiqhxnld@@2iwjxoq')
    server.sendmail('shatakshishree25@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    greetMe()
    while True:
    # if 1:
        query = takeInstructions().lower()

        if 'wikipedia' in query:
            speak('Going through Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'coding problem' in query:
            webbrowser.open("stackoverflow.com")

        elif 'dsa' in query:
            webbrowser.open("programiz.com")
        
        elif 'github' in query:
            webbrowser.open("https://github.com/shatakshii25")

        elif 'linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/shatakshi-shree-b6b971a1/")
        
        elif 'portfolio' in query:
            webbrowser.open("https://shatakshii25.github.io/")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Shatakshi Shree'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'whats the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {time}")

        elif 'open vscode' in query:
            vsCodePath = "C:\\Users\\Shatakshi Shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodePath)
        
        elif 'send email to my vit id' in query:
            try:
                speak("what should I say?")
                content = takeInstructions()
                to = "shatakshi.shree2020@vitstudent.ac.in"
                sendEmail(to, content)
                speak("email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("Sorry the mail was not sent, but it's not your fault. Try later")

        

