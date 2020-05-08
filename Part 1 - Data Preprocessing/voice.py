# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:00:03 2020

@author: Rishwi Binnu
"""
"""
Requirements:

pip install SpeechRecognition
pip install pyaudio
pip install google
pip install PyGithub
"""
"""
Voice Commands:

import xyz package
print xyz
assign variable x with 5 || assign variable x to 10 || x equals 20
open for from 1 to 10
open if i greater than to 5 || open if i greater than or equals to xyz|| open if i equals to xyz
close -> to close a loop or conditional
search armstrong number program -> for google search
github x y z. -> github is the keyword and next words are key words
stop - > To stop the program

***definitely use close after opening if or for loops.

"""

import speech_recognition as sr
import pyaudio
import webbrowser
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
            L = ['print(']
            c = 0
            temp = audio.split()
            for i in temp:
                if i == 'quotation':
                    c = 1
                    L.append('"')
            for i in temp:
                if i == 'print' or i == 'in' or i == 'quotation':
                    continue
                else:
                    L.append(i)
            file1 = open("myfile.py", "a+")
            if c == 1:
                L.append('")')
            else:
                L.append(')')
            file1.writelines("\n")
            file1.writelines(L)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")
            
        if 'equals' in audio:
            temp=audio.split(' ')
            if temp[2].isdigit():
                L.append(temp[0] + " = " + temp[2])
            else:
                L.append(temp[0] + " = " + '"'+temp[2]+'"')
            file1 = open("myfile.py", "a+")
            file1.writelines("\n")
            file1.writelines(L)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")

        if 'assign' in audio:
            L = []
            temp = audio.split()
            s = 'variable'
            j = ' '
            for i in temp:
                if i == s:
                    j = temp[temp.index(i) + 1]
                    L.append(j)
                    L.append(' = ')
                if i == 'with' or i == 'to':
                    j = temp[temp.index(i) + 1]
                    if j.isdigit():
                        L.append(j)
                        L.append('\n')
                        L.append(' ' * ind * 4)
                    else:
                        L.append('"')
                        L.append(j)
                        L.append('"')
                        L.append('\n')
                        L.append(' ' * ind * 4)
            file1 = open("myfile.py", "a+")
            file1.writelines("\n")
            file1.writelines(L)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")

        if 'open' in audio:
            if 'for' in audio:
                L = ['for ']
                temp = audio.split()
                res = [int(i) for i in audio.split() if i.isdigit()]
                for i in temp:
                    if i == 'for':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append(' in range(')
                    if i == 'from':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append(', ')
                    if i == 'to':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append('):\n')
                        ind = ind + 1
                        L.append(' ' * ind * 4)
                    if i == 'of':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append('):\n')
                        ind = ind + 1
                        L.append(' ' * ind * 4)

                file1 = open("myfile.py", "a+")
                file1.writelines("\n")
                file1.writelines(L)
                file1.close()
                webbrowser.open("myfile.py")
                print("success")

            if 'if' in audio:
                L = ['if ']
                ind = ind + 1
                temp = audio.split()
                for i in temp:
                    if i == 'condition':
                        j = temp[temp.index(i) + 1]
                        if j == 1 or j == 'true':
                            L.append(j)
                            L.append(':\n')
                            L.append(' ' * ind * 4)
                        else:
                            L.append(j)
                            L.append(' ')
                    if i == 'greater':
                        j = temp[temp.index(i) + 2]
                        if j == 'equals' or j == 'equal':
                            L.append('>=')
                            L.append(' ')
                        else:
                            L.append('>')
                            L.append(' ')
                    elif i == 'less':
                        if j == 'equals' or j == 'equal':
                            L.append('<=')
                            L.append(' ')
                        else:
                            L.append('<')
                            L.append(' ')
                    elif i == 'equals':
                        L.append('==')
                        L.append(' ')
                    if i == 'to':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append(':\n')
                        L.append(' ' * ind * 4)
                file1 = open("myfile.py", "a+")
                file1.writelines("\n")
                file1.writelines(L)
                file1.close()
                webbrowser.open("myfile.py")
                print("success")

            if 'elif' in audio:
                L = ['elif ']
                ind = ind + 1
                temp = audio.split()
                for i in temp:
                    if i == 'condition':
                        j = temp[temp.index(i) + 1]
                        if j == 1 or j == 'true':
                            L.append(j)
                            L.append(':\n')
                            L.append(' ' * ind * 4)
                        else:
                            L.append(j)
                            L.append(' ')
                    if i == 'greater':
                        j = temp[temp.index(i) + 2]
                        if j == 'equals' or j == 'equal':
                            L.append('>=')
                            L.append(' ')
                        else:
                            L.append('>')
                            L.append(' ')
                    elif i == 'less':
                        if j == 'equals' or j == 'equal':
                            L.append('<=')
                            L.append(' ')
                        else:
                            L.append('<')
                            L.append(' ')
                    elif i == 'equals':
                        L.append('==')
                        L.append(' ')
                    if i == 'to':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append(':\n')
                        L.append(' ' * ind * 4)
                file1 = open("myfile.py", "a+")
                file1.writelines("\n")
                file1.writelines(L)
                file1.close()
                webbrowser.open("myfile.py")
                print("success")

            if 'else' in audio:
                L = ['else :']
                ind = ind + 1
                L.append('\n')
                L.append(' ' * ind * 4)
                file1 = open("myfile.py", "a+")
                file1.writelines("\n")
                file1.writelines(L)
                file1.close()
                webbrowser.open("myfile.py")
                print("success")

            if 'while' in audio:
                L = ['while ']
                ind = ind + 1
                temp = audio.split()
                for i in temp:
                    if i == 'condition':
                        j = temp[temp.index(i) + 1]
                        if j == 1 or j == 'true':
                            L.append(j)
                            L.append(':\n')
                            L.append(' ' * ind * 4)
                        else:
                            L.append(j)
                            L.append(' ')
                    if i == 'greater':
                        j = temp[temp.index(i) + 2]
                        if j == 'equals' or j == 'equal':
                            L.append('>=')
                            L.append(' ')
                        else:
                            L.append('>')
                            L.append(' ')
                    elif i == 'less':
                        if j == 'equals' or j == 'equal':
                            L.append('<=')
                            L.append(' ')
                        else:
                            L.append('<')
                            L.append(' ')
                    elif i == 'double':
                        L.append('==')
                        L.append(' ')
                    if i == 'to':
                        j = temp[temp.index(i) + 1]
                        L.append(j)
                        L.append(':\n')
                        L.append(' ' * ind * 4)
                file1 = open("myfile.py", "a+")
                file1.writelines("\n")
                file1.writelines(L)
                file1.close()
                webbrowser.open("myfile.py")
                print("success")

        if 'close' in audio:
            L = ['\n']
            ind = ind - 1
            L.append(' ' * ind * 4)
            file1 = open("myfile.py", "a+")
            file1.writelines("\n")
            file1.writelines(L)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")



        if 'import' in audio:
            L = "import "
            if 'package':
                j = audio.split(' ')
                L.append(j[1])

            file1 = open("myfile.py", "a")
            file1.writelines("\n")
            file1.writelines(L)
            file1.close()
            webbrowser.open("myfile.py")
            print("success")
            
        if 'search' in audio:
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            try:
                from googlesearch import search
            except ImportError:
                print("No Module named 'google' Found")
            for i in search(query=audio,tld='co.in',lang='en',num=10,stop=1,pause=2):
                webbrowser.get(path).open(i)
                
        if 'github' in audio:
            def search_github(keyword):
                rate_limit = g.get_rate_limit()
                rate = rate_limit.search
                
                query = f'"{keyword} python" in:file extension:py'
                result = g.search_code(query, order='desc')
             
                max_size = 1
                if result.totalCount > max_size:
                    result = result[:max_size]
             
                for file in result:
                    t=f'{file.download_url}'
                    print(t)
                    r = requests.get(t)
                    open("file3.py", "wb").write(r.content)
                    webbrowser.open("file3.py")
    
            keywords = audio.strip('github ').split(' ')
            #keywords = [keyword.strip() for keyword in keywords.split(',')]
            search_github(keywords)

        if 'stop' in audio:
            break




    except :
        print("apologize me, i couldn't recognize it")