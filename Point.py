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

    # Exercício 7
    def get_line_to(self,other):
        x0, y0 = self.get()
        x1, y1 = other.get()

        m = (y1-y0)/(x1-x0)
        b = y0 - m*x0

        return (m,b)
