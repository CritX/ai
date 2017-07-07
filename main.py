import random   # random ints
import tkinter as tk    # the scren
from tkinter import *
import os   # deleting files when doing /clear

#
#   AI (in Python)
#   Created by NotJustCringe
#   Version 1.0
#

file = open('sentenceData.txt', 'a+')   # Makes sure the file is created if it isn't
log = []
logFile = open('log.txt', 'a+')
logFile.close()
logFile = open('log.txt', 'r+')
file.close()
file = open('sentenceData.txt', 'r+')
if file.read() == "":
    print("Sentence Data is empty...loading default phrases")
    file.write("Hello!,Howdy!")
    file.close()
    logFile.write("Hello!,Howdy!")  # This is unnecessary, I just don't want to change it :P
    logFile.close()
    logFile = open('log.txt', 'r+')
    log = logFile.read().split(',')
    file = open('sentenceData.txt', 'r+')
    phrases = file.read().split(',')
    log = logFile.read().split(',')
else:
    file = open('sentenceData.txt', 'r+')
    phrases = file.read().split(',')
    log = logFile.read().split(',')
root = Tk() # Creates the screen
root.configure(background='#7DEE9F')
logo = PhotoImage(file="logo.png").subsample(2, 2)
placeholderLabel = Label(root, image=logo, bg = '#7DEE9F').grid(row=0)
aiOutput = StringVar()
T = Label(root, height=1, textvariable=aiOutput, fg="blue", bg = '#7DEE9F', font=('Helvetica', 14))
T.grid(row=1)
userEntry = Entry(root, width=30)
userEntry.grid(row=2)
helpCommand = (open('help.txt', 'r'))
debugMode = False
talk = True
UserInput = ""
aiOutput.set(phrases[random.randint(0, len(phrases)-1)])
def buttonCommand():    # The reason this is all in a command is so I can use the command property in the button
    """The main button command, this makes the AI 'respond' to the user"""
    global talk
    global aiOutput
    global userEntry
    global UserInput
    global phrases
    global debugMode
    global T
    global log
    global file
    global logFile
    global root
    if talk == True:
        UserInput = userEntry.get()
        userEntry.delete(0, 'end')
        
        
        smart()
        if(UserInput[0] == "/"):    # Makes sure commands or command typos don't affect the log
            #
            # NOTE:
            # All commands are printed to the console, NOT the bot
            #
            if(UserInput == "/help"):
                print(helpCommand.read())
            elif(UserInput == "/exit"):
                print("Closing...")
                file.close()
                os.remove('sentenceData.txt')
                file = open('sentenceData.txt', 'a+')
                file.close()
                file = open('sentenceData.txt', 'r+')
                for i in range (len(phrases)):
                    file.write(phrases[i])
                    if i < len(phrases)-1:
                        file.write(",")
                file.close()
                logFile.close()
                os.remove('log.txt')
                logFile = open('log.txt', 'a+')
                logFile.close()
                logFile = open('log.txt', 'r+')
                for i in range (len(log)):
                    logFile.write(log[i])
                    if i < len(log)-1:
                        logFile.write(",")
                logFile.close()
                talk = False
                root.destroy()
            elif(UserInput == "/debug"):    # Just makes sure users can't type in any debugging commands on default
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
                elif(UserInput == "/clear"):    # Closes similarly to /exit but doesn't write
                    file.close()
                    os.remove('sentenceData.txt')
                    logFile.close()
                    os.remove('log.txt')
                    talk = False
                    root.destroy()
                elif(UserInput == "/log"):
                    print(log)
                elif(UserInput == "/len log"):
                    print(len(log))
            else:
                print("Enter a valid command!")
        else:
           log.append(aiOutput.get())   # Appends what the AI says and what the user says
           phrases.append(UserInput)
def smart():    # This function works similarly to Cleverbot, taking user input and finding how it correlates to what the AI says
    """The 'smartness and responsive' algorithm for the AI"""
    global phrases
    global aiOutput
    global log
    global UserInput
    done = 0
    choose = []
    if(random.randint(1,9)<8):  # Don't want the bot to always give the 'correct' response to what has been said to make it more realistic
        for i in range (len(log)):
            if (done == 0):
                if(UserInput == log[i]):
                    choose = [i for i, x in enumerate(log) if x==UserInput]
                    aiOutput.set(choose[random.randint(0, len(choose)-1)]) 
    if done == 0:
        aiOutput.set(phrases[random.randint(0, len(phrases)-1)])
                
userConfirm = Button(root, text="Talk to the AI!", command=buttonCommand)
userConfirm.grid(row=2,column=1)
root.mainloop() # Starts main loop
