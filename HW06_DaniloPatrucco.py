# Danilo Patrucco
# CS 100 2019F Section 103
# HW 06, October 2, 2019

import random

# Problem 1

def twoWords(lenght, firstLetter):
    lst = []
    while True:
        wordLenght = str(input('Enter a ' + str(lenght) + ' -letter word please: '))
        if lenght == len(wordLenght):
            lst.append(wordLenght)
            break
    while True:
        oneWord = str(input('Enter a word beginning with ' + str(firstLetter) + ' please: '))
        if oneWord[0] == firstLetter:
            lst.append(oneWord)
            break
    return lst


print("\r\nProblem 1: \r\n")
print(twoWords(4, 'B'))

# Problem 2

def twoWords(lenght, firstLetter):
    oneWord = '\n'
    wordLenght = '\n'
    lst = []
    while lenght != len(wordLenght):
        wordLenght = input('Enter a ' + str(lenght) + ' -letter word please: ')
        if lenght == len(wordLenght):
            lst.append(wordLenght)
    while firstLetter != oneWord[0]:
        oneWord = str(input('Enter a word beginning with ' + str(firstLetter) + ' please: '))
        if oneWord[0] == firstLetter:
            lst.append(oneWord)
    return lst


print("\r\nProblem 2: \r\n")
print(twoWords(4, 'B'))

# Problem 3

def enterNewPassword():
    while True:
        password = input("please insert a password that is between 8 and 15 chars: ")
        if len(password) >= 8 and len(password) <= 15:
            break
    return None


print("\r\nProblem 3: \r\n")
enterNewPassword()
print("Well Done!")

# Problem 4

def GuessNumber():
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    rdmNumber = random.randint(0, 50)
    gNumber = 5
    gbase = 1
    while gbase != gNumber+1:
        number = int(input("Guess nr." + str(gbase) + "?"))
        if number == rdmNumber:
            print("You are right! I was thinking of " + str(rdmNumber) + "!")
            return
        elif number < rdmNumber:
            print("Your number is too low")
            gbase += 1
        elif number > rdmNumber:
            print("Your number is too high")
            gbase += 1
    if gbase == gNumber+1:
        print("\n\rToo many attempts, the number was " + str(rdmNumber) + "!")

print("\r\nProblem 4: \r\n")
GuessNumber()
