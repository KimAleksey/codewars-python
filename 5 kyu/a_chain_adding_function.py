"""
https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python
"""


class Add(int):
    def __call__(self, a):
        return Add(self + a)


def add(n: int):
    return Add(n)

print(add(1)(3)(4)(5))