'''
import turtle


def staircase(t, num, tread, riser):
    for i in range(num):
        stair(t, tread, riser)
    return


def stair(t, tread, riser):
    t.down()
    t.forward(tread)
    t.right(90)
    t.forward(riser)
    t.left(90)
    return

s = turtle.screen()
t = turtle.Turtle()
staircase()


def first_last(string_list):
    returnList = []
    for string in string_list:
        if string != '' and string[0] == string[-1]:
            returnList.append(string)
    return returnList




def vowel_tracker(words):
    init_vowel = 0
    ending_vowel = 0
    vowel_lst = 'aeiouAEIOU'
    for i in words:
        if i[0] in vowel_lst:
            init_vowel += 1
        if i[-1] in vowel_lst:
            ending_vowel += 1
    return [init_vowel, ending_vowel]





# review this
def number_luck(lucky, unlucky):
    num = int(input('give me a number between 2 and 12'))
    int_loop=[]
    int_loop.append(lucky)
    int_loop.append(unlucky)
    for i in int_loop:
        if i in lucky:
            if i == num:
                print('number is lucky')
        elif i in unlucky:
            if i == num:
                print('number is unlucky')
        else:
            print('your number is boring')
    return

l = [3,4,5]
u = [6,7,8]



def month_info(medium_lenght):
    month = str(input('What month is it?'))
    days = int(input('How many days in a month'))
    if days < medium_lenght:
        print('month is short')
    elif days == medium_lenght:
        print('month is medium')
    else :
        print('month is long')
    return month

print(month_info(30))



#exam 2

#remenmber the .readline() command, it will read a whole line of a text file and store it in a list
# remember to review the remainder and all that stuff from class beginning
# remember the data type
# if a key does not exist in a dictionary we will get a key error print(d[0][1]) means do two lookups, first find the value for d[0]
# then do a lookup on key [1] and see if the result of d[0] (that will become a value) is present in [1]
#if bool means if true
#

def compare(s, wordList):
    rtnList = []
    for word in s.split():
        print(word)
        print(word[0])
        print(word[-1])
        if word in wordList:
            continue
        if word[0] == word[-1]:
            break
        rtnList.append(word)
    print(rtnList)
    return len(rtnList)

bill = "big dreams create the magic that stir souls to greatness"
print(compare(bill, ['to', 'the', 'that']))

# continue restart the loop, break leave it

for i in range(1, 3):
    for j in range(1, 2):
        print('#', end=' ')


boolList = [True or False, not False, not not True, 9//2 == 4.5, False, True]
i = 0
while boolList[i]:
    print(boolList[i])
    print(i)
    i += 1
print(i)

#true or false is true


def asymmetry(s):
    symmetric = ''
    for i in range(len(s)):
        print(i)
        print(s[i])
        print(s[-i-1])
        if s[i] == s[-i-1]:
            symmetric += s[i]
        else:
            return s[i:-i]
    return symmetric


t = 'sambas'
print(asymmetry(t))

# remember not included



menu = [{1:['Salad', 'Soup']}, {2:['Entree']}, {3:{'Desert':257, 'Fruit':95}}]
print(menu[1][2][0])


activities = ['eating', 'sleeping']
vowels = 'aeiou'
for vowel in vowels:
    for activity in activities:
        if vowel in activity:
            print(activity + ' ', end='')
        else:
            break


outF = open('digits.txt', 'w')
for i in range(2):
    outF.write(str(i))
outF.close()

inF = open('digits.txt', 'r')
for line in inF:
    print(line)
inF.close()



words = ['the', 'dust', 'which', 'the', 'wind', 'blows', 'in', 'your', 'face']
extremelyOdd = ''
for word in words:
    length = len(word)
    if length % 2 == 1 or length > len(extremelyOdd):
        extremelyOdd = word

print(extremelyOdd)




import turtle

t = turtle.Turtle()

for i in range(4):
    if i%2 == 0:
        t.up()
        t.forward(100)
        t.right(90)
    if i%3 == 0:
        t.down()
        t.forward(100)
        t.right(90)

# these are two separate blocks

# i%n is always 0



def inFileCount(fileName):
    inF = open(fileName)
    length = len(inF.read())
    inF.close()
    return length


outF = open('inspire.txt', 'w')
outF.write("Don't be the same." + "\n")
outF.write("Be better." + "\n")
outF.close()
print(inFileCount('inspire.txt'))



import turtle

def drawSquare(t, lenght):
    t.down()
    t.speed(5)
    for i in range(4):
        t.forward(lenght)
        t.right(90)


def offsetSquares(t, lenght, num, xoffset, yoffset):
    for i in range(num):
        drawSquare(t, lenght)
        t.up()
        t.goto(xoffset*(i+1),-yoffset*(i+1))
    turtle.done()


t = turtle.Turtle()
offsetSquares(t, 100, 4, 20, 10)




def indexByLength(s):
    s = s.lower()
    d= {}
    s = s.split()
    for i in range(len(s)):
        wordlen = len(s[i])
        if wordlen not in d:
            d[wordlen] = []
            d[wordlen].append(s[i])
        else:
            d[wordlen].append(s[i])
    return d

text = 'I was indecisive but now I am not too sure'
print(indexByLength(text))

# add a list to the dictionary before updating the list in the value position

'''

def cloneLines(inFile,outFile):
    inf = open(inFile, 'r')
    out = open(outFile, 'w')
    linelst = inf.readlines()
    for i in linelst:
        words = i.split()





print(cloneLines('infile2.txt','outfile3.txt'))
