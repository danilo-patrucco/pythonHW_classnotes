#class exercises
'''

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

'''
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
