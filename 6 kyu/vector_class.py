"""
https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python
"""
class Vector:
    def __init__(self, lst: list):
        self.lst = lst

    def __str__(self):
        return str(tuple(self.lst)).replace(" ", "")

    def check_length(self, other):
        if len(self.lst) != len(other.lst):
            raise ValueError("Vectors must have the same length")

    def add(self, other):
        self.check_length(other)
        return Vector([x + y for x, y in zip(self.lst, other.lst)])

    def subtract(self, other):
        self.check_length(other)
        return Vector([x - y for x, y in zip(self.lst, other.lst)])

    def dot(self, other):
        self.check_length(other)
        return sum(x * y for x, y in zip(self.lst, other.lst))

    def norm(self):
        return sum(x**2 for x in self.lst)**0.5

    def equals(self, other):
        return self.lst == other.lst

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception