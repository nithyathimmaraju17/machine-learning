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
            L = []
            L.append(' ' * ind * 4)
            L = ['print(']
            c = 0
            temp = audio.split()
            if temp[1] != 'variable':
                L.append('"')
            for i in temp:
                if i == 'variable':
                    c = 1
            for i in temp:
                if i == 'print':
                    continue
                elif i == 'variable':
                    j = temp[temp.index(i) - 1]
                    if j != 'print':
                        L.append('",')
                else:
                    L.append(i)
                    L.append(' ')

            file1 = open("myfile.py", "a+")
            if c == 0:
                L.append('")')
            else:
                L.append(')')
            file1.writelines(L)
            file1.writelines('\n')
            file1.close()
            web.open("myfile.py")
            print("success")

    except:
        print("apologize me, i couldn't recognize it")