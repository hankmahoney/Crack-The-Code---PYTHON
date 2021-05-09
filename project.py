import random

digits = list(range(10))
random.shuffle(digits)
digits = digits[:3]
print(digits)

def checkAnswer(guess, code):
    perfect = False
    match = False
    close = False
    count = 0

    for i in range(3):
        for j in range(3):
            if int(guess[i]) == code[j] and i == j:
                match = True
                count += 1
                if count == 2:
                    perfect = True
            elif int(guess[i]) == code[j]:
                close = True

    if perfect == True:
        print("You cracked the code!")
    elif match == True:
        print("Match")
    elif close == True:
        print("Close")
    else:
        print("Nope")
    return perfect

while(True):
    guess = input("Enter a 3 digit number: ")
    if(checkAnswer(guess,digits)):
        break
