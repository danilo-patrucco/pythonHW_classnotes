# class exercises
"""

lst = ['159.99', '160.00', '205.95', '128.83', '175.49']

lst.append('160.00')

print(lst.count('160.00'))

minCost = min(lst)

print(minCost)

print(lst.index(minCost))

lst.remove(minCost)

print(lst)

lst.sort()

print(lst)

# when you slice a list you get a list in output

# lst[1:1] will return nothing inside of a list ( will return [])

# typecasting, pythong need to convert types of data to the same type before using them together EX( 3 + 3.0 has an issue, will need to turn 3
# into float and then you can sum it together

age=int(input('what is your age'))
name=input('what is your name')
print(name, ', next year you will be', str(age+1), 'years old!')

total=0
if True or False:
    total += 1
elif not True or not False:
    total += 2
else:
    total += 4

if True and False:
    total += 8
elif True:
    total += 16

print(total)

# total is going to be 17


letters = ['s', 'r', 'a', 'c', 's', 'o']
concat = letters[-5] + letters[2] + letters[-3]
print(concat)


def getNegativeNum(integ):
    while integ >= 0:
        integ = int(input("write a negative number"))

    return integ


integerNumber = 0
finalcountdown = getNegativeNum(integerNumber)
print("Good Job! The number written is ", finalcountdown)


thresh = 502
prev = 1
curr = 1

# update two variables at the same time

while curr <= thresh:
    prev, curr = curr, curr + prev


print(curr)




def cities():
    returnList = []
    while True:
        city = input("City:")

        if city == '':
            return returnList
        returnList.append(city)

cities()


def cities2():
    returnList = []
    city = input("City:")
    while city != '':
        city = input("City:")
        returnList.append(city)

    return returnList

cities2()



cities = []

while True:
    city = input("City: ")
    if city == "":
        break
    cities.append(city)

print(cities)


# continue and break in nested loops

def before (table):
    for row in table:
        for num in row:
            if num == 0:
                break
            print(num, end='')
        print()
table = [
    [1,0,3,4,5],
    [1,6,7,0,9],
    [12,67,54,0,12]]

before(table)


def ignore(table):
    for row in table:
        for num in row:
            if num == 0:
                continue
            print(num, end="")
        print()


ignore(table)

"""



