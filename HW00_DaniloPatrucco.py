# Danilo Patrucco
# CS 100 2019F Section 103
# HW 00, September 4, 2019

# Exercise 5b
months = 12
days = 19
year = 2019

# Exercise 5c
height = 7.63
weight = 200.36
diameter = 293.459

# Exercise 5d
speaksParseltongue = 'Harry Potter'
houseName = 'hufflepuff'
wandCore = 'phoenix tail'

print("Hello World!")

'''

Chapter 1 

Exercise 1-1

1.

Q: In a print statement, what happens if you leave out one of the parentheses, or
both?

A: unexpected EOF while parsing

2.

Q: If you are trying to print a string, what happens if you leave out one of the quotation
marks, or both?

A single quotation out : invalid syntax -> when removing both quotation marks

A both quotation mark out : EOL while scanning string literal -> when removing one quote mark only

3.

Q: You can use a minus sign to make a negative number like -2. What happens if
you put a plus sign before a number? 

A: the number will return as positive, no error will happen

Q: What about 2++2?

A: will return 4

4.

Q: In math notation, leading zeros are okay, as in 02. What happens if you try this in
Python?

A: Idle will throw SyntaxError: invalid token

5.

Q: What happens if you have two values with no operator between them?

A: SyntaxError: invalid syntax

Exercise 1-2

1. 

Q: How many seconds are there in 42 minutes 42 seconds?

A: >>> 42*60+42
2562

2.

Q: How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
mile.

A: >>> 10/1.61
6.211180124223602

3.

Q: If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
pace (time per mile in minutes and seconds)? 

A: >>> (((10/2562)*3600)/10)/1.61
0.8727653570337615

Q: What is your average speed in
miles per hour?

A: >>> ((10/2562)*3600)/1.61
8.727653570337614

Exercise 2-1

1.

Q: We’ve seen that n = 42 is legal. What about 42 = n?      
A: SyntaxError: can't assign to literal
Q: How about x = y = 1?
A: x and y will both have value 1 (if type print x the result is 1 and the same goes for y)
Q: In some languages every statement ends with a semicolon, ;. What happens if
you put a semicolon at the end of a Python statement?
A: the behaviour is the same as without semicolon 
Q: What if you put a period at the end of a statement?
A: SyntaxError: invalid syntax
Q: In math notation you can multiply x and y like this: xy. What happens if you try
that in Python?
A: Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    xy
NameError: name 'xy' is not defined

Exercise 2-2

1. 

Q:The volume of a sphere with radius r is 43 πr3. What is the volume of a sphere with
radius 5?
A: >>> pi = 3.141592653589793
>>> (3/4*pi)*(5**3)
294.5243112740431

Correction (4/3*pi)**(5**3)

2.

Q: Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
the total wholesale cost for 60 copies?
A: >>> ((24.95*0.6)*60)+3+(0.75*59)

945.4499999999999 

Corrected

'''