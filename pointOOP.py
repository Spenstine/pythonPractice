class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        '''
        return new Point object
        '''
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        else:
            x = self.x + other[0]
            y = self.y + other[1]
            return Point(x, y)
            
    def __radd__(self, other):
        return self.__add__(other)


c = Point(3,4)
origin = Point()

print(c)
print(c + origin)