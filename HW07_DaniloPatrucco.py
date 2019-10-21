# Danilo Patrucco
# CS 100 2019F Section 103
# HW 07, October 20, 2019

horton = ['I', 'say', 'what', 'Igor', 'sometimes', 'wants', 'to', 'say', 'to', 'Isabela']

print("\r\nProblem 1: \r\n")

def initialLetterCount(wordList):
    dict= {}
    for i in wordList:
        if i[0] not in dict:
            dict[i[0]] = 1
        else:
            dict[i[0]] += 1

    return dict


print(initialLetterCount(horton))

print("\r\nProblem 2: \r\n")


def initialLetters(wordList):
    dict= {}
    for i in wordList:
        if i[0] not in dict:
            dict[i[0]] = [i]
        else:
            dict[i[0]].append(i)
    return dict


print(initialLetters(horton))


print("\r\nProblem 3: \r\n")

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say',]

def shareALetter(wordList):
    dict = {}
    for words in wordList:
        if words not in dict:
            dict[words] = [words]
        for word in dict.keys():
            if word != words:
                for letters in word:
                    if letters in words and word not in dict[words]:
                        dict[words].append(word)

    return dict

print(shareALetter(horton))
