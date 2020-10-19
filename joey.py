import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """takes microphone input and gives string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        #dynamic energy threshold bhada do if you dont want k ghar ki awaz bhi sun le ai..sirf tez chillane wali sune
        r.pause_threshold = 1

        audio = r.listen(source)
    try:
        print ("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print "User said:", str(query)
    except Exception as e:
        #dont want error to be shown
        #print (e)
        speak ("I did not get it!")
        return "None"
    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak ("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Joey! How may I help you?")

if __name__ == '__main__':
    wishMe()
    ans = 'yes'
    while 'yes' in ans:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")

            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print (result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'it\'s my birthday today' in query:
            print(" Wow! Wish you a very Happy Birthday")
            speak(" Wow! Wish you a very Happy Birthday")

        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)
            # os.system("start chrome https://www.google.nl/maps/place/" + location)

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.com")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Time is "+str(strTime))
        elif 'open chrome' in query:
            path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(path)
        else:
            webbrowser.open(query)

        speak("Anything else?")
        ans = takeCommand()
        if ans == 'no':
            speak ("Alrighty!! Bye... Bye!")
            break
