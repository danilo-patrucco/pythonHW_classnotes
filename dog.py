class Dog:
    ''' Danilo Patrucco - CS100-103 - 11/17/2019 - HW 10'''

    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, tricks):
        self.tricks.append(tricks)
        print('Sugar knows ' + self.tricks[-1])


