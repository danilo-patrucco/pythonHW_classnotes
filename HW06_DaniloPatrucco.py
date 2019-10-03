# Danilo Patrucco
# CS 100 2019F Section 103
# HW 06, October 2, 2019

# Exercise 1

def twoWords(lenght, firstLetter):
    oneWord = '0'
    wordLenght = 0
    lst = []
    while lenght != wordLenght:
        wordLenght = str(input('Enter a ' + str(lenght) + ' -letter word please: '))
        if lenght == len(wordLenght):
            lst.append(wordLenght)
            break
    while firstLetter != oneWord[0]:
        oneWord = str(input('Enter a word beginning with ' + str(firstLetter) + ' please: '))
        if oneWord[0] == firstLetter:
            lst.append(oneWord)
            break
    return lst


print("\r\nProblem 1: \r\n")
print(twoWords(4, 'B'))
