from math import inf

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    # Exercício 5
    def reflect_x (self):
        return Point(self.x,-self.y)

    #Exercício 6
    def slope_from_origin (self):
        return self.y/self.x if self.x != 0 else inf
