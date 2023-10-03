class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError('You must substract two vectors only')

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError('You must add two vectors only')

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x*scalar, self.y*scalar)
        raise ValueError('Scalar must be a int or float')

    def __rmul__(self, scalar):
        return self.__mul__(scalar)


v1 = Vector2D(6, 7)
v2 = Vector2D(-2, 5)

print('v1 + v2 =', v2 + v1)
print('v1 - v2 =', v1 - v2)
print('v1 * 2 =', v1 * 2)
print('3 * v2 =', 5 * v2)
