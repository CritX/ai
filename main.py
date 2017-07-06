import random
import tkinter as tk
from tkinter import *
import os
file = open('sentenceData.txt', 'a+')
file.close()
file = open('sentenceData.txt', 'r+')
if file.read() == "":
    print("Sentence Data is empty...loading default phrases")
    file.write("Hello!,Howdy!")
    file.close()
    file = open('sentenceData.txt', 'r+')
    phrases = file.read().split(',')
else:
    file = open('sentenceData.txt', 'r+')
    phrases = file.read().split(',')
root = Tk()
aiOutput = "asdfsadf"
T = Label(root, height=1, text=aiOutput)
T.grid(row=0)
userEntry = Entry(root, width=50)
userEntry.grid(row=1)
helpCommand = (open('help.txt', 'r'))
debugMode = False
talk = True
UserInput = ""
aiOutput = phrases[random.randint(0, len(phrases)-1)] + " "
def buttonCommand():
    global talk
    global aiOutput
    global userEntry
    global UserInput
    global phrases
    global debugMode
    global T
    if talk == True:
        UserInput = userEntry.get()
        userEntry.delete(0, 'end')
        print(aiOutput)
        T.text = aiOutput
        aiOutput = phrases[random.randint(0, len(phrases)-1)] + " "
        T = Label(root, height=1, text=aiOutput)
        if(UserInput[0] == "/"):
            if(UserInput == "/help"):
                print(helpCommand.read())
            elif(UserInput == "/exit"):
                print("Closing...")
                for i in range (len(phrases)):
                    file.write(phrases[i])
                    if i < len(phrases)-1:
                        file.write(",")
                file.close()
                talk = False
            elif(UserInput == "/debug"):
                print("Syntax: /debug [value]")
            elif(UserInput == "/debug 1"):
                print("Starting debug...hold on.")
                debugMode = True
            elif(UserInput == "/debug 0"):
                print("Closing debug...hold on.")
                debugMode = False
            elif(debugMode == True):
                if(UserInput == "/phrases"):
                    print(phrases)
                elif(UserInput == "/len"):
                    print(len(phrases))
                elif(UserInput == "/clear"):
                    file.close()
                    os.remove('sentenceData.txt')
                    talk = False
        
            else:
                print("Enter a valid command!")
        else:
            phrases.append(UserInput)

userConfirm = Button(root, text="Talk to the AI!", command=buttonCommand)
userConfirm.grid(row=1, column=1)
mainloop()
