import math

class Point:
    '''A point in time and space'''


    def __init__(self,x,y):
        self.x_coor = x
        self.y_coor = y

    def coordinates(self):
        return (self.x_coor, self.y_coor)

    def move_to(selfself, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

    def move(self, x, y):
        self.x_pos += x
        self.y_pos += y

    def distance_to(self, apoint):
        return (math.sqrt(((apoint.x_coor-self.x_coor)**2) + ((apoint.y_coor-self.y_coor)**2)))

