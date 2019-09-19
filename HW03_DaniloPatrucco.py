# Danilo Patrucco
# CS 100 2019F Section 103
# HW 03, September 18, 2019

import turtle

# exercise 1

# a

a = 3
b = 4
c = 5

# b

if a < b:
    print('OK')

# c

if c < b:
    print('OK')

# d

if a + b == c:
    print('OK')

# e

if a**2 + b**2 == c**2:
    print('OK')

# exercise 2

if not (a < b):
    print('NOT OK')
if not (c < b):
    print('NOT OK')
if not (a + b == c):
    print('NOT OK')
if not (a ** 2 + b ** 2 == c ** 2):
    print('NOT OK')

# Exercise 3

lColor = input('Please enter the color you want the line to be: ')
lWidth = int(input('Please enter the width you want the line to be: '))
lLength = int(input('Please enter the length you want the line to be: '))
shapeType = input('Please enter the type of shape you want to make (please choose between line, triangle or square): ').lower()


turtle.width(lWidth)
turtle.pencolor(lColor)

if shapeType == 'triangle':
    turtle.forward(lLength)
    turtle.left(120)
    turtle.forward(lLength)
    turtle.left(120)
    turtle.forward(lLength)
elif shapeType == 'square':
    turtle.forward(lLength)
    turtle.left(90)
    turtle.forward(lLength)
    turtle.left(90)
    turtle.forward(lLength)
    turtle.left(90)
    turtle.forward(lLength)
elif shapeType == 'line':
    turtle.forward(lLength)
else:
    print('bad selection')

turtle.done()