"""
https://www.codewars.com/kata/532a69ee484b0e27120000b6/train/python
"""
import math

from typing import Iterable, overload


class Vector:
    @overload
    def __init__(self, x: int, y: int, z: int) -> None: ...

    @overload
    def __init__(self, *args: Iterable[int]) -> None: ...

    def __init__(self, *args):
        x, y, z = args if len(args) == 3 else args[0]
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value: int) -> None:
        self.z = value

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def cross(self, other: "Vector") -> "Vector":
        return Vector(
            self._y * other._z - self._z * other._y,
            self._z * other._x - self._x * other._z,
            self._x * other._y - self._y * other._x
        )

    def dot(self, other: "Vector") -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self) -> tuple:
        return (self.x, self.y, self.z)

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"


examples = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(Vector(examples[0]).cross(Vector(*examples[1])))
print(Vector(-3, 6, -3))