# Danilo Patrucco
# CS 100 2019F Section 103
# HW 02, September 18, 2019

# Exercise 2.

import turtle
import math

# Exercise 1

# triangle
scrn = turtle.Screen()
trtl = turtle.Turtle()

# instead of turtle.speed you can do trtl.speed

turtle.speed(10)

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.penup()


# square

turtle.goto(-200, 0)
turtle.pendown()
turtle.left(120)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()

# pentagon

turtle.goto(0,-200)
turtle.pendown()
turtle.left(18)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.penup()

# Exercise 2

turtle.goto(-400,-300)
turtle.pendown()
turtle.right(288)
turtle.circle(50)
turtle.circle(100)
turtle.circle(150)
turtle.circle(200)

turtle.done()

# Exercise 3

# a

print('factorial of 100 is : ', math.factorial(100))

# b

print('log 2 of 1,000,000 is -> ', math.log2(1000000))

# c

print('The greatest common divisor of 63 and 49 is -> ', math.gcd(63, 49))