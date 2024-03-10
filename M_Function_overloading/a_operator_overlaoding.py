# Operator Overloading


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.y, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"vecotr:({self.x}, {self.y})"



v1 = Vector(1,2)
v2 = Vector(3,4)
print("Vector addition:", v1 + v2)
print(v1)



print("Veter subtraction:", v1 - v2)
print("Scalar multiplication:", v1 * 2)
print("Scalar multiplication:", v2 * 2)



