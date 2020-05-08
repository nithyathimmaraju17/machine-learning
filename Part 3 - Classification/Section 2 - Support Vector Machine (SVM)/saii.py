import speech_recognition as sr
import pyaudio
import webbrowser as web
from github import Github
import requests
# r2 = sr.Recognizer()
ACCESS_TOKEN = '6948f3c5d96bcd86f88ba30526304ab8bcd5a8cf'
g = Github(ACCESS_TOKEN)
print(g.get_user().get_repos())

ind = 0
while 1:

    j = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        text = j.listen(source)

    try:
            audio = j.recognize_google(text)
            print("You said : {}".format(audio))
            if 'print' in audio:
                l=[]
                temp = audio.split()
                l.append('print("')
            for i in temp:
                if i != 'print':
                    l.append(i)
                    l.append(" ")
            
            s=''
            for i in l:
                if i!='variable':
                    s = s+i
                elif i=='variable':
                    s = s+'",'
            if "variable" in l:
                s=s+')'
            else:
                s=s+'")'
            print(s)
            file1 = open("myfile.py", "a+")
            file1.writelines("\n")
            file1.writelines(s)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")
    except:
        print("apologize me, i couldn't recognize it")