import random
file = open('sentenceData.txt', 'r+')
helpCommand = (open('help.txt', 'r'))
debugMode = False
if file.read() == "":
    print("Sentence Data is empty...loading default phrases")
    file.write("Hello!,Howdy!")
    file.close()
    file = open('sentenceData.txt', 'r+')
else:
    file = open('sentenceData.txt', 'r+')
    phrases = file.read().split(',')
talk = True
while talk == True:
    UserInput = input(phrases[random.randint(0, len(phrases)-1)] + " ")
    if(UserInput[0] == "/"):
        if(UserInput == "/help"):
            print(helpCommand.read())
        if(UserInput == "/exit"):
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
        elif(UserInput == "debug 0"):
            print("Closing debug...hold on.")
            debugMode = False
        if(debugMode == True):
            if(UserInput == "/phrases"):
                print(phrases)
            elif(UserInput == "/len"):
                print(len(phrases))
            elif(UserInput == "/clear"):    #   Doesn't work
                phrases = []
                print("Closing...")
                for i in range (len(phrases)):
                    file.write(phrases[i])
                    if i < len(phrases)-1:
                        file.write(",")
                file.close()
                talk = False
        
        else:
            print("Enter a valid command!")
    else:
        phrases.append(UserInput)
