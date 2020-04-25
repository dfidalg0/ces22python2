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

    # Exercício 12
    def __add__ (self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__ (self, other): # Complex multiplication
        return Point(
            self.x * other.x - self.y * other.y,
            self.x * other.y + self.y * other.x
        )

    def __rmul__(self, other):
        return Point(
            self.x * other.real - self.y * other.imag,
            self.x * other.imag + self.y * other.real
        )

    def __radd__ (self, other):
        return Point(other.real + self.x , self.y + other.imag)

    def __str__ (self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return self.__str__()
