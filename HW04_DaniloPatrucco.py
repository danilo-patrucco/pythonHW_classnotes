# Danilo Patrucco
# CS 100 2019F Section 103
# HW 05, September 25, 2019

# Exercise 1

print('\n\r Exercise 1 \n\r')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

for month in months:
    if 'J' in month:
        print(month)

# Exercise 2

print('\n\r Exercise 2 \n\r')

for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

# Exercise 3

print('\n\r Exercise 3 \n\r')

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for i in horton:
    if i in vowels:
        print(i)
