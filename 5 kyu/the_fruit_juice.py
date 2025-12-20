"""
https://www.codewars.com/kata/5264603df227072e6500006d/train/python
"""

class Jar:
    def __init__(self):
        self._fruits = {}

    def add(self, amount: int, kind: str):
        self._fruits[kind] = self._fruits.get(kind, 0) + amount

    def pour_out(self, amount: int):
        buff = {}
        for kind, value in self._fruits.items():
            buff[kind] = value - self.get_concentration(kind) * amount
        for kind, value in self._fruits.items():
            self._fruits[kind] = buff[kind]

    def get_total_amount(self):
        if not self._fruits:
            return 0
        return sum(value for value in self._fruits.values())

    def get_concentration(self, kind) -> float:
        if kind not in self._fruits:
            return 0
        if self.get_total_amount() == 0:
            return 0
        return  self._fruits.get(kind, 0) / self.get_total_amount()


jar = Jar()
print(jar.get_total_amount())
print(jar.get_concentration("apple"))

jar.add(100, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))

jar.add(100, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))

jar.add(200, "banana")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))

jar.pour_out(200)
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))

jar.add(200, "apple")
print(jar.get_total_amount())
print(jar.get_concentration("apple"))
print(jar.get_concentration("banana"))