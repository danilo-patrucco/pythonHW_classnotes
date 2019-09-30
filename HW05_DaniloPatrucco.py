# Danilo Patrucco
# CS 100 2019F Section 103
# HW 05, September 25, 2019

# Exercise 1

print('\n\rExercise 1.b\n\r')


def hasFinalLetter(strList, letters):
    # initialize an empty list to return when the function is completed.
    lst = []
    # loop to verify each word in the list variable strList
    for i in strList:
        # assign to a variable the last letter of the word currently selected in the loop
        lastLetter = i[-1]
        # test to see if the letter is present in the list variable called letters. if so the letter is appended in the list lst
        if lastLetter in letters:
            lst.append(lastLetter)
    return lst


strList_1 = ['ambivert', 'calcspar', 'deaness', 'entrete', 'gades']
letters_1 = ['a', 'b', 'f', 'L', 'G']

lst1 = hasFinalLetter(strList_1, letters_1)
print('empty list', lst1)

strList_2 = ['monkeydom', 'outclimbeb', 'outdaref', 'pistoleerL', 'redbuG']
letters_2 = ['m', 'b', 'f', 'L', 'G']

lst2 = hasFinalLetter(strList_2, letters_2)
print('Non Empty list', lst2)

strList_3 = ['snake-line', 'subrules', 'subtrends', 'toreniA', 'unhides']
letters_3 = ['a', 'e', 'f', 'A', 'G']

lst3 = hasFinalLetter(strList_3, letters_3)
print('Non Empty list', lst3)

print('\n\rExercise 2.b\n\r')


def isDivisible(maxInt, twoInts):
    # initialize an empty list to return when the function is completed.
    lst = []
    # loop to verify if the numbers are divisible
    for i in range(maxInt, 0, -1):
        # converted all the variables in integer form and extrapolated the variable i for Boolean operation
        t1 = int(twoInts[0])
        t2 = int(twoInts[1])
        integ = i
        if integ % t1 == 0 and integ % t2 == 0:
            # append numbers passing the boolean operation to the container variable called lst
            lst.append(i)
    return lst


maxInt_1 = int()
twoInts_1 = tuple()

lst4 = isDivisible(maxInt_1, twoInts_1)

print('\n\r', lst4, '\n\r')

maxInt_2 = int(1050)
twoInts_2 = ("2", "5")

lst5 = isDivisible(maxInt_2, twoInts_2)

print('\n\r', lst5, '\n\r')

maxInt_3 = int(122)
twoInts_3 = ("10", "6")

lst6 = isDivisible(maxInt_3, twoInts_3)

print('\n\r', lst6)

# I did not make this code DRY because i wanted to show the tought process, otherwise i would have just created a function to get the inputs. Let me know if that is ok or not.
