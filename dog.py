class Dog:
    ''' Danilo Patrucco - CS100-103 - 11/17/2019 - HW 10'''

    species = 'canis lupus familiaris'

    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(self.name + ' ' + trick)
        else:
            print(self.name, 'already know', trick)

# Problem 4

    def knows (self, trick):
        if trick in self.tricks:
            print('Yes,', self.namem, self.species, trick)
            return True
        else:
            print('No,', self.namem, self.species, trick)
            return False




