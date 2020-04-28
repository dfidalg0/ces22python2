# Exercício 9

class Shape:
    geometric_type = 'Generic Shape'

    def area (self):
        raise NotImplementedError

    def get_geometric_type (self):
        return self.geometric_type

class Plotter:
    def plot (self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon (Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon (Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self,side):
        self.side = side

class RegularHexagon (RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area (self):
        return 1.5 * (3 ** .5 * self.side **2)

class Square (RegularPolygon):
    geometric_type = 'Square'

    def area (self):
        return self.side * self.side

class SquareHexagon (Square,RegularHexagon):
    pass

class HexagonSquare (RegularHexagon,Square):
    pass

print('MRO for SquareHexagon:')
for (i,class_type) in enumerate(SquareHexagon.mro()):
    print(f'{i+1}. {class_type.__name__}')
print()

print('MRO for HexagonSquare:')
for (i,class_type) in enumerate(HexagonSquare.mro()):
    print(f'{i+1}. {class_type.__name__}')
print()

L = [SquareHexagon(3), HexagonSquare(3)]

print('Areas:')
for poly in L:
    print(poly.__class__.__name__,':',poly.area())
print()

print('Geometric types:')
for poly in L:
    print(poly.__class__.__name__,':',poly.get_geometric_type())
print()
