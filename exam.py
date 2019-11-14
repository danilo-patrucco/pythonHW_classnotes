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



def cloneLines(inFile,outFile):
    inf = open(inFile, 'r')
    out = open(outFile, 'w')
    linelst = inf.readlines()
    wordlst = []
    for i in linelst:
        cont = i
        cont.split(wordlst)
        print(wordlst)
        if (linelst.count(i)) >= 2:
            inf.write(i)


def cloneLines(inFile, outFile):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')

    for line in inF:
        words = line.split()

        for word in words:
            if words.count(word) > 1:
                outF.write(line)
                break

    inF.close()
    outF.close()







print(cloneLines('infile2.txt','outfile3.txt'))



nurseryRhyme = 'Rain rain go away'
vowelCount = 0
n = -1
while vowelCount < 3:
    if nurseryRhyme[n] in 'aeiouAEIOU':
        vowelCount += 1+
    n -= 1
print(n)


def splitLength(sentence):
    result = 0
    for s in sentence.split():
        print(s)
        if len(s) > 3:
            result += 1
    return result


lisa = 'Dad, are you listening to me?'
print(splitLength(lisa))


boolList = [False, False or False, False and False, not False, not not False]
sum = 0
for b in boolList:
    if not b:
        sum += 1
print(sum)


def mirrorOnWheels(s):
    prev = 0
    for current in range(1, len(s) - 1):
        prev = current - 1
        next = current + 1
        if s[prev] == s[next]:
            break
        else:
            continue
        return 0
    return prev


s = 'Good decision!'
print(mirrorOnWheels(s))

noOddHeroes = []
heroes = ['superman', 'batman', 'aquaman']
for hero in heroes:
    if len(hero) % 2 == 0:
        noOddHeroes.append(hero)
print(noOddHeroes)


candyOnStick = 'lolli lolli lolli lollipop lollipop'
wordList = candyOnStick.split('i')
d = {}
for word in wordList:
    print(word)
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(len(d))

#when you specify the command it will always use that and not the others



def oldMcDonald(farm):
    result = 0
    for animal in farm:
        if animal[0] in farm[animal]:
            result += 1
    return result


farm = {'cow':'moo', 'duck':'quack', 'cricket':'chirp'}
print(oldMcDonald(farm))

#animal[0] in farm[animal] is checking if the first letter of the word loaded in animal is present in the value called by farm[animal]


def analyzer(fileName):
    inputFile = open(fileName)
    line = inputFile.read()
    inputFile.close()
    print(line)
    return line.count(',')

quotes = open('alice.txt', 'w')
quotes.write('Now, here, you see, it takes all the running\n')
quotes.write('you can do, to keep in the same place.\n')
quotes.close()
print(analyzer('alice.txt'))

#it reads only the first line the readline, unless you run a loop


def triangle(t, lenght):
    t.down()
    for i in range(3):
        t.forward(lenght)
        t.left(120)
    return


def umbrella(t, side, rotation, count):
    for i in range(count):
        triangle(t, side)
        t.right(rotation)



import turtle
snappy = turtle.Turtle()
umbrella(snappy, 100, 60, 6)

# all good !



def analyzeAreaCodes(phones):
    d={}
    for i in range(len(phones)):
        areaCode = phones[i]
        areaCode = areaCode[0:3]
        if areaCode not in d:
            d[areaCode] = 1
        elif areaCode in d:
            d[areaCode] += 1
    return d

phones = ['982-867-5309', '800-649-2568', '979-606-0842', '982-779-311']
print(analyzeAreaCodes(phones))


import string

def lineStats(infile, outfile):
    inF = open(infile, 'r')
    outF = open(outfile, 'w')
    for i in inF :
        cons = 0
        voc = 0
        for l in i:
            print(l)
            if l in ('aeiouAEIOU'):
                voc += 1
            elif l not in ('aeiouAEIOU |\n'):
                cons += 1
        writeout = str(voc) + ' ' + str(cons) + '\n'
        outF.write(writeout)
    inF.close()
    outF.close()

lineStats('infile2.txt','outfile4.txt')



def frequencyAnalysis(aStr, i):
    d = {}
    for element in aStr:
        freq = aStr.count(element)
        if element not in d:
            d[element] = freq
        elif aStr.count(element) >= i:
            d[element] *= 2
        else:
            d[element] *= -2
    return d[aStr[-1]]


print(frequencyAnalysis('606', 1))



def substring(a, b):
    s = ''
    while True:
        if a in b:
            continue
        elif b in a:
            return b
        else:
            return a
    return s


print(substring('ark', 'snark'))



def textFunction(text):
    words = text.split()
    rtnList = []
    for idx in range(len(words)-1):
        word = words[idx]
        if word in words[idx+1:]:
            rtnList.append(word)
    return rtnList

s = 'I want what I want when I want it'
print(textFunction(s))


def test(t,o):
    inF = open(t,'r')
    outF = open (o,'w')
    test1 = inF.readline()
    test2 = inF.readlines()
    for i in test1:
        print(i)
    print('test', '\n\n')
    for l in test2:
        print(l)
    inF.close()
    outF.close()
    return

test('infile2.txt','outfile5.txt')



def substring(a, b):
    while a in b:
        b = b[1:-1]
        if a in b:
            continue
        elif b in a:
            return b
        else:
            return a
    return b

print(substring('the','hypothermia'))




booleans = [True and False, not False, False or True, not not False]
binary = 0
powerOfTwo = 8
for boolean in booleans:
    if boolean:
        binary += powerOfTwo
    powerOfTwo =powerOfTwo//2
    print(powerOfTwo)




print(binary)



d = {}
for x in range(1, 7):
    d[x // 4] = x
print(d)



language = 'DRAKON'
output = ''
for w in language[:2]:
    print(w)
    output += w
    print(output)
    for x in language[-2:]:
        print(x)
        output += x
        print(output)
print(output)

#output is donron



polonius = 'To shine own self be true.'
extreme = ''
for word in polonius.split():
    if not(len(word) < len(extreme)):
        extreme = word
print(extreme)

'''
print('test', '\n', 'test1', '\n', 'test1', '\n', 'test1', '\n')
