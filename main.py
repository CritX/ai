import random

nouns = ["Car", "Cat"]
verbs = ["eat", "sleep", "run"]
restOfPredicate = ["everyday", "sometimes", "in the morning"]
combinedString = ""
punctuation = ['.', '?', '!']
while 1 == 1:
    user = input(nouns[random.randint(0, len(nouns)-1)] + " " + verbs[random.randint(0, len(verbs)-1)] + " " + restOfPredicate[random.randint(0, len(restOfPredicate)-1)] + punctuation[random.randint(0, len(punctuation)-1)] + " ")
    user = user.split(' ')
    if len(user) == 1:
        if user[0] != "":
            verbs.append(user[0])
        else:
            print("What?")
    elif len(user) > 1:
        nouns.append(user[0])
        verbs.append(user[1])
        combinedString = ""
        if(len(user) > 2):
            for i in range(3, len(user)+1):
                combinedString = combinedString + user[i - 1]
                if i < len(user):
                    combinedString = combinedString + " "
            restOfPredicate.append(combinedString)
