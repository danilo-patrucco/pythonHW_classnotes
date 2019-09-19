# Danilo Patrucco
# CS 100 2019F Section 103
# HW 01, September 11, 2019

# Exercise 1.

import random

gradeRatings = ['A', 'B', 'C', 'D', 'F']
grades = []
frequency = []

print('\r\n' + 'Exercise 1' + '\r\n')
for count in range(10):
    grades.append(random.choice(gradeRatings))

print('grade list', grades, '\r\n')

for grade in gradeRatings:
    frequency.append(grades.count(grade))

print('grade frequency', frequency, '\r\n')

# exercise 2.

print('Exercise 2')

# 2.a

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

# 2.b

print('\r\n', 'Exercise 2.b', '\r\n')
sliceVar = slice(2)
herdingDog = dog_breeds[sliceVar]
print(herdingDog)

# 2.c

print('\r\n' + 'Exercise 2.c' + '\r\n')
tiny_dogs = dog_breeds[-1]
print(tiny_dogs)

# 2.d

print('\r\n' + 'Exercise 2.d' + '\r\n')
comp = 'Persian'
print('Is persian present in the list ? {T/F} : ', comp in dog_breeds)
